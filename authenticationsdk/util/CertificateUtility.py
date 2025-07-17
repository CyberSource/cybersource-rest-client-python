import os
import re
from datetime import datetime, timezone
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import NameOID
from authenticationsdk.util.GlobalLabelParameters import GlobalLabelParameters
import CyberSource.logging.log_factory as LogFactory
from CyberSource.logging.log_configuration import LogConfiguration
from cryptography.hazmat.primitives.serialization import pkcs12

class CertificateUtility:
    logger = None

    @staticmethod
    def validate_path_and_file(file_path, path_type, log_config):
        if CertificateUtility.logger is None:
            CertificateUtility.logger = LogFactory.setup_logger(__name__, log_config)
        logger = CertificateUtility.logger
       
        if not file_path or not file_path.strip():
            logger.error(f"{path_type} path cannot be null or empty.")
            raise ValueError(f"{path_type} path cannot be null or empty.")

        # Normalize Windows-style paths that start with a slash before the drive letter
        normalized_path = file_path
        if os.sep == '\\' and re.match(r'^/[A-Za-z]:.*', normalized_path):
            normalized_path = normalized_path[1:]

        path = normalized_path

        if not os.path.exists(path):
            logger.error(f"{path_type} does not exist: {path}")
            raise IOError(f"{path_type} does not exist: {path}")

        if os.path.isdir(path):
            logger.error(f"{path_type} does not have valid file: {path}")
            raise IOError(f"{path_type} does not have valid file: {path}")

        try:
            with open(path, "rb"):
                return path
        except Exception:
            logger.error(f"{path_type} is not readable: {path}")
            raise IOError(f"{path_type} is not readable: {path}")

    @staticmethod
    def validate_certificate_expiry(certificate, key_alias, mle_cache_key_identifier, log_config):
        if CertificateUtility.logger is None:
            CertificateUtility.logger = LogFactory.setup_logger(__name__, log_config)
        logger = CertificateUtility.logger

        warning_message_for_no_expiry_date = "Certificate does not have expiry date"
        warning_message_for_certificate_expiring_soon = "Certificate with alias {} is going to expire on {}. Please update the certificate before then."
        warning_message_for_expired_certificate = "Certificate with alias {} is expired as of {}. Please update the certificate."
        
        if GlobalLabelParameters.MLE_CACHE_IDENTIFIER_FOR_CONFIG_CERT == mle_cache_key_identifier:
            warning_message_for_no_expiry_date = "Certificate for MLE Requests does not have expiry date from mleForRequestPublicCertPath in merchant configuration."
            warning_message_for_certificate_expiring_soon = "Certificate for MLE Requests with alias {} is going to expire on {}. Please update the certificate provided in mleForRequestPublicCertPath in merchant configuration before then."
            warning_message_for_expired_certificate = "Certificate for MLE Requests with alias {} is expired as of {}. Please update the certificate provided in mleForRequestPublicCertPath in merchant configuration."
        
        if GlobalLabelParameters.MLE_CACHE_IDENTIFIER_FOR_P12_CERT == mle_cache_key_identifier:
            warning_message_for_no_expiry_date = "Certificate for MLE Requests does not have expiry date in the P12 file."
            warning_message_for_certificate_expiring_soon = "Certificate for MLE Requests with alias {} is going to expire on {}. Please update the P12 file before then."
            warning_message_for_expired_certificate = "Certificate for MLE Requests with alias {} is expired as of {}. Please update the P12 file."
        
        # cryptography.x509.Certificate uses .not_valid_after for the expiry date, returns a datetime object
        not_after = certificate.not_valid_after_utc
        if not_after is None:
            logger.warning(warning_message_for_no_expiry_date)
        else:
            now = datetime.now(timezone.utc)
            if not_after < now:
                logger.warning(warning_message_for_expired_certificate.format(key_alias, not_after))
            else:
                time_to_expire = not_after - now
                if time_to_expire.days < GlobalLabelParameters.CERTIFICATE_EXPIRY_DATE_WARNING_DAYS:
                    logger.warning(warning_message_for_certificate_expiring_soon.format(key_alias, not_after))

    @staticmethod
    def load_certificates_from_pem_file(certificate_file_path):
        """
        Load all certificates from a PEM file and return as a list of cryptography.x509.Certificate objects.
        """
        certificates = []
        with open(certificate_file_path, 'rb') as f:
            pem_data = f.read()

        # Split the file into individual PEM certificates
        for cert in pem_data.split(b'-----END CERTIFICATE-----'):
            if b'-----BEGIN CERTIFICATE-----' in cert:
                cert_block = cert + b'-----END CERTIFICATE-----'
                certificate = x509.load_pem_x509_certificate(cert_block, default_backend())
                certificates.append(certificate)
        return certificates

    @staticmethod
    def get_cert_based_on_key_alias(certs, key_alias):
        for cert in certs:
            # Extract the Common Name (CN) from the certificate subject
            common_names = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
            if common_names:
                cn = common_names[0].value
                if cn.lower() == key_alias.lower():
                    return cert
        raise Exception(f"ERROR : Certificate with alias {key_alias} not found.")

    @staticmethod
    def fetch_certificate_collection_from_p12_file(p12_file_path, key_password):
        """
        Loads all certificates from a PKCS#12 (.p12/.pfx) file.
        
        Returns:
            List of cryptography.x509.Certificate objects.
        """
        with open(p12_file_path, "rb") as f:
            p12_data = f.read()

        # key_password should be bytes or None
        if key_password is not None:
            key_password_bytes = key_password.encode()
        else:
            key_password_bytes = None

        private_key, cert, additional_certs = pkcs12.load_key_and_certificates(p12_data, key_password_bytes)
        certs = []
        if cert is not None:
            certs.append(cert)
        if additional_certs is not None:
            certs.extend(additional_certs)
        return certs
