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

    def jwt_signature_token(self, mconfig, date_time):
        self.merchant_config = mconfig
        self.jwt_method = mconfig.request_type_method
        self.date = date_time

    def get_token(self):
        return self.set_token()

    # This function decides to call the methods responsible for token generation based on the jwt_method
    def set_token(self):
        token = ""

        if self.jwt_method.upper() == GlobalLabelParameters.GET:
            token = self.token_for_get()
        elif self.jwt_method.upper() == GlobalLabelParameters.POST:
            token = self.token_for_post()
        elif self.jwt_method.upper() == GlobalLabelParameters.PUT:
            token = self.token_for_put()
        elif self.jwt_method.upper() == GlobalLabelParameters.DELETE:
            token = self.token_for_delete()
        elif self.jwt_method.upper() == GlobalLabelParameters.PATCH:
            token = self.token_for_patch()

        return token

    # This function has the logic to generate token when the Jwt_method is get
    def token_for_get(self):

        # Setting the jwt body for JWT-get
        jwt_body = {GlobalLabelParameters.JWT_TIME: self.date}
        # reading the p12 file from cache memory
        cache_obj = FileCache()
        cache_memory = cache_obj.grab_file(self.merchant_config, self.merchant_config.key_file_path,
                                           self.merchant_config.key_file_name)
        der_cert_string = cache_memory[0]
        private_key = cache_memory[1]
        # setting the headers  -merchant_id and the public key
        headers_jwt = {
            GlobalLabelParameters.MERCHANT_ID: str(self.merchant_config.key_alias)}
        public_key_list = ([])
        public_key_list.append(der_cert_string.decode("utf-8"))
        public_key_headers = {GlobalLabelParameters.PUBLIC_KEY: public_key_list}
        headers_jwt.update(public_key_headers)


        # generating the token of jwt
        encoded_jwt = jwt.encode(jwt_body, private_key, algorithm='RS256', headers=headers_jwt)

        return encoded_jwt

    def token_for_post(self):

        digest_payload_obj = DigestAndPayload()
        digest = digest_payload_obj.string_digest_generation(
            self.merchant_config.request_json_path_data)
        # Setting the jwt body for JWT-post

        jwt_body = {GlobalLabelParameters.JWT_DIGEST: digest.decode("utf-8"), GlobalLabelParameters.JWT_ALGORITHM: "SHA-256",
                    GlobalLabelParameters.JWT_TIME: self.date}
        # reading the p12 file from cache memory
        cache_obj = FileCache()
        cache_memory = cache_obj.grab_file(self.merchant_config, self.merchant_config.key_file_path,
                                           self.merchant_config.key_file_name)
        der_cert_string = cache_memory[0]
        private_key = cache_memory[1]
        # setting the headers  -merchant_id and the public key
        headers_jwt = {
            GlobalLabelParameters.MERCHANT_ID: str(self.merchant_config.key_alias)}
        public_key_list = ([])
        public_key_list.append(der_cert_string.decode("utf-8"))
        public_key_headers = {GlobalLabelParameters.PUBLIC_KEY: public_key_list}
        headers_jwt.update(public_key_headers)
        # generating the token of jwt
        encoded_jwt = jwt.encode(jwt_body, private_key, algorithm='RS256', headers=headers_jwt)

        return encoded_jwt

    def token_for_put(self):

        digest_payload_obj = DigestAndPayload()
        digest = digest_payload_obj.string_digest_generation(
            self.merchant_config.request_json_path_data)
        # Setting the jwt body for JWT-post
        jwt_body = {GlobalLabelParameters.JWT_DIGEST: digest.decode("utf-8"), GlobalLabelParameters.JWT_ALGORITHM: "SHA-256",
                    GlobalLabelParameters.JWT_TIME: self.date}
        # reading the p12 file from cache memory
        cache_obj = FileCache()
        cache_memory = cache_obj.grab_file(self.merchant_config, self.merchant_config.key_file_path,
                                           self.merchant_config.key_file_name)
        der_cert_string = cache_memory[0]
        private_key = cache_memory[1]
        # setting the headers  -merchant_id and the public key
        headers_jwt = {
            GlobalLabelParameters.MERCHANT_ID: str(self.merchant_config.key_alias)}
        public_key_list = ([])
        public_key_list.append(der_cert_string.decode("utf-8"))
        public_key_headers = {GlobalLabelParameters.PUBLIC_KEY: public_key_list}
        headers_jwt.update(public_key_headers)
        # generating the token of jwt
        encoded_jwt = jwt.encode(jwt_body, private_key, algorithm='RS256', headers=headers_jwt)

        return encoded_jwt

    def token_for_patch(self):

        digest_payload_obj = DigestAndPayload()
        digest = digest_payload_obj.string_digest_generation(
            self.merchant_config.request_json_path_data)
        # Setting the jwt body for JWT-post
        jwt_body = {GlobalLabelParameters.JWT_DIGEST: digest.decode("utf-8"),
                    GlobalLabelParameters.JWT_ALGORITHM: "SHA-256",
                    GlobalLabelParameters.JWT_TIME: self.date}
        # reading the p12 file from cache memory
        cache_obj = FileCache()
        cache_memory = cache_obj.grab_file(self.merchant_config, self.merchant_config.key_file_path,
                                           self.merchant_config.key_file_name)
        der_cert_string = cache_memory[0]
        private_key = cache_memory[1]
        # setting the headers  -merchant_id and the public key
        headers_jwt = {
            GlobalLabelParameters.MERCHANT_ID: str(self.merchant_config.key_alias)}
        public_key_list = ([])
        public_key_list.append(der_cert_string.decode("utf-8"))
        public_key_headers = {GlobalLabelParameters.PUBLIC_KEY: public_key_list}
        headers_jwt.update(public_key_headers)
        # generating the token of jwt
        encoded_jwt = jwt.encode(jwt_body, private_key, algorithm='RS256', headers=headers_jwt)

        return encoded_jwt

    def token_for_delete(self):

        # Setting the jwt body for JWT-get
        jwt_body = {GlobalLabelParameters.JWT_TIME: self.date}
        # reading the p12 file from cache memory
        cache_obj = FileCache()
        cache_memory = cache_obj.grab_file(self.merchant_config, self.merchant_config.key_file_path,
                                           self.merchant_config.key_file_name)
        der_cert_string = cache_memory[0]
        private_key = cache_memory[1]
        # setting the headers  -merchant_id and the public key
        headers_jwt = {
            GlobalLabelParameters.MERCHANT_ID: str(self.merchant_config.key_alias)}
        public_key_list = ([])
        public_key_list.append(der_cert_string.decode("utf-8"))
        public_key_headers = {GlobalLabelParameters.PUBLIC_KEY: public_key_list}
        headers_jwt.update(public_key_headers)
        # generating the token of jwt
        encoded_jwt = jwt.encode(jwt_body, private_key, algorithm='RS256', headers=headers_jwt)

        return encoded_jwt
