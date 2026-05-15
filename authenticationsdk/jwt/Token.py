import time
from jwcrypto import jwt
import uuid
from authenticationsdk.payloaddigest.PayLoadDigest import *
from authenticationsdk.core.TokenGeneration import *
from authenticationsdk.util.Cache import *
from authenticationsdk.util.MLEUtility import MLEUtility
import CyberSource.logging.log_factory as LogFactory
from cryptography.hazmat.primitives import serialization


class JwtSignatureToken(TokenGeneration):
    def __init__(self):
        self.merchant_config = None
        self.request_body = None
        self.jwt_method = None
        self.date = None
        self.request_json_path_data = None
        self.isResponseMLEforApi =False
        self.request_target = None

    def jwt_signature_token(self, mconfig, date_time, request_type_method, request_target, request_json_path_data=None, isResponseMLEforApi=False):
        self.merchant_config = mconfig
        self.jwt_method = request_type_method
        self.date = date_time
        self.request_target = request_target
        self.request_json_path_data = request_json_path_data
        self.isResponseMLEforApi = isResponseMLEforApi

    def get_token(self):
        return self.set_token()

    
    def set_token(self):
        """
        Generates and returns a signed JWT token.
        Branches on jwtKeyType to use either P12 (RS256) or SHARED_SECRET (HS256) signing.
        """
        if self.merchant_config.is_shared_secret_key_type():
            # JWT with SHARED_SECRET — sign with HMAC-SHA256 (symmetric)
            return self.set_token_with_hmac()
        else:
            # JWT with P12 (default) — sign with RS256 (asymmetric)
            return self.set_token_with_p12()

    def set_token_with_p12(self):
        """
        Signs JWT using RS256 with P12 certificate (existing behavior).
        """
        payload_claim_set = self.get_payload_claim_set()

        cache_obj = FileCache()
        cache_memory = cache_obj.fetch_cached_p12_certificate(self.merchant_config, self.merchant_config.p12KeyFilePath, self.merchant_config.key_password)
        
        x509cert = cache_memory.x509_certificate
        header_claim_set = self.get_rs256_header(x509cert)
        
        token = jwt.JWT(claims = payload_claim_set, header=header_claim_set)

        private_key = cache_memory.private_key
        private_key_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        key = jwk.JWK.from_pem(private_key_pem)
        token.make_signed_token(key)

        serialized_jwt = token.serialize()
        return serialized_jwt

    def set_token_with_hmac(self):
        """
        Signs JWT using HS256 with shared secret key (new behavior).
        """
        payload_claim_set = self.get_payload_claim_set()
        
        # Get the header for HMAC signing
        header_claim_set = self.get_hs256_header()
        
        # Decode the base64-encoded merchant secret key
        secret_key_bytes = base64.b64decode(self.merchant_config.merchant_secretkey)
        
        # Create JWK from the raw bytes for HS256
        key = jwk.JWK(kty="oct", k=base64.urlsafe_b64encode(secret_key_bytes).decode('utf-8').rstrip('='))
        
        # Create and sign the JWT token
        token = jwt.JWT(claims=payload_claim_set, header=header_claim_set)
        token.make_signed_token(key)
        
        serialized_jwt = token.serialize()
        return serialized_jwt

    
    def get_payload_claim_set(self):

        jwt_payload = {}

        # setting the JWT digest and digest Algorithm when a `POST` or `PUT` or `PATCH` request is made
        if self.jwt_method.upper() in [GlobalLabelParameters.POST, GlobalLabelParameters.PUT, GlobalLabelParameters.PATCH]:
            digest_payload_obj = DigestAndPayload()
            digest = digest_payload_obj.string_digest_generation(
                self.request_json_path_data)
            jwt_payload = {GlobalLabelParameters.JWT_DIGEST: digest.decode("utf-8"), GlobalLabelParameters.JWT_ALGORITHM: "SHA-256"}

        # Set the iat and exp claims
        jwt_payload[GlobalLabelParameters.JWT_TIME] = int(time.time())
        jwt_payload[GlobalLabelParameters.JWT_EXP] = jwt_payload[GlobalLabelParameters.JWT_TIME] + 120 # The exp claim is set to 2 mins more than the iat claim
        
        # Set the request method, host and resource path in the JWT body as per the specification for all the request types
        jwt_payload["request-method"] = str(self.jwt_method.upper())
        jwt_payload["request-host"] = self.merchant_config.run_environment
        jwt_payload["request-resource-path"] = str(self.request_target).split('?', 1)[0] #Split the string to remove the query params

        issuer = ''
        # Choose issuer claim in the JWT body as per the use_metakey flag in the config file
        if(self.merchant_config.use_metakey):
            issuer = str(self.merchant_config.portfolio_id)
        else:
            issuer = str(self.merchant_config.merchant_id)

        jwt_payload["iss"] = issuer 
        jwt_payload["jti"] = str(uuid.uuid4())
        jwt_payload["v-c-jwt-version"] = "2"
        jwt_payload[GlobalLabelParameters.MERCHANT_ID] = str(self.merchant_config.merchant_id)

        if self.isResponseMLEforApi:
            logger = LogFactory.setup_logger(__name__, self.merchant_config.log_config)
            response_mle_kid = MLEUtility.validate_and_auto_extract_response_mle_kid(self.merchant_config, logger)
            jwt_payload['v-c-response-mle-kid'] = response_mle_kid

        return jwt_payload

    def get_rs256_header(self, certificate):
        """
        Creates JWT header for RS256 signing (P12 certificate).
        Uses certificate serial number as kid.
        """
        serial_number = CertificateUtility.extract_serial_number_from_certificate(certificate)
        jwt_headers = {
            "kid": str(serial_number),
            "alg": "RS256",
            "typ": "JWT"
        }

        # Add any other future parameters to the header claim set here
        return jwt_headers

    def get_hs256_header(self):
        """
        Creates JWT header for HS256 signing (shared secret).
        Uses merchantKeyId as kid.
        """
        jwt_headers = {
            "kid": str(self.merchant_config.merchant_keyid),
            "alg": "HS256",
            "typ": "JWT"
        }

        return jwt_headers


