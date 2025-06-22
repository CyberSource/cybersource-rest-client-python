from pathlib import Path
from typing import List, Tuple


def validate_path(paths: List[Tuple[str, str]]) -> None:
    """
    Validate that all specified paths exist.

    Args:
        paths: List of tuples containing (path, description)

    Raises:
        ValueError: If a required path is None or empty
        FileNotFoundError: If any of the paths don't exist
        TypeError: If the paths parameter is not a list of tuples
    """
    if not isinstance(paths, list):
        raise TypeError("paths must be a list of (path, description) tuples")

    for path_tuple in paths:
        if not isinstance(path_tuple, tuple) or len(path_tuple) != 2:
            raise TypeError(
                "Each item in the paths list must be a (path, description) tuple"
            )

        path, description = path_tuple

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
