"""
Batch Upload with mTLS API for CyberSource.

This module provides functionality for batch uploads to CyberSource using mTLS authentication,
supporting both file-based and in-memory operations with various configuration options.
"""

from pathlib import Path
from typing import Optional

import CyberSource.logging.log_factory as LogFactory
from CyberSource.utilities.pgpBatchUpload.mutual_auth_upload import MutualAuthUpload
from CyberSource.utilities.pgpBatchUpload.pgp_encryption import PgpEncryption


def _validate_paths(paths: list) -> None:
    """
    Validate that all specified paths exist.

    Args:
        paths: List of tuples containing (path, description)

    Raises:
        FileNotFoundError: If any of the paths don't exist
    """
    for path, description in paths:
        if path is None:
            continue  # Skip validation for None paths
        if not path:
            raise ValueError(f"{description} path is required")
        if not Path(path).exists():
            raise FileNotFoundError(f"{description} not found: {path}")


class BatchUploadWithMTLSApi:
    """
    A class for handling batch uploads to CyberSource using mTLS authentication.

    This class provides methods for encrypting and uploading batch files to CyberSource
    using PGP encryption and mutual TLS authentication. It supports various authentication
    methods including separate key/cert files.

    Attributes:
        logger: Logger instance for logging operations and errors
        pgp_encryption: PgpEncryption instance for handling PGP encryption
        mutual_auth_upload: MutualAuthUpload instance for handling mTLS uploads
    """

    _end_point = "/pts/v1/transaction-batch-upload"

    def __init__(self, log_config=None):
        """
        Initialize the BatchUploadWithMTLSApi.

        Args:
            log_config: Optional configuration for the logger
        """
        self.logger = LogFactory.setup_logger(self.__class__.__name__, log_config)
        self.pgp_encryption = PgpEncryption(log_config)
        self.mutual_auth_upload = MutualAuthUpload(log_config)

    def upload_batch_api_with_separate_key_and_cert_file(
        self,
        input_file: str,
        environment_hostname: str,
        pgp_encryption_public_key_path: str,
        client_cert_path: str,
        client_key_path: str,
        server_trust_cert_path: str = None,
        client_cert_password: Optional[str] = None,
        verify_ssl: bool = True,
    ) -> str:
        """
        Upload a batch file using separate key and certificate files.

        This method encrypts the input file using PGP and uploads it to CyberSource
        using mutual TLS authentication with separate key and certificate files.

        Args:
            input_file: Path to the file to upload
            environment_hostname: CyberSource environment hostname
            pgp_encryption_public_key_path: Path to the PGP public key file
            client_cert_path: Path to the client certificate file
            client_key_path: Path to the client private key file
            server_trust_cert_path: Path to the server trust certificate file (optional)
            client_cert_password: Optional password for the client certificate file
            verify_ssl: Whether to verify SSL certificates (default: True). Set to False only for development purposes.

        Returns:
            str: The response data from the server as a string

        Raises:
            ValueError: If required parameters are missing or invalid
            FileNotFoundError: If any of the required files don't exist
            requests.exceptions.RequestException: If there's an error during the upload process
        """
        try:
            # Step 1: Create endpoint URL
            endpoint_url = self.get_base_url(environment_hostname) + self._end_point

            # Step 2: Validations
            _validate_paths(
                [
                    (input_file, "Input file"),
                    (pgp_encryption_public_key_path, "PGP public key"),
                    (client_cert_path, "Client certificate"),
                    (client_key_path, "Client private key"),
                    (server_trust_cert_path, "Server trust certificate"),
                ]
            )

            # Validate file size (maximum 75 MB)
            file_size = Path(input_file).stat().st_size
            max_size_bytes = 75 * 1024 * 1024  # 75 MB in bytes
            if file_size > max_size_bytes:
                error_msg = f"Input file size ({file_size} bytes) exceeds the maximum allowed size of 75 MB ({max_size_bytes} bytes)"
                if self.logger is not None:
                    self.logger.error(error_msg)
                raise ValueError(error_msg)

            # Validate file extension (.csv)
            file_extension = Path(input_file).suffix.lower()
            if file_extension != ".csv":
                error_msg = (
                    f"Input file must have a .csv extension, but got '{file_extension}'"
                )
                if self.logger is not None:
                    self.logger.error(error_msg)
                raise ValueError(error_msg)

            # Step 3: PGP encryption
            encrypted_pgp_bytes = self.pgp_encryption.handle_encrypt_operation(
                input_file, pgp_encryption_public_key_path
            )

            # Step 4: Upload the encrypted PGP file using mTLS
            # Replace the file extension with .pgp
            file_name = Path(input_file).stem + ".pgp"
            
            # Log a warning if SSL verification is disabled
            if not verify_ssl and self.logger is not None:
                self.logger.warning(
                    "SSL certificate verification is disabled. This should only be used in development environments."
                )
                
            response_data = self.mutual_auth_upload.handle_upload_operation_using_private_key_and_certs(
                encrypted_pgp_bytes=encrypted_pgp_bytes,
                endpoint_url=endpoint_url,
                file_name=file_name,
                client_private_key_path=client_key_path,
                client_cert_path=client_cert_path,
                server_trust_cert_path=server_trust_cert_path,
                client_cert_password=client_cert_password,
                verify_ssl=verify_ssl,
            )
            if self.logger is not None:
                self.logger.info("Batch file uploaded successfully")
            return response_data
        except ValueError as e:
            if self.logger is not None:
                self.logger.error(f"Validation error: {str(e)}")
            raise
        except FileNotFoundError as e:
            if self.logger is not None:
                self.logger.error(f"File not found: {str(e)}")
            raise
        except Exception as e:
            if self.logger is not None:
                self.logger.error(
                    f"Error in upload_batch_api_with_separate_key_and_cert_file: {str(e)}"
                )
            raise

    @staticmethod
    def get_base_url(environment_hostname: str) -> str:
        """
        Get the base URL from the environment hostname.

        Args:
            environment_hostname: CyberSource environment hostname

        Returns:
            str: The base URL with https:// prefix if not already present
        """
        if not environment_hostname:
            raise ValueError("Environment hostname is required")

        base_url = environment_hostname.strip()
        if not base_url.startswith("https://"):
            base_url = "https://" + base_url
        return base_url

    def __enter__(self):
        """
        Enter the context manager.

        Returns:
            BatchUploadWithMTLSApi: The instance itself
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context manager.

        Args:
            exc_type: Exception type if an exception was raised
            exc_val: Exception value if an exception was raised
            exc_tb: Exception traceback if an exception was raised
        """
        # Currently no resources to clean up
        pass
