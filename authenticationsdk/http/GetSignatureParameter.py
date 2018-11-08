import hmac
from authenticationsdk.payloaddigest.PayLoadDigest import *
from authenticationsdk.util.GlobalLabelParameters import *


# This method returns value for parameter Signature which is then passed to Signature header
# paramter 'Signature' is calucated based on below keyvalues and then signed with SECRET KEY
# host: Sandbox(apitest.cybersource.com) or Production(api.cybersource.com) hostname
# date: "HTTP-date" format as defined by RFC7231
# (request-target): Should be in format of httpMethod: path Example: "post /pts/v2/payments"
# Digest: Only needed for POST calls. digestString = BASE64( HMAC-SHA256 ( Payload ));

# v-c-merchant-id: set value to Cybersource Merchant ID This ID can be found on EBC portal


class GetSignatureParameter:
    def __init__(self):

        self.merchant_config_sigparam = None
        self.date = None

    def get_signature_parameter(self, mconfig, merchant_secret_key, merchant_id, httpmethod, date):

        self.merchant_config_sigparam = mconfig
        self.date = date

        return self.get_signature_param(merchant_secret_key, merchant_id, httpmethod)

    # This method adds the Host-Date-(request-target)-v-c-merchant_id for get method
    # This method adds the Host-Date-(request-target)-digest-v-c-merchant_id for post method
    def get_signature_param(self, merchant_secret_key, merchant_id, httpmethod):

        signature_list = ([])
        # This method adds the host header
		

        signature_list.append(GlobalLabelParameters.HOST.lower())
        signature_list.append(": ")
        signature_list.append(self.merchant_config_sigparam.request_host)
        signature_list.append("\n")

        # This method adds the date header
        signature_list.append(GlobalLabelParameters.DATE.lower())
        signature_list.append(": ")
        signature_list.append(self.date)

        signature_list.append("\n")

        # This method adds the request-target header
        signature_list.append(GlobalLabelParameters.REQUEST_TARGET)
        signature_list.append(": ")
        # This forms the get_request_target
        if httpmethod.upper() == GlobalLabelParameters.GET:
            get_request_target = GlobalLabelParameters.GET_LOWER_CASE + self.merchant_config_sigparam.request_target
            signature_list.append(get_request_target)
        # This forms the post_request_target
        elif httpmethod.upper() == GlobalLabelParameters.POST:
            post_request_target = GlobalLabelParameters.POST_LOWER_CASE + self.merchant_config_sigparam.request_target
            signature_list.append(post_request_target)
        elif httpmethod.upper() == GlobalLabelParameters.PUT:
            put_request_target = GlobalLabelParameters.PUT_LOWER_CASE + self.merchant_config_sigparam.request_target
            signature_list.append(put_request_target)
        elif httpmethod.upper() == GlobalLabelParameters.PATCH:
            patch_request_target = GlobalLabelParameters.PATCH_LOWER_CASE + self.merchant_config_sigparam.request_target
            signature_list.append(patch_request_target)
        elif httpmethod.upper() == GlobalLabelParameters.DELETE:
            delete_request_target = GlobalLabelParameters.DELETE_LOWER_CASE + self.merchant_config_sigparam.request_target
            signature_list.append(delete_request_target)

        signature_list.append("\n")

        # This method adds the digest header only for post
        if httpmethod.upper() == GlobalLabelParameters.POST or httpmethod.upper() == GlobalLabelParameters.PUT or httpmethod.upper() == GlobalLabelParameters.PATCH :
            digest_get_obj = DigestAndPayload()
            digest = digest_get_obj.string_digest_generation(
                self.merchant_config_sigparam.request_json_path_data)
            signature_list.append(GlobalLabelParameters.DIGEST.lower())
            signature_list.append(": ")
            signature_list.append(GlobalLabelParameters.DIGEST_PREFIX + digest.decode("utf-8"))
            signature_list.append("\n")


        # This method adds the v-c-merchant-id header
        signature_list.append(GlobalLabelParameters.MERCHANT_ID)
        signature_list.append(": ")
        signature_list.append(str(merchant_id))
        sig_value = "".join(signature_list)


        sig_value_string = str(sig_value)
        sig_value_utf = bytes(sig_value_string,encoding='utf-8')

        # Signature string generated from above parameters is signed with secret key hashed with SHA-256
        # Secret key is base 64 decoded before signing

        secret = base64.b64decode(merchant_secret_key)

        hash_value = hmac.new(secret, sig_value_utf, hashlib.sha256)

        return base64.b64encode(hash_value.digest()).decode("utf-8")
