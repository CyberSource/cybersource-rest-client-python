import json
import logging
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from cryptography.hazmat.primitives.asymmetric import rsa
from jwcrypto import jwe, jwk

from authenticationsdk.core.MerchantConfiguration import MerchantConfiguration
from authenticationsdk.jwt.Token import JwtSignatureToken
from authenticationsdk.test.MockData import MockData
from authenticationsdk.util.MLEUtility import MLEUtility

class TestResponseMleClaims(unittest.TestCase):
    """
    Verifies the JWS payload claims added when Response MLE is enabled:
      - v-c-response-mle-kid  (existing behavior)
            - v-c-response-mle-algo == "RSA-OAEP-256" (new claim per Issue #39)

    Also verifies backward compatibility: when Response MLE is NOT enabled,
    neither claim is present in the payload.
    """

    RESPONSE_MLE_ALG_CLAIM = "v-c-response-mle-algo"
    RESPONSE_MLE_KID_CLAIM = "v-c-response-mle-kid"
    EXPECTED_ALG = "RSA-OAEP-256"

    def setUp(self):
        logging.disable(logging.CRITICAL)
        self.merchant_config = MerchantConfiguration()
        self.merchant_config.set_merchantconfig(MockData.JWT_SHARED_SECRET_VALUES)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def _build_token(self, is_response_mle_for_api):
        token = JwtSignatureToken()
        token.jwt_signature_token(
            self.merchant_config,
            self.merchant_config.get_time(),
            "GET",
            "/pts/v2/payments/1234",
            None,
            is_response_mle_for_api,
        )
        return token

    @patch(
        "authenticationsdk.jwt.Token.MLEUtility.validate_and_auto_extract_response_mle_kid",
        return_value="test-mle-kid-serial",
    )
    def test_response_mle_alg_claim_present_when_enabled(self, _mock_kid):
        token = self._build_token(is_response_mle_for_api=True)
        claims = token.get_payload_claim_set()

        self.assertIn(self.RESPONSE_MLE_ALG_CLAIM, claims)
        self.assertEqual(claims[self.RESPONSE_MLE_ALG_CLAIM], self.EXPECTED_ALG)

    @patch(
        "authenticationsdk.jwt.Token.MLEUtility.validate_and_auto_extract_response_mle_kid",
        return_value="test-mle-kid-serial",
    )
    def test_response_mle_kid_claim_still_present_when_enabled(self, _mock_kid):
        token = self._build_token(is_response_mle_for_api=True)
        claims = token.get_payload_claim_set()

        self.assertIn(self.RESPONSE_MLE_KID_CLAIM, claims)
        self.assertEqual(claims[self.RESPONSE_MLE_KID_CLAIM], "test-mle-kid-serial")

    def test_response_mle_claims_absent_when_disabled(self):
        token = self._build_token(is_response_mle_for_api=False)
        claims = token.get_payload_claim_set()

        self.assertNotIn(self.RESPONSE_MLE_ALG_CLAIM, claims)
        self.assertNotIn(self.RESPONSE_MLE_KID_CLAIM, claims)


class TestResponseMleDecryptRoundTrip(unittest.TestCase):
    """
    End-to-end proof that a response body encrypted with RSA-OAEP-256 / A256GCM
    round-trips through MLEUtility.decrypt_mle_response_payload() using the
    JWEUtility path.
    """

    PLAINTEXT = '{"status":"OK","id":"abc123"}'

    def setUp(self):
        logging.disable(logging.CRITICAL)
        # Build a 2048-bit RSA keypair in memory (no cert / cache required).
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.private_jwk = jwk.JWK.from_pyca(private_key)
        self.public_jwk = jwk.JWK.from_pyca(private_key.public_key())

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def _make_encrypted_response_body(self):
        headers = {"alg": "RSA-OAEP-256", "enc": "A256GCM", "kid": "test-kid"}
        token = jwe.JWE(
            plaintext=self.PLAINTEXT.encode("utf-8"),
            protected=json.dumps(headers),
        )
        token.add_recipient(self.public_jwk)
        return json.dumps({"encryptedResponse": token.serialize(compact=True)})

    def test_round_trip_decrypt_rsa_oaep_256(self):
        encrypted_body = self._make_encrypted_response_body()
        merchant_config = SimpleNamespace(responseMlePrivateKey=self.private_jwk)

        decrypted = MLEUtility.decrypt_mle_response_payload(merchant_config, encrypted_body)

        self.assertEqual(decrypted, self.PLAINTEXT)

    def test_non_encrypted_response_raises(self):
        merchant_config = SimpleNamespace(responseMlePrivateKey=self.private_jwk)
        with self.assertRaises(MLEUtility.MLEException):
            MLEUtility.decrypt_mle_response_payload(
                merchant_config, '{"status":"OK"}'
            )


if __name__ == "__main__":
    unittest.main()

