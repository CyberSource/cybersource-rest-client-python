import base64
import ssl

from OpenSSL import crypto
from jwcrypto import jwk

from authenticationsdk.util.GlobalLabelParameters import *


class FileCache:

    def __init__(self):
        self.filecache = {}

    def get_private_key_from_pem(self, pem_file_path):
        with open(pem_file_path, 'r') as pem_file:
            cert = pem_file.read()
            private_key = jwk.JWK.from_pem(cert.encode('utf-8'))
            return private_key

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

    def get_cached_private_key_from_pem(self, file_path, cache_key):
        file_mod_time = os.stat(file_path).st_mtime
        if (cache_key not in self.filecache) or file_mod_time != self.filecache[str(cache_key)][1]:
            private_key = self.get_private_key_from_pem(file_path)
            self.filecache.setdefault(str(cache_key), []).append(private_key)
            self.filecache.setdefault(str(cache_key), []).append(file_mod_time)
        return self.filecache[str(cache_key)][0]


