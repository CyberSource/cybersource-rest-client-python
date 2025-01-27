
import json
import time
# from jose import jwe
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import datetime

import json
import time
import base64
import logging
from datetime import datetime
from wsgiref.handlers import format_date_time
from time import mktime
from jwcrypto import jwe, jwk
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import jwt
from authenticationsdk.util.Cache import FileCache
from authenticationsdk.util.GlobalLabelParameters import *
# from jose import jwe
# from jose.constants import ALGORITHMS
from cryptography.hazmat.primitives import serialization
import json
from jwcrypto import jwk, jwe
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend



class MLEUtility:
    class MLEException(Exception):
        def __init__(self, message, errors=None):
            super().__init__(message)
            self.errors = errors
            

    @staticmethod
    def check_is_mle_for_api(merchant_config, isMLESupportedByCybsForApi, operationIds):
        isMLEForAPI = False
        if isMLESupportedByCybsForApi and merchant_config.get_useMLEGlobally():
            isMLEForAPI = True
        operation_array = [op_id.strip() for op_id in operationIds.split(",")]
        map_to_control_mle = merchant_config.get_mapToControlMLEonAPI()
        if map_to_control_mle is not None and map_to_control_mle:
            for op_id in operation_array:
                if op_id in map_to_control_mle:
                    isMLEForAPI = map_to_control_mle[op_id]
                    break
        return isMLEForAPI



    @staticmethod
    def encrypt_request_payload(merchant_config, requestBody):
        # Load the x509 certificate
        cert = MLEUtility.get_certificate(merchant_config)
        
        # Extract the public key from the certificate
        public_key = cert.public_key()
        
        # Extract the serial number from the certificate
        serial_number = MLEUtility.extract_serial_number(cert)
        
        return requestBody
        
        # return encrypted_json



    @staticmethod
    def get_certificate(merchant_config):
        cache_obj = FileCache()
        try:
            cert_data = cache_obj.grab_file_mle(merchant_config, merchant_config.key_file_path, merchant_config.key_file_name)
            certificate = cert_data[0]
            if certificate is not None:
                return certificate
            else:
                raise MLEUtility.MLEException(f"No certificate found for MLE for given mleKeyAlias {merchant_config.get_mleKeyAlias()} in p12 file {merchant_config.key_file_name}.p12")
        except KeyError:
            raise MLEUtility.MLEException(f"No certificate found matching the MLE key alias: {merchant_config.get_mleKeyAlias()}")
        except Exception as e:
            raise MLEUtility.MLEException(f"Unable to load PEM file: {str(e)}")

    @staticmethod
    def extract_serial_number(x509_certificate):
        serial_number = None
        serial_number_prefix = "SERIALNUMBER="
        principal = x509_certificate.subject.rfc4514_string().upper()
        beg = principal.find(serial_number_prefix)
        if beg >= 0:
            #check if using this is required.
            end = principal.find(",", beg)
            if end == -1:
                end = len(principal)
            print("m here fr s no")
            serial_number = principal[beg + len(serial_number_prefix):end]
        else:
            for attribute in x509_certificate.subject:
                if attribute.oid == x509.NameOID.SERIAL_NUMBER:
                    serial_number = attribute.value
                    print("m there fr s no")
                    break
            else:
                logging.warning("Serial number not found in MLE certificate for alias.")
                serial_number = str(x509_certificate.serial_number)
        print("serial number", serial_number)
        return serial_number
     
    # @staticmethod
    # def create_json_object(jwe_token):
    #     return json.dumps({"encryptedRequest": jwe_token})