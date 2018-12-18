import os
class MockData:
    HTTP_VALUES = {
        "authentication_type": "HTTP_SIGNATURE",
        "merchantid": "testrest",
        "run_environment": "CyberSource.Environment.SANDBOX",
        "key_alias": "testrest",
        "key_password": "testrest",
        "key_file_name": "testrest",
        "keys_directory": os.path.join(os.getcwd(),"resources"),
        "merchant_keyid": "08c94330-f618-42a3-b09d-e1e43be5efda",
        "merchant_secretkey": "yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE=",
        "enable_log": False,
        "log_file_name": "cybs",
        "log_maximum_size": 10485760,
        "log_directory": os.path.join(os.getcwd(),"Logs"),
        "proxy_address": "userproxy.com",
        "proxy_port": ""
    }
    JWT_VALUES = {
        "authentication_type": "jwt",
        "merchantid": "testrest",
        "run_environment": "CyberSource.Environment.SANDBOX",
        "key_alias": "testrest",
        "key_password": "testrest",
        "key_file_name": "testrest",
        "keys_directory": os.path.join(os.getcwd(),"resources"),
        "merchant_keyid": "08c94330-f618-42a3-b09d-e1e43be5efda",
        "merchant_secretkey": "yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE=",
        "enable_log": False,
        "log_file_name": "cybs",
        "log_maximum_size": 10485760,
        "log_directory": os.path.join(os.getcwd(),"Logs"),
        "proxy_address": "userproxy.com",
        "proxy_port": ""
    }
    HTTP_DEFAULT_VALUES = {
        "authentication_type": "HTTP_SIGNATURE",
        "merchantid": "testrest",
        "run_environment": "CyberSource.Environment.SANDBOX",
        "key_alias": "testrest",
        "key_password": "testrest",
        "key_file_name": "testrest",
        "keys_directory": os.path.join(os.getcwd(),"resources"),
        "merchant_keyid": "08c94330-f618-42a3-b09d-e1e43be5efda",
        "merchant_secretkey": "yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE=",
        "enable_log": "",
        "log_file_name": "cybs",
        "log_maximum_size": "",
        "log_directory": "",
        "proxy_address": "userproxy.com",
        "proxy_port": ""
    }
    JWT_VALUES_FOR_PRODUCTION = {
        "authentication_type": "jwt",
        "merchantid": "testrest",
        "run_environment": "CyberSource.Environment.PRODUCTION",
        "key_alias": "testrest",
        "key_password": "",
        "key_file_name": "",
        "keys_directory": "",
        "merchant_keyid": "08c94330-f618-42a3-b09d-e1e43be5efda",
        "merchant_secretkey": "yBJxy6LjM2TmcPGu+GaJrHtkke25fPpUX+UY6/L/1tE=",
        "enable_log": False,
        "log_file_name": "cybs",
        "log_maximum_size": 10485760,
        "log_directory": os.path.join(os.getcwd(),"Logs"),
        "proxy_address": "userproxy.com",
        "proxy_port": ""
    }
    REQUEST_DATA = {
        "clientReferenceInformation": {
            "code": "TC50171_3"
        },
        "processingInformation": {
            "commerceIndicator": "internet"
        },
        "aggregatorInformation": {
            "subMerchant": {
                "cardAcceptorID": "1234567890",
                "country": "US",
                "phoneNumber": "650-432-0000",
                "address1": "900 Metro Center",
                "postalCode": "94404-2775",
                "locality": "Foster City",
                "name": "Visa Inc",
                "administrativeArea": "CA",
                "region": "PEN",
                "email": "test@cybs.com"
            },
            "name": "V-Internatio",
            "aggregatorID": "123456789"
        },
        "orderInformation": {
            "billTo": {
                "country": "US",
                "lastName": "VDP",
                "address2": "Address 2",
                "address1": "201 S. Division St.",
                "postalCode": "48104-2201",
                "locality": "Ann Arbor",
                "administrativeArea": "MI",
                "firstName": "RTS",
                "phoneNumber": "999999999",
                "district": "MI",
                "buildingNumber": "123",
                "company": "Visa",
                "email": "test@cybs.com"
            },
            "amountDetails": {
                "totalAmount": "102.21",
                "currency": "USD"
            }
        },
        "paymentInformation": {
            "card": {
                "expirationYear": "2031",
                "number": "5555555555554444",
                "securityCode": "123",
                "expirationMonth": "12",
                "type": "002"
            }
        }
    }
    TRR_DATA = {
        "startDay": "23",
        "timeZone": "America/Chicago",
        "reportDefinitionName": "TransactionRequestClass",
        "startTime": "1100",
        "reportFrequency": "DAILY",
        "ReportName": "TRRReport",
        "reportFormat": "csv",
        "orgId": "testrest",
        "reportType": "detail",
        "reportFields": ["Request.RequestID", "Request.TransactionDate", "Request.MerchantReferenceNumber",
                         "Request.MerchantID"]
    }
