import base64
import ssl
import threading

from jwcrypto import jwk

from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import pkcs12, load_pem_private_key

from typing_extensions import deprecated

from authenticationsdk.util.CertificateUtility import CertificateUtility
from authenticationsdk.util.GlobalLabelParameters import *
import CyberSource.logging.log_factory as LogFactory
import os

class CertInfo:
    def __init__(self, certificate, timestamp, private_key):
        self.certificate = certificate
        self.timestamp = timestamp
        self.private_key = private_key

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
        self._p12_cache_lock = threading.RLock()
        self.mlecache = {}
        self._mle_cache_lock = threading.RLock()
        self.p12_parsed_cache = {}
        self._p12_parsed_cache_lock = threading.RLock()

    def fetch_cached_p12_certificate(self, merchant_config, p12_file_path, key_password):
        try:
            file_last_modified_time = os.stat(p12_file_path).st_mtime
            filename_without_ext = os.path.splitext(os.path.basename(p12_file_path))[0]
            if filename_without_ext not in self.filecache or file_last_modified_time != self.filecache[filename_without_ext].timestamp:
                self.update_cache(merchant_config, p12_file_path, key_password)
            return self.filecache[filename_without_ext]
        except Exception:
            raise ValueError(f"ERROR : KeyPassword provided: {key_password} is incorrect.")
        
    def update_cache(self, merchant_config, p12_file_path, key_password):
        file_last_modified_time = os.stat(p12_file_path).st_mtime
        filename_without_ext = os.path.splitext(os.path.basename(p12_file_path))[0]
        private_key, certificate_list = CertificateUtility.fetch_certificate_collection_from_p12_file(p12_file_path, key_password)

        jwt_certificate = CertificateUtility.get_cert_based_on_key_alias(certificate_list, merchant_config.key_alias)
        jwt_certificate_pem = jwt_certificate.public_bytes(serialization.Encoding.PEM)
        jwt_certificate_pem_unicode_str = jwt_certificate_pem.decode('utf-8')
        jwt_certificate_der_format = base64.b64encode(ssl.PEM_cert_to_DER_cert(jwt_certificate_pem_unicode_str))

        certificate_information = CertInfo(
            jwt_certificate_der_format,
            file_last_modified_time,
            private_key
        )

        with self._p12_cache_lock:
            self.filecache[str(filename_without_ext)] = certificate_information

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
        if (merchant_config.mleForRequestPublicCertPath and 
            merchant_config.mleForRequestPublicCertPath.strip()):
            certificate_identifier = GlobalLabelParameters.MLE_CACHE_IDENTIFIER_FOR_CONFIG_CERT
            certificate_file_path = merchant_config.mleForRequestPublicCertPath
        # Priority #2: If mle_for_request_public_cert_path not provided, get mlecert from p12 if provided and jwt auth type
        elif (GlobalLabelParameters.JWT.lower() == merchant_config.authentication_type.lower() and 
              merchant_config.p12KeyFilePath):
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
        cert_info = self.mlecache.get(cache_key)

        file_timestamp = os.path.getmtime(certificate_file_path)
        if cert_info is None or cert_info.timestamp != file_timestamp:
            self.setup_mle_cache(merchant_config, cache_key, certificate_file_path)
            cert_info = self.mlecache.get(cache_key)

        return cert_info.certificate if cert_info else None

    def setup_mle_cache(self, merchant_config, cache_key, file_path):
        if FileCache.logger is None:
            FileCache.logger = LogFactory.setup_logger(__name__, merchant_config.log_config)
        logger = FileCache.logger

        mle_certificate = None
        private_key = None

        # Handle Response MLE Private Key
        if cache_key.endswith(GlobalLabelParameters.MLE_CACHE_KEY_IDENTIFIER_FOR_RESPONSE_PRIVATE_KEY):
            try:
                file_extension = os.path.splitext(file_path)[1].lower()
                password = merchant_config.responseMlePrivateKeyFilePassword

                if file_extension in ('.p12', '.pfx'):
                    private_key, _certs = CertificateUtility.fetch_certificate_collection_from_p12_file(
                        file_path,
                        password
                    )
                elif file_extension in ('.pem', '.key', '.p8'):
                    private_key = CertificateUtility.load_private_key_from_pem(
                        file_path,
                        password
                    )
                else:
                    raise ValueError(f"Unsupported file format: {file_extension}")

                cert_info = CertInfo(
                    None,  # No certificate for standalone private key
                    os.path.getmtime(file_path),
                    private_key
                )
                with self._mle_cache_lock:
                    self.mlecache[cache_key] = cert_info
                return
            except Exception as e:
                logger.error("Error loading Response MLE private key")
                raise ValueError(f"Error loading Response MLE private key: {e}")

        # Handle PEM certificate case
        if cache_key.endswith(GlobalLabelParameters.MLE_CACHE_IDENTIFIER_FOR_CONFIG_CERT):
            certificates = CertificateUtility.load_certificates_from_pem_file(file_path)
            try:
                mle_certificate = CertificateUtility.get_cert_based_on_key_alias(certificates, merchant_config.requestMleKeyAlias)
            except Exception:
                if mle_certificate is None:
                    file_name = os.path.basename(file_path)
                    logger.warning(f"No certificate found for the specified mle_key_alias '{merchant_config.requestMleKeyAlias}'. Using the first certificate from file {file_name} as the MLE request certificate.")
                    mle_certificate = certificates[0]  # Take first certificate

        # Handle P12 certificate case
        if cache_key.endswith(GlobalLabelParameters.MLE_CACHE_IDENTIFIER_FOR_P12_CERT):
            try:
                private_key, certificates = CertificateUtility.fetch_certificate_collection_from_p12_file(merchant_config.p12KeyFilePath, merchant_config.key_password)
                mle_certificate = CertificateUtility.get_cert_based_on_key_alias(certificates, merchant_config.requestMleKeyAlias)
            except Exception:
                file_name = os.path.basename(merchant_config.p12KeyFilePath)
                logger.error(f"No certificate found for the specified mle_key_alias '{merchant_config.requestMleKeyAlias}' in file {file_name}.")
                raise ValueError(f"No certificate found for the specified mle_key_alias '{merchant_config.requestMleKeyAlias}' in file {file_name}.")

        # Save to cache (thread-safe)
        cert_info = CertInfo(
            mle_certificate,
            os.path.getmtime(file_path),
            private_key
        )
        with self._mle_cache_lock:
            self.mlecache[cache_key] = cert_info

    def get_mle_response_private_key(self, merchant_config):
        """
        Gets the private key for Response MLE decryption.
        
        :param merchant_config: Merchant configuration object
        :return: Private key object for decryption
        :raises ValueError: If the private key cannot be obtained
        """
        merchant_id = merchant_config.merchant_id
        identifier = GlobalLabelParameters.MLE_CACHE_KEY_IDENTIFIER_FOR_RESPONSE_PRIVATE_KEY
        cache_key = f"{merchant_id}_{identifier}"
        file_path = merchant_config.responseMlePrivateKeyFilePath
        
        if not file_path:
            raise ValueError("Response MLE private key file path not provided")
        
        # Check if key exists in cache
        cert_info = self.mlecache.get(cache_key)
        try:
                file_timestamp = os.path.getmtime(file_path)
            # If not in cache or file was modified, load it
                if cert_info is None or cert_info.timestamp != file_timestamp:
                    self.setup_mle_cache(merchant_config, cache_key, file_path)
                    cert_info = self.mlecache.get(cache_key)
                
                return cert_info.private_key if cert_info else None
        except Exception as e:
            if FileCache.logger:
                FileCache.logger.error(f"Error getting Response MLE private key")
            raise ValueError(f"Error getting Response MLE private key: {str(e)}")
    
    def fetch_cached_p12_from_file(self, file_path, password, logger=None, cache_key=None):
        """
        Fetches a parsed P12 object from cache or parses and caches it.
        
        Args:
            file_path (str): Path to the P12/PFX file
            password (str): Password for the P12 file
            logger: Logger instance for logging
            cache_key (str): Optional custom cache key. Defaults to filePath + identifier
            
        Returns:
            tuple: (private_key, certificates_list)
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If password is incorrect or parsing fails
        """
        from authenticationsdk.util.Utility import parse_p12_file
        
        # Use provided cache key or default
        final_cache_key = cache_key or (file_path + GlobalLabelParameters.RESPONSE_MLE_P12_PFX_CACHE_IDENTIFIER)
        
        if logger:
            logger.debug(f"Fetching P12/PFX from cache with key: {final_cache_key}")
        
        # Check if file exists
        if not os.path.exists(file_path):
            error_msg = f"File not found: {file_path}"
            if logger:
                logger.error(error_msg)
            raise FileNotFoundError(error_msg)
        
        current_file_last_modified_time = os.path.getmtime(file_path)
        
        # Check if cache is valid (exists and file hasn't been modified)
        with self._p12_parsed_cache_lock:
            cached_entry = self.p12_parsed_cache.get(final_cache_key)
            
            if cached_entry and cached_entry['timestamp'] == current_file_last_modified_time:
                if logger:
                    logger.debug("P12/PFX found in cache and file not modified")
                return cached_entry['p12_object']
            
            # Cache miss or file modified - parse and cache
            if logger:
                logger.debug(f"P12/PFX not in cache or file modified. Loading from file: {file_path}")
            
            try:
                p12_object = parse_p12_file(file_path, password, logger)
                
                # Store in cache with file modification time
                self.p12_parsed_cache[final_cache_key] = {
                    'p12_object': p12_object,
                    'timestamp': current_file_last_modified_time
                }
                
                if logger:
                    logger.debug("Successfully cached P12/PFX object")
                return p12_object
                
            except Exception as e:
                error_msg = f"Error parsing P12/PFX file: {str(e)}"
                if logger:
                    logger.error(error_msg)
                raise ValueError(error_msg)
        
