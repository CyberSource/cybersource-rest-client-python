# coding: utf-8
"""
Public Key API Controller Module.

This module provides functionality to fetch RSA public keys in JWK format
from the CyberSource Flex V2 public keys API endpoint.
"""

from __future__ import absolute_import

import requests
import json

from authenticationsdk.util.jwt.JWTUtility import get_rsa_public_key_from_jwk
from authenticationsdk.util.jwt.JWTExceptions import InvalidJwkException


def fetch_public_key(kid, run_environment):
    """
    Fetch the public key for the given key ID (kid) from the specified run environment.
    
    This function makes an HTTP GET request to the Flex V2 public keys endpoint
    to retrieve the RSA public key in JWK format.
    
    Args:
        kid (str): The key ID for which to fetch the public key
        run_environment (str): The environment domain (e.g., 'apitest.cybersource.com')
        
    Returns:
        dict: The RSA public key in JWK format
        
    Raises:
        ValueError: If kid or run_environment is missing
        requests.exceptions.RequestException: If the HTTP request fails
        InvalidJwkException: If the JWK cannot be parsed correctly
        Exception: For other errors during the fetch or parse process
    """
    if not kid:
        raise ValueError('kid parameter is required')
    
    if not run_environment:
        raise ValueError('runEnvironment parameter is required')
    
    url = f"https://{run_environment}/flex/v2/public-keys/{kid}"
    
    headers = {
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()
        
        if not response.text:
            raise Exception('Empty response received from public key endpoint')
        
        # Parse the response
        try:
            response_data = response.json()
            jwk_json_string = json.dumps(response_data)
        except json.JSONDecodeError:
            # If it's already a string, use it directly
            jwk_json_string = response.text
        
        # Extract and validate the RSA public key from JWK
        try:
            public_key = get_rsa_public_key_from_jwk(jwk_json_string)
            if not public_key:
                raise Exception('Invalid public key received from JWK')
            return public_key
        except InvalidJwkException as parse_error:
            error = Exception(f'Failed to parse JWK response: {str(parse_error)}')
            error.original_error = parse_error
            raise error
            
    except requests.exceptions.HTTPError as http_error:
        status_code = http_error.response.status_code if http_error.response else 'Unknown'
        status_text = http_error.response.reason if http_error.response else 'Unknown'
        error = Exception(
            f'HTTP {status_code}: {status_text} - Failed to fetch public key for kid: {kid}'
        )
        error.status = status_code
        error.original_error = http_error
        raise error
        
    except requests.exceptions.ConnectionError as conn_error:
        error = Exception(f'No response received - Failed to fetch public key for kid: {kid}')
        error.original_error = conn_error
        raise error
        
    except requests.exceptions.RequestException as req_error:
        error = Exception(f'Request error: {str(req_error)}')
        error.original_error = req_error
        raise error
    
    except Exception as general_error:
        # Re-raise if it's already one of our custom errors
        if hasattr(general_error, 'original_error'):
            raise
        # Otherwise wrap it
        error = Exception(f'Error fetching public key: {str(general_error)}')
        error.original_error = general_error
        raise error
