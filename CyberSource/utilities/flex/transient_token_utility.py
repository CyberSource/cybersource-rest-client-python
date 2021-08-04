from . import base64
from . import json


class TransientTokenUtility:
    def __init__(self):
        pass

    def generate_transient_token(self,jwt):
        split_contents[] = jwt.split(",")
        if(len(split_contents) > 1):
            encoded_string = split_contents[1]
            data = base64.b64decode(encoded_string)
            transient_model = json.load(data)
            return transient_model
        return none;  


