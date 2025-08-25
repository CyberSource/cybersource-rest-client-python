import json
import time

from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import NameOID
from jwcrypto import jwe, jwk

from authenticationsdk.util.Cache import FileCache
from authenticationsdk.util.GlobalLabelParameters import GlobalLabelParameters
import CyberSource.logging.log_factory as LogFactory

class MLEUtility:
    logger = None

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
    def get_mle_certificate(merchant_config):
        cache_obj = FileCache()
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