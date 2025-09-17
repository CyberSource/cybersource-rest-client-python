import json
import time
import os

from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import NameOID
from jwcrypto import jwe, jwk
import json

from authenticationsdk.util.Cache import FileCache
from authenticationsdk.util.GlobalLabelParameters import GlobalLabelParameters
import CyberSource.logging.log_factory as LogFactory
from CyberSource.utilities.JWEResponse.JWEUtility import JWEUtility
from authenticationsdk.util.Utility import to_jwk_private_key

class MLEUtility:
    logger = None
    _cache = None  # Static cache instance
    
    @classmethod
    def get_cache(cls):
        """Get or create the shared cache instance"""
        if cls._cache is None:
            from authenticationsdk.util.Cache import FileCache
            cls._cache = FileCache()
        return cls._cache

    class MLEException(Exception):
        def __init__(self, message, errors=None):
            super().__init__(message)
            self.errors = errors

    @staticmethod
    def check_is_mle_for_api(merchant_config, inbound_mle_status, operation_ids):
        is_mle_for_api = False

        if str(inbound_mle_status).lower() == "optional" and merchant_config.get_enableRequestMLEForOptionalApisGlobally():
            is_mle_for_api = True

        if str(inbound_mle_status).lower() == "mandatory":
            is_mle_for_api = not merchant_config.get_disableRequestMLEForMandatoryApisGlobally()

        
        operation_array = [op_id.strip() for op_id in operation_ids.split(",")]
        # Use internalMapToControlRequestMLEonAPI instead of mapToControlMLEonAPI
        if (merchant_config.internalMapToControlRequestMLEonAPI is not None and 
            merchant_config.internalMapToControlRequestMLEonAPI):
            for op_id in operation_array:
                if op_id in merchant_config.internalMapToControlRequestMLEonAPI:
                    is_mle_for_api = merchant_config.internalMapToControlRequestMLEonAPI[op_id]
                    break
        return is_mle_for_api

    @staticmethod
    def check_is_response_mle_for_api(merchant_config, operation_ids):
        """
        Checks if response MLE should be enabled for the specified API operation
        
        Args:
            merchant_config: The merchant configuration object
            operation_ids: Comma-separated list of operation IDs
            
        Returns:
            bool: True if response MLE should be enabled, False otherwise
        """
        is_response_mle_for_api = False
        if merchant_config.get_enableResponseMleGlobally():
            is_response_mle_for_api = True
        operation_array = [op_id.strip() for op_id in operation_ids.split(",")]
        if (merchant_config.internalMapToControlResponseMLEonAPI is not None and 
            merchant_config.internalMapToControlResponseMLEonAPI):
            for op_id in operation_array:
                if op_id in merchant_config.internalMapToControlResponseMLEonAPI:
                    is_response_mle_for_api = merchant_config.internalMapToControlResponseMLEonAPI[op_id]
                    break
        return is_response_mle_for_api

    @staticmethod
    def encrypt_request_payload(merchant_config, request_body):
        if MLEUtility.logger is None:
            MLEUtility.logger = LogFactory.setup_logger(__name__, merchant_config.log_config)
        logger = MLEUtility.logger

        if request_body is None:
            return None

        payload = str(request_body)
        logger.debug(GlobalLabelParameters.MESSAGE_BEFORE_MLE_REQUEST + ' ' + payload)

        mle_certificate = MLEUtility.get_mle_certificate(merchant_config)

        # Special case: MLE Certificate is not currently available for HTTP Signature
        if (mle_certificate is None and merchant_config.authentication_type.lower() == GlobalLabelParameters.HTTP.lower()):
            logger.debug("The certificate to use for MLE for requests is not provided in the merchant configuration. Please ensure that the certificate path is provided.")
            logger.debug("Currently, MLE for requests using HTTP Signature as authentication is not supported by Cybersource. By default, the SDK will fall back to non-encrypted requests.")
            return request_body

        serial_number = MLEUtility.get_serial_number_from_certificate(mle_certificate, merchant_config)
        payload_bytes = payload.encode('utf-8')

        # Extract the public RSA key from the certificate
        public_key = mle_certificate.public_key()  # cryptography.x509.Certificate object

        # Convert public key to jwk
        rsa_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
        jwk_key = jwk.JWK.from_pem(rsa_pem)

        # Prepare JWE headers
        headers = {
            "alg": "RSA-OAEP-256",
            "enc": "A256GCM",
            "kid": serial_number,
            "iat": int(time.time())
        }

        # Create the JWE object and encrypt
        jwe_token = jwe.JWE(plaintext=payload_bytes, protected=json.dumps(headers))
        jwe_token.add_recipient(jwk_key)

        mle_request = MLEUtility.create_json_object(jwe_token.serialize(compact=True))
        logger.debug(GlobalLabelParameters.MESSAGE_AFTER_MLE_REQUEST + ' ' + str(mle_request))

        return mle_request
    
    @staticmethod
    def check_is_mle_encrypted_response(response_body):
        """
        Checks if the response is MLE encrypted.
        
        :param response_body: Response body as string
        :return: True if the response is MLE encrypted, False otherwise
        """
        if response_body is None or not response_body.strip():
            return False
            
        try:
            response_json = json.loads(response_body)
            # Check if the JSON has exactly one key named "encryptedResponse"
            if len(response_json) != 1:
                return False
                
            if "encryptedResponse" in response_json:
                value = response_json["encryptedResponse"]
                return isinstance(value, str)
                
            return False
        except Exception:
            # If JSON parsing fails, it's not a valid JSON thus not an MLE response
            return False
    
    @staticmethod
    def decrypt_mle_response_payload(merchant_config, mle_response_body):
        """
        Decrypts MLE encrypted response payload.
        
        :param merchant_config: Merchant configuration object
        :param mle_response_body: Encrypted response body
        :return: Decrypted response as string
        :raises MLEException: If decryption fails
        """
        
        if not MLEUtility.check_is_mle_encrypted_response(mle_response_body):
            raise MLEUtility.MLEException("Response body is not MLE encrypted.")
        
        try:
            # Get private key for decryption
            private_key = MLEUtility._get_mle_response_private_key(merchant_config)
            private_key_jwk = to_jwk_private_key(private_key)
            # Extract the JWE token
            jwe_response_token = MLEUtility._get_response_mle_token(mle_response_body)
            
            if not jwe_response_token:
                # If token extraction fails, return the original response
                return mle_response_body
                
            # Use the existing JWEUtility for decryption
            if MLEUtility.logger:
                MLEUtility.logger.debug(f"LOG_NETWORK_RESPONSE_BEFORE_MLE_DECRYPTION: {mle_response_body}")
                
            decrypted_response = JWEUtility.decrypt_jwe_response_using_private_key(
                private_key_jwk, jwe_response_token
            )
            
            if MLEUtility.logger:
                MLEUtility.logger.debug(f"LOG_NETWORK_RESPONSE_AFTER_MLE_DECRYPTION: {decrypted_response}")
                
            return decrypted_response
            
        except Exception as e:
            raise MLEUtility.MLEException(f"MLE Response decryption error: {str(e)}")
    
    @staticmethod
    def _get_response_mle_token(mle_response_body):
        """
        Extracts the JWE token from the MLE encrypted response.
        
        :param mle_response_body: MLE encrypted response body
        :return: JWE token string or None if extraction fails
        """
        try:
            import json
            response_json = json.loads(mle_response_body)
            return response_json.get("encryptedResponse")
        except Exception as e:
            if MLEUtility.logger:
                MLEUtility.logger.error(f"Failed to extract Response MLE token: {str(e)}")
            return None
    
    @staticmethod
    def _get_mle_response_private_key(merchant_config):
        """
        Gets the private key for Response MLE decryption.
        
        :param merchant_config: Merchant configuration object
        :return: Private key object for decryption
        :raises MLEException: If the private key cannot be obtained
        """
        # First priority - if privateKey is given in merchant config return that
        if hasattr(merchant_config, 'responseMlePrivateKey') and merchant_config.responseMlePrivateKey:
            return merchant_config.responseMlePrivateKey
            
        # Second priority - get the privateKey from the file path
        try:
            # Get from cache - directly use the cache instance
            cache_obj = MLEUtility.get_cache()
            
            try:
                private_key = cache_obj.get_mle_response_private_key(merchant_config)
                if private_key is None:
                    raise MLEUtility.MLEException("Failed to get Response MLE private key from cache")
                return private_key
            except Exception as e:
                raise MLEUtility.MLEException(f"Error getting Response MLE private key: {str(e)}")
                
        except Exception as e:
            raise MLEUtility.MLEException(f"Error loading Response MLE private key: {str(e)}")

    @staticmethod
    def get_mle_certificate(merchant_config):
        cache_obj = MLEUtility.get_cache()
        mle_certificate = cache_obj.get_request_mle_cert_from_cache(merchant_config)
        return mle_certificate

    @staticmethod
    def get_serial_number_from_certificate(certificate, merchant_config):
        if MLEUtility.logger is None:
            MLEUtility.logger = LogFactory.setup_logger(__name__, merchant_config.log_config)
        logger = MLEUtility.logger

        if certificate is None:
            raise ValueError("MLE certificate is null")

        # Get subject and look for 'serialNumber'
        subject = certificate.subject
        serial_number = None
        for attribute in subject:
            if attribute.oid == NameOID.SERIAL_NUMBER:
                serial_number = attribute.value
                break

        if not serial_number:
            logger.warning(f"Serial number not found in MLE certificate for alias {merchant_config.requestMleKeyAlias} in {merchant_config.p12KeyFilePath}.p12")
            # Use the hex serial number from the certificate as fallback
            return format(certificate.serial_number, 'x')

        return serial_number

    @staticmethod
    def create_json_object(jwe_token):
        return json.dumps({"encryptedRequest": jwe_token})