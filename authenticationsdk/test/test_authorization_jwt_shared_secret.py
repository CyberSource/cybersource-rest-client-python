import unittest
import json
from authenticationsdk.core.MerchantConfiguration import MerchantConfiguration
from authenticationsdk.core.Authorization import Authorization
from authenticationsdk.test.MockData import MockData
import CyberSource.logging.log_factory as LogFactory
import logging


class TestAuthorizationJwtSharedSecret(unittest.TestCase):
    """
    Authorization-level integration tests for JWT with SHARED_SECRET.
    Tests end-to-end token generation through the Authorization interface,
    matching the Java AuthorizationTest test cases from feature/jwt-v2-shared-secret-with-mle.
    """

    def setUp(self):
        self.authorization = Authorization()
        self.merchant_config = MerchantConfiguration()
        self.date = self.merchant_config.get_time()
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_authorization_jwt_shared_secret_post(self):
        """Test Authorization.get_token() with JWT SHARED_SECRET for POST request."""
        # Use MockData configuration
        self.merchant_config.set_merchantconfig(MockData.JWT_SHARED_SECRET_VALUES)
        self.merchant_config.request_type_method = "POST"
        self.merchant_config.request_target = "/pts/v2/payments"
        
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)
        
        self.merchant_config.request_json_path_data = json.dumps(MockData.REQUEST_DATA)
        
        # Get token through Authorization interface
        token = self.authorization.get_token(
            self.merchant_config, 
            self.date, 
            self.merchant_config.request_type_method,
            self.merchant_config.request_target,
            self.merchant_config.request_json_path_data,
            self.logger
        )
        
        # Verify token is generated
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        
        # Verify JWT structure (3 parts)
        parts = token.split('.')
        self.assertEqual(len(parts), 3, "JWT should have 3 parts (header.payload.signature)")

    def test_authorization_jwt_shared_secret_get(self):
        """Test Authorization.get_token() with JWT SHARED_SECRET for GET request."""
        self.merchant_config.set_merchantconfig(MockData.JWT_SHARED_SECRET_VALUES)
        self.get_id = "5246387105766473203529"
        
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)
        
        # Get token through Authorization interface
        token = self.authorization.get_token(
            self.merchant_config, 
            self.date, 
            "GET",
            "/pts/v2/payments/" + self.get_id,
            None,
            self.logger
        )
        
        # Verify token is generated
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        
        # Verify JWT structure
        parts = token.split('.')
        self.assertEqual(len(parts), 3)

    def test_authorization_jwt_shared_secret_put(self):
        """Test Authorization.get_token() with JWT SHARED_SECRET for PUT request."""
        self.merchant_config.set_merchantconfig(MockData.JWT_SHARED_SECRET_VALUES)
        
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)
        
        # Get token through Authorization interface
        token = self.authorization.get_token(
            self.merchant_config, 
            self.date, 
            "PUT",
            "/pts/v2/payments/5246387105766473203529",
            json.dumps(MockData.REQUEST_DATA),
            self.logger
        )
        
        # Verify token is generated
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        
        # Verify JWT structure
        parts = token.split('.')
        self.assertEqual(len(parts), 3)

    def test_authorization_jwt_shared_secret_delete(self):
        """Test Authorization.get_token() with JWT SHARED_SECRET for DELETE request."""
        self.merchant_config.set_merchantconfig(MockData.JWT_SHARED_SECRET_VALUES)
        
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)
        
        # Get token through Authorization interface
        token = self.authorization.get_token(
            self.merchant_config, 
            self.date, 
            "DELETE",
            "/pts/v2/payments/5246387105766473203529",
            None,
            self.logger
        )
        
        # Verify token is generated
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        
        # Verify JWT structure
        parts = token.split('.')
        self.assertEqual(len(parts), 3)

    def test_authorization_jwt_shared_secret_patch(self):
        """Test Authorization.get_token() with JWT SHARED_SECRET for PATCH request."""
        self.merchant_config.set_merchantconfig(MockData.JWT_SHARED_SECRET_VALUES)
        
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)
        
        # Get token through Authorization interface
        token = self.authorization.get_token(
            self.merchant_config, 
            self.date, 
            "PATCH",
            "/pts/v2/payments/5246387105766473203529",
            json.dumps(MockData.REQUEST_DATA),
            self.logger
        )
        
        # Verify token is generated
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        
        # Verify JWT structure
        parts = token.split('.')
        self.assertEqual(len(parts), 3)

    def test_authorization_invalid_http_verb(self):
        """Test that invalid HTTP verb raises an exception (similar to Java test)."""
        self.merchant_config.set_merchantconfig(MockData.JWT_SHARED_SECRET_VALUES)
        
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)
        
        # Should raise exception for invalid HTTP verb
        with self.assertRaises(Exception):
            self.authorization.get_token(
                self.merchant_config, 
                self.date, 
                "INVALID_VERB",
                "/pts/v2/payments",
                json.dumps(MockData.REQUEST_DATA),
                self.logger
            )

    def test_authorization_jwt_shared_secret_empty_body(self):
        """Test Authorization.get_token() with JWT SHARED_SECRET for POST with empty body."""
        self.merchant_config.set_merchantconfig(MockData.JWT_SHARED_SECRET_VALUES)
        
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)
        
        # Get token through Authorization interface
        token = self.authorization.get_token(
            self.merchant_config, 
            self.date, 
            "POST",
            "/pts/v2/payments",
            "",  # Empty body
            self.logger
        )
        
        # Verify token is generated even with empty body
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)

    def test_authorization_jwt_shared_secret_with_trr_data(self):
        """Test Authorization.get_token() with JWT SHARED_SECRET using TRR report data."""
        self.merchant_config.set_merchantconfig(MockData.JWT_SHARED_SECRET_VALUES)
        
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)
        
        # Get token through Authorization interface
        token = self.authorization.get_token(
            self.merchant_config, 
            self.date, 
            "PUT",
            "/reporting/v2/reportSubscriptions/TRRReport?organizationId=testrest",
            json.dumps(MockData.TRR_DATA),
            self.logger
        )
        
        # Verify token is generated
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        
        # Verify JWT structure
        parts = token.split('.')
        self.assertEqual(len(parts), 3)

    def test_authorization_jwt_shared_secret_token_contains_bearer_prefix(self):
        """Test that token can be used with Bearer prefix for Authorization header."""
        self.merchant_config.set_merchantconfig(MockData.JWT_SHARED_SECRET_VALUES)
        
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)
        
        token = self.authorization.get_token(
            self.merchant_config, 
            self.date, 
            "GET",
            "/pts/v2/payments/5246387105766473203529",
            None,
            self.logger
        )
        
        # Verify token format is suitable for Bearer authentication
        self.assertIsNotNone(token)
        # Token should not already contain "Bearer" prefix (that's added by API client)
        self.assertNotIn('Bearer', token)
        
        # Verify it's a valid JWT structure
        parts = token.split('.')
        self.assertEqual(len(parts), 3)


if __name__ == '__main__':
    unittest.main()
