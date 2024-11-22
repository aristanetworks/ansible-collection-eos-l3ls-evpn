# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from .get import get


def validate_dict(input_dict: dict, required_keys: list[str] | None = None, required_key_values: dict | None = None) -> tuple[bool, str]:
    """Validate that a dictionary has the required keys and values.

    Args:
    ----
        input_dict (dict): The dictionary to validate.
        required_keys (list[str]): A list of keys that must be present in the dictionary.
        required_key_values (dict): A dictionary of key-value pairs that must be present in the dictionary. Support dot-notation keys.

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

    missing_keys = [exp_key for exp_key in required_keys if get(input_dict, exp_key) is None if required_keys]

    if required_key_values:
        for exp_key, exp_value in required_key_values.items():
            if (act_value := get(input_dict, exp_key)) is None:
                missing_keys.append(exp_key)
            elif act_value != exp_value:
                invalid_values.append(f"{exp_key} != {exp_value}")

    issues = ""
    if missing_keys:
        issues += f"Unavailable keys: {', '.join(missing_keys)}; "
    if invalid_values:
        issues += f"Ineligible values: {', '.join(invalid_values)}"

    # Remove trailing semicolon and space if present
    if issues.endswith("; "):
        issues = issues[:-2]

    return (not issues), issues
