# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from collections.abc import Iterable, Mapping
from functools import partial
from typing import Any

from jinja2.runtime import Undefined
from jinja2.utils import Namespace

SPLIT_PATTERN = re.compile(r"(\d+)")


def natural_sort(iterable: Iterable | None, sort_key: str | None = None, *, strict: bool = True, ignore_case: bool = True, default_value: Any = None) -> list:
    """
    Sorts an iterable in a natural (alphanumeric) order.

    Args:
        iterable: Input iterable.
        sort_key: Key to sort by, defaults to None.
        strict: If strict is True, raise an error if the sort_key is missing and no default value is given.
        ignore_case: If ignore_case is True, strings are applied lower() function.
        default_value: Default value to use if the sort_key is missing.

    Returns:
        list: Sorted iterable.

    Raises:
        KeyError, AttributeError: if strict=True and sort_key is not present in an item in the iterable.
    """
    if isinstance(iterable, Undefined) or iterable is None:
        return []

    alphanum_key = partial(_alphanum_key, sort_key=sort_key, strict=strict, ignore_case=ignore_case, default_value=default_value)

    return sorted(iterable, key=alphanum_key)


def _alphanum_key(item: Any, sort_key: str | None = None, *, strict: bool = True, ignore_case: bool = True, default_value: Any = None) -> list:
    """Get the key to natural sort by. Falling back to the item itself."""
    if sort_key is not None and isinstance(item, Mapping):
        if strict and sort_key not in item and default_value is None:
            msg = f"Missing key '{sort_key}' in item to sort {item}."
            raise KeyError(msg)
        if default_value is None:
            default_value = item
        return [_convert(c, ignore_case) for c in re.split(SPLIT_PATTERN, str(item.get(sort_key, default_value)))]
    if sort_key is not None and isinstance(item, Namespace):
        if strict and not hasattr(item, sort_key) and default_value is None:
            msg = f"Missing attribute '{sort_key}' in item to sort {item}."
            raise AttributeError(msg)
        if default_value is None:
            default_value = item
        return [_convert(c, ignore_case) for c in re.split(SPLIT_PATTERN, str(getattr(item, sort_key, default_value)))]
    return [_convert(c, ignore_case) for c in re.split(SPLIT_PATTERN, str(item))]


def _convert(text: str, ignore_case: bool) -> int | str:
    """
    Converts the input string to be sorted.

    Converts the string to an integer if it is a digit, otherwise converts
    it to lower case if ignore_case is True.

    Args:
        text: Input string.
        ignore_case: If ignore_case is True, strings are applied lower() function.

    Returns:
        Converted string.
    """
    if text.isdigit():
        return int(text)
    return text.lower() if ignore_case else text
