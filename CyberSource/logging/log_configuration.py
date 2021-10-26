from authenticationsdk.util.GlobalLabelParameters import *

class LogConfiguration:
    def __init__(self):
        self.enable_log = GlobalLabelParameters.DEFAULT_ENABLE_LOG
        self.log_file_name = GlobalLabelParameters.LOG_FILE_NAME_DEFAULT
        self.log_directory = GlobalLabelParameters.DEFAULT_LOG_DIRECTORY
        self.log_format = GlobalLabelParameters.DEFAULT_LOG_FORMAT
        self.log_date_format = GlobalLabelParameters.DEFAULT_LOG_DATE_FORMAT
        self.log_maximum_size = GlobalLabelParameters.DEFAULT_MAXIMUM_SIZE
        self.log_level = GlobalLabelParameters.DEFAULT_LOG_LEVEL
        self.enable_masking = GlobalLabelParameters.DEFAULT_ENABLE_MASKING
    
    def set_enable_log(self, value):
        if value is not None and (type(value) == bool or (value.lower() == 'true' or value.lower() == 'false')):
            if type(value) == bool:
                self.enable_log = value
            elif value.lower() == 'true':
                self.enable_log = True
            else:
                self.enable_log = False
        else:
            self.enable_log = GlobalLabelParameters.DEFAULT_ENABLE_LOG
    
    def set_log_directory(self, value):
        if not (value is None or value == ""):
            self.log_directory = value
        else:
            self.log_directory = GlobalLabelParameters.DEFAULT_LOG_DIRECTORY

    def set_log_file_name(self, value):
        if not (value is None or value == ""):
            self.log_file_name = value
        else:
            self.log_file_name = GlobalLabelParameters.LOG_FILE_NAME_DEFAULT
    
    def set_log_maximum_size(self, value):
        if value is not None and (type(value) == int or value != ""):
            if type(value) == int:
                self.log_maximum_size = value
            else:
                self.log_maximum_size = int(value)
        else:
            self.log_maximum_size = GlobalLabelParameters.DEFAULT_MAXIMUM_SIZE  # 10 MB = 10485760 bytes

    def set_log_level(self, value):
        if not (value is None or value == ""):
            self.log_level = value
        else:
            self.log_level = GlobalLabelParameters.DEFAULT_LOG_LEVEL

    def set_enable_masking(self, value):
        if value is not None and (type(value) == bool or (value.lower() == 'true' or value.lower() == 'false')):
            if type(value) == bool:
                self.enable_masking = value
            elif value.lower() == 'true':
                self.enable_masking = True
            else:
                self.enable_masking = False
        else:
            self.enable_masking = True

    def set_log_format(self, value):
        if not (value is None or value == ""):
            self.log_format = value
        else:
            self.log_format = GlobalLabelParameters.DEFAULT_LOG_FORMAT

    def set_log_date_format(self, value):
        if not (value is None or value == ""):
            self.log_date_format = value
        else:
            self.log_date_format = GlobalLabelParameters.DEFAULT_LOG_DATE_FORMAT