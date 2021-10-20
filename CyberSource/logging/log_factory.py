import logging
from datetime import datetime
import os
from logging.handlers import RotatingFileHandler
from CyberSource.logging.log_configuration import LogConfiguration


def setup_logger(className, log_config = None):
    if log_config is None:
        log_config = LogConfiguration()
    if log_config.enable_log is True:
        # create logger
        logger = logging.getLogger(className)
        log_level = log_config.log_level.upper()
        logger.setLevel(log_level)

        log_folder = log_config.log_folder
        log_file_name = log_config.log_file_name

        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        file_name = os.path.join(log_folder , log_file_name) + ".log"

        # create console handler and set level to debug
        handler = RotatingFileHandler(filename = file_name, maxBytes=log_config.log_max_size, backupCount=10)
        handler.setLevel(log_level)

        # create formatter
        formatter = logging.Formatter(log_config.log_format, log_config.log_date_format)

        # add formatter to ch
        handler.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(handler)

        return logger