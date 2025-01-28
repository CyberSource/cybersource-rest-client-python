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

    # def grab_file(self, mconfig, filepath, filename, key_alias):
    #     file_mod_time = os.stat(os.path.join(filepath, filename) + GlobalLabelParameters.P12_PREFIX).st_mtime

        # if key_alias not in self.filecache or file_mod_time != self.filecache[key_alias][2]:
        #     if filename not in self.filecache:
        #         print(f"Cache miss: {key_alias} not found in cache. Loading from file.")
        #     else:
        #         print("Cached file is outdated. Reloading from file.")

        #     private_key, certificate, additional_certificates = self.load_certificates(filepath, filename, mconfig.key_password)

        #     target_cert = None

        #     # Check the main certificate
        #     for attribute in certificate.subject:
        #         if attribute.oid.dotted_string == '2.5.4.3':  # OID for CN
        #             cn_value = attribute.value
        #             if cn_value == key_alias:
        #                 target_cert = certificate
        #                 break

        #     # Check the additional certificates if not found in the main certificate
        #     if not target_cert:
        #         for cert in additional_certificates:
        #             for attribute in cert.subject:
        #                 if attribute.oid.dotted_string == '2.5.4.3':  # OID for CN
        #                     cn_value = attribute.value
        #                     if cn_value == key_alias:
        #                         target_cert = cert
        #                         break
        #             if target_cert:
        #                 break
            

        #     if target_cert:
        #         if key_alias == mconfig.get_mleKeyAlias:
        #             self.filecache[str(key_alias)] = [target_cert, None ,file_mod_time]
        #         elif key_alias == mconfig.key_alias:
        #             cert_pem = target_cert.public_bytes(serialization.Encoding.PEM)
        #             cert_pem_str = cert_pem.decode('utf-8')
        #             der_cert_string = base64.b64encode(ssl.PEM_cert_to_DER_cert(cert_pem_str))

        #             self.filecache[str(key_alias)] = [der_cert_string, private_key, file_mod_time]
        #     else:
        #         self.filecache[str(key_alias)] = [None, None, None, None]

        # print("target_cert", target_cert)
        # print("self.filecache[filename]", self.filecache[key_alias])

        # return self.filecache[key_alias]
    
    def get_cert_based_on_key_alias(self, certificate, additional_certificates, key_alias):
        target_cert = None

        # Check the main certificate
        for attribute in certificate.subject:
            if attribute.oid.dotted_string == '2.5.4.3':  # OID for CN
                cn_value = attribute.value
                if cn_value == key_alias:
                    target_cert = certificate
                    break

        # Check the additional certificates if not found in the main certificate
        if not target_cert:
            for cert in additional_certificates:
                for attribute in cert.subject:
                    if attribute.oid.dotted_string == '2.5.4.3':  # OID for CN
                        cn_value = attribute.value
                        if cn_value == key_alias:
                            target_cert = cert
                            break
                if target_cert:
                    break
        print("target_cert", target_cert)

        return target_cert

    
    def update_cache(self, mconfig, filepath, filename):
        file_mod_time = os.stat(os.path.join(filepath, filename) + GlobalLabelParameters.P12_PREFIX).st_mtime
        private_key, certificate, additional_certificates = self.load_certificates(filepath, filename, mconfig.key_password)
        
        jwt_cert= self.get_cert_based_on_key_alias(certificate, additional_certificates, mconfig.key_alias)
        jwt_cert_pem = jwt_cert.public_bytes(serialization.Encoding.PEM)
        jwt_cert_pem_str = jwt_cert_pem.decode('utf-8')
        jwt_der_cert_string = base64.b64encode(ssl.PEM_cert_to_DER_cert(jwt_cert_pem_str))
        
        mle_cert = self.get_cert_based_on_key_alias(certificate, additional_certificates, mconfig.get_mleKeyAlias())
        print("mle_cert",mle_cert)
        
        self.filecache.setdefault(str(filename), []).append(jwt_der_cert_string)
        self.filecache.setdefault(str(filename), []).append(private_key)
        self.filecache.setdefault(str(filename), []).append(file_mod_time)
        self.filecache.setdefault(str(filename), []).append(mle_cert)

    def grab_file(self, mconfig, filepath, filename):
        file_mod_time = os.stat(os.path.join(filepath, filename) + GlobalLabelParameters.P12_PREFIX).st_mtime
        if filename not in self.filecache or file_mod_time != self.filecache[filename][2]:
            self.update_cache(mconfig, filepath, filename)
        return self.filecache[filename]
    
    def get_cached_private_key_from_pem(self, file_path, cache_key):
        file_mod_time = os.stat(file_path).st_mtime
        if (cache_key not in self.filecache) or file_mod_time != self.filecache[str(cache_key)][1]:
            private_key = self.get_private_key_from_pem(file_path)
            self.filecache.setdefault(str(cache_key), []).append(private_key)
            self.filecache.setdefault(str(cache_key), []).append(file_mod_time)
        return self.filecache[str(cache_key)][0]
