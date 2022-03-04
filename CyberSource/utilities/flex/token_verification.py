from . import rsa_verify
from .exception.flex_security_exception import FlexSecurityException 

class TokenVerification:
    def __init__(self):
        pass

    def verify_token(self, key, postparams):
        signed_list = []

        if postparams is None:
            raise flex_security_exception("A valid Dictionary must be supplied")
        signature = postparams.get("signature")
        if signature is None:
            raise flex_security_exception("Missing required field: signature")
        signed_fields = postparams.get("signedFields")
        if signed_fields is None:
            raise flex_security_exception("Missing required field: signedFields")

        signed_field = (signed_fields.split(","))    

        for i in signed_field:
            signed_list.append(",")
            signed_list.append(str(postparams.get("" + i)))

        signed_string = "".join(signed_list)
        signed_string = signed_string[1:]
        return rsa_verify.verify_token(key, signature, signed_string)
