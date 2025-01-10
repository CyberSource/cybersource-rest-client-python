

class MLEUtility:
    @staticmethod
    def check_is_mle_for_api(merchant_config, isMLESupportedByCybsForApi, operationId):
        isMLEForAPI = False
        if isMLESupportedByCybsForApi and merchant_config.get_useMLEGlobally():
            isMLEForAPI = True
        operation_array = [op_id.strip() for op_id in operationId.split(",")]
        if merchant_config.get_mapToControlMLEonAPI() and merchant_config.get_mapToControlMLEonAPI():
            for op_id in operation_array:
                if op_id in merchant_config.get_mapToControlMLEonAPI():
                    isMLEForAPI = merchant_config.get_mapToControlMLEonAPI()[op_id]
                    break
        return isMLEForAPI
    
    @staticmethod
    def encrypt_request_payload(merchant_config, requestBody):
        # complete the logic to encrypt request payload for mle    

        # return encrypted requestBody
        return requestBody

