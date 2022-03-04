import unittest
from authenticationsdk.core.MerchantConfiguration import *
from authenticationsdk.core.Authorization import *
import CyberSource.logging.log_factory as LogFactory
import authenticationsdk.util.PropertiesUtil
import logging
from authenticationsdk.core.MockData import *


class TestBasicFunction(unittest.TestCase):
    def setUp(self):
        self.func = Authorization()
        self.merchant_config = MerchantConfiguration()
        self.date = self.merchant_config.get_time()
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    # This method checks the HTTP_Get token  Generation Unit Testing
    def test_token_for_get_http(self):
        self.merchant_config.set_merchantconfig(MockData.HTTP_VALUES)
        self.merchant_config.request_type_method = "GET"
        self.get_id = "5246387105766473203529"
        self.merchant_config.request_target = "/pts/v2/payments/" + self.get_id

        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)

        self.assertIsNotNone(self.func.get_token(self.merchant_config, self.date, self.logger))

    # This method checks the HTTP_Get token  Generation when enable_log,Log_Maximum_Size,Log_Directory  is None/Empty
    def test_get_http_enable_log(self):
        self.merchant_config.set_merchantconfig(MockData.HTTP_DEFAULT_VALUES)

        self.merchant_config.request_type_method = "GET"
        self.get_id = "5246387105766473203529"
        self.merchant_config.request_target = "/pts/v2/payments/" + self.get_id
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)
        self.merchant_config.validate_merchant_details(MockData.HTTP_DEFAULT_VALUES, self.merchant_config)

        self.assertIsNotNone(self.func.get_token(self.merchant_config, self.date, self.logger))

    # This method checks the HTTP_Get token  Generation when the run_environment="CyberSource.Environment.PRODUCTION"
    def test_get_jwt_production_url(self):
        self.merchant_config.set_merchantconfig(MockData.JWT_VALUES_FOR_PRODUCTION)

        self.merchant_config.request_type_method = "GET"
        self.get_id = "5246387105766473203529"
        self.merchant_config.request_target = "/pts/v2/payments/" + self.get_id
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)
        self.merchant_config.validate_merchant_details(MockData.JWT_VALUES_FOR_PRODUCTION,
                                                       self.merchant_config)

        self.assertIsNotNone(self.func.get_token(self.merchant_config, self.date, self.logger))

    # This method checks the HTTP_Post token  Generation Unit Testing
    def test_token_for_post_http(self):
        self.merchant_config.set_merchantconfig(MockData.HTTP_VALUES)
        self.merchant_config.request_type_method = "POST"
        self.merchant_config.request_target = "/pts/v2/payments"

        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)
        
        self.merchant_config.request_json_path_data = json.dumps(MockData.REQUEST_DATA)

        self.assertIsNotNone(self.func.get_token(self.merchant_config, self.date, self.logger))

    # This method checks the HTTP_Put token  Generation Unit Testing
    def test_token_for_put_http(self):
        self.merchant_config.set_merchantconfig(MockData.HTTP_VALUES)
        self.merchant_config.request_type_method = "PUT"

        self.merchant_config.request_target = "/reporting/v2/reportSubscriptions/TRRReport?organizationId=testrest"

        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)
        
        self.merchant_config.request_json_path_data = json.dumps(MockData.TRR_DATA)

        self.assertIsNotNone(self.func.get_token(self.merchant_config, self.date, self.logger))

    # This method checks the HTTP_Delete token  Generation Unit Testing
    def test_token_for_delete_http(self):
        self.merchant_config.set_merchantconfig(MockData.HTTP_VALUES)
        self.merchant_config.request_type_method = "DELETE"

        self.merchant_config.request_target = "/reporting/v2/reportSubscriptions/TRRReport?organizationId=testrest/5246387105766473203529"

        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)

        self.assertIsNotNone(self.func.get_token(self.merchant_config, self.date, self.logger))

    # This method checks the JWT_Get token  Generation Unit Testing
    def test_token_for_get_jwt(self):
        self.merchant_config.set_merchantconfig(MockData.JWT_VALUES)
        self.merchant_config.request_type_method = "GET"
        self.get_id = "5246387105766473203529"
        self.merchant_config.request_target = "/pts/v2/payments/" + self.get_id

        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)

        self.assertIsNotNone(self.func.get_token(self.merchant_config, self.date, self.logger))

    # This method checks the JWT_Post token  Generation Unit Testing
    def test_token_for_post_jwt(self):
        self.merchant_config.set_merchantconfig(MockData.JWT_VALUES)
        self.merchant_config.request_type_method = "POST"
        self.merchant_config.request_target = "/pts/v2/payments/5246387105766473203529"
        
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)

        self.merchant_config.request_json_path_data = json.dumps(MockData.REQUEST_DATA)

        self.assertIsNotNone(self.func.get_token(self.merchant_config, self.date, self.logger))

    # This method checks the JWT_Put token  Generation Unit Testing
    def test_token_for_put_jwt(self):
        self.merchant_config.set_merchantconfig(MockData.JWT_VALUES)
        self.merchant_config.request_type_method = "PUT"

        self.merchant_config.request_target = "/reporting/v2/reportSubscriptions/TRRReport?organizationId=testrest"

        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)
        
        self.merchant_config.request_json_path_data =json.dumps(MockData.TRR_DATA)

        self.assertIsNotNone(self.func.get_token(self.merchant_config, self.date, self.logger))

    # This method checks the JWT_Delete token  Generation Unit Testing
    def test_token_for_delete_jwt(self):
        self.merchant_config.set_merchantconfig(MockData.JWT_VALUES)
        self.merchant_config.request_type_method = "DELETE"
        self.merchant_config.request_target = "/reporting/v2/reportSubscriptions/TRRReport?organizationId=testrest/5246387105766473203529"

        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.merchant_config.log_config)

        self.assertIsNotNone(self.func.get_token(self.merchant_config, self.date, self.logger))


if __name__ == '__main__':
    unittest.main()
