# coding: utf-8
"""
JWT (JSON Web Token) Utility Module.

This module provides utilities for parsing and verifying JWT tokens, including:
- Parsing JWT tokens into header, payload, and signature components
- Verifying JWT signatures using RSA public keys in JWK format
- Converting JWK (JSON Web Key) to PEM format for cryptographic operations

Supports JWT algorithms: RS256, RS384, RS512
"""

from __future__ import absolute_import

import base64
import json
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

from .JWTExceptions import InvalidJwkException, InvalidJwtException, JwtSignatureValidationException


# Supported JWT algorithms and their corresponding hash algorithms
SUPPORTED_ALGORITHMS = {
    'RS256': hashes.SHA256(),
    'RS384': hashes.SHA384(),
    'RS512': hashes.SHA512()
}


def _base64url_decode(input_str):
    """
    Decode a base64url encoded string.
    
    Base64url encoding is similar to base64 but uses URL-safe characters
    and removes padding.
    
    Args:
        input_str (str): The base64url encoded string
        
    Returns:
        bytes: The decoded bytes
        
    Raises:
        Exception: If decoding fails
    """
    # Add padding and replace URL-safe characters with standard base64 characters
    # Adding '==' ensures proper padding (base64 decoder ignores excess padding)
    input_str = (input_str + '==').replace('-', '+').replace('_', '/')
    
    return base64.b64decode(input_str)


def _decode_jwt_part(base64url_string, part_name):
    """
    Decode a base64url encoded string to a JSON object.
    
    Args:
        base64url_string (str): The base64url encoded string
        part_name (str): Name of the JWT part for error reporting (e.g., 'header', 'payload')
        
    Returns:
        dict: The decoded JSON object
        
    Raises:
        InvalidJwtException: If decoding or parsing fails
    """
    try:
        decoded_bytes = _base64url_decode(base64url_string)
        json_string = decoded_bytes.decode('utf-8')
        return json.loads(json_string)
    except json.JSONDecodeError as decode_err:
        raise InvalidJwtException('Invalid JSON in JWT {}'.format(part_name), decode_err)
    except Exception as decode_err:
        raise InvalidJwtException('Failed to decode JWT {} from base64url'.format(part_name), decode_err)


def _validate_and_parse_jwk(public_key):
    """
    Validate and parse a JWK public key.
    
    Args:
        public_key (dict or str): The RSA public key (JWK object or JSON string)
        
    Returns:
        dict: The validated JWK object
        
    Raises:
        InvalidJwkException: If the public key is invalid
    """
    jwk_key = None
    
    if isinstance(public_key, str):
        try:
            jwk_key = json.loads(public_key)
        except json.JSONDecodeError as parse_err:
            raise InvalidJwkException('Invalid public key JSON format', parse_err)
    elif isinstance(public_key, dict) and 'kty' in public_key:
        jwk_key = public_key
    else:
        raise InvalidJwkException('Invalid public key format. Expected JWK object or JSON string.')
    
    if jwk_key.get('kty') != 'RSA':
        raise InvalidJwkException('Public key must be an RSA key (kty: RSA)')
    
    if not jwk_key.get('n') or not jwk_key.get('e'):
        raise InvalidJwkException('Invalid RSA JWK: missing required parameters (n, e)')
    
    return jwk_key


def _convert_jwk_to_public_key(jwk_key):
    """
    Convert JWK RSA parameters to a cryptography RSA public key object.
    
    Args:
        jwk_key (dict): The JWK object with RSA parameters
        
    Returns:
        RSAPublicKey: The cryptography RSA public key object
        
    Raises:
        InvalidJwkException: If key conversion fails
    """
    try:
        # Decode base64url encoded n and e parameters
        n_bytes = _base64url_decode(jwk_key['n'])
        e_bytes = _base64url_decode(jwk_key['e'])
    except Exception as decode_err:
        raise InvalidJwkException('Invalid base64url encoding in JWK parameters', decode_err)
    
    try:
        # Convert bytes to integers
        n = int.from_bytes(n_bytes, byteorder='big')
        e = int.from_bytes(e_bytes, byteorder='big')
        
        # Create RSA public key
        public_numbers = rsa.RSAPublicNumbers(e, n)
        public_key = public_numbers.public_key(default_backend())
        
        return public_key
    except Exception as key_err:
        raise InvalidJwkException('Failed to create RSA public key from JWK', key_err)


