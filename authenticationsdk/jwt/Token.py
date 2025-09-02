import jwt
from authenticationsdk.payloaddigest.PayLoadDigest import *
from authenticationsdk.core.TokenGeneration import *
from authenticationsdk.util.Cache import *


class JwtSignatureToken(TokenGeneration):
    def __init__(self):
        self.merchant_config = None
        self.request_body = None
        self.jwt_method = None
        self.date = None
        self.request_json_path_data = None

    def jwt_signature_token(self, mconfig, date_time, request_type_method, request_json_path_data=None):
        self.merchant_config = mconfig
        self.jwt_method = request_type_method
        self.date = date_time
        self.request_json_path_data = request_json_path_data

    def get_token(self):
        return self.set_token()

    # This function decides to call the methods responsible for token generation based on the jwt_method
    def set_token(self):
        token = ""

        if self.jwt_method.upper() == GlobalLabelParameters.GET or self.jwt_method.upper() == GlobalLabelParameters.DELETE:
            token = self.token_for_get_and_delete()
        elif self.jwt_method.upper() == GlobalLabelParameters.POST or self.jwt_method.upper() == GlobalLabelParameters.PUT or self.jwt_method.upper() == GlobalLabelParameters.PATCH:
            token = self.token_for_post_and_put_and_patch()

        return token

    # This function has the logic to generate token when the Jwt_method is get
    def token_for_get_and_delete(self):
        # Setting the jwt body for JWT-get
        jwt_body = {GlobalLabelParameters.JWT_TIME: self.date}
        # reading the p12 file from cache memory
        cache_obj = FileCache()
        cache_memory = cache_obj.fetch_cached_p12_certificate(self.merchant_config, self.merchant_config.p12KeyFilePath, self.merchant_config.key_password)
        der_cert_string = cache_memory.certificate
        private_key = cache_memory.private_key
        # setting the headers  -merchant_id and the public key
        headers_jwt = {GlobalLabelParameters.MERCHANT_ID: str(self.merchant_config.key_alias)}
        public_key_list = ([])
        public_key_list.append(der_cert_string.decode("utf-8"))
        public_key_headers = {GlobalLabelParameters.PUBLIC_KEY: public_key_list}
        headers_jwt.update(public_key_headers)


        # generating the token of jwt
        encoded_jwt = jwt.encode(jwt_body, private_key, algorithm='RS256', headers=headers_jwt)

        return encoded_jwt

    def token_for_post_and_put_and_patch(self):
        digest_payload_obj = DigestAndPayload()
        digest = digest_payload_obj.string_digest_generation(
            self.request_json_path_data)
        # Setting the jwt body for JWT-post

        jwt_body = {GlobalLabelParameters.JWT_DIGEST: digest.decode("utf-8"), GlobalLabelParameters.JWT_ALGORITHM: "SHA-256", GlobalLabelParameters.JWT_TIME: self.date}
        # reading the p12 file from cache memory
        cache_obj = FileCache()
        cache_memory = cache_obj.fetch_cached_p12_certificate(self.merchant_config, self.merchant_config.p12KeyFilePath, self.merchant_config.key_password)
        der_cert_string = cache_memory.certificate
        private_key = cache_memory.private_key
        # setting the headers  -merchant_id and the public key
        headers_jwt = {GlobalLabelParameters.MERCHANT_ID: str(self.merchant_config.key_alias)}
        public_key_list = ([])
        public_key_list.append(der_cert_string.decode("utf-8"))
        public_key_headers = {GlobalLabelParameters.PUBLIC_KEY: public_key_list}
        headers_jwt.update(public_key_headers)
        # generating the token of jwt
        encoded_jwt = jwt.encode(jwt_body, private_key, algorithm='RS256', headers=headers_jwt)

        return encoded_jwt
