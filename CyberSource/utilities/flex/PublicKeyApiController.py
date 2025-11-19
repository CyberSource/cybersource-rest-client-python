# coding: utf-8
"""
Public Key API Controller Module.

This module provides functionality to fetch RSA public keys in JWK format
from the CyberSource Flex V2 public keys API endpoint.
"""

from __future__ import absolute_import

import json
import ssl
import certifi
import urllib3

from authenticationsdk.util.jwt.JWTUtility import get_rsa_public_key_from_jwk
from authenticationsdk.util.jwt.JWTExceptions import InvalidJwkException
from CyberSource.configuration import Configuration


def fetch_public_key(kid, run_environment):
    """
    Fetch the public key for the given key ID (kid) from the specified run environment.
    
    This function makes an HTTP GET request to the Flex V2 public keys endpoint
    to retrieve the RSA public key in JWK format.
    
    Args:
        kid (str): The key ID for which to fetch the public key
        run_environment (str): The environment domain (e.g., 'apitest.cybersource.com')
        
    Returns:
        RSAPublicKey: The RSA public key object from cryptography library
        
    Raises:
        ValueError: If kid or run_environment is missing
        urllib3.exceptions.HTTPError: If the HTTP request fails
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
    
    # Use the same SSL configuration pattern as rest.py
    configuration = Configuration()
    if configuration.ssl_ca_cert:
        cert_reqs = ssl.CERT_REQUIRED
        ca_certs = configuration.ssl_ca_cert
    else:
        # Use certifi bundle as fallback (same as rest.py)
        cert_reqs = ssl.CERT_REQUIRED  # ← Changed from CERT_NONE
        ca_certs = certifi.where()     # ← Use certifi instead of None
    
    # Create urllib3 PoolManager with SSL configuration (matches rest.py pattern)
    http = urllib3.PoolManager(
        cert_reqs=cert_reqs,
        ca_certs=ca_certs
    )
    
    try:
        # Make the HTTP GET request
        response = http.request('GET', url, headers=headers)
        
        # Check if the request was successful
        if response.status not in range(200, 300):
            error = Exception(
                f'HTTP {response.status}: {response.reason} - Failed to fetch public key for kid: {kid}'
            )
            error.status = response.status
            raise error
        
        # Get response data as string
        response_data = response.data.decode('utf-8')
        
        if not response_data:
            raise Exception('Empty response received from public key endpoint')
        
        # Use response data directly as JSON string
        jwk_json_string = response_data
        
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
            
    except urllib3.exceptions.HTTPError as http_error:
        error = Exception(f'HTTP error - Failed to fetch public key for kid: {kid}')
        error.original_error = http_error
        raise error
        
    except urllib3.exceptions.MaxRetryError as retry_error:
        error = Exception(f'No response received - Failed to fetch public key for kid: {kid}')
        error.original_error = retry_error
        raise error
        
    except urllib3.exceptions.SSLError as ssl_error:
        error = Exception(f'SSL error - Failed to fetch public key for kid: {kid}')
        error.original_error = ssl_error
        raise error
    
    except Exception as general_error:
        # Re-raise if it's already one of our custom errors
        if hasattr(general_error, 'original_error'):
            raise
        # Otherwise wrap it
        error = Exception(f'Error fetching public key: {str(general_error)}')
        error.original_error = general_error
        raise error
