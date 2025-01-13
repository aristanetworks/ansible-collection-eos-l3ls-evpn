# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pathlib import Path


def get_validated_path(path_input: str | Path, *, parent: bool = False) -> Path:
    """Verify if the given path or its parent directory exists and return the Path object.

    Args:
    ----
    path_input (str or Path): A string or Path object representing a file system path.
    parent (bool, optional): Flag to indicate whether to check the path itself (False)
                             or its parent directory (True). Defaults to False.

    Returns:
    -------
    Path: The given file system path as a Path object.

    Raises:
    ------
    TypeError: If the input is not a string or Path object.
    FileNotFoundError: If the specified path or its parent does not exist.
    """
    if not isinstance(path_input, (str, Path)):
        msg = f"Input path {path_input} must be a string or a Path object."
        raise TypeError(msg)
    path = Path(path_input)
    if (parent and path.parent.exists()) or (not parent and path.exists()):
        return path
    msg = f"The {'parent directory of ' if parent else ''}path {path} does not exist."
    raise FileNotFoundError(msg)