def parse(jwt_token):
    """
    Parse a JWT token and extract its header, payload, and signature components.
    
    Args:
        jwt_token (str): The JWT token to parse
        
    Returns:
        dict: Dictionary containing:
            - header (dict): Decoded JWT header
            - payload (dict): Decoded JWT payload
            - signature (str): Base64url encoded signature
            - raw_header (str): Raw base64url encoded header
            - raw_payload (str): Raw base64url encoded payload
            
    Raises:
        InvalidJwtException: If the JWT token is invalid or malformed
    """
    if jwt_token is None:
        raise InvalidJwtException('JWT token is null or undefined')
    
    if not isinstance(jwt_token, str):
        raise InvalidJwtException('JWT token must be a string')
    
    token_parts = jwt_token.split('.')
    if len(token_parts) != 3:
        raise InvalidJwtException('Invalid JWT token format: expected 3 parts separated by dots')
    
    # Validate that all parts are non-empty
    if not token_parts[0] or not token_parts[1] or not token_parts[2]:
        raise InvalidJwtException('Malformed JWT : JWT provided does not conform to the proper structure for JWT')
    
    try:
        # Decode header and payload
        header = _decode_jwt_part(token_parts[0], 'header')
        payload = _decode_jwt_part(token_parts[1], 'payload')
        signature = token_parts[2]
        
        return {
            'header': header,
            'payload': payload,
            'signature': signature,
            'raw_header': token_parts[0],
            'raw_payload': token_parts[1]
        }
    except InvalidJwtException:
        # Re-raise our custom exceptions
        raise
    except Exception as err:
        raise InvalidJwtException('Malformed JWT cannot be parsed', err)


def verify_jwt(jwt_token, public_key):
    """
    Verify a JWT token using an RSA public key.
    
    This function validates the JWT signature using the provided RSA public key
    in JWK format. It supports RS256, RS384, and RS512 signing algorithms.
    
    Args:
        jwt_token (str): The JWT token to verify
        public_key (dict or str): The RSA public key (JWK object or JSON string)
        
    Raises:
        InvalidJwtException: If JWT parsing fails
        InvalidJwkException: If the public key is invalid
        JwtSignatureValidationException: If signature verification fails or
                                         if the algorithm is unsupported
    """
    if not public_key:
        raise JwtSignatureValidationException('No public key provided')
    
    if not jwt_token:
        raise JwtSignatureValidationException('JWT token is null or undefined')
    
    # Parse the JWT token
    parsed_jwt = parse(jwt_token)
    
    header = parsed_jwt['header']
    signature = parsed_jwt['signature']
    raw_header = parsed_jwt['raw_header']
    raw_payload = parsed_jwt['raw_payload']
    
    # Get the algorithm from header
    algorithm = header.get('alg')
    if not algorithm:
        raise JwtSignatureValidationException('JWT header missing algorithm (alg) field')
    
    # Check if algorithm is supported
    hash_algorithm = SUPPORTED_ALGORITHMS.get(algorithm)
    if not hash_algorithm:
        supported = ', '.join(SUPPORTED_ALGORITHMS.keys())
        raise JwtSignatureValidationException(
            'Unsupported JWT algorithm: {}. Supported algorithms: {}'.format(algorithm, supported)
        )
    
    # Validate and parse the JWK public key
    jwk_key = _validate_and_parse_jwk(public_key)
    
    # Convert JWK to cryptography public key object
    rsa_public_key = _convert_jwk_to_public_key(jwk_key)
    
    # Prepare signing input (header.payload)
    signing_input = '{}.{}'.format(raw_header, raw_payload)
    signing_input_bytes = signing_input.encode('utf-8')
    
    # Decode the signature from base64url
    try:
        signature_bytes = _base64url_decode(signature)
    except Exception as sig_decode_err:
        raise JwtSignatureValidationException(
            'Invalid base64url encoding in JWT signature', sig_decode_err
        )
    
    # Verify the signature
    try:
        rsa_public_key.verify(
            signature_bytes,
            signing_input_bytes,
            padding.PKCS1v15(),
            hash_algorithm
        )
    except Exception as verify_err:
        raise JwtSignatureValidationException('JWT signature verification failed', verify_err)


def get_rsa_public_key_from_jwk(jwk_json_string):
    """
    Extract an RSA public key from a JWK JSON string.
    
    Args:
        jwk_json_string (str): The JWK JSON string containing the RSA key
        
    Returns:
        dict: The RSA public key object (JWK)
        
    Raises:
        InvalidJwkException: If the JWK is invalid or not an RSA key
    """
    try:
        jwk_data = json.loads(jwk_json_string)
        if jwk_data.get('kty') != 'RSA':
            raise InvalidJwkException('JWK Algorithm mismatch. Expected algorithm : RSA')
        return jwk_data
    except InvalidJwkException:
        raise
    except Exception as err:
        raise InvalidJwkException('Failed to parse JWK or extract RSA public key', err)
