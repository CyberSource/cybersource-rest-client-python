import json
import os
from cybersource_rest_client_python.authenticationsdk.core.ExceptionHandling import *
from cybersource_rest_client_python.authenticationsdk.util.GlobalLabelParameters import *
from cybersource_rest_samples_python.data.Configaration import *



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

    def configarion(self):
        configaration = Configaration()
        return configaration.get_configaration()

