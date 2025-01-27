import json
import time
from datetime import datetime, timezone

from cryptography import x509
from jwcrypto import jwk, jwe

from authenticationsdk.util.Cache import FileCache
from authenticationsdk.util.GlobalLabelParameters import GlobalLabelParameters
import CyberSource.logging.log_factory as LogFactory

class MLEUtility:
    logger = None

    @staticmethod
    def setup_logger(merchant_config):
        MLEUtility.logger = LogFactory.setup_logger(__name__, merchant_config.log_config)

    class MLEException(Exception):
        def __init__(self, message, errors=None):
            super().__init__(message)
            self.errors = errors

    @staticmethod
    def check_is_mle_for_api(merchant_config, is_mle_supported_by_cybs_for_api, operation_ids):
        if MLEUtility.logger is None:
            MLEUtility.setup_logger(merchant_config)
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
        try:
            cert = MLEUtility.get_certificate(merchant_config)
        except Exception as e:
            raise MLEUtility.MLEException(f"Unable to load certificate: {str(e)}")

        try:
            public_key = cert.public_key()
            serial_number = MLEUtility.extract_serial_number(cert)

            jwk_key = jwk.JWK.from_pyca(public_key)

            payload = request_body.encode('utf-8')


            header = {
                "alg": "RSA-OAEP-256",
                "enc": "A256GCM",
                "cty": "JWT",
                "kid": serial_number,
                "iat": int(time.time())
            }

            jwe_token = jwe.JWE(plaintext=payload,
                                protected=json.dumps(header))

            jwe_token.add_recipient(jwk_key)

            encrypted_request_body = jwe_token.serialize(compact=True)
            MLEUtility.logger.info(f"Request payload encrypted successfully. {encrypted_request_body}")
            return MLEUtility.create_json_object(encrypted_request_body)
        except Exception as e:
            MLEUtility.logger.error(f"Error encrypting request payload: {str(e)}")
            raise MLEUtility.MLEException(f"Error encrypting request payload: {str(e)}")

    @staticmethod
    def get_certificate(merchant_config):
        cache_obj = FileCache()
        try:
            cert_data = cache_obj.grab_file_mle(merchant_config, merchant_config.key_file_path,
                                                merchant_config.key_file_name)
            certificate = cert_data[0]
            if certificate is not None:
                MLEUtility.validate_certificate_expiry(certificate, merchant_config.get_mleKeyAlias())
                MLEUtility.logger.info(f"Certificate found for MLE with alias {merchant_config.get_mleKeyAlias()}")
                return certificate
            else:
                MLEUtility.logger.error(
                    f"No certificate found for MLE for given mleKeyAlias {merchant_config.get_mleKeyAlias()} in p12 file {merchant_config.key_file_name}.p12")
                raise MLEUtility.MLEException(
                    f"No certificate found for MLE for given mleKeyAlias {merchant_config.get_mleKeyAlias()} in p12 file {merchant_config.key_file_name}.p12")
        except KeyError:
            MLEUtility.logger.error(
                f"No certificate found matching the MLE key alias: {merchant_config.get_mleKeyAlias()}")
            raise MLEUtility.MLEException(
                f"No certificate found matching the MLE key alias: {merchant_config.get_mleKeyAlias()}")
        except Exception as e:
            MLEUtility.logger.error(f"Unable to load certificate: {str(e)}")
            raise MLEUtility.MLEException(f"Unable to load PEM file: {str(e)}")

    @staticmethod
    def extract_serial_number(x509_certificate):
        serial_number = None
        serial_number_prefix = "SERIALNUMBER="
        principal = x509_certificate.subject.rfc4514_string().upper()
        beg = principal.find(serial_number_prefix)
        if beg >= 0:
            end = principal.find(",", beg)
            if end == -1:
                end = len(principal)
            serial_number = principal[beg + len(serial_number_prefix):end]
        else:
            for attribute in x509_certificate.subject:
                if attribute.oid == x509.NameOID.SERIAL_NUMBER:
                    serial_number = attribute.value
                    break
            else:
                MLEUtility.logger.warning("Serial number not found in MLE certificate for alias.")
                serial_number = str(x509_certificate.serial_number)
        return serial_number

    @staticmethod
    def create_json_object(jwe_token):
        return json.dumps({"encryptedRequest": jwe_token})

    @staticmethod
    def validate_certificate_expiry(certificate, key_alias):
        try:
            if certificate.not_valid_after_utc is None:
                MLEUtility.logger.info("Certificate for MLE doesn't have an expiry date.")
            elif certificate.not_valid_after_utc < datetime.now(timezone.utc):
                MLEUtility.logger.warning(
                    f"Certificate with MLE alias {key_alias} is expired as of {certificate.not_valid_after_utc}. Please update p12 file.")
            else:
                time_to_expire = (certificate.not_valid_after_utc - datetime.now(timezone.utc)).total_seconds()
                if time_to_expire < GlobalLabelParameters.CERTIFICATE_EXPIRY_DATE_WARNING_DAYS * 24 * 60 * 60:
                    MLEUtility.logger.warning(
                        f"Certificate for MLE with alias {key_alias} is going to expire on {certificate.not_valid_after_utc}. Please update p12 file before that.")
        except Exception as e:
            MLEUtility.logger.error(f"Error while checking certificate expiry: {str(e)}")
