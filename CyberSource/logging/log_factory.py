import logging
from datetime import datetime
import os
from logging.handlers import RotatingFileHandler
from .log_configuration import LogConfiguration
from .sensitive_formatter import SensitiveFormatter


def setup_logger(className, log_config = None):
    if log_config is None:
        log_config = LogConfiguration()
    if log_config.enable_log is True:
        # create logger
        logger = logging.getLogger(className)
        log_level = log_config.log_level.upper()
        logger.setLevel(log_level)

        log_folder = log_config.log_directory
        log_file_name = log_config.log_file_name

        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        file_name = os.path.join(log_folder , log_file_name) + ".log"

        # create console handler and set level
        handler = RotatingFileHandler(filename = file_name, maxBytes=log_config.log_maximum_size, backupCount=10)
        handler.setLevel(log_level)

        if log_config.enable_masking:
            # add formatter to ch
            handler.setFormatter(SensitiveFormatter(log_config.log_format))
        else:
            # create formatter
            formatter = logging.Formatter(log_config.log_format, log_config.log_date_format)
            handler.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(handler)

        return logger