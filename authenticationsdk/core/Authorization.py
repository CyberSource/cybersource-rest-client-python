from authenticationsdk.http.HTTPSignatureToken import *
from authenticationsdk.jwt.Token import *
from authenticationsdk.core.ExceptionHandling import *
import authenticationsdk.util.ExceptionAuth


# This class calls for the generation of Signature message depending on the authentication type
class Authorization:

    # This method generates and return a encrypted signature based on the Authentication type
    def get_token(self, mconfig, date_time, logger):
        authentication_type = mconfig.authentication_type
        self.validate_request_type_method(mconfig)
        # Initializing the logger object

        try:
            # HTTP-Call

            if authentication_type.upper() == GlobalLabelParameters.HTTP.upper():
                http_sig_token = HTTPSignatureToken()
                http_sig_token.http_signature_token(mconfig, date_time)
                sig_token = http_sig_token.get_token()
                # Logging the parameters Content-Type,Merchant id,Date ,Host to the log file
                if mconfig.enable_log is True:
                    logger.info("Using Request Target:   " + mconfig.request_target)
                    logger.info("Authentication Type:   " + mconfig.authentication_type)
                    logger.info("Request-Type:      " + mconfig.request_type_method)
                    logger.info(GlobalLabelParameters.CONTENT_TYPE + ":   " + GlobalLabelParameters.APPLICATION_JSON)
                    logger.info(GlobalLabelParameters.MERCHANT_ID + ":   " + str(mconfig.merchant_id))
                    logger.info(GlobalLabelParameters.DATE + ":   " + date_time)
                    logger.info(GlobalLabelParameters.HOST + ":   " + mconfig.request_host)
                    # Logging the Digest when Request_type_method is Post
                    if mconfig.request_type_method.upper() == GlobalLabelParameters.POST or mconfig.request_type_method.upper() == GlobalLabelParameters.PUT:
                        digest_obj = DigestAndPayload()
                        encoded_digest = digest_obj.string_digest_generation(
                            mconfig.request_json_path_data)
                        logger.info(
                            GlobalLabelParameters.DIGEST + ":" + GlobalLabelParameters.DIGEST_PREFIX + (
                                encoded_digest).decode("utf-8"))
                    logger.info("Signature:     " + sig_token)

                return sig_token
            # JWT-Call
            elif authentication_type.upper() == GlobalLabelParameters.JWT.upper():

                jwt_sig_token = JwtSignatureToken()
                jwt_sig_token.jwt_signature_token(mconfig, date_time)
                sig_token_jwt = jwt_sig_token.get_token()

                # Logging the parameters Content-Type,Merchant id,Date ,Host to the log file
                if mconfig.enable_log is True:
                    logger.info("Using Request Target:   " + mconfig.request_target)
                    logger.info("Authentication Type:   " + mconfig.authentication_type)
                    logger.info("Request-Type:      " + mconfig.request_type_method)
                    logger.info(GlobalLabelParameters.CONTENT_TYPE + ":   " + GlobalLabelParameters.APPLICATION_JSON)
                    logger.info(GlobalLabelParameters.MERCHANT_ID + ":   " + str(mconfig.merchant_id))
                    logger.info(GlobalLabelParameters.DATE + ":   " + date_time)
                    logger.info(GlobalLabelParameters.HOST + ":   " + mconfig.request_host)
                    # Logging the Digest when Request_type_method is Post
                    logger.info("Authorization Bearer:     " + sig_token_jwt.decode("utf-8"))
                return sig_token_jwt
            else:
                raise ApiException(1, GlobalLabelParameters.AUTH_ERROR)
        except ApiException as e:
            authenticationsdk.util.ExceptionAuth.log_exception(logger, e, mconfig)
        except IOError as e:
            authenticationsdk.util.ExceptionAuth.log_exception(logger,
                                                               GlobalLabelParameters.FILE_NOT_FOUND + str(e.filename),
                                                               mconfig)
        except OSError as e:
            authenticationsdk.util.ExceptionAuth.log_exception(logger,
                                                               GlobalLabelParameters.SYSTEM_ERROR + str(e.filename),
                                                               mconfig)
        except Exception as e:
            if "mac verify failure" in str(e):
                authenticationsdk.util.ExceptionAuth.log_exception(logger, GlobalLabelParameters.INCORRECT_KEY_PASSWORD,
                                                                   mconfig)
            else:
                authenticationsdk.util.ExceptionAuth.log_exception(logger, repr(e), mconfig)

    # noinspection PyMethodMayBeStatic
    def validate_request_type_method(self, mconfig):

        if not (
                mconfig.request_type_method.upper() == GlobalLabelParameters.GET or mconfig.request_type_method.upper() == GlobalLabelParameters.POST or mconfig.request_type_method.upper() == GlobalLabelParameters.PUT or mconfig.request_type_method.upper() == GlobalLabelParameters.DELETE or mconfig.request_type_method.upper() == GlobalLabelParameters.PATCH):
            raise ApiException(1, GlobalLabelParameters.INVALID_REQUEST_TYPE_METHOD)
