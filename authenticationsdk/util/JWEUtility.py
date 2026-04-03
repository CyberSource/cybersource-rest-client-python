from jwcrypto import jwe

from authenticationsdk.util.Cache import FileCache

from typing_extensions import deprecated


class JWEUtility:
    @staticmethod
    @deprecated("This method has been marked as Deprecated and will be removed in coming releases. Use decrypt_jwe_using_private_key(private_key, encoded_message) instead.")
    def decrypt_jwe_using_pem(merchant_config, jwe_base_64_data):
        jwe_token = jwe.JWE()
        cache_obj = FileCache()
        cached_private_key = cache_obj.get_cached_private_key_from_pem(merchant_config.get_jwePEMFileDirectory(), 'privateKeyFromPEMFile')
        jwe_token.deserialize(jwe_base_64_data, cached_private_key)
        payload = jwe_token.payload
        return payload.decode('utf-8')

    @staticmethod
    def decrypt_jwe_using_private_key(private_key, encoded_message):
        jwe_token = jwe.JWE()
        jwe_token.deserialize(encoded_message, private_key)
        payload = jwe_token.payload
        return payload.decode('utf-8')

