import logging
from datetime import datetime
import os


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# python 3 style
class MyLogger(object, metaclass=SingletonType):
    # __metaclass__ = SingletonType   # python 2 Style

    def __init__(self, mconfig):
        self.mconfig = mconfig

        if mconfig.enable_log is True:
            logger_folder = mconfig.log_directory
            logger_file = os.path.join(logger_folder, mconfig.log_file_name) + ".log"
            if not os.path.exists(logger_folder):
                os.makedirs(logger_folder)
            if not os.path.exists(logger_file):
                open(logger_file, "a+")
            if logger_file:
                if os.stat(logger_file).st_size > int(mconfig.maximum_size):
                    updated_file = os.path.join(logger_folder, mconfig.log_file_name) + "_" + datetime.now().strftime(
                        "%Y%m%d%H%M%S") + ".log"
                    os.rename(logger_file, updated_file)
            # setting the logger object
            self.logger = logging.getLogger()
            if not self.logger.handlers:
                # add a File handler
                handler = logging.FileHandler(filename=logger_file)
                # create a logging format
                formatter = logging.Formatter('%(asctime)s- %(message)s')
                handler.setFormatter(formatter)

                self.logger.setLevel(logging.INFO)
                # add the handlers to the logger
                self.logger.addHandler(handler)

    def get_logger(self):
        if self.mconfig.enable_log is True:
            return self.logger
