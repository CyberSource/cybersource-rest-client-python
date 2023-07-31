from jwcrypto import jwe, jwk


class JWEUtility:
    @staticmethod
    def get_private_key_from_pem(pem_file_path):
        with open(pem_file_path, 'r') as pem_file:
            cert = pem_file.read()
            private_key = jwk.JWK.from_pem(cert.encode('utf-8'))
            return private_key

    @staticmethod
    def decrypt_jwe_using_pem(merchant_config, jwe_base_64_data):
        jwe_token = jwe.JWE()
        private_key = JWEUtility.get_private_key_from_pem(merchant_config.get_jwePEMFileDirectory())
        jwe_token.deserialize(jwe_base_64_data, private_key)
        payload = jwe_token.payload
        return payload.decode('utf-8')
