import json
import time
import os

from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import NameOID
from jwcrypto import jwe, jwk

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
                MLEUtility.logger.debug(GlobalLabelParameters.LOG_NETWORK_RESPONSE_BEFORE_MLE_DECRYPTION + ' ' + str(mle_response_body))
                
            decrypted_response = JWEUtility.decrypt_jwe_response_using_private_key(
                private_key_jwk, jwe_response_token
            )
            
            if MLEUtility.logger:
                MLEUtility.logger.debug(GlobalLabelParameters.LOG_NETWORK_RESPONSE_AFTER_MLE_DECRYPTION + ' ' + str(decrypted_response))
                
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
            response_json = json.loads(mle_response_body)
            return response_json.get("encryptedResponse")
        except Exception as e:
            if MLEUtility.logger:
                MLEUtility.logger.error("Failed to extract response MLE token from response body.")
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
            error_msg = f"Serial number not found in MLE certificate for alias {merchant_config.requestMleKeyAlias} in {merchant_config.p12KeyFilePath}"
            logger.error(error_msg)
            raise ValueError(error_msg)

        return serial_number

    @staticmethod
    def create_json_object(jwe_token):
        return json.dumps({"encryptedRequest": jwe_token})
    
    @staticmethod
    def extract_response_mle_kid(file_path, password, merchant_id, logger):
        """
        Extracts the serial number (KID) from a certificate's subject in a P12 file where CN matches the merchantId.
        
        Args:
            file_path (str): Path to the P12 file
            password (str): Password for the P12 file
            merchant_id (str): The merchant ID to match against the CN in the certificate subject
            logger: Logger instance for logging
            
        Returns:
            str: The serial number extracted from the certificate's subject attributes
            
        Raises:
            ValueError: If the certificate with matching CN is not found or serial number is missing
        """
        try:
            logger.debug(f"Extracting MLE KID from P12 file: {file_path} for merchantId: {merchant_id}")
            
            # Get cached P12 object
            cache_obj = MLEUtility.get_cache()
            certificates = cache_obj.fetch_cached_p12_from_file(file_path, password, logger)
            
            if not certificates:
                error_msg = f"No certificates found in P12 file: {file_path}"
                logger.error(error_msg)
                raise ValueError(error_msg)
            
            logger.debug(f"Found {len(certificates)} certificate(s) in P12 file")
            
            # Iterate through certificates to find one with matching CN
            for i, cert in enumerate(certificates):
                try:
                    # Extract CN from certificate subject
                    cn_attribute = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
                    if not cn_attribute:
                        logger.debug(f"Certificate {i + 1} has no CN in subject, skipping")
                        continue
                    
                    cn = cn_attribute[0].value
                    logger.debug(f"Certificate {i + 1} CN: {cn}")
                    
                    # Check if CN matches merchantId (case-insensitive)
                    if cn.lower() == merchant_id.lower():
                        logger.debug(f"Found certificate with matching CN: {cn}")
                        
                        # Extract serial number from subject attributes
                        serial_number_attr = cert.subject.get_attributes_for_oid(NameOID.SERIAL_NUMBER)
                        if not serial_number_attr:
                            error_msg = f"Serial number not found in certificate subject for CN={cn}"
                            logger.error(error_msg)
                            raise ValueError(error_msg)
                        
                        serial_number = serial_number_attr[0].value
                        logger.debug(f"Serial number (MLE KID) extracted: {serial_number}")
                        
                        return serial_number
                except Exception as e:
                    logger.debug(f"Error processing certificate {i + 1}: {str(e)}")
                    continue
            
            # If we get here, no matching certificate was found
            error_msg = f"No certificate with CN matching merchantId ({merchant_id}) found in P12 file: {file_path}"
            logger.error(error_msg)
            raise ValueError(error_msg)
            
        except Exception as e:
            error_msg = f"Error extracting MLE KID from P12 file: {file_path}: {str(e)}"
            logger.error(error_msg)
            raise ValueError(error_msg)
    
    @staticmethod
    def validate_and_auto_extract_response_mle_kid(merchant_config, logger):
        """
        Validates and auto-extracts responseMleKID if necessary.
        
        This function attempts to auto-extract the response MLE KID from CyberSource P12 files,
        or uses the manually configured value if provided.
        
        Args:
            merchant_config: Merchant configuration object
            logger: Logger instance for logging
            
        Returns:
            str: The validated or auto-extracted responseMleKID
            
        Raises:
            ValueError: If responseMleKID is not available and cannot be auto-extracted
        """
        logger.debug("Validating responseMleKID for JWT token generation")
        
        # Variable to store auto-extracted KID
        cybs_kid = None
        
        # First, try to auto-extract from CyberSource P12 certificate if applicable
        has_valid_file_path = (
            hasattr(merchant_config, 'responseMlePrivateKeyFilePath') and
            isinstance(merchant_config.responseMlePrivateKeyFilePath, str) and
            merchant_config.responseMlePrivateKeyFilePath.strip()
        )
        
        if has_valid_file_path:
            import os
            file_extension = os.path.splitext(merchant_config.responseMlePrivateKeyFilePath)[1].lower()
            is_p12_file = file_extension in ('.p12', '.pfx')
            
            if is_p12_file:
                logger.debug("P12/PFX file detected, checking if it is a CyberSource certificate")
                
                from authenticationsdk.util.Utility import is_cybersource_p12
                is_cybs_p12 = is_cybersource_p12(
                    merchant_config.responseMlePrivateKeyFilePath,
                    merchant_config.responseMlePrivateKeyFilePassword,
                    logger
                )
                
                if is_cybs_p12:
                    logger.debug("Detected CyberSource P12 file, attempting to auto-extract responseMleKID")
                    try:
                        cybs_kid = MLEUtility.extract_response_mle_kid(
                            merchant_config.responseMlePrivateKeyFilePath,
                            merchant_config.responseMlePrivateKeyFilePassword,
                            merchant_config.merchant_id,
                            logger
                        )
                        logger.info("Successfully auto-extracted responseMleKID from CyberSource P12 certificate")
                    except Exception as e:
                        logger.warning(f"Failed to auto-extract responseMleKID from P12 file: {str(e)}. Will check for manually configured value.")
                else:
                    logger.debug("P12 file is not a CyberSource-generated certificate, skipping auto-extraction")
            else:
                logger.debug("Private key file is not a P12/PFX file, skipping auto-extraction")
        else:
            logger.debug("No valid private key file path provided, skipping auto-extraction")
        
        # Get manually configured responseMleKID
        configured_kid = None
        if (hasattr(merchant_config, 'responseMleKID') and 
            isinstance(merchant_config.responseMleKID, str) and 
            merchant_config.responseMleKID.strip()):
            configured_kid = merchant_config.responseMleKID.strip()
        
        # Determine which value to use
        if not cybs_kid and not configured_kid:
            error_msg = (
                "responseMleKID is required when response MLE is enabled. "
                "Could not auto-extract from certificate and no manual configuration provided. "
                "Please provide responseMleKID explicitly in your configuration."
            )
            logger.error(error_msg)
            raise ValueError(error_msg)
        
        if cybs_kid and not configured_kid:
            logger.debug("Using auto-extracted responseMleKID from CyberSource P12 certificate")
            return cybs_kid
        
        if not cybs_kid and configured_kid:
            logger.debug("Using manually configured responseMleKID")
            return configured_kid
        
        # Both exist
        if cybs_kid != configured_kid:
            logger.warning("Auto-extracted responseMleKID does not match manually configured responseMleKID. Using configured value as preference.")
        else:
            logger.debug("Auto-extracted responseMleKID matches manually configured value")
        
        return configured_kid