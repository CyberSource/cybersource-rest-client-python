import json
import os
from authenticationsdk.core.ExceptionHandling import *
from authenticationsdk.util.GlobalLabelParameters import *



class PropertiesUtil:
    def __init__(self):
        self.cybs_path = "..\Resources/cybs.json"


    # This method reads from cybs.json if provided else it reads from configuration file
    def properties_util(self):
        if os.path.exists(self.cybs_path):

            with open(self.cybs_path) as json_data:
                details_dict = json.load(json_data)

                return details_dict

        else:
            raise ApiException(1, GlobalLabelParameters.INVALID_CYBS_PATH)



