import base64
import ssl

from jwcrypto import jwk
from cryptography import x509

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import pkcs12

from authenticationsdk.util.GlobalLabelParameters import *


class FileCache:

    def __init__(self):
        self.filecache = {}

    def get_private_key_from_pem(self, pem_file_path):
        with open(pem_file_path, 'r') as pem_file:
            cert = pem_file.read()
            private_key = jwk.JWK.from_pem(cert.encode('utf-8'))
            return private_key
        
    def load_certificates(self, filepath, filename, password):
        return pkcs12.load_key_and_certificates(
            open(os.path.join(filepath, filename) + GlobalLabelParameters.P12_PREFIX, 'rb').read(),
            password=password.encode(),
            backend=default_backend()
        )

    def update_cache(self, cache_key, certificate, private_key, file_mod_time, is_mle, filename, additional_certificates):
        if is_mle:
            mle_cert = None

            # Check the main certificate
            for attribute in certificate.subject:
                if attribute.oid.dotted_string == '2.5.4.3':  # OID for CN
                    cn_value = attribute.value
                    if cn_value == GlobalLabelParameters.DEFAULT_MLE_ALIAS_FOR_CERT:
                        mle_cert = certificate
                        break

            # Check the additional certificates if not found in the main certificate
            if not mle_cert:
                for cert in additional_certificates:
                    for attribute in cert.subject:
                        if attribute.oid.dotted_string == '2.5.4.3':  # OID for CN
                            cn_value = attribute.value
                            if cn_value == GlobalLabelParameters.DEFAULT_MLE_ALIAS_FOR_CERT:
                                mle_cert = cert
                                break
                    if mle_cert:
                        break

            if mle_cert:
                self.filecache[cache_key] = [mle_cert, file_mod_time]
            else:
                raise ValueError(f"No certificate found matching the MLE key alias: {GlobalLabelParameters.DEFAULT_MLE_ALIAS_FOR_CERT}")
        else:
            cert_pem = certificate.public_bytes(serialization.Encoding.PEM)
            cert_pem_str = cert_pem.decode('utf-8')
            der_cert_string = base64.b64encode(ssl.PEM_cert_to_DER_cert(cert_pem_str))

            self.filecache.setdefault(str(filename), []).append(der_cert_string)
            self.filecache.setdefault(str(filename), []).append(private_key)
            self.filecache.setdefault(str(filename), []).append(file_mod_time)
            

    def grab_file(self, mconfig, filepath, filename, is_mle=False):
        file_mod_time = os.stat(os.path.join(filepath, filename) + GlobalLabelParameters.P12_PREFIX).st_mtime

        if is_mle:
            cache_key = GlobalLabelParameters.MLE_CERT
        else:
            cache_key = filename
            
        if cache_key not in self.filecache:

            private_key, certificate, additional_certificates = self.load_certificates(filepath, filename, mconfig.key_password)
            self.update_cache(cache_key, certificate, private_key, file_mod_time, is_mle, filename, additional_certificates)

        if file_mod_time != self.filecache[cache_key][1 if is_mle else 2]:

            private_key, certificate, additional_certificates = self.load_certificates(filepath, filename, mconfig.key_password)
            self.update_cache(cache_key, certificate, private_key, file_mod_time, is_mle, filename, additional_certificates)

        return self.filecache[cache_key]

    def get_cached_private_key_from_pem(self, file_path, cache_key):
        file_mod_time = os.stat(file_path).st_mtime
        if (cache_key not in self.filecache) or file_mod_time != self.filecache[str(cache_key)][1]:
            private_key = self.get_private_key_from_pem(file_path)
            self.filecache.setdefault(str(cache_key), []).append(private_key)
            self.filecache.setdefault(str(cache_key), []).append(file_mod_time)
        return self.filecache[str(cache_key)][0]