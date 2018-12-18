import logging
from datetime import datetime
import os


def setup_logger(mconfig):
    # Creating a log directory if the directory is not present
    # If the directory is present then just append in the file
    if mconfig.enable_log is True:
        logger_folder = mconfig.log_directory
        logger_file = os.path.join(logger_folder , mconfig.log_file_name)+ ".log"
        if not os.path.exists(logger_folder):
            os.makedirs(logger_folder)
        if not os.path.exists(logger_file):
            open(logger_file, "a+")
        if logger_file:
            if os.stat(logger_file).st_size > int(mconfig.maximum_size):
                updated_file = os.path.join(logger_folder , mconfig.log_file_name)+"_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".log"
                os.rename(logger_file, updated_file)
        # setting the logger object
        logger = logging.getLogger()
        if not logger.handlers:
            # add a File handler
            handler = logging.FileHandler(filename=logger_file)
            # create a logging format
            formatter = logging.Formatter('%(asctime)s- %(message)s')
            handler.setFormatter(formatter)

            logger.setLevel(logging.INFO)
            # add the handlers to the logger
            logger.addHandler(handler)

        return logger
