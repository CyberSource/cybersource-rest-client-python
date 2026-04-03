from authenticationsdk.util.JWEUtility import JWEUtility as authJWEUtility
from .JWEException.JWEException import JWEException
from typing_extensions import deprecated

class JWEUtility:

    @staticmethod
    @deprecated("This method has been marked as Deprecated and will be removed in coming releases. Use decrypt_jwe_response_using_private_key(private_key, encoded_response) instead.")
    def decrypt_jwe_response(encoded_response, merchant_config):
        try:
            return authJWEUtility.decrypt_jwe_using_pem(merchant_config, encoded_response)
        except Exception as e:
            raise JWEException(e)

    @staticmethod
    def decrypt_jwe_response_using_private_key(private_key, encoded_response):
        try:
            return authJWEUtility.decrypt_jwe_using_private_key(private_key, encoded_response)
        except Exception as e:
            raise JWEException(e)

