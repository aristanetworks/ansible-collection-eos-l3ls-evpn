# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations


def compare_dicts(dict1: dict, dict2: dict, ignore_keys: set[str] | None = None) -> tuple[bool, set[str]]:
    """
    Efficient comparison of dicts, where we can ignore certain keys.

    Returns:
    -------
    bool
        Do dict1 and dict2 match
    set[str]
        Set of keys that differs
    """
    keys1 = set(dict1).difference(ignore_keys or [])
    keys2 = set(dict2).difference(ignore_keys or [])
    result = keys1 == keys2 and all(dict1[key] == dict2[key] for key in keys1)
    if result:
        return (result, set())

    # We have some difference, so now compare again listing the keys that differ.
    diff_keys = keys1.difference(keys2)
    same_keys = keys1.intersection(keys2)
    diff_keys.update(key for key in same_keys if dict1[key] != dict2[key])

    return (result, diff_keys)
