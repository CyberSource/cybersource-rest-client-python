import sys


def log_exception(logger, message, mconfig):
    if mconfig.enable_log is True:
        print(message)
        print("Error: Check Log file for more details.")
        logger.exception(message)
    raise Exception(message)



def validate_merchant_details_log(logger, message, mconfig):

    if mconfig.enable_log is True:
        print(message)
        print("Error: Check Log file for more details.")
        logger.error(message)
    raise Exception(message)




def validate_default_values(logger, message, mconfig):
    if mconfig.enable_log is True:
        print(message)
        logger.warning(message)

