from authenticationsdk.http.GetSignatureParameter import *

from authenticationsdk.core.TokenGeneration import *
from authenticationsdk.util.GlobalLabelParameters import *


# HttpSigToken return SignatureHeader Value that contains following paramters
# keyid     -- Merchant ID obtained from EBC portal
# algorithm -- Should have value as "HmacSHA256"
# headers   -- List of all header name passed in the Signature paramter below
# String getHeaders = "host date request-target" + " " + "v-c-merchant-id"
# String postHeaders = "host date request-target digest v-c-merchant-id"
# Note: Digest is not passed for GET calls
# signature -- Signature header has paramter called signature
# Paramter 'Signature' must contain all the paramters mentioned in header above in given order


class HTTPSignatureToken(TokenGeneration):
    def __init__(self):
        self.merchant_config_sighead = None
        self.merchant_key_id_sig = None
        self.merchant_secret_key_sig = None
        self.http_method_sig = None
        self.http_merchant_id = None
        self.http_get_id = None
        self.date_time = None

    def http_signature_token(self, mconfig,date_time):

        self.merchant_config_sighead = mconfig
        self.merchant_key_id_sig = str(mconfig.merchant_keyid)
        self.merchant_secret_key_sig = str(mconfig.merchant_secretkey)
        self.http_method_sig = mconfig.request_type_method
        self.http_merchant_id = mconfig.merchant_id
        self.date_time = date_time
		

    def get_token(self):

        return self.signature_header()

    def signature_header(self):

        # Initializing the logger object

        header_list = ([])
        # Key id is the key obtained from EBC
        header_list.append(
            GlobalLabelParameters.KEY_ID + str(self.merchant_config_sighead.merchant_keyid) + "\"")
        header_list.append(GlobalLabelParameters.ALGORITHM)
        # Headers are chosen based on HTTP method.Digest is not required for get method

        if self.http_method_sig.upper() == GlobalLabelParameters.GET:
            getheaders = "host date request-target" + " " + "v-c-merchant-id"
            header_list.append(GlobalLabelParameters.HEADERS_PARAM + getheaders + "\"")
        elif self.http_method_sig.upper() == GlobalLabelParameters.POST:
            postheaders = "host date request-target digest v-c-merchant-id"
            header_list.append(GlobalLabelParameters.HEADERS_PARAM + postheaders + "\"")
        elif self.http_method_sig.upper() == GlobalLabelParameters.PUT:
            putheaders = "host date request-target digest v-c-merchant-id"
            header_list.append(GlobalLabelParameters.HEADERS_PARAM + putheaders + "\"")
        elif self.http_method_sig.upper() == GlobalLabelParameters.PATCH:
            patchheaders = "host date request-target digest v-c-merchant-id"
            header_list.append(GlobalLabelParameters.HEADERS_PARAM + patchheaders + "\"")
        elif self.http_method_sig.upper() == GlobalLabelParameters.DELETE:
            deleteheaders = "host date request-target" + " " + "v-c-merchant-id"
            header_list.append(GlobalLabelParameters.HEADERS_PARAM + deleteheaders + "\"")

        get_signature_paramobj = GetSignatureParameter()
        # Getting value of the signature parameter
        signature = get_signature_paramobj.get_signature_parameter(self.merchant_config_sighead,
                                                                   self.merchant_secret_key_sig,
                                                                   self.http_merchant_id, self.http_method_sig,
                                                             self.date_time)

        header_list.append(
            GlobalLabelParameters.SIGNATURE_HEADER + signature + "\"")
        signature_value = ''.join(header_list)
		


        return signature_value
