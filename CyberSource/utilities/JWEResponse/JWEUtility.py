from authenticationsdk.util.JWEUtility import JWEUtility as authJWEUtility
from .JWEException.JWEException import JWEException


class JWEUtility:

    @staticmethod
    def decrypt_jwe_response(encoded_response, merchant_config):
        try:
            return authJWEUtility.decrypt_jwe_using_pem(merchant_config, encoded_response)
        except Exception as e:
            raise JWEException(e)

