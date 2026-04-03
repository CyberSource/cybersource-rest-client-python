# coding: utf-8
"""
Custom exception classes for JWT operations.

This module provides specialized exception classes for handling JWT-related errors,
including invalid JWT tokens, invalid JWK (JSON Web Key) formats, and signature
validation failures.
"""


class InvalidJwkException(Exception):
    """
    Exception raised when a JWK (JSON Web Key) is invalid or malformed.
    
    This exception is used for errors related to:
    - Invalid JWK JSON format
    - Missing required JWK parameters (e.g., n, e for RSA keys)
    - Incorrect key type (kty)
    - Base64url decoding errors in JWK parameters
    
    Args:
        message (str): Error message describing the invalid JWK
        cause (Exception, optional): The underlying exception that caused this error
    """
    
    def __init__(self, message, cause=None):
        """
        Initialize the InvalidJwkException.
        
        Args:
            message (str): Error message describing the invalid JWK
            cause (Exception, optional): The underlying exception that caused this error
        """
        super(InvalidJwkException, self).__init__(message)
        self.cause = cause
        self.message = message
        
        # Chain the exception if cause is provided
        if cause:
            self.__cause__ = cause


class InvalidJwtException(Exception):
    """
    Exception raised when a JWT token is invalid or malformed.
    
    This exception is used for errors related to:
    - Invalid JWT token format (not 3 parts separated by dots)
    - Empty or null JWT tokens
    - Base64url decoding errors
    - Invalid JSON in header or payload
    
    Args:
        message (str): Error message describing the invalid JWT token
        cause (Exception, optional): The underlying exception that caused this error
    """
    
    def __init__(self, message, cause=None):
        """
        Initialize the InvalidJwtException.
        
        Args:
            message (str): Error message describing the invalid JWT token
            cause (Exception, optional): The underlying exception that caused this error
        """
        super(InvalidJwtException, self).__init__(message)
        self.cause = cause
        self.message = message
        
        # Chain the exception if cause is provided
        if cause:
            self.__cause__ = cause


class JwtSignatureValidationException(Exception):
    """
    Exception raised when JWT signature validation fails.
    
    This exception is used for errors related to:
    - Signature verification failures
    - Missing or unsupported signing algorithms
    - Missing public key
    - Cryptographic verification errors
    
    Args:
        message (str): Error message describing the signature validation failure
        cause (Exception, optional): The underlying exception that caused this error
    """
    
    def __init__(self, message, cause=None):
        """
        Initialize the JwtSignatureValidationException.
        
        Args:
            message (str): Error message describing the signature validation failure
            cause (Exception, optional): The underlying exception that caused this error
        """
        super(JwtSignatureValidationException, self).__init__(message)
        self.cause = cause
        self.message = message
        
        # Chain the exception if cause is provided
        if cause:
            self.__cause__ = cause
