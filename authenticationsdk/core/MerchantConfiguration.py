from CyberSource.logging.log_configuration import LogConfiguration
from authenticationsdk.util.GlobalLabelParameters import *
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import ast
import json
import authenticationsdk.util.ExceptionAuth
import os
import CyberSource.logging.log_factory as LogFactory


class MerchantConfiguration:

    def __init__(self):
        self.merchant_keyid = None
        self.merchant_secretkey = None
        self.merchant_id = None
        self.use_metakey = None
        self.portfolio_id = None
        self.host_name = None
        self.url = None
        self.request_host = None
        self.request_type_method = None
        self.request_target = None
        self.authentication_type = None
        self.key_file_path = None
        self.run_environment = None
        self.key_alias = None
        self.key_password = None
        self.enable_client_cert = None
        self.client_cert_dir = None
        self.ssl_client_cert = None
        self.private_key = None
        self.ssl_key_password = None
        self.client_id = None
        self.client_secret = None
        self.access_token = None
        self.refresh_token = None
        self.response_code = None
        self.response_message = None
        self.v_c_correlation_id = None
        self.enable_log = None
        self.maximum_size = None
        self.log_directory = None
        self.log_file_name = None
        self.proxy_address = None
        self.proxy_port = None
        self.key_file_name = None
        self.request_json_path_data = None        
        self.solution_id = None
        self.log_config = None
        self.log_level = None
        self.log_format = None
        self.log_date_format = None
        self.enable_masking = None
        self.logger = LogFactory.setup_logger(self.__class__.__name__)

    def set_merchant_keyid(self, value):
        if not (value.get('merchant_keyid') is None):
            self.merchant_keyid = value['merchant_keyid']

    def set_merchant_secretkey(self, value):
        if not (value.get('merchant_secretkey') is None):
            self.merchant_secretkey = value['merchant_secretkey']

    def set_key_file_path(self, value):
        if not (value.get('keys_directory') is None):
            self.key_file_path = value['keys_directory']

    def set_log_file_name(self, value):
        if not (value.get('log_file_name') is None or value.get('log_file_name') == ""):
            self.log_file_name = value['log_file_name']
        else:
            self.log_file_name = GlobalLabelParameters.LOG_FILE_NAME_DEFAULT

    def set_key_alias(self, value):
        if not (value.get('key_alias') is None):
            self.key_alias = value['key_alias']

    def set_key_password(self, value):
        if not (value.get('key_password') is None):
            self.key_password = value['key_password']

    def set_authentication_type(self, value):
        if not (value.get('authentication_type') is None):
            self.authentication_type = value['authentication_type']

    def set_merchant_id(self, value):
        if not (value.get('merchantid') is None):
            self.merchant_id = value['merchantid']

    def set_use_metakey(self, value):
        if not (value.get('use_metakey') is None):
            self.use_metakey = value['use_metakey']
        else:
            self.use_metakey = False
    
    def set_portfolio_id(self, value):
        if not (value.get('portfolio_id') is None):
            self.portfolio_id = value['portfolio_id']

    def set_enable_log(self, value):

        if not (value.get('enable_log') == "" or value.get('enable_log') is None):
            self.enable_log = value['enable_log']
        else:
            self.enable_log = GlobalLabelParameters.DEFAULT_ENABLE_LOG

    def set_maximum_size(self, value):

        if not (value.get('log_maximum_size') == "" or value.get('log_maximum_size') is None):
            self.maximum_size = value['log_maximum_size']
        else:
            self.maximum_size = GlobalLabelParameters.DEFAULT_MAXIMUM_SIZE  # 10 MB = 10485760 bytes

    def set_log_directory(self, value):

        if not (value.get('log_directory') == "" or value.get('log_directory') is None):
            if os.path.exists(value['log_directory']) or os.path.isdir(value['log_directory']):
                self.log_directory = value['log_directory']
            else:
                self.log_directory = GlobalLabelParameters.DEFAULT_LOG_DIRECTORY
        else:
            self.log_directory = GlobalLabelParameters.DEFAULT_LOG_DIRECTORY

    def set_run_environment(self, value):
        if not (value.get('run_environment') is None):
            self.run_environment = value['run_environment']

    # setting up hostname based on the run environment value
    def set_request_host(self, value):
        if not (value.get("run_environment") is None):
            if self.run_environment.upper() in GlobalLabelParameters.OLD_RUN_ENVIRONMENT_CONSTANTS:
                raise AttributeError(GlobalLabelParameters.DEPRECATED_RUN_ENVIRONMENT)
            else:
                self.request_host = self.run_environment

    def set_proxy_address(self, value):
        if not (value.get('proxy_address') is None):
            self.proxy_address = value['proxy_address']

    def set_proxy_port(self, value):
        if not (value.get("proxy_port") is None):
            self.proxy_port = value['proxy_port']

    def set_key_file_name(self, value):
        if not (value.get('key_file_name') is None):
            self.key_file_name = value['key_file_name']

    def set_solution_id(self, value):
        if not (value.get('solution_id') is None):
            self.solution_id = value['solution_id']

    def set_enable_client_cert(self, value):
        if not (value.get('enable_client_cert') is None):
            self.enable_client_cert = value['enable_client_cert']
        else:
            self.enable_client_cert = False
    
    def set_client_cert_dir(self, value):
        if not (value.get('client_cert_dir') is None):
            self.client_cert_dir = value['client_cert_dir']

    def set_ssl_client_cert(self, value):
        if not (value.get('ssl_client_cert') is None):
            self.ssl_client_cert = value['ssl_client_cert']

    def set_private_key(self, value):
        if not (value.get('private_key') is None):
            self.private_key = value['private_key']

    def set_ssl_key_password(self, value):
        if not (value.get('ssl_key_password') is None):
            self.ssl_key_password = value['ssl_key_password']

    def set_client_id(self, value):
        if not (value.get('client_id') is None):
            self.client_id = value['client_id']

    def set_client_secret(self, value):
        if not (value.get('client_secret') is None):
            self.client_secret = value['client_secret']

    def set_access_token(self, value):
        if not (value.get('access_token') is None):
            self.access_token = value['access_token']

    def set_refresh_token(self, value):
        if not (value.get('refresh_token') is None):
            self.refresh_token = value['refresh_token']

    def set_log_level(self, value):
        if not (value.get('log_level') is None):
            self.log_level = value['log_level']
        else:
            self.log_level = GlobalLabelParameters.DEFAULT_LOG_LEVEL

    def set_enable_masking(self, value):
        if not (value.get('enable_masking') is None):
            self.enable_masking = value['enable_masking']
        else:
            self.enable_masking = True

    def set_log_format(self, value):
        if not (value.get('log_format') is None):
            self.log_format = value['log_format']
        else:
            self.log_format = GlobalLabelParameters.DEFAULT_LOG_FORMAT

    def set_log_date_format(self, value):
        if not (value.get('log_date_format') is None):
            self.log_date_format = value['log_date_format']
        else:
            self.log_date_format = GlobalLabelParameters.DEFAULT_LOG_DATE_FORMAT

    def set_log_configuration(self):
        self.log_config = LogConfiguration()
        self.log_config.set_enable_log(self.enable_log)
        self.log_config.set_log_folder(self.log_directory)
        self.log_config.set_log_file_name(self.log_file_name)
        self.log_config.set_log_max_size(self.maximum_size)
        self.log_config.set_log_level(self.log_level)
        self.log_config.set_enable_masking(self.enable_masking)
        self.log_config.set_log_format(self.log_format)
        self.log_config.set_log_date_format(self.log_date_format)


    # This method sets the Merchant Configuration Variables to its respective values after reading from cybs.properties
    def set_merchantconfig(self, val):

        self.set_key_password(val)
        self.set_key_alias(val)
        self.set_key_file_path(val)
        self.set_key_file_name(val)
        self.set_merchant_keyid(val)
        self.set_merchant_secretkey(val)
        self.set_use_metakey(val)
        self.set_portfolio_id(val)
        self.set_run_environment(val)
        self.set_merchant_id(val)
        self.set_authentication_type(val)
        self.set_enable_log(val)
        self.set_maximum_size(val)
        self.set_log_directory(val)
        self.set_request_host(val)
        self.set_log_file_name(val)
        self.set_proxy_address(val)
        self.set_proxy_port(val)
        self.set_enable_client_cert(val)
        self.set_client_cert_dir(val)
        self.set_ssl_client_cert(val)
        self.set_ssl_key_password(val)
        self.set_private_key(val)
        self.set_client_id(val)
        self.set_client_secret(val)
        self.set_access_token(val)
        self.set_refresh_token(val)
        self.set_enable_masking(val)
        self.set_log_date_format(val)
        self.set_log_format(val)
        self.set_log_level(val)
        self.set_log_configuration()

    # Returns the time in format as defined by RFC7231
    def get_time(self):
        now = datetime.now()
        stamp = mktime(now.timetuple())

        return format_date_time(stamp)

    # This validates the Merchant details
    def validate_merchant_details(self, details):
        # verify Mandatory Properties
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.log_config)
        if self.log_config.enable_log is True:
            self.logger.info("START> ======================================= ")       

        if self.authentication_type is None or self.authentication_type == "":
            authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger,
                                                                               GlobalLabelParameters.AUTHENTICATION_REQ,
                                                                               self.log_config)

        if self.run_environment is None or self.run_environment == "":
            authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger,
                                                                               GlobalLabelParameters.RUN_ENVIRONMENT_EMPTY,
                                                                               self.log_config)

        # Fallback for missing values
        if details.get('enable_log') is None or details.get('enable_log') == "":
            authenticationsdk.util.ExceptionAuth.validate_default_values(self.logger,
                                                                         GlobalLabelParameters.ENABLE_LOG_DEFAULT_MESSAGE,
                                                                         self.log_config)

        if details.get('log_maximum_size') is None or details.get('log_maximum_size') == "":
            authenticationsdk.util.ExceptionAuth.validate_default_values(self.logger,
                                                                         GlobalLabelParameters.LOG_MAXIMUM_SIZE_DEFAULT_MESSAGE,
                                                                         self.log_config)
        if details.get('log_file_name') is None or details.get('log_file_name') == "":
            authenticationsdk.util.ExceptionAuth.validate_default_values(self.logger,
                                                                         GlobalLabelParameters.DEFAULT_LOG_FILE_NAME,
                                                                         self.log_config)

        if details.get('log_directory') is None or details.get('log_directory') == "":
            authenticationsdk.util.ExceptionAuth.validate_default_values(self.logger,
                                                                         GlobalLabelParameters.LOG_DIRECTORY_DEFAULT_MESSAGE,
                                                                         self.log_config)
        elif not (os.path.exists(details.get('log_directory')) or os.path.isdir(details.get('log_directory'))):

            authenticationsdk.util.ExceptionAuth.validate_default_values(self.logger,
                                                                         GlobalLabelParameters.LOG_DIRECTORY_INCORRECT_MESSAGE,
                                                                         self.log_config)


        if self.use_metakey and (self.portfolio_id is None or self.portfolio_id == ""):
            authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger, GlobalLabelParameters.PORTFOLIO_ID_REQ, self.log_config)

        if self.enable_client_cert is not None and self.enable_client_cert:
            if self.client_cert_dir is None or self.client_cert_dir == "":
                    authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger,
                                                                               GlobalLabelParameters.CLIENT_CERT_DIR_EMPTY,
                                                                               self.log_config)
            
            if self.ssl_client_cert is None or self.ssl_client_cert == "":
                    authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger,
                                                                               GlobalLabelParameters.SSL_CLIENT_CERT_EMPTY,
                                                                               self.log_config)
            
            if self.private_key is None or self.private_key == "":
                    authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger,
                                                                               GlobalLabelParameters.PRIVATE_KEY_EMPTY,
                                                                               self.log_config)

        # This process ensures that merchant_keyid and merchant_secretkey are mandatory in case of HTTP
        # And displays warning if key alias ,key_password,key_filepath,keyfilename are not present when
        # the method is JWT

        if type(self.authentication_type) == str:
            if self.authentication_type.lower() == GlobalLabelParameters.HTTP.lower():
                if self.merchant_id is None or self.merchant_id == "":
                    authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger,
                                                                               GlobalLabelParameters.MERCHANTID_REQ,
                                                                               self.log_config)
                
                if self.merchant_keyid is None or self.merchant_keyid == "":
                    authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger,
                                                                                       GlobalLabelParameters.MERCHANT_KEY_ID_REQ,
                                                                                       self.log_config)

                if self.merchant_secretkey is None or self.merchant_secretkey == "":
                    authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger,
                                                                                       GlobalLabelParameters.MERCHANT_SECRET_KEY_REQ,
                                                                                       self.log_config)

            elif self.authentication_type.lower() == GlobalLabelParameters.JWT.lower():
                if self.merchant_id is None or self.merchant_id == "":
                    authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger,
                                                                               GlobalLabelParameters.MERCHANTID_REQ,
                                                                               self.log_config)
                
                if self.key_alias is None or self.key_alias == "":
                    self.key_alias = self.merchant_id
                    authenticationsdk.util.ExceptionAuth.validate_default_values(self.logger,
                                                                                 GlobalLabelParameters.KEY_ALIAS_NULL_EMPTY,
                                                                                 self.log_config)
                if not (self.key_alias == self.merchant_id):
                    self.key_alias = self.merchant_id
                    authenticationsdk.util.ExceptionAuth.validate_default_values(self.logger,
                                                                                 GlobalLabelParameters.INVALID_KEY_ALIAS,
                                                                                 self.log_config)

                if self.key_password is None or self.key_password == "":
                    self.key_password = self.merchant_id
                    authenticationsdk.util.ExceptionAuth.validate_default_values(self.logger,
                                                                                 GlobalLabelParameters.KEY_PASSWORD_EMPTY,
                                                                                 self.log_config)

                if self.key_file_path is None or self.key_file_path == "":
                    self.key_file_path = GlobalLabelParameters.DEFAULT_KEY_FILE_PATH
                    authenticationsdk.util.ExceptionAuth.validate_default_values(self.logger,
                                                                                 GlobalLabelParameters.KEY_DIRECTORY_EMPTY + self.key_file_path,
                                                                                 self.log_config)

                if self.key_file_name is None or self.key_file_name == "":
                    self.key_file_name = self.merchant_id

                    authenticationsdk.util.ExceptionAuth.validate_default_values(self.logger,
                                                                                 GlobalLabelParameters.KEY_FILE_EMPTY,
                                                                                 self.log_config)

            elif self.authentication_type.lower() == GlobalLabelParameters.OAUTH.lower():                
                if self.access_token is None or self.access_token == "":
                    authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger,
                                                                               GlobalLabelParameters.ACCESS_TOKEN_EMPTY,
                                                                               self.log_config)
            
                if self.ssl_client_cert is None or self.ssl_client_cert == "":
                    authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger,
                                                                               GlobalLabelParameters.REFRESH_TOKEN_EMPTY,
                                                                               self.log_config)
            
            elif self.authentication_type.lower() == GlobalLabelParameters.MUTUAL_AUTH.lower():                
                if self.client_id is None or self.client_id == "":
                    authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger,
                                                                               GlobalLabelParameters.CLIENT_ID_EMPTY,
                                                                               self.log_config)
            
                if self.client_secret is None or self.client_secret == "":
                    authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger,
                                                                               GlobalLabelParameters.CLIENT_SECRET_EMPTY,
                                                                               self.log_config)
        else:
            authenticationsdk.util.ExceptionAuth.validate_merchant_details_log(self.logger,
                                                                               GlobalLabelParameters.AUTH_ERROR,
                                                                               self.log_config)

        log_items = GlobalLabelParameters.HIDE_MERCHANT_CONFIG_PROPS
        # This displays the logic for logging all cybs.json values
        if self.log_config.enable_log is True:
            for key, value in list(details.items()):
                if key in log_items:
                    del details[key]

                for keys, values in list(details.items()):
                    details[keys] = str(values)

            self.logger.info("Mconfig >      " + str(ast.literal_eval(json.dumps(details))))
