# coding: utf-8
"""
Capture Context Parsing Utility Module.

This module provides functionality to parse and verify JWT capture context responses
from CyberSource. It supports signature verification using public keys fetched from
the Flex V2 API, with caching to improve performance.
"""

from __future__ import absolute_import

from authenticationsdk.util.jwt.JWTUtility import parse, verify_jwt
from authenticationsdk.util.jwt.JWTExceptions import (
    InvalidJwtException, 
    InvalidJwkException, 
    JwtSignatureValidationException
)
from authenticationsdk.util.Cache import FileCache
from CyberSource.utilities.flex.PublicKeyApiController import fetch_public_key


def parse_capture_context_response(jwt_value, merchant_config, verify_jwt_signature=True):
    """
    Parse a capture context JWT response and optionally verify its signature.
    
    This function parses a JWT token and optionally verifies its signature using
    the public key fetched from the CyberSource Flex V2 API. Public keys are cached
    to improve performance on subsequent verifications.
    
    Args:
        jwt_value (str): The JWT token to parse
        merchant_config (object): The merchant configuration object containing run_environment
        verify_jwt_signature (bool): Whether to verify the JWT signature (default: True)
        
    Returns:
        dict: The decoded JWT payload
        
    Raises:
        InvalidJwtException: If the JWT token is invalid or cannot be parsed
        InvalidJwkException: If the public key (JWK) is invalid
        JwtSignatureValidationException: If signature verification fails
        ValueError: If merchant_config is missing or invalid
        Exception: For other errors during parsing or verification
        
    Example:
        >>> from authenticationsdk.core.MerchantConfiguration import MerchantConfiguration
        >>> merchant_config = MerchantConfiguration()
        >>> merchant_config.run_environment = "apitest.cybersource.com"
        >>> payload = parse_capture_context_response(jwt_token, merchant_config, True)
        >>> print(payload)
    """
    if not jwt_value:
        raise InvalidJwtException('JWT value is null or undefined')
    
    if not merchant_config:
        raise ValueError('merchantConfig is required')
    
    # Parse the JWT token
    try:
        parsed_jwt = parse(jwt_value)
    except InvalidJwtException:
        raise
    except Exception as parse_error:
        raise InvalidJwtException('Failed to parse JWT token', parse_error)
    
    # If verification is not requested, return the payload immediately
    if not verify_jwt_signature:
        return parsed_jwt['payload']
    
    # Extract the key ID from the JWT header
    header = parsed_jwt['header']
    kid = header.get('kid')
    
    if not kid:
        raise JwtSignatureValidationException('JWT header missing key ID (kid) field')
    
    # Get the run environment from merchant config
    run_environment = None
    if hasattr(merchant_config, 'run_environment'):
        run_environment = merchant_config.run_environment
    elif hasattr(merchant_config, 'getRunEnvironment'):
        run_environment = merchant_config.getRunEnvironment()
    
    if not run_environment:
        raise ValueError('Run environment not found in merchant config')
    
    # Try to get the public key from cache
    cache = FileCache()
    public_key = None
    is_public_key_from_cache = False
    
    try:
        public_key = cache.get_public_key_from_cache(run_environment, kid)
        is_public_key_from_cache = True
    except KeyError:
        is_public_key_from_cache = False
    
    # If public key is not in cache or verification fails, fetch from API
    if not is_public_key_from_cache:
        public_key = _fetch_public_key_and_verify(jwt_value, kid, run_environment, cache)
        return parsed_jwt['payload']
    
    # Try to verify with cached public key
    try:
        verify_jwt(jwt_value, public_key)
        return parsed_jwt['payload']
    except (JwtSignatureValidationException, InvalidJwkException):
        # If verification fails with cached key, fetch fresh key from API
        public_key = _fetch_public_key_and_verify(jwt_value, kid, run_environment, cache)
        return parsed_jwt['payload']


def _fetch_public_key_and_verify(jwt_value, kid, run_environment, cache):
    """
    Fetch public key from API and perform JWT verification.
    
    This is a private helper function that fetches the public key from the
    Flex V2 API, caches it, and verifies the JWT signature.
    
    Args:
        jwt_value (str): The JWT token
        kid (str): The key ID
        run_environment (str): The runtime environment
        cache (FileCache): The cache instance
        
    Returns:
        dict: The public key in JWK format
        
    Raises:
        InvalidJwkException: If the JWK cannot be parsed
        JwtSignatureValidationException: If verification fails
        Exception: For other errors during fetch or verification
    """
    try:
        # Fetch the public key from the Flex V2 API
        public_key = fetch_public_key(kid, run_environment)
        
        # Add to cache (cache failure is not critical)
        try:
            cache.add_public_key_to_cache(run_environment, kid, public_key)
        except Exception:
            # Cache failure is not critical, continue with the public key
            pass
            
    except Exception as fetch_error:
        # Re-raise with appropriate error type
        if 'Invalid Runtime URL' in str(fetch_error):
            raise ValueError('Invalid Runtime URL in Merchant Config')
        elif 'No response received' in str(fetch_error) or 'Network error' in str(fetch_error):
            raise Exception('Error while trying to retrieve public key from server')
        elif 'Failed to parse JWK' in str(fetch_error):
            raise InvalidJwkException('JWK received from server cannot be parsed correctly', fetch_error)
        else:
            raise Exception('Error while trying to retrieve public key from server')
    
    # Verify the JWT with the fetched public key
    try:
        verify_jwt(jwt_value, public_key)
        return public_key
    except (JwtSignatureValidationException, InvalidJwkException):
        raise JwtSignatureValidationException('JWT validation failed')
