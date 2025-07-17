import base64
import ssl

from jwcrypto import jwk

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import pkcs12

from typing_extensions import deprecated

from authenticationsdk.util.CertificateUtility import CertificateUtility
from authenticationsdk.util.GlobalLabelParameters import *
import CyberSource.logging.log_factory as LogFactory
import threading

class CertInfo:
    def __init__(self, mle_certificate, timestamp):
        self.MLECertificate = mle_certificate
        self.Timestamp = timestamp

class FileCache:
    _instance = None
    logger = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FileCache, cls).__new__(cls, *args, **kwargs)
            # Initialize your cache here
            cls._instance._initialize_cache()
        return cls._instance

    def _initialize_cache(self):
        # Your cache initialization code here
        self.filecache = {}
        self.mlecache = {}
        self._cache_lock = threading.RLock()

    @deprecated("This method has been marked as Deprecated and will be removed in coming releases.")
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

        return target_cert

    def update_cache(self, mconfig, filepath, filename):
        file_mod_time = os.stat(os.path.join(filepath, filename) + GlobalLabelParameters.P12_PREFIX).st_mtime
        private_key, certificate, additional_certificates = self.load_certificates(filepath, filename, mconfig.key_password)
        
        jwt_cert= self.get_cert_based_on_key_alias(certificate, additional_certificates, mconfig.key_alias)
        jwt_cert_pem = jwt_cert.public_bytes(serialization.Encoding.PEM)
        jwt_cert_pem_str = jwt_cert_pem.decode('utf-8')
        jwt_der_cert_string = base64.b64encode(ssl.PEM_cert_to_DER_cert(jwt_cert_pem_str))
        
        mle_cert = self.get_cert_based_on_key_alias(certificate, additional_certificates, mconfig.get_mleKeyAlias())
        
        self.filecache[str(filename)] = [jwt_der_cert_string, private_key, file_mod_time, mle_cert]

    def grab_file(self, mconfig, filepath, filename):
        file_mod_time = os.stat(os.path.join(filepath, filename) + GlobalLabelParameters.P12_PREFIX).st_mtime
        if filename not in self.filecache or file_mod_time != self.filecache[filename][2]:
            self.update_cache(mconfig, filepath, filename)
        return self.filecache[filename]

    @deprecated("This method has been marked as Deprecated and will be removed in coming releases.")
    def get_cached_private_key_from_pem(self, file_path, cache_key):
        file_mod_time = os.stat(file_path).st_mtime
        if (cache_key not in self.filecache) or file_mod_time != self.filecache[str(cache_key)][1]:
            private_key = self.get_private_key_from_pem(file_path)
            self.filecache[str(cache_key)] = [private_key, file_mod_time]
        return self.filecache[str(cache_key)][0]

    def get_request_mle_cert_from_cache(self, merchant_config):
        if FileCache.logger is None:
            FileCache.logger = LogFactory.setup_logger(__name__, merchant_config.log_config)
        logger = FileCache.logger

        merchant_id = merchant_config.merchant_id
        certificate_identifier = None
        certificate_file_path = None

        # Priority #1: Get cert from merchantConfig.mle_for_request_public_cert_path if certPath is provided
        if merchant_config.mleForRequestPublicCertPath and merchant_config.mleForRequestPublicCertPath.strip():
            certificate_identifier = GlobalLabelParameters.MLE_CACHE_IDENTIFIER_FOR_CONFIG_CERT
            certificate_file_path = merchant_config.mleForRequestPublicCertPath
        # Priority #2: If mle_for_request_public_cert_path not provided, get mlecert from p12 if provided and jwt auth type
        elif (GlobalLabelParameters.JWT.lower() == merchant_config.authentication_type.lower() and merchant_config.p12KeyFilePath):
            certificate_identifier = GlobalLabelParameters.MLE_CACHE_IDENTIFIER_FOR_P12_CERT
            certificate_file_path = merchant_config.p12KeyFilePath
        # Priority #3: Get mlecert from default cert in SDK as per CAS or PROD env.
        else:
            logger.debug("The certificate to use for MLE for requests is not provided in the merchant configuration. Please ensure that the certificate path is provided.")
            return None

        cache_key = f"{merchant_id}_{certificate_identifier}"
        mle_certificate = self.get_mle_cert_based_on_cache_key(merchant_config, cache_key, certificate_file_path)

        CertificateUtility.validate_certificate_expiry(mle_certificate, merchant_config.key_alias, certificate_identifier, merchant_config.log_config)

        return mle_certificate

    def get_mle_cert_based_on_cache_key(self, merchant_config, cache_key, certificate_file_path):
        with self._cache_lock:
            cert_info = self.mlecache.get(cache_key)

            file_timestamp = os.path.getmtime(certificate_file_path)
            if cert_info is None or cert_info.Timestamp != file_timestamp:
                self.setup_mle_cache(merchant_config, cache_key, certificate_file_path)
                cert_info = self.mlecache.get(cache_key)

            return cert_info.MLECertificate if cert_info else None

    def setup_mle_cache(self, merchant_config, cache_key, certificate_file_path):
        if FileCache.logger is None:
            FileCache.logger = LogFactory.setup_logger(__name__, merchant_config.log_config)
        logger = FileCache.logger

        mle_certificate = None

        # Handle PEM certificate case
        if cache_key.endswith(GlobalLabelParameters.MLE_CACHE_IDENTIFIER_FOR_CONFIG_CERT):
            certificates = CertificateUtility.load_certificates_from_pem_file(certificate_file_path)
            try:
                mle_certificate = CertificateUtility.get_cert_based_on_key_alias(certificates, merchant_config.mleKeyAlias)
            except Exception:
                if mle_certificate is None:
                    file_name = os.path.basename(certificate_file_path)
                    logger.warning(f"No certificate found for the specified mle_key_alias '{merchant_config.mleKeyAlias}'. Using the first certificate from file {file_name} as the MLE request certificate.")
                    mle_certificate = certificates[0]  # Take first certificate

        # Handle P12 certificate case
        if cache_key.endswith(GlobalLabelParameters.MLE_CACHE_IDENTIFIER_FOR_P12_CERT):
            try:
                certificates = CertificateUtility.fetch_certificate_collection_from_p12_file(merchant_config.p12KeyFilePath, merchant_config.key_password)
                mle_certificate = CertificateUtility.get_cert_based_on_key_alias(certificates, merchant_config.mleKeyAlias)
            except Exception:
                file_name = os.path.basename(merchant_config.p12KeyFilePath)
                logger.error(f"No certificate found for the specified mle_key_alias '{merchant_config.mleKeyAlias}' in file {file_name}.")
                raise ValueError(f"No certificate found for the specified mle_key_alias '{merchant_config.mleKeyAlias}' in file {file_name}.")

        # Save to cache (thread-safe)
        cert_info = CertInfo(
            mle_certificate,
            os.path.getmtime(certificate_file_path)
        )
        with self._cache_lock:
            self.mlecache[cache_key] = cert_info