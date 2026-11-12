import base64
import datetime
import json
import logging
import os
import tempfile
import unittest
import uuid

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from jwcrypto import jwe, jwk

from authenticationsdk.core.MerchantConfiguration import MerchantConfiguration
from authenticationsdk.util.MLEUtility import MLEUtility

# Default CyberSource MLE cert alias (authenticationsdk.util.GlobalLabelParameters.DEFAULT_MLE_ALIAS_FOR_CERT),
# used so these tests exercise the real MerchantConfiguration alias-defaulting path instead of a hand-rolled one.
DEFAULT_MLE_ALIAS = "CyberSource_SJC_US"


def _make_self_signed_cert_with_serial(serial):
    """Generates a fresh self-signed cert whose subject carries the given serialNumber
    and CN=CyberSource_SJC_US, writes the cert PEM to a temp file (mleForRequestPublicCertPath
    expects a PEM file), and returns (cert_path, private_key_pem)."""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, DEFAULT_MLE_ALIAS),
        x509.NameAttribute(NameOID.SERIAL_NUMBER, serial),
    ])
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.now(datetime.timezone.utc))
        .not_valid_after(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=365))
        .sign(private_key, hashes.SHA256())
    )
    cert_pem = cert.public_bytes(serialization.Encoding.PEM)
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    fd, cert_path = tempfile.mkstemp(prefix="mle-request-test-", suffix=".pem")
    with os.fdopen(fd, "wb") as f:
        f.write(cert_pem)

    return cert_path, private_key_pem


def _build_merchant_config(cert_path, merchant_id):
    config = MerchantConfiguration()
    config.set_merchantconfig({
        "authentication_type": "jwt",
        "jwt_key_type": "SHARED_SECRET",
        "merchantid": merchant_id,
        "run_environment": "apitest.cybersource.com",
        "merchant_keyid": "08c94330-f618-42a3-b09d-e1e43be5efda",
        "merchant_secretkey": "yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE=",
        "enable_log": False,
        "log_file_name": "cybs",
        "log_maximum_size": 10485760,
        "log_directory": os.path.join(os.getcwd(), "Logs"),
        "mleForRequestPublicCertPath": cert_path,
        # requestMleKeyAlias intentionally omitted: MerchantConfiguration defaults it to
        # DEFAULT_MLE_ALIAS_FOR_CERT ("CyberSource_SJC_US"), which matches the cert's CN above.
    })
    return config


def _decode_protected_header(compact_jwe):
    header_b64 = compact_jwe.split(".")[0]
    padding = "=" * (-len(header_b64) % 4)
    header_json = base64.urlsafe_b64decode(header_b64 + padding)
    return json.loads(header_json)


def _decrypt(compact_jwe, private_key_pem):
    key = jwk.JWK.from_pem(private_key_pem)
    token = jwe.JWE()
    token.deserialize(compact_jwe, key=key)
    return token.payload.decode("utf-8")


class TestRequestMleCtyHeader(unittest.TestCase):
    """
    Verifies that MLEUtility.encrypt_request_payload() sets the JWE 'cty' header to the
    exact Content-Type selected by the API operation, instead of omitting it entirely.
    """

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_cty_set_to_exact_content_type(self):
        for content_type in ("application/json", "application/hal+json", "application/json; charset=utf-8"):
            with self.subTest(content_type=content_type):
                serial = "7000000000000000111222"
                cert_path, private_key_pem = _make_self_signed_cert_with_serial(serial)
                merchant_config = _build_merchant_config(cert_path, "mle-cty-test-" + uuid.uuid4().hex)
                payload = '{"amount":"100"}'

                try:
                    result = MLEUtility.encrypt_request_payload(merchant_config, payload, content_type)
                    envelope = json.loads(result)
                    jwe_token = envelope["encryptedRequest"]
                    header = _decode_protected_header(jwe_token)

                    self.assertEqual(header["cty"], content_type)
                    self.assertEqual(header["alg"], "RSA-OAEP-256")
                    self.assertEqual(header["enc"], "A256GCM")
                    self.assertEqual(header["kid"], serial)

                    decrypted = _decrypt(jwe_token, private_key_pem)
                    self.assertEqual(decrypted, payload)
                finally:
                    os.remove(cert_path)

    def test_cty_omitted_when_content_type_not_supplied(self):
        cert_path, private_key_pem = _make_self_signed_cert_with_serial("7000000000000000333444")
        merchant_config = _build_merchant_config(cert_path, "mle-cty-test-" + uuid.uuid4().hex)

        try:
            result = MLEUtility.encrypt_request_payload(merchant_config, '{"amount":"100"}')
            envelope = json.loads(result)
            header = _decode_protected_header(envelope["encryptedRequest"])
            self.assertNotIn("cty", header)
        finally:
            os.remove(cert_path)

    def test_cty_omitted_when_content_type_is_blank(self):
        cert_path, private_key_pem = _make_self_signed_cert_with_serial("7000000000000000555666")
        merchant_config = _build_merchant_config(cert_path, "mle-cty-test-" + uuid.uuid4().hex)

        try:
            result = MLEUtility.encrypt_request_payload(merchant_config, '{"amount":"100"}', "   ")
            envelope = json.loads(result)
            header = _decode_protected_header(envelope["encryptedRequest"])
            self.assertNotIn("cty", header)
        finally:
            os.remove(cert_path)

    def test_empty_json_object_body_encrypts_and_decrypts_to_literal_braces(self):
        cert_path, private_key_pem = _make_self_signed_cert_with_serial("7000000000000000777888")
        merchant_config = _build_merchant_config(cert_path, "mle-cty-test-" + uuid.uuid4().hex)

        try:
            result = MLEUtility.encrypt_request_payload(merchant_config, "{}", "application/json")
            envelope = json.loads(result)
            jwe_token = envelope["encryptedRequest"]
            header = _decode_protected_header(jwe_token)

            self.assertEqual(header["cty"], "application/json")
            self.assertEqual(_decrypt(jwe_token, private_key_pem), "{}")
        finally:
            os.remove(cert_path)

    def test_http_signature_without_cert_returns_payload_unchanged(self):
        merchant_config = MerchantConfiguration()
        merchant_config.set_merchantconfig({
            "authentication_type": "http_signature",
            "merchantid": "mle-cty-test-" + uuid.uuid4().hex,
            "run_environment": "apitest.cybersource.com",
            "merchant_keyid": "08c94330-f618-42a3-b09d-e1e43be5efda",
            "merchant_secretkey": "yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE=",
            "enable_log": False,
            "log_file_name": "cybs",
            "log_maximum_size": 10485760,
            "log_directory": os.path.join(os.getcwd(), "Logs"),
        })
        payload = '{"amount":"100"}'

        result = MLEUtility.encrypt_request_payload(merchant_config, payload, "application/json")
        self.assertEqual(result, payload)


if __name__ == "__main__":
    unittest.main()
