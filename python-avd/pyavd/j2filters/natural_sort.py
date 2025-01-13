# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from collections.abc import Iterable, Mapping
from typing import Any

from jinja2.runtime import Undefined
from jinja2.utils import Namespace


def convert(text: str, ignore_case: bool) -> int | str:
    """Converts the input string to be sorted.

    Converts the string to an integer if it is a digit, otherwise converts
    it to lower case if ignore_case is True.

    Args:
    -----
        text (str): Input string.
        ignore_case (bool): If ignore_case is True, strings are applied lower() function.

    Returns:
    -------
        int | str: Converted string.
    """
    if text.isdigit():
        return int(text)
    return text.lower() if ignore_case else text


def natural_sort(iterable: Iterable | None, sort_key: str | None = None, *, strict: bool = True, ignore_case: bool = True) -> list:
    """Sorts an iterable in a natural (alphanumeric) order.

    Args:
        iterable: Input iterable.
        sort_key: Key to sort by, defaults to None.
        strict: If strict is True, raise an error is the sort_key is missing.
        ignore_case: If ignore_case is True, strings are applied lower() function.

    Returns:
        list: Sorted iterable.

    Raises:
        KeyError, AttributeError: if strict=True and sort_key is not present in an item in the iterable.
    """
    if isinstance(iterable, Undefined) or iterable is None:
        return []

    def alphanum_key(key: Any) -> list:
        pattern = r"(\d+)"
        if sort_key is not None and isinstance(key, Mapping):
            if strict and sort_key not in key:
                msg = f"Missing key '{sort_key}' in item to sort {key}."
                raise KeyError(msg)
            return [convert(c, ignore_case) for c in re.split(pattern, str(key.get(sort_key, key)))]
        if sort_key is not None and isinstance(key, Namespace):
            if strict and not hasattr(key, sort_key):
                msg = f"Missing attribute '{sort_key}' in item to sort {key}."
                raise AttributeError(msg)
            return [convert(c, ignore_case) for c in re.split(pattern, str(getattr(key, sort_key)))]
        return [convert(c, ignore_case) for c in re.split(pattern, str(key))]

    return sorted(iterable, key=alphanum_key)
