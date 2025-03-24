import json
import re

def get_response_code_message(response):
    switcher = {
        200: "Transaction Successful",
        400: "Bad Request",
        401: "Authentication Failed",
        403: "Forbidden",
        404: "URL Not Found",
        201: "Transaction Successful",
        500: "Internal Server Error",
        502:  "Bad Gateway",
        503: "SERVICE UNAVAILABLE",
        504: "Gateway Timeout"

    }
    return switcher.get(response, "Un-Identified")

def replace_underscore(dict_obj, deep=True):
    assert type(dict_obj) == dict
    converted_dict_obj = {}
    for snake_case_k in dict_obj:
        camel_case_k = re.sub('_([a-z])', lambda match: match.group(1).upper(), snake_case_k)
        value = dict_obj[snake_case_k]

        if type(value) == dict and deep:
            converted_dict_obj[camel_case_k] = replace_underscore(value, deep)
        elif type(value) == list and deep:
            converted_list_items = []
            for item in value:
                if type(item) == str:
                    converted_list_items.append(item)
                else:
                    converted_list_items.append(replace_underscore(item, deep))
            converted_dict_obj[camel_case_k] = converted_list_items
        else:
            converted_dict_obj[camel_case_k] = dict_obj[snake_case_k]
    return converted_dict_obj

def process_body(body):
    temp_body = body.replace("\"_", "\"")
    request_body = replace_underscore(json.loads(temp_body))
    body = json.dumps(request_body)
    body = body.replace("companyTaxId", "companyTaxID")
    body = body.replace("productSku", "productSKU")
    body = body.replace("secCode", "SECCode")
    return body
