"""
File Utility Functions for CyberSource.

This module provides utility functions for file operations,
including path validation and directory creation.
"""

from pathlib import Path
from typing import List, Tuple


def validate_path(path: str, path_type: str, logger=None) -> None:
    """
    Validate that a path exists, creating directories if necessary.

    Args:
        path: The path to validate
        path_type: Description of the path type for error messages
        logger: Optional logger instance for logging operations

    Raises:
        FileNotFoundError: If the path doesn't exist and isn't an output directory
    """
    file_path = Path(path)
    if path_type == "Output directory":
        if not file_path.exists():
            file_path.mkdir(parents=True, exist_ok=True)
            if logger is not None:
                logger.info(f"Created output directory: {path}")
    elif not file_path.exists():
        raise FileNotFoundError(f"{path_type} does not exist: {path}")


def validate_paths(paths: List[Tuple[str, str]], logger=None) -> None:
    """
    Validate that all specified paths exist.

    Args:
        paths: List of tuples containing (path, description)
        logger: Optional logger instance for logging operations

    Raises:
        ValueError: If a required path is None or empty
        FileNotFoundError: If any of the paths don't exist
    """
    for path, description in paths:
        # Check if this is an optional parameter (currently only "Server trust certificate")
        is_optional = "Server trust certificate" in description

        if path is None:
            if is_optional:
                continue  # Skip validation for None paths that are optional
            else:
                raise ValueError(f"{description} is required but was None")

        if not path:
            raise ValueError(f"{description} path is required")
        if not Path(path).exists():
            raise FileNotFoundError(f"{description} not found: {path}")
