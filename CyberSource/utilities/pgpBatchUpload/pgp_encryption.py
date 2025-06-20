"""
PGP Encryption Utility for CyberSource Batch Upload.

This module provides functionality for PGP encryption operations,
supporting both file-based and in-memory operations with various configuration options.
"""

import os
from datetime import datetime

import pgpy

import CyberSource.logging.log_factory as LogFactory
from CyberSource.utilities.file_utils import validate_path


class PgpEncryption:
    """
    A class for handling PGP encryption operations.

    This class provides methods for encrypting data using PGP,
    with support for both file-based and in-memory operations.

    Attributes:
        logger: Logger instance for logging operations and errors
    """

    def __init__(self, log_config=None):
        """
        Initialize the PGP encryption utility.

        Args:
            log_config: Optional configuration for the logger
        """
        self.logger = LogFactory.setup_logger(self.__class__.__name__, log_config)

    def handle_encrypt_operation(
        self,
        input_file: str,
        pgp_public_key: str,
    ) -> bytes:
        """
        Handle the encryption operation for a file using a PGP public key.

        Args:
            input_file: Path to the file to encrypt
            pgp_public_key: Path to the PGP public key file

        Returns:
            bytes: The encrypted data as bytes

        Raises:
            ValueError: If required parameters are missing
            FileNotFoundError: If input file or public key file doesn't exist
            pgpy.errors.PGPError: If there's an error in PGP operations
            IOError: If there's an error reading or writing files
        """
        try:
            if input_file is None or pgp_public_key is None:
                raise ValueError("Missing required options for encrypt operation")

            validate_path(input_file, "Input file", self.logger)
            validate_path(pgp_public_key, "Public key", self.logger)
            input_file_name = os.path.basename(input_file)

            public_key = self.load_public_key(pgp_public_key)
            self._validate_key_for_encryption(public_key)
            if self.logger is not None:
                self.logger.info(f"Starting file encryption: {input_file_name}")
            encrypted_pgp_bytes = self.encrypt_file(input_file, public_key)
            if self.logger is not None:
                self.logger.info(f"File encrypted successfully: {input_file_name}")

            return encrypted_pgp_bytes
        except ValueError as e:
            if self.logger is not None:
                self.logger.error(f"Value error in handle_encrypt_operation: {str(e)}")
            raise
        except FileNotFoundError as e:
            if self.logger is not None:
                self.logger.error(
                    f"File not found in handle_encrypt_operation: {str(e)}"
                )
            raise
        except pgpy.errors.PGPError as e:
            if self.logger is not None:
                self.logger.error(f"PGP error in handle_encrypt_operation: {str(e)}")
            raise
        except IOError as e:
            if self.logger is not None:
                self.logger.error(f"I/O error in handle_encrypt_operation: {str(e)}")
            raise
        except Exception as e:
            if self.logger is not None:
                self.logger.error(
                    f"Unexpected error in handle_encrypt_operation: {str(e)}"
                )
            raise

    def encrypt_file(
        self,
        input_file: str,
        public_key: pgpy.PGPKey,
    ) -> bytes:
        """
        Encrypt a file using the provided PGP public key.

        Args:
            input_file: Path to the file to encrypt
            public_key: PGP public key to use for encryption

        Returns:
            bytes: The encrypted data as bytes

        Raises:
            IOError: If there's an error reading the file
            pgpy.errors.PGPError: If there's an error in PGP operations
        """
        try:
            with open(input_file, "rb") as f:
                file_data = f.read()
                return self.encrypt_data(file_data, public_key)
        except IOError as e:
            if self.logger is not None:
                self.logger.error(f"I/O error in encrypt_file: {str(e)}")
            raise
        except pgpy.errors.PGPError as e:
            if self.logger is not None:
                self.logger.error(f"PGP error in encrypt_file: {str(e)}")
            raise
        except Exception as e:
            if self.logger is not None:
                self.logger.error(f"Unexpected error in encrypt_file: {str(e)}")
            raise

    def encrypt_data(
        self,
        data: bytes,
        public_key: pgpy.PGPKey,
    ) -> bytes:
        """
        Encrypt data using the provided PGP public key.

        Args:
            data: The data to encrypt
            public_key: PGP public key to use for encryption

        Returns:
            bytes: The encrypted data as bytes

        Raises:
            pgpy.errors.PGPError: If there's an error in PGP operations
        """
        try:
            message = pgpy.PGPMessage.new(data)

            # Configure encryption options
            encryption_options = {}

            encrypted_message = public_key.encrypt(message, **encryption_options)
            return bytes(encrypted_message)
        except pgpy.errors.PGPError as e:
            if self.logger is not None:
                self.logger.error(f"PGP error in encrypt_data: {str(e)}")
            raise
        except Exception as e:
            if self.logger is not None:
                self.logger.error(f"Unexpected error in encrypt_data: {str(e)}")
            raise

    def load_public_key(self, key_path: str) -> pgpy.PGPKey:
        """
        Load a PGP public key from a file.

        Args:
            key_path: Path to the public key file

        Returns:
            pgpy.PGPKey: The loaded PGP public key

        Raises:
            IOError: If there's an error reading the key file
            pgpy.errors.PGPError: If there's an error parsing the key
        """
        try:
            with open(key_path, "r") as key_file:
                key_data = key_file.read()
                key, _ = pgpy.PGPKey.from_blob(key_data)
                if self.logger is not None:
                    self.logger.info(f"Successfully loaded public key from: {key_path}")
                return key
        except IOError as e:
            if self.logger is not None:
                self.logger.error(f"I/O error loading public key: {str(e)}")
            raise
        except pgpy.errors.PGPError as e:
            if self.logger is not None:
                self.logger.error(f"PGP error loading public key: {str(e)}")
            raise
        except Exception as e:
            if self.logger is not None:
                self.logger.error(f"Unexpected error loading public key: {str(e)}")
            raise

    def _validate_key_for_encryption(self, key: pgpy.PGPKey) -> None:
        """
        Validate that a key is suitable for encryption.

        Args:
            key: The PGP key to validate

        Raises:
            ValueError: If the key is not suitable for encryption
        """
        # Enforce that the key must be a public key
        if not key.is_public:
            if self.logger is not None:
                self.logger.error("The provided key is not a public key")
            raise ValueError("Only public keys can be used for encryption")

        # Check if key has expired

        now = datetime.utcnow()
        if key.expires_at is not None:
            expires_at = key.expires_at
            # Compare naive datetime objects for expiration check
            if expires_at.tzinfo is not None:
                # If expires_at is timezone-aware, convert to naive UTC for comparison
                expires_at = expires_at.replace(tzinfo=None)
            if now > expires_at:
                raise ValueError(f"The public key has expired on {expires_at}")

        # Check if key can be used for encryption
        # PGP keys typically have usage flags that indicate their capabilities
        # We'll check if the key or any of its subkeys can be used for encryption
        can_encrypt = False

        # Check if the primary key can encrypt
        if hasattr(key, "key_algorithm"):
            # RSA, ElGamal, and some other algorithms support encryption
            can_encrypt = True

        # If primary key can't encrypt, check subkeys
        if not can_encrypt and hasattr(key, "subkeys"):
            for subkey in key.subkeys.values():
                # Check if this subkey can be used for encryption
                if hasattr(subkey, "key_algorithm"):
                    can_encrypt = True
                    break

        if not can_encrypt:
            raise ValueError("The public key cannot be used for encryption")

    def __enter__(self):
        """
        Enter the context manager.

        The context manager pattern allows the class to be used with Python's 'with' statement.
        This provides a cleaner way to use the class and ensures proper resource management.

        Example:
            with PgpEncryption() as pgp:
                pgp.handle_encrypt_operation(...)

        Returns:
            PgpEncryption: The instance itself
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context manager.

        This method is called when exiting the 'with' block. It can be used to clean up
        resources, handle exceptions, or perform other finalization tasks.

        Args:
            exc_type: Exception type if an exception was raised
            exc_val: Exception value if an exception was raised
            exc_tb: Exception traceback if an exception was raised
        """
        # Currently no resources to clean up, but this method is required for the context manager pattern
        pass
