import sys


def log_exception(logger, message, mconfig):
    if mconfig.enable_log is True:
        print("Error: Check Log file for more details.")
        logger.exception(message)
    sys.exit(1)


def validate_merchant_details_log(logger, message, mconfig):

    if mconfig.enable_log is True:
        print("Error: Check Log file for more details.")
        logger.error(message)
    sys.exit(1)



def validate_default_values(logger, message, mconfig):
    if mconfig.enable_log is True:
        logger.warning(message)
