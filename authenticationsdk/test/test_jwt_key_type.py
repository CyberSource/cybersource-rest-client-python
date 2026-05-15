import unittest
import json
from authenticationsdk.core.MerchantConfiguration import MerchantConfiguration
from authenticationsdk.jwt.Token import JwtSignatureToken
from authenticationsdk.util.GlobalLabelParameters import GlobalLabelParameters
import CyberSource.logging.log_factory as LogFactory
import logging


class TestJwtKeyType(unittest.TestCase):
    """
    Test suite for JWT Key Type feature (P12 vs SHARED_SECRET).
    Tests configuration validation and token generation for both key types.
    """

    def setUp(self):
        self.merchant_config = MerchantConfiguration()
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_jwt_key_type_defaults_to_p12(self):
        """Test that jwtKeyType defaults to P12 when not specified (backward compatibility)."""
        config_data = {
            'authentication_type': 'JWT',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'key_alias': 'testrest',
            'key_password': 'testrest',
            'key_file_name': 'testrest',
            'keys_directory': 'resources'
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        
        # Should default to P12
        self.assertEqual(self.merchant_config.get_jwt_key_type(), GlobalLabelParameters.JWT_KEY_TYPE_P12)
        self.assertFalse(self.merchant_config.is_shared_secret_key_type())

    def test_jwt_key_type_p12_explicit(self):
        """Test that jwtKeyType can be explicitly set to P12."""
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'P12',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'key_alias': 'testrest',
            'key_password': 'testrest',
            'key_file_name': 'testrest',
            'keys_directory': 'resources'
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        
        self.assertEqual(self.merchant_config.get_jwt_key_type(), 'P12')
        self.assertFalse(self.merchant_config.is_shared_secret_key_type())

    def test_jwt_key_type_shared_secret(self):
        """Test that jwtKeyType can be set to SHARED_SECRET."""
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'SHARED_SECRET',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'merchant_keyid': '08c94330-f618-42a3-b09d-e1e43be5efda',
            'merchant_secretkey': 'yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE='
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        
        self.assertEqual(self.merchant_config.get_jwt_key_type(), 'SHARED_SECRET')
        self.assertTrue(self.merchant_config.is_shared_secret_key_type())

    def test_jwt_key_type_case_insensitive(self):
        """Test that jwtKeyType comparison is case-insensitive."""
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'shared_secret',  # lowercase
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'merchant_keyid': '08c94330-f618-42a3-b09d-e1e43be5efda',
            'merchant_secretkey': 'yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE='
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        
        # Should still recognize it as SHARED_SECRET
        self.assertTrue(self.merchant_config.is_shared_secret_key_type())

    def test_jwt_key_type_invalid_value(self):
        """Test that invalid jwtKeyType values are rejected."""
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'INVALID_TYPE',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com'
        }
        
        # Should raise exception during validation
        with self.assertRaises(Exception):  # validate_merchant_details_log raises Exception
            self.merchant_config.set_merchantconfig(config_data)
            self.merchant_config.validate_merchant_details(config_data)

    def test_shared_secret_requires_merchant_keyid(self):
        """Test that SHARED_SECRET requires merchantKeyId."""
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'SHARED_SECRET',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            # Missing merchant_keyid
            'merchant_secretkey': 'yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE='
        }
        
        with self.assertRaises(Exception):
            self.merchant_config.set_merchantconfig(config_data)
            self.merchant_config.validate_merchant_details(config_data)

    def test_shared_secret_requires_merchant_secretkey(self):
        """Test that SHARED_SECRET requires merchantSecretKey."""
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'SHARED_SECRET',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'merchant_keyid': '08c94330-f618-42a3-b09d-e1e43be5efda'
            # Missing merchant_secretkey
        }
        
        with self.assertRaises(Exception):
            self.merchant_config.set_merchantconfig(config_data)
            self.merchant_config.validate_merchant_details(config_data)

    def test_p12_does_not_require_merchant_keyid(self):
        """Test that P12 mode does not require merchantKeyId."""
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'P12',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'key_alias': 'testrest',
            'key_password': 'testrest',
            'key_file_name': 'testrest',
            'keys_directory': 'resources'
            # No merchant_keyid or merchant_secretkey needed
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        # Validation logic should not require merchant_keyid for P12
        self.assertFalse(self.merchant_config.is_shared_secret_key_type())

    def test_token_generation_shared_secret_get(self):
        """Test JWT token generation with SHARED_SECRET for GET request."""
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'SHARED_SECRET',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'merchant_keyid': '08c94330-f618-42a3-b09d-e1e43be5efda',
            'merchant_secretkey': 'yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE='
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        
        jwt_token_gen = JwtSignatureToken()
        jwt_token_gen.jwt_signature_token(
            self.merchant_config,
            self.merchant_config.get_time(),
            "GET",
            "/pts/v2/payments/5246387105766473203529"
        )
        
        token = jwt_token_gen.get_token()
        
        # Verify token is generated
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        
        # Verify token has 3 parts (header.payload.signature)
        parts = token.split('.')
        self.assertEqual(len(parts), 3)
        
        # Decode and verify header contains HS256 algorithm
        import base64
        header_json = base64.urlsafe_b64decode(parts[0] + '==').decode('utf-8')
        header = json.loads(header_json)
        self.assertEqual(header['alg'], 'HS256')
        self.assertEqual(header['typ'], 'JWT')
        self.assertEqual(header['kid'], '08c94330-f618-42a3-b09d-e1e43be5efda')

    def test_token_generation_shared_secret_post(self):
        """Test JWT token generation with SHARED_SECRET for POST request."""
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'SHARED_SECRET',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'merchant_keyid': '08c94330-f618-42a3-b09d-e1e43be5efda',
            'merchant_secretkey': 'yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE='
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        
        request_data = {
            "clientReferenceInformation": {
                "code": "TC50171_3"
            }
        }
        
        jwt_token_gen = JwtSignatureToken()
        jwt_token_gen.jwt_signature_token(
            self.merchant_config,
            self.merchant_config.get_time(),
            "POST",
            "/pts/v2/payments",
            json.dumps(request_data)
        )
        
        token = jwt_token_gen.get_token()
        
        # Verify token is generated
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        
        # Verify token structure
        parts = token.split('.')
        self.assertEqual(len(parts), 3)
        
        # Decode and verify payload contains digest for POST
        import base64
        payload_json = base64.urlsafe_b64decode(parts[1] + '==').decode('utf-8')
        payload = json.loads(payload_json)
        self.assertIn('digest', payload)
        self.assertIn('digestAlgorithm', payload)
        self.assertEqual(payload['digestAlgorithm'], 'SHA-256')

    def test_backward_compatibility_p12_without_jwt_key_type(self):
        """Test that existing P12 configs work without specifying jwtKeyType."""
        config_data = {
            'authentication_type': 'JWT',
            # No jwt_key_type specified
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'key_alias': 'testrest',
            'key_password': 'testrest',
            'key_file_name': 'testrest',
            'keys_directory': 'resources'
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        
        # Should default to P12
        self.assertEqual(self.merchant_config.get_jwt_key_type(), GlobalLabelParameters.JWT_KEY_TYPE_P12)
        self.assertFalse(self.merchant_config.is_shared_secret_key_type())

    def test_http_signature_unaffected(self):
        """Test that HTTP_Signature authentication is unaffected by jwtKeyType."""
        config_data = {
            'authentication_type': 'HTTP_Signature',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'merchant_keyid': '08c94330-f618-42a3-b09d-e1e43be5efda',
            'merchant_secretkey': 'yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE='
            # jwt_key_type should be irrelevant for HTTP_Signature
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        
        # HTTP_Signature should work regardless of jwtKeyType
        self.assertEqual(self.merchant_config.authentication_type, 'HTTP_Signature')

    def test_token_generation_shared_secret_put(self):
        """Test JWT token generation with SHARED_SECRET for PUT request."""
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'SHARED_SECRET',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'merchant_keyid': '08c94330-f618-42a3-b09d-e1e43be5efda',
            'merchant_secretkey': 'yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE='
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        
        request_data = {
            "clientReferenceInformation": {
                "code": "TC50171_3"
            }
        }
        
        jwt_token_gen = JwtSignatureToken()
        jwt_token_gen.jwt_signature_token(
            self.merchant_config,
            self.merchant_config.get_time(),
            "PUT",
            "/pts/v2/payments/5246387105766473203529",
            json.dumps(request_data)
        )
        
        token = jwt_token_gen.get_token()
        
        # Verify token is generated
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        
        # Verify token structure
        parts = token.split('.')
        self.assertEqual(len(parts), 3)
        
        # Decode and verify payload contains digest for PUT
        import base64
        payload_json = base64.urlsafe_b64decode(parts[1] + '==').decode('utf-8')
        payload = json.loads(payload_json)
        self.assertIn('digest', payload)
        self.assertIn('digestAlgorithm', payload)
        self.assertEqual(payload['digestAlgorithm'], 'SHA-256')

    def test_token_generation_shared_secret_delete(self):
        """Test JWT token generation with SHARED_SECRET for DELETE request."""
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'SHARED_SECRET',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'merchant_keyid': '08c94330-f618-42a3-b09d-e1e43be5efda',
            'merchant_secretkey': 'yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE='
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        
        jwt_token_gen = JwtSignatureToken()
        jwt_token_gen.jwt_signature_token(
            self.merchant_config,
            self.merchant_config.get_time(),
            "DELETE",
            "/pts/v2/payments/5246387105766473203529"
        )
        
        token = jwt_token_gen.get_token()
        
        # Verify token is generated
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        
        # Verify token structure
        parts = token.split('.')
        self.assertEqual(len(parts), 3)
        
        # Decode and verify header
        import base64
        header_json = base64.urlsafe_b64decode(parts[0] + '==').decode('utf-8')
        header = json.loads(header_json)
        self.assertEqual(header['alg'], 'HS256')

    def test_token_generation_shared_secret_patch(self):
        """Test JWT token generation with SHARED_SECRET for PATCH request."""
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'SHARED_SECRET',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'merchant_keyid': '08c94330-f618-42a3-b09d-e1e43be5efda',
            'merchant_secretkey': 'yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE='
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        
        request_data = {
            "clientReferenceInformation": {
                "code": "TC50171_3"
            }
        }
        
        jwt_token_gen = JwtSignatureToken()
        jwt_token_gen.jwt_signature_token(
            self.merchant_config,
            self.merchant_config.get_time(),
            "PATCH",
            "/pts/v2/payments/5246387105766473203529",
            json.dumps(request_data)
        )
        
        token = jwt_token_gen.get_token()
        
        # Verify token is generated
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        
        # Verify token structure
        parts = token.split('.')
        self.assertEqual(len(parts), 3)
        
        # Decode and verify payload contains digest for PATCH
        import base64
        payload_json = base64.urlsafe_b64decode(parts[1] + '==').decode('utf-8')
        payload = json.loads(payload_json)
        self.assertIn('digest', payload)
        self.assertIn('digestAlgorithm', payload)

    def test_token_generation_shared_secret_empty_body(self):
        """Test JWT token generation with SHARED_SECRET for PUT request with empty body."""
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'SHARED_SECRET',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'merchant_keyid': '08c94330-f618-42a3-b09d-e1e43be5efda',
            'merchant_secretkey': 'yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE='
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        
        jwt_token_gen = JwtSignatureToken()
        jwt_token_gen.jwt_signature_token(
            self.merchant_config,
            self.merchant_config.get_time(),
            "PUT",
            "/pts/v2/payments/5246387105766473203529",
            ""  # Empty body
        )
        
        token = jwt_token_gen.get_token()
        
        # Verify token is generated even with empty body
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        
        # Verify token structure
        parts = token.split('.')
        self.assertEqual(len(parts), 3)

    def test_p12_token_header_uses_rs256(self):
        """Test that P12 mode still uses RS256 algorithm (regression test)."""
        import os
        
        # Check if P12 file exists before running test
        p12_path = os.path.join(os.getcwd(), 'resources', 'testrest.p12')
        if not os.path.exists(p12_path):
            self.skipTest(f"P12 file not found at {p12_path}. Skipping regression test.")
        
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'P12',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'key_alias': 'testrest',
            'key_password': 'testrest',
            'key_file_name': 'testrest',
            'keys_directory': 'resources'
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        
        jwt_token_gen = JwtSignatureToken()
        jwt_token_gen.jwt_signature_token(
            self.merchant_config,
            self.merchant_config.get_time(),
            "GET",
            "/pts/v2/payments/5246387105766473203529"
        )
        
        token = jwt_token_gen.get_token()
        
        # Verify token is generated
        self.assertIsNotNone(token)
        
        # Decode and verify header uses RS256 for P12
        import base64
        parts = token.split('.')
        header_json = base64.urlsafe_b64decode(parts[0] + '==').decode('utf-8')
        header = json.loads(header_json)
        self.assertEqual(header['alg'], 'RS256')
        self.assertEqual(header['typ'], 'JWT')

    def test_shared_secret_get_token_no_digest(self):
        """Test that GET request does NOT contain digest in payload (negative test)."""
        config_data = {
            'authentication_type': 'JWT',
            'jwt_key_type': 'SHARED_SECRET',
            'merchantid': 'testrest',
            'run_environment': 'apitest.cybersource.com',
            'merchant_keyid': '08c94330-f618-42a3-b09d-e1e43be5efda',
            'merchant_secretkey': 'yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE='
        }
        
        self.merchant_config.set_merchantconfig(config_data)
        
        jwt_token_gen = JwtSignatureToken()
        jwt_token_gen.jwt_signature_token(
            self.merchant_config,
            self.merchant_config.get_time(),
            "GET",
            "/pts/v2/payments/5246387105766473203529"
        )
        
        token = jwt_token_gen.get_token()
        
        # Decode and verify payload does NOT contain digest for GET
        import base64
        parts = token.split('.')
        payload_json = base64.urlsafe_b64decode(parts[1] + '==').decode('utf-8')
        payload = json.loads(payload_json)
        
        # GET requests should NOT have digest
        self.assertNotIn('digest', payload)
        self.assertNotIn('digestAlgorithm', payload)


if __name__ == '__main__':
    unittest.main()
