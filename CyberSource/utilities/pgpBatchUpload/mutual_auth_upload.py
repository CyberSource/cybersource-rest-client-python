import ssl
import uuid

import certifi
import urllib3
from urllib3 import BaseHTTPResponse
from urllib3.exceptions import HTTPError

import CyberSource.logging.log_factory as LogFactory
from authenticationsdk.util.GlobalLabelParameters import GlobalLabelParameters
from CyberSource.rest import ApiException


def _prepare_files(encrypted_pgp_bytes: bytes, file_name: str) -> tuple:
    """
    Prepare the file data for multipart/form-data upload with urllib3.

    :param encrypted_pgp_bytes: Encrypted PGP file content
    :param file_name: Name of the file to be uploaded
    :return: Tuple containing the file field name, filename, file content, and content type
    """
    return "file", file_name, encrypted_pgp_bytes, "application/octet-stream"


class MutualAuthUpload:
    def __init__(self, log_config=None):
        self.logger = LogFactory.setup_logger(self.__class__.__name__, log_config)

    def handle_upload_operation_using_private_key_and_certs(
        self,
        encrypted_pgp_bytes: bytes,
        endpoint_url: str,
        file_name: str,
        client_private_key_path: str,
        client_cert_path: str,
        server_trust_cert_path: str = None,
        client_key_password: str = None,
        verify_ssl: bool = True,
    ) -> tuple:
        """
        Handle upload operation using private key and certificates.

        :param encrypted_pgp_bytes: Encrypted PGP file content
        :param endpoint_url: URL to upload the file
        :param file_name: Name of the file to be uploaded
        :param client_private_key_path: Path to the client private key file
        :param client_cert_path: Path to the client certificate file
        :param server_trust_cert_path: Path to the server trust certificate file
        :param client_key_password: Password for the client key file
        :param verify_ssl: Whether to verify SSL certificates (default: True)
        :raises urllib3.exceptions.HTTPError: If there's an error during the upload process
        :raises CyberSource.rest.ApiException: If the response status is not successful (2xx)
        :return: A tuple containing (response_data, status_code, headers)
        """
        try:
            if self.logger is not None:
                self.logger.info(
                    "Handling upload operation with private key and certificates"
                )
                if not verify_ssl and self.logger is not None:
                    self.logger.warning(
                        "SSL verification is disabled. This should only be used in development environments."
                    )
            return self.upload_file(
                encrypted_pgp_bytes,
                endpoint_url,
                file_name,
                client_cert_path=client_cert_path,
                client_key_path=client_private_key_path,
                ca_cert_path=server_trust_cert_path,
                cert_password=client_key_password,
                verify_ssl=verify_ssl,
            )
        except (HTTPError, ApiException) as e:
            if self.logger is not None:
                self.logger.error(
                    f"Error in handle_upload_operation_using_private_key_and_certs: {str(e)}"
                )
            raise

    def upload_file(
        self,
        encrypted_pgp_bytes: bytes,
        endpoint_url: str,
        file_name: str,
        client_cert_path: str = None,
        client_key_path: str = None,
        ca_cert_path: str = None,
        cert_password: str = None,
        verify_ssl: bool = True,
    ) -> tuple:
        """
        Upload encrypted PGP file to the specified endpoint.

        :param encrypted_pgp_bytes: Encrypted PGP file content
        :param endpoint_url: URL to upload the file
        :param file_name: Name of the file to be uploaded
        :param client_cert_path: Path to the client certificate file
        :param client_key_path: Path to the client private key file
        :param ca_cert_path: Path to the CA certificate file
        :param cert_password: Password for the certificate file
        :param verify_ssl: Whether to verify SSL certificates (default: True)
        :raises urllib3.exceptions.HTTPError: If there's an error during the upload process
        :raises CyberSource.rest.ApiException: If the response status is not successful (2xx)
        :return: A tuple containing (response_data, status_code, headers)
        """
        try:
            if self.logger is not None:
                self.logger.info("Starting file upload process")
            headers = self._create_headers()
            file_tuple = _prepare_files(encrypted_pgp_bytes, file_name)

            response = self._send_request(
                endpoint_url,
                headers,
                file_tuple,
                client_cert_path,
                client_key_path,
                ca_cert_path,
                cert_password,
                verify_ssl,
            )
            return self._handle_response(response)
        except HTTPError as e:
            if self.logger is not None:
                self.logger.error(f"HTTPError in upload_file: {str(e)}")
            raise
        except ApiException as e:
            if self.logger is not None:
                self.logger.error(f"ApiException in upload_file: {str(e)}")
            raise

    def _create_headers(self) -> dict:
        correlation_id = str(uuid.uuid4())
        if self.logger is not None:
            self.logger.info(f"Created correlation ID: {correlation_id}")
        return {GlobalLabelParameters.V_C_CORRELATION_ID: correlation_id}

    def _send_request(
        self,
        endpoint_url: str,
        headers: dict,
        file_tuple: tuple,
        client_cert_path: str,
        client_key_path: str,
        ca_cert_path: str,
        cert_password: str = None,
        verify_ssl: bool = True,
    ) -> BaseHTTPResponse:
        """
        Send HTTP request with the file and certificates.

        :param endpoint_url: URL to upload the file
        :param headers: HTTP headers
        :param file_tuple: Tuple containing file information
        :param client_cert_path: Path to the client certificate file
        :param client_key_path: Path to the client private key file
        :param ca_cert_path: Path to the CA certificate file
        :param cert_password: Password for the certificate file
        :param verify_ssl: Whether to verify SSL certificates (default: True)
        :return: HTTP response
        :raises urllib3.exceptions.HTTPError: If there's an error during the HTTP request
        :raises ssl.SSLError: If there's an SSL-related error
        :raises Exception: For any other unexpected errors
        """
        if self.logger is not None:
            self.logger.info(f"Sending HTTP POST request to URL: {endpoint_url}")

        try:
            if verify_ssl:
                # Create SSL context with default CA certificates
                ssl_context = ssl.create_default_context(cafile=certifi.where())

                # If server trust cert path is provided, add it to the context
                if ca_cert_path:
                    ssl_context.load_verify_locations(cafile=ca_cert_path)

                # Create a pool manager with the SSL context
                http = urllib3.PoolManager(
                    cert_file=client_cert_path,
                    key_file=client_key_path,
                    key_password=cert_password,
                    ssl_context=ssl_context,
                )
            else:
                # Create a pool manager with SSL verification disabled
                if self.logger is not None:
                    self.logger.warning("SSL certificate verification is disabled")

                # Use direct parameters to disable SSL verification
                http = urllib3.PoolManager(
                    cert_file=client_cert_path,
                    key_file=client_key_path,
                    key_password=cert_password,
                    cert_reqs=ssl.CERT_NONE,
                    assert_hostname=False,
                )

            # Prepare multipart form data
            field_name, filename, file_data, content_type = file_tuple

            # Send the request
            return http.request(
                "POST",
                endpoint_url,
                headers=headers,
                fields={field_name: (filename, file_data, content_type)},
            )
        except HTTPError as e:
            if self.logger is not None:
                self.logger.error(f"HTTP error in _send_request: {str(e)}")
            raise
        except ssl.SSLError as e:
            if self.logger is not None:
                self.logger.error(f"SSL error in _send_request: {str(e)}")
            raise HTTPError(f"SSL error: {str(e)}")
        except Exception as e:
            if self.logger is not None:
                self.logger.error(f"Unexpected error in _send_request: {str(e)}")
            raise HTTPError(f"Unexpected error during HTTP request: {str(e)}")

    def _handle_response(self, response: urllib3.HTTPResponse) -> tuple:
        """
        Handle the HTTP response.

        :param response: HTTP response
        :raises CyberSource.rest.ApiException: If the response status is not successful (2xx)
        :return: A tuple containing (response_data, status_code, headers)
        """
        status_code = response.status
        self.logger.info(f"Upload completed. Response status code: {status_code}")

        if 200 <= status_code < 300:
            if self.logger is not None:
                self.logger.info("File uploaded successfully")
            # Decode the response data to a string
            response_data = response.data.decode("utf-8")
            return response_data, status_code, response.headers
        else:
            error_message = f"File upload failed. Status code: {status_code}, body: {response.data.decode('utf-8')}"
            if self.logger is not None:
                self.logger.error(error_message)
            # Throw ApiException instead of HTTPError for consistency with rest.py
            raise ApiException(http_resp=response)
