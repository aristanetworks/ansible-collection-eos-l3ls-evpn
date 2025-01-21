# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path


def write_file(content: str, filename: str, file_mode: str = "0o664", dir_mode: str = "0o775") -> bool:
    """
    This function writes the file only if the content has changed.

    Parameters
    ----------
        content: The content to write
        filename: Target filename

    Returns:
    -------
        bool: Indicate if the content of filename has changed.
    """
    path = Path(filename)
    if not path.exists():
        # Create parent dirs automatically.
        path.parent.mkdir(mode=int(dir_mode, 8), parents=True, exist_ok=True)
        # Touch file
        path.touch(mode=int(file_mode, 8))
    elif path.read_text(encoding="UTF-8") == content:
        return False

    path.write_text(content, encoding="UTF-8")
    return True
