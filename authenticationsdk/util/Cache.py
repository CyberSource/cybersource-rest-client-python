import os
from authenticationsdk.util.GlobalLabelParameters import *
from OpenSSL import crypto
import ssl
import base64


class FileCache:

    def __init__(self):
        self.filecache = {}

    def grab_file(self, mconfig, filepath, filename):

        file_mod_time = os.stat(os.path.join(filepath, filename)+GlobalLabelParameters.P12_PREFIX).st_mtime

        if filename not in self.filecache:

            p12 = crypto.load_pkcs12(open(
                os.path.join(filepath, filename)+GlobalLabelParameters.P12_PREFIX,
                'rb').read(), mconfig.key_password)
            cert_str = crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate())
            der_cert_string = base64.b64encode(ssl.PEM_cert_to_DER_cert(cert_str.decode("utf-8")))
            private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey()).decode("utf-8")

            self.filecache.setdefault(str(filename), []).append(der_cert_string)
            self.filecache.setdefault(str(filename), []).append(private_key)
            self.filecache.setdefault(str(filename), []).append(file_mod_time)

        if file_mod_time != self.filecache[filename][2]:
            p12 = crypto.load_pkcs12(open(
                os.path.join(filepath, filename) + GlobalLabelParameters.P12_PREFIX,
                'rb').read(), mconfig.key_password)
            cert_str = crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate())
            der_cert_string = base64.b64encode(ssl.PEM_cert_to_DER_cert(cert_str.decode("utf-8")))
            private_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey()).decode("utf-8")

            self.filecache.setdefault(str(filename), []).append(der_cert_string)
            self.filecache.setdefault(str(filename), []).append(private_key)
            self.filecache.setdefault(str(filename), []).append(file_mod_time)

        return self.filecache[filename]
