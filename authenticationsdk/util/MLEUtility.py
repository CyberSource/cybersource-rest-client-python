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
from jwcrypto.common import json_encode

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



    # @staticmethod
    # def encrypt_request_payload_jwcrypto_without_headers(merchant_config, requestBody):
    # # Load the X.509 certificate
    #     cert = MLEUtility.get_certificate(merchant_config)
    
    # # Extract the public key from the certificate
    #     public_key = cert.public_key()
    
    # # Convert the public key to a JWK (JSON Web Key)
    #     jwk_key = jwk.JWK.from_pyca(public_key)
        
    #     payload = json_encode(requestBody).encode('utf-8')
        
    #     print("payload", payload)

    
    # # Create a JWE object
    #     jwetoken = jwe.JWE(plaintext=payload, 
    #                        protected={"alg": "RSA-OAEP", "enc": "A256GCM"})
    
    
    # # Encrypt the payload using the public key
    #     jwetoken.add_recipient(jwk_key)
    
    # # Serialize the JWE token to compact format
    #     encrypted_request_body = jwetoken.serialize(compact=True)
        
    #     print("encrypted_request_body", encrypted_request_body)

    
    # # Return the encrypted request body in JSON format
    #     return json.dumps({"encryptedRequest": encrypted_request_body})
    
    

    # @staticmethod
    # def encrypt_request_payload_jwcrypto_with_headers(merchant_config, requestBody):
    #     if requestBody is not None:
    #         token = MLEUtility.generate_jwe_token(requestBody, merchant_config)
    #         print("token", token)

    #         return token
    #     else:
    #         return requestBody

    # @staticmethod
    # def generate_jwe_token(requestBody, merchant_config):
    #     print("requestBody", requestBody)
    

        
    #     # Get the MLE cert and verify the expiry of cert
    #     cert = MLEUtility.get_certificate(merchant_config)
    #     print("A")
    #     # is_cert_expired = MLEUtility.verify_is_certificate_expired(cert, merchant_config.get_mleKeyAlias(), logger)
    #     # if is_cert_expired:
    #     #     raise Exception(f"Certificate for MLE with alias {merchant_config.get_mleKeyAlias()} is expired in {merchant_config.key_file_name}.p12")

    #     custom_headers = {
    #         "iat": int(time.time())  # epoch time in seconds
    #     }
    #     print("B")
    #     serial_number = MLEUtility.extract_serial_number(cert)
    #     print("C")
    #     headers = {
    #         "alg": "RSA-OAEP-256",
    #         "enc": "A256GCM",
    #         "cty": "JWT",
    #         "kid": serial_number,
    #         **custom_headers
    #     }
    #     print("D")


    #     # if isinstance(requestBody, dict):
    #     #     requestBody = json.dumps(requestBody)
            
    #     print("requestBody11", requestBody)

    #     payload = requestBody.encode()
    #     print("E")
    #     public_key = cert.public_key()
    #     print("F")
    #     jwk_key = jwk.JWK.from_pyca(public_key)
    #     print("G")

    #     jwetoken = jwe.JWE(plaintext=payload, protected=headers)
    #     print("H")
    #     jwetoken.add_recipient(jwk_key)
    #     print("I")
        
    #     encrypted_request_body = jwetoken.serialize(compact=True)


    #     return json.dumps({"encryptedRequest": encrypted_request_body})


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