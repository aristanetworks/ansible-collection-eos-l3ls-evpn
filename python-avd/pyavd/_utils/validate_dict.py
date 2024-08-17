# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations


def validate_dict(input_dict: dict, required_keys: list[str] | None = None, required_key_values: dict | None = None) -> tuple[bool, str]:
    """Validate that a dictionary has the required keys and values.

    Args:
    ----
        input_dict (dict): The dictionary to validate.
        required_keys (list[str]): A list of keys that must be present in the dictionary.
        required_key_values (dict): A dictionary of key-value pairs that must be present in the dictionary.

    Returns:
    -------
        tuple[bool, str]: A tuple where the first element is a boolean indicating whether the dictionary is valid,
        and the second element is a string describing any issues with the dictionary.

    """
    if not any((required_keys, required_key_values)):
        msg = "required_keys or required_key_values must be provided."
        raise ValueError(msg)

    missing_keys = []
    invalid_values = []

    missing_keys = [key for key in required_keys if key not in input_dict if required_keys]

    if required_key_values:
        for key, value in required_key_values.items():
            if key not in input_dict:
                missing_keys.append(key)
            elif input_dict[key] != value:
                invalid_values.append(f"{key} != {value}")

    issues = ""
    if missing_keys:
        issues += f"Missing keys: {', '.join(missing_keys)}; "
    if invalid_values:
        issues += f"Invalid values: {', '.join(invalid_values)}"

    # Remove trailing semicolon and space if present
    if issues.endswith("; "):
        issues = issues[:-2]

    return (not issues), issues
