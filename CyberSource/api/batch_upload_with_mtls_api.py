from pathlib import Path
from typing import Optional

import CyberSource.logging.log_factory as LogFactory
from CyberSource.utilities.pgpBatchUpload.mutual_auth_upload import MutualAuthUpload
from CyberSource.utilities.pgpBatchUpload.pgp_encryption import PgpEncryption
from CyberSource.utilities.file_utils import validate_path
from authenticationsdk.util.GlobalLabelParameters import GlobalLabelParameters
from CyberSource.rest import ApiException


class BatchUploadWithMTLSApi:
    """
    A class for handling batch uploads to CyberSource using mTLS authentication.

    This class provides methods for encrypting and uploading batch files to CyberSource
    using PGP encryption and mutual TLS authentication. It orchestrates the entire process
    from file validation, PGP encryption, to secure transmission via mTLS.

    The class follows a secure workflow:
    1. Validates input files and certificates
    2. Encrypts the input file using PGP encryption
    3. Establishes a secure mTLS connection with CyberSource
    4. Uploads the encrypted file to CyberSource's batch processing endpoint
    5. Handles responses and provides comprehensive error reporting

    This class supports various authentication methods including separate key/cert files
    and can be used either directly or as a context manager with the 'with' statement.

    Attributes:
        logger: Logger instance for logging operations and errors
        pgp_encryption: PgpEncryption instance for handling PGP encryption
        mutual_auth_upload: MutualAuthUpload instance for handling mTLS uploads
    """

    _end_point = "/pts/v1/transaction-batch-upload"
    _max_size_bytes = 75 * 1024 * 1024  # 75 MB in bytes

    def __init__(self, log_config=None):
        """
        Initialize the BatchUploadWithMTLSApi.

        Args:
            log_config: Optional configuration for the logger. If provided, it should be
                        a LogConfiguration instance with appropriate settings.

        Example:
            ```python
            from CyberSource.logging.log_configuration import LogConfiguration

            # Create and configure the logger
            log_config = LogConfiguration()
            log_config.set_enable_log(True)
            log_config.set_log_directory("logs")
            log_config.set_log_file_name("cybersource_batch.log")
            log_config.set_log_maximum_size(10 * 1024 * 1024)  # 10 MB
            log_config.set_log_level("INFO")
            log_config.set_enable_masking(True)
            log_config.set_log_format("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            log_config.set_log_date_format("%Y-%m-%d %H:%M:%S")

            # Create the batch upload API instance with logging
            batch_api = BatchUploadWithMTLSApi(log_config)
            ```
        """
        self.logger = LogFactory.setup_logger(self.__class__.__name__, log_config)
        self.pgp_encryption = PgpEncryption(log_config)
        self.mutual_auth_upload = MutualAuthUpload(log_config)

    def upload_batch_api_with_key_and_certs_file(
        self,
        input_file_path: str,
        environment_hostname: str,
        pgp_encryption_public_key_path: str,
        client_cert_path: str,
        client_key_path: str,
        server_trust_cert_path: str = None,
        client_key_password: Optional[str] = None,
        verify_ssl: bool = True,
    ) -> tuple:
        """
        Upload a batch file using separate key and certificate files.

        This method handles the complete process of batch file upload to CyberSource:
        1. Validates all input parameters and files
        2. Checks file size (must be under 75MB) and format (must be .csv)
        3. Encrypts the input file using PGP with the provided public key
        4. Uploads the encrypted file to CyberSource using mutual TLS authentication
        5. Returns the server response or raises appropriate exceptions

        The method supports secure communication through mutual TLS authentication,
        where both the client and server authenticate each other using certificates.

        Args:
            input_file_path: Path to the CSV file to upload (must exist and be under 75MB)
            environment_hostname: CyberSource environment hostname (e.g., "apitest.cybersource.com")
            pgp_encryption_public_key_path: Path to the PGP public key file for encryption
            client_cert_path: Path to the client certificate file (.pem or .crt)
            client_key_path: Path to the client private key file (.key)
            server_trust_cert_path: Path to the server trust certificate file (optional)
                                   If not provided, system CA certificates will be used
            client_key_password: Optional password for the client private key if it's encrypted
            verify_ssl: Whether to verify SSL certificates (default: True)
                       Set to False only for development/testing purposes.
                       WARNING: Disabling SSL verification poses a significant security risk
                       and should never be used in production environments as it makes the
                       connection vulnerable to man-in-the-middle attacks.

        Returns:
            tuple: A tuple containing (response_data, status_code, headers) where:
                  - response_data: The response data from the server as a string, typically containing a batch ID and status information
                  - status_code: The HTTP status code of the response
                  - headers: The HTTP headers of the response

        Raises:
            CyberSource.rest.ApiException: If there's an error during the upload process, including:
                - Validation errors (status 400): If required parameters are missing or invalid (e.g., file too large)
                - File not found errors (status 400): If any of the required files don't exist
                - API errors: If the response status is not successful (2xx)
                - Unexpected errors (status 500): For any other unexpected errors

        Notes:
            This method will log warnings but not raise exceptions if:
            - The provided PGP key is not a public key
            - The PGP public key has expired

        Example:
            ```python
            batch_api = BatchUploadWithMTLSApi()
            try:
                response = batch_api.upload_batch_api_with_key_and_certs_file(
                    input_file_path="path/to/transactions.csv",
                    environment_hostname="apitest.cybersource.com",
                    pgp_encryption_public_key_path="path/to/cybersource_public.asc",
                    client_cert_path="path/to/client.crt",
                    client_key_path="path/to/client.key",
                    server_trust_cert_path="path/to/server_ca.crt"
                )
                print(f"Upload successful. Response: {response}")
            except ApiException as e:
                print(f"Upload failed: {str(e)}")
                print(f"Status code: {e.status}")
                print(f"Response body: {e.body}")
            ```
        """
        try:
            # Step 1: Create endpoint URL
            endpoint_url = self.get_base_url(environment_hostname) + self._end_point

            # Step 2: Validations
            validate_path(
                [
                    (input_file_path, "Input file"),
                    (pgp_encryption_public_key_path, "PGP public key"),
                    (client_cert_path, "Client certificate"),
                    (client_key_path, "Client private key"),
                    (server_trust_cert_path, "Server trust certificate"),
                ]
            )

            # Validate file size (maximum 75 MB)
            file_size = Path(input_file_path).stat().st_size
            if file_size > self._max_size_bytes:
                error_msg = "Input file size exceeds the maximum allowed size of 75 MB"
                if self.logger is not None:
                    self.logger.error(error_msg)
                raise ApiException(
                    status=400,
                    reason="Validation error: Input file size exceeds the maximum allowed size of 75 MB",
                )

            # Validate file extension (.csv)
            file_extension = Path(input_file_path).suffix.lower()
            if file_extension != ".csv":
                error_msg = "Input file must have a .csv extension"
                if self.logger is not None:
                    self.logger.error(error_msg)
                raise ApiException(
                    status=400,
                    reason="Validation error: Input file must have a .csv extension",
                )

            # Step 3: PGP encryption
            encrypted_pgp_bytes = self.pgp_encryption.handle_encrypt_operation(
                input_file_path, pgp_encryption_public_key_path
            )

            # Step 4: Upload the encrypted PGP file using mTLS
            # Replace the file extension with .pgp
            file_name = Path(input_file_path).stem + ".pgp"

            # Log a warning if SSL verification is disabled
            if not verify_ssl and self.logger is not None:
                self.logger.warning(
                    "SSL verification is disabled. This should not be used in production environments."
                )

            response_tuple = self.mutual_auth_upload.handle_upload_operation_using_private_key_and_certs(
                encrypted_pgp_bytes=encrypted_pgp_bytes,
                endpoint_url=endpoint_url,
                file_name=file_name,
                client_private_key_path=client_key_path,
                client_cert_path=client_cert_path,
                server_trust_cert_path=server_trust_cert_path,
                client_key_password=client_key_password,
                verify_ssl=verify_ssl,
            )
            if self.logger is not None:
                self.logger.info("Batch file uploaded successfully")
            return response_tuple
        except ValueError:
            if self.logger is not None:
                self.logger.error(
                    "Validation error: Input parameters failed validation requirements"
                )
            raise ApiException(
                status=400,
                reason="Validation error: Input parameters failed validation requirements",
            )
        except FileNotFoundError:
            if self.logger is not None:
                self.logger.error("File not found: Required file could not be located")
            raise ApiException(
                status=400, reason="File not found: Required file could not be located"
            )
        except ApiException:
            if self.logger is not None:
                self.logger.error(
                    "API error: Batch upload request to CyberSource Batch Upload API failed"
                )
            raise
        except Exception:
            if self.logger is not None:
                self.logger.error(
                    "Error in upload_batch_api_with_key_and_certs_file: Batch upload operation failed"
                )
            raise ApiException(
                status=500, reason="Unexpected error during batch upload operation"
            )

    @staticmethod
    def get_base_url(environment_hostname: str) -> str:
        """
        Get the base URL from the environment hostname.

        This method ensures that the environment hostname is properly formatted as a URL
        by adding the 'https://' prefix if not already present. It also validates that
        the hostname is not empty.

        Args:
            environment_hostname: CyberSource environment hostname (e.g., "apitest.cybersource.com")

        Returns:
            str: The base URL with https:// prefix (e.g., "https://apitest.cybersource.com")

        Raises:
            CyberSource.rest.ApiException: If the environment hostname is None, empty, or consists only of whitespace

        """
        if not environment_hostname:
            raise ApiException(
                status=400,
                reason="Environment Host Name for Batch Upload API cannot be null or empty.",
            )

        base_url = environment_hostname.strip()
        if not base_url.startswith(GlobalLabelParameters.HTTP_URL_PREFIX):
            base_url = GlobalLabelParameters.HTTP_URL_PREFIX + base_url
        return base_url
