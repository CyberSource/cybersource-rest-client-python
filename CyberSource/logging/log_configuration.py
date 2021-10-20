from authenticationsdk.util.GlobalLabelParameters import *

class LogConfiguration:
    def __init__(self):
        self.enable_log = False
        self.log_file_name = GlobalLabelParameters.LOG_FILE_NAME_DEFAULT
        self.log_folder = GlobalLabelParameters.DEFAULT_LOG_DIRECTORY
        self.log_format = GlobalLabelParameters.DEFAULT_LOG_FORMAT
        self.log_date_format = GlobalLabelParameters.DEFAULT_LOG_DATE_FORMAT
        self.log_max_size = GlobalLabelParameters.DEFAULT_MAXIMUM_SIZE
        self.log_level = GlobalLabelParameters.DEFAULT_LOG_LEVEL
        self.enable_masking = True
    
    def set_enable_log(self, val):
        self.enable_log = val

    def set_log_folder(self, val):
        self.log_folder = val

    def set_log_file_name(self, val):
        self.log_file_name = val

    def set_log_max_size(self, val):
        self.log_max_size = val

    def set_log_level(self, val):
        self.log_level = val

    def set_log_format(self, val):
        self.log_format = val

    def set_log_date_format(self, val):
        self.log_date_format = val

    def set_enable_masking(self, val):
        self.enable_masking = val