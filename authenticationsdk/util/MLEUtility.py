import json
import time
from datetime import datetime, timezone

from cryptography import x509
from jwcrypto import jwk, jwe

from authenticationsdk.util.Cache import FileCache
from authenticationsdk.util.GlobalLabelParameters import GlobalLabelParameters
import CyberSource.logging.log_factory as LogFactory

class MLEUtility:
    class MLEException(Exception):
        def __init__(self, message, errors=None):
            super().__init__(message)
            self.errors = errors

    @staticmethod
    def check_is_mle_for_api(merchant_config, is_mle_supported_by_cybs_for_api, operation_ids):

        is_mle_for_api = False
        if is_mle_supported_by_cybs_for_api and merchant_config.get_useMLEGlobally():
            is_mle_for_api = True
        operation_array = [op_id.strip() for op_id in operation_ids.split(",")]
        map_to_control_mle = merchant_config.get_mapToControlMLEonAPI()
        if map_to_control_mle is not None and map_to_control_mle:
            for op_id in operation_array:
                if op_id in map_to_control_mle:
                    is_mle_for_api = map_to_control_mle[op_id]
                    break
        return is_mle_for_api

    @staticmethod
    def encrypt_request_payload(merchant_config, request_body):
        if request_body is None or request_body == "":
            return request_body

        logger = LogFactory.setup_logger(__name__, merchant_config.log_config)
             
        if merchant_config.log_config.enable_log:
            logger.debug(f"{GlobalLabelParameters.MESSAGE_BEFORE_MLE_REQUEST}{request_body}")

        cert = MLEUtility.get_mle_certificate(merchant_config, logger)

        try:
            serialized_jwe_token = MLEUtility.generate_token(cert, request_body, merchant_config.log_config, logger)
            mleRequest = MLEUtility.create_json_object(serialized_jwe_token)
            if merchant_config.log_config.enable_log:
                logger.debug(f"{GlobalLabelParameters.MESSAGE_AFTER_MLE_REQUEST}{mleRequest}")
            return mleRequest

        except Exception as e:
            if merchant_config.log_config.enable_log:
                logger.error(f"Error encrypting request payload.")
            raise MLEUtility.MLEException(f"Error encrypting request payload.")

    @staticmethod
    def generate_token(cert, request_body, log_config, logger):
        public_key = cert.public_key()
        serial_number = MLEUtility.extract_serial_number(cert, log_config, logger)

        jwk_key = jwk.JWK.from_pyca(public_key)
        payload = request_body.encode('utf-8')

        header = {
            "alg": "RSA-OAEP-256",
            "enc": "A256GCM",
            "cty": "JWT",
            "kid": serial_number,
            "iat": int(time.time())
        }

        jwe_token = jwe.JWE(plaintext=payload, protected=json.dumps(header))
        jwe_token.add_recipient(jwk_key)

        return jwe_token.serialize(compact=True)

    @staticmethod
    def get_mle_certificate(merchant_config, logger):
        cache_obj = FileCache()
        try:
            cert_data = cache_obj.grab_file(merchant_config, merchant_config.key_file_path, merchant_config.key_file_name)
            mle_certificate_x509 = cert_data[3]
            if mle_certificate_x509 is not None:
                MLEUtility.validate_certificate_expiry(mle_certificate_x509, merchant_config.get_mleKeyAlias(), merchant_config.log_config, logger)
                return mle_certificate_x509
            else:
                if merchant_config.log_config.enable_log:
                    logger.error(f"No certificate found for MLE for given mleKeyAlias {merchant_config.get_mleKeyAlias()} in p12 file {merchant_config.key_file_name}.p12")
                raise MLEUtility.MLEException(f"No certificate found for MLE for given mleKeyAlias {merchant_config.get_mleKeyAlias()} in p12 file {merchant_config.key_file_name}.p12")
        except KeyError:
            if merchant_config.log_config.enable_log:
                logger.error(f"No certificate found for MLE for given mleKeyAlias {merchant_config.get_mleKeyAlias()} in p12 file {merchant_config.key_file_name}.p12")
            raise MLEUtility.MLEException(f"No certificate found for MLE for given mleKeyAlias {merchant_config.get_mleKeyAlias()} in p12 file {merchant_config.key_file_name}.p12")
        except Exception as e:
            if merchant_config.log_config.enable_log:
                logger.error(f"Unable to load certificate: {str(e)}")
            raise MLEUtility.MLEException(f"Unable to load PEM file: {str(e)}")

    @staticmethod
    def extract_serial_number(x509_certificate, log_config, logger):
        serial_number = None

        for attribute in x509_certificate.subject:
            if attribute.oid == x509.NameOID.SERIAL_NUMBER:
                serial_number = attribute.value
                break
        if serial_number is None:
            if log_config.enable_log:
                logger.warning("Serial number not found in MLE certificate for alias.")
                serial_number = str(x509_certificate.serial_number)
        return serial_number

    @staticmethod
    def create_json_object(jwe_token):
        return json.dumps({"encryptedRequest": jwe_token})

    @staticmethod
    def validate_certificate_expiry(certificate, key_alias, log_config, logger):
        try:
            if certificate.not_valid_after_utc < datetime.now(timezone.utc):
                if log_config.enable_log:
                    logger.warning(f"Certificate with MLE alias {key_alias} is expired as of {certificate.not_valid_after_utc}. Please update p12 file.")
                    # raise Exception(f"Certificate with MLE alias {key_alias} is expired.")
            else:
                time_to_expire = (certificate.not_valid_after_utc - datetime.now(timezone.utc)).total_seconds()
                if time_to_expire < GlobalLabelParameters.CERTIFICATE_EXPIRY_DATE_WARNING_DAYS * 24 * 60 * 60:
                    if log_config.enable_log:
                        logger.warning(f"Certificate for MLE with alias {key_alias} is going to expire on {certificate.not_valid_after_utc}. Please update p12 file before that.")
        except Exception as e:
            if log_config.enable_log:
                logger.error(f"Error while checking certificate expiry: {str(e)}")