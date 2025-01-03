# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import Any


def get_validated_value(data: dict, key: str, expected_type: type, default_value: Any = None, allowed_values: list[str] | None = None) -> Any:
    """Retrieve and validate a value from a given dictionary based on its type and, optionally, a list of allowed values.

    Args:
    ----
        data (dict): Dictionary to retrieve the value from.
        key (str): Key corresponding to the value.
        expected_type (type): Expected type of the value.
        default_value (Any, optional): Default value if key is not found. Defaults to None.
        allowed_values (list[str] | None, optional): List of permissible values for the key. Defaults to None.

    Returns:
    -------
        Any: The validated value.

    Raises:
    ------
        TypeError: If value type is not 'expected_type'.
        ValueError: If value is not in 'allowed_values'.
    """
    value = data.get(key, default_value)

    if not isinstance(value, expected_type):
        msg = f"'{key}' value must be a {expected_type.__name__}, got {type(value).__name__}."
        raise TypeError(msg)

    if allowed_values is not None and value not in allowed_values:
        msg = f"'{key}' value must be in {allowed_values}, got {value}."
        raise ValueError(msg)

    return value
