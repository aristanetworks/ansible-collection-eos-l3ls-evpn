# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations


def hide_passwords(value: str, hide_passwords: bool = False) -> str:
    """
    Replaces the input data with "<removed>" if the hide_passwords parameter is true.

    Args:
        value (str): Value to be hidden
        hide_passwords(bool) : Enable/disable hide_passwords
    Returns:
        str: "<removed>" or value

    """
    if not isinstance(hide_passwords, bool):
        msg = f"{hide_passwords} in hide_passwords filter is not of type bool"
        raise TypeError(msg)
    return "<removed>" if hide_passwords else value
