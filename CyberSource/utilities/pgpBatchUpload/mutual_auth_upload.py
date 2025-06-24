import ssl
import uuid

import certifi
import urllib3
from urllib3 import BaseHTTPResponse

import CyberSource.logging.log_factory as LogFactory
from authenticationsdk.util.GlobalLabelParameters import GlobalLabelParameters
from CyberSource.rest import ApiException


def _create_file_form_field_tuple(encrypted_pgp_bytes: bytes, file_name: str) -> tuple:
    """
    Create a tuple that represents a file field for a multipart/form-data upload with urllib3.

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
        :raises CyberSource.rest.ApiException: If there's an error during the upload process or if the response status is not successful (2xx)
        :return: A tuple containing (response_data, status_code, headers)
        """
        try:
            if self.logger is not None:
                self.logger.info(
                    "Handling upload operation with private key and certificates"
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
        except ApiException:
            if self.logger is not None:
                self.logger.error(
                    "Error in handle_upload_operation_using_private_key_and_certs: Failed to upload file using mTLS authentication"
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
        :raises CyberSource.rest.ApiException: If there's an error during the upload process or if the response status is not successful (2xx)
        :return: A tuple containing (response_data, status_code, headers)
        """
        try:
            if self.logger is not None:
                self.logger.info("Starting file upload process")
            headers = self._create_headers()
            file_tuple = _create_file_form_field_tuple(encrypted_pgp_bytes, file_name)

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
        except ApiException:
            if self.logger is not None:
                self.logger.error(
                    "ApiException in upload_file: File upload operation failed"
                )
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
        :raises CyberSource.rest.ApiException: If there's an error during the HTTP request, including SSL errors or any other unexpected errors
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
        except urllib3.exceptions.HTTPError:
            if self.logger is not None:
                self.logger.error(
                    "HTTP error in _send_request: Network communication failure during file upload"
                )
            raise ApiException(
                status=None,
                reason="HTTP communication error occurred during file upload",
            )
        except ssl.SSLError:
            if self.logger is not None:
                self.logger.error(
                    "SSL error in _send_request: Certificate validation or secure connection failure"
                )
            raise ApiException(
                status=None,
                reason="SSL certificate or connection error occurred",
            )
        except Exception:
            if self.logger is not None:
                self.logger.error(
                    "Unexpected error in _send_request: Failure during HTTP request processing"
                )
            raise ApiException(
                status=None,
                reason="An unexpected error occurred during file upload",
            )

    def _handle_response(self, response: urllib3.HTTPResponse) -> tuple:
        """
        Handle the HTTP response from the file upload operation.

        This method processes the HTTP response, checks the status code, and decodes the response body.
        For successful responses (status code 2xx), it returns the decoded response data along with
        status code and headers. For unsuccessful responses, it raises an ApiException.

        :param response: HTTP response from the upload request
        :raises CyberSource.rest.ApiException: If any of the following conditions occur:
               - The response status code is not in the 2xx range (indicating failure)
               - The response body cannot be decoded using the specified encoding
               - The response body cannot be decoded using UTF-8 as a fallback
        :return: A tuple containing (response_data, status_code, headers)
                 - response_data: Decoded response body as a string
                 - status_code: HTTP status code of the response
                 - headers: HTTP headers from the response
        """
        status_code = response.status
        if self.logger is not None:
            self.logger.info(f"Upload completed. Response status code: {status_code}")

        if 200 <= status_code < 300:
            if self.logger is not None:
                self.logger.info("File uploaded successfully")

            try:
                # Check the type of response.data
                if isinstance(response.data, bytes):
                    response_data = response.data.decode("utf-8")
                else:
                    # Already a string (Python 2 case)
                    response_data = response.data
                if self.logger is not None:
                    self.logger.info("Successfully processed response data")
            except Exception:
                if self.logger is not None:
                    self.logger.error(
                        "Response data processing error: Unable to decode or process server response"
                    )
                raise ApiException(
                    http_resp=response,
                    status=status_code,
                    reason="Failed to process response data",
                )

            return response_data, status_code, response.headers
        else:
            try:
                if isinstance(response.data, bytes):
                    error_body = response.data.decode("utf-8")
                else:
                    error_body = response.data
            except Exception:
                if self.logger is not None:
                    self.logger.error(
                        "Error processing error response: Unable to decode error response from server"
                    )
                raise ApiException(
                    http_resp=response,
                    status=status_code,
                    reason="Unable to process error response from server",
                )

            if self.logger is not None:
                self.logger.error(f"File upload failed. Status code: {status_code}")

            if 400 <= status_code < 500:
                error_message = f"File upload failed due to client error (Status code: {status_code}). Details: {error_body}"
            elif 500 <= status_code < 600:
                error_message = f"File upload failed due to server error (Status code: {status_code}). Details: {error_body}"
            else:
                error_message = f"File upload failed (Status code: {status_code}). Details: {error_body}"

            raise ApiException(
                http_resp=response, status=status_code, reason=error_message
            )
