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
        except ApiException as e:
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
        except urllib3.exceptions.HTTPError as e:
            if self.logger is not None:
                self.logger.error(f"HTTP error in _send_request: {str(e)}")
            raise ApiException(
                status=None,
                reason=f"HTTP error during request: {str(e)}",
            )
        except ssl.SSLError as e:
            if self.logger is not None:
                self.logger.error(f"SSL error in _send_request: {str(e)}")
            raise ApiException(
                status=None,
                reason=f"SSL error: {str(e)}",
            )
        except Exception as e:
            if self.logger is not None:
                self.logger.error(f"Unexpected error in _send_request: {str(e)}")
            raise ApiException(
                status=None,
                reason=f"Unexpected error during HTTP request: {str(e)}",
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

            # Determine encoding from Content-Type header or default to UTF-8
            content_type = response.headers.get("Content-Type", "").lower()
            encoding = "utf-8"  # Default to UTF-8
            if "charset=" in content_type:
                encoding = content_type.split("charset=")[-1]

            # Attempt to decode the response data
            try:
                response_data = response.data.decode(encoding)
            except UnicodeDecodeError as e:
                if self.logger is not None:
                    self.logger.error(
                        f"Decoding error with {encoding} encoding: {str(e)}"
                    )

                # Fall back to UTF-8 if the specified encoding fails and it's not already UTF-8
                if encoding.lower() != "utf-8":
                    try:
                        response_data = response.data.decode("utf-8")
                        if self.logger is not None:
                            self.logger.info(
                                "Successfully decoded response with UTF-8 fallback"
                            )
                    except Exception as e:
                        if self.logger is not None:
                            self.logger.error(
                                f"UTF-8 fallback decoding error: {str(e)}"
                            )
                        raise ApiException(
                            http_resp=response,
                            status=status_code,
                            reason=f"Failed to decode response data: {str(e)}",
                        )
                else:
                    raise ApiException(
                        http_resp=response,
                        status=status_code,
                        reason=f"Failed to decode response data: {str(e)}",
                    )

            return response_data, status_code, response.headers
        else:
            try:
                error_body = response.data.decode("utf-8")
            except Exception as e:
                if self.logger is not None:
                    self.logger.error(f"Error decoding error response: {str(e)}")
                error_body = "<Unable to decode response body>"

            error_message = (
                f"File upload failed. Status code: {status_code}, body: {error_body}"
            )
            if self.logger is not None:
                self.logger.error(error_message)
            # Throw ApiException instead of HTTPError for consistency with rest.py
            raise ApiException(
                http_resp=response, status=status_code, reason=error_message
            )
