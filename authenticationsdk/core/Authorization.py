from authenticationsdk.http.HTTPSignatureToken import *
from authenticationsdk.jwt.Token import *
from authenticationsdk.oauth.OAuthToken import *
from authenticationsdk.core.ExceptionHandling import *
import authenticationsdk.util.ExceptionAuth
import CyberSource.logging.log_factory as LogFactory


# This class calls for the generation of Signature message depending on the authentication type
class Authorization:

    def __init__(self):
        self.logger = None

    # This method generates and return a encrypted signature based on the Authentication type
    def get_token(self, mconfig, date_time, logger = None):        
        authentication_type = mconfig.authentication_type
        self.validate_request_type_method(mconfig)
        # Initializing the logger object
        self.logger = LogFactory.setup_logger(self.__class__.__name__, mconfig.log_config)

        try:
            # HTTP-Call

            if authentication_type.upper() == GlobalLabelParameters.HTTP.upper():
                http_sig_token = HTTPSignatureToken()
                http_sig_token.http_signature_token(mconfig, date_time)
                sig_token = http_sig_token.get_token()
                # Logging the parameters Content-Type,Merchant id,Date ,Host to the log file
                if mconfig.log_config.enable_log is True:
                    self.logger.info("Using Request Target:   " + mconfig.request_target)
                    self.logger.info("Authentication Type:   " + mconfig.authentication_type)
                    self.logger.info("Request-Type:      " + mconfig.request_type_method)
                    self.logger.info(GlobalLabelParameters.CONTENT_TYPE + ":   " + GlobalLabelParameters.APPLICATION_JSON)
                    self.logger.info(GlobalLabelParameters.MERCHANT_ID + ":   " + str(mconfig.merchant_id))
                    self.logger.info(GlobalLabelParameters.DATE + ":   " + date_time)
                    self.logger.info(GlobalLabelParameters.HOST + ":   " + mconfig.request_host)
                    # Logging the Digest when Request_type_method is Post
                    if mconfig.request_type_method.upper() == GlobalLabelParameters.POST or mconfig.request_type_method.upper() == GlobalLabelParameters.PUT:
                        digest_obj = DigestAndPayload()
                        encoded_digest = digest_obj.string_digest_generation(
                            mconfig.request_json_path_data)
                        self.logger.info(
                            GlobalLabelParameters.DIGEST + ":" + GlobalLabelParameters.DIGEST_PREFIX + (
                                encoded_digest).decode("utf-8"))
                    self.logger.info("Signature:     " + sig_token)

                return sig_token
            # JWT-Call
            elif authentication_type.upper() == GlobalLabelParameters.JWT.upper():

                jwt_sig_token = JwtSignatureToken()
                jwt_sig_token.jwt_signature_token(mconfig, date_time)
                sig_token_jwt = jwt_sig_token.get_token()

                # Logging the parameters Content-Type,Merchant id,Date ,Host to the log file
                if mconfig.log_config.enable_log is True:
                    self.logger.info("Using Request Target:   " + mconfig.request_target)
                    self.logger.info("Authentication Type:   " + mconfig.authentication_type)
                    self.logger.info("Request-Type:      " + mconfig.request_type_method)
                    self.logger.info(GlobalLabelParameters.CONTENT_TYPE + ":   " + GlobalLabelParameters.APPLICATION_JSON)
                    self.logger.info(GlobalLabelParameters.MERCHANT_ID + ":   " + str(mconfig.merchant_id))
                    self.logger.info(GlobalLabelParameters.DATE + ":   " + date_time)
                    self.logger.info(GlobalLabelParameters.HOST + ":   " + mconfig.request_host)
                    # Logging the Digest when Request_type_method is Post
                    # self.logger.info("Authorization Bearer:     " + sig_token_jwt.encode("utf-8").decode("utf-8"))
                return sig_token_jwt
            elif authentication_type.upper() == GlobalLabelParameters.OAUTH.upper():
                token = OAuthToken()
                token.oauth_token(mconfig)
                o_auth_token = token.get_token() 
                # self.logger.info("Authorization Bearer:     " + o_auth_token.encode("utf-8").decode("utf-8"))
                return o_auth_token
            else:
                raise ApiException(1, GlobalLabelParameters.AUTH_ERROR)
        except ApiException as e:
            authenticationsdk.util.ExceptionAuth.log_exception(self.logger, e, mconfig.log_config)
        except IOError as e:
            authenticationsdk.util.ExceptionAuth.log_exception(self.logger,
                                                               GlobalLabelParameters.FILE_NOT_FOUND + str(e.filename),
                                                               mconfig.log_config)
        except OSError as e:
            authenticationsdk.util.ExceptionAuth.log_exception(self.logger,
                                                               GlobalLabelParameters.SYSTEM_ERROR + str(e.filename),
                                                               mconfig.log_config)
        except Exception as e:
            if "mac verify failure" in str(e):
                authenticationsdk.util.ExceptionAuth.log_exception(self.logger, GlobalLabelParameters.INCORRECT_KEY_PASSWORD,
                                                                   mconfig.log_config)
            else:
                authenticationsdk.util.ExceptionAuth.log_exception(self.logger, repr(e), mconfig.log_config)

    # noinspection PyMethodMayBeStatic
    def validate_request_type_method(self, mconfig):

        if not (
                mconfig.request_type_method.upper() == GlobalLabelParameters.GET or mconfig.request_type_method.upper() == GlobalLabelParameters.POST or mconfig.request_type_method.upper() == GlobalLabelParameters.PUT or mconfig.request_type_method.upper() == GlobalLabelParameters.DELETE or mconfig.request_type_method.upper() == GlobalLabelParameters.PATCH):
            raise ApiException(1, GlobalLabelParameters.INVALID_REQUEST_TYPE_METHOD)
