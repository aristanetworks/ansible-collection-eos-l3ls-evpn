# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import Any

from pyavd._utils.password_utils import METHODS_DIR


def encrypt(value: Any, passwd_type: str | None = None, key: str | None = None, **kwargs: Any) -> str:
    """
    Umbrella function to execute the correct encrypt method based on the input type.

    Args:
        value (any): The value to encrypt.
        passwd_type (str): The type of encryption method to use. Must be provided.
        key (str or None): Optional encryption key or parameter.
        **kwargs: Additional keyword arguments passed to the specific encryption method.

    Returns:
        str: The encrypted value as a string.

    Raises:
        TypeError: If `passwd_type` is not provided.
        KeyError: If `passwd_type` is not found in `METHODS_DIR`.
    """
    if not passwd_type:
        msg = "type keyword must be present to use this test"
        raise TypeError(msg)
    try:
        encrypt_method = METHODS_DIR[passwd_type][0]
    except KeyError as exc:
        msg = f"Type {passwd_type} is not supported for the encrypt filter"
        raise KeyError(msg) from exc
    return encrypt_method(str(value), key=key, **kwargs)
