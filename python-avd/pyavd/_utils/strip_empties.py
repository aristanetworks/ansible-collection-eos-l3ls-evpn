# Copyright (c) 2019-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


def strip_null_from_data(data: T, strip_values_tuple: tuple = (None,)) -> T:
    """
    strip_null_from_data Generic function to strip null entries regardless type of variable.

    Parameters
    ----------
    data : Any
        Data to look for null content to strip out

    Returns:
    -------
    Any
        Cleaned data with no null.
    """
    if isinstance(data, dict):
        return strip_empties_from_dict(data, strip_values_tuple)
    if isinstance(data, list):
        return strip_empties_from_list(data, strip_values_tuple)
    return data


def strip_empties_from_list(data: list, strip_values_tuple: tuple = (None, "", [], {})) -> list:
    """
    strip_empties_from_list Remove entries with null value from a list.

    Parameters
    ----------
    data : Any
        data to filter
    strip_values_tuple : tuple, optional
        Value to remove from data, by default (None, "", [], {},)

    Returns:
    -------
    Any
        Cleaned list with no strip_values_tuple
    """
    new_data = []
    for v in data:
        if isinstance(v, dict):
            stripped_v = strip_empties_from_dict(v, strip_values_tuple)
        elif isinstance(v, list):
            stripped_v = strip_empties_from_list(v, strip_values_tuple)
        else:
            stripped_v = v

        if stripped_v not in strip_values_tuple:
            new_data.append(stripped_v)
    return new_data


def strip_empties_from_dict(data: dict, strip_values_tuple: tuple = (None, "", [], {})) -> dict:
    """
    strip_empties_from_dict Remove entries with null value from a dict.

    Parameters
    ----------
    data : Any
        data to filter
    strip_values_tuple : tuple, optional
        Value to remove from data, by default (None, "", [], {},)

    Returns:
    -------
    Any
        Cleaned dict with no strip_values_tuple
    """
    new_data = {}
    for k, v in data.items():
        if isinstance(v, dict):
            stripped_v = strip_empties_from_dict(v, strip_values_tuple)
        elif isinstance(v, list):
            stripped_v = strip_empties_from_list(v, strip_values_tuple)
        else:
            stripped_v = v
        if stripped_v not in strip_values_tuple:
            new_data[k] = stripped_v
    return new_data
