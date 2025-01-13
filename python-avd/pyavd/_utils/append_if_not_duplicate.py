# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pyavd._errors import AristaAvdDuplicateDataError

from .compare_dicts import compare_dicts
from .get import get
from .get_item import get_item


def append_if_not_duplicate(
    list_of_dicts: list[dict],
    primary_key: str,
    new_dict: dict,
    context: str,
    context_keys: list[str],
    ignore_same_dict: bool = True,
    ignore_keys: set[str] | None = None,
) -> None:
    """
    Append new_dict to list_of_dicts if there is not already an item with the same primary key in list_of_dicts.

    Raise AristaAvdDuplicateDataError with relevant context and context_keys extracted from new_dict and existing duplicate.

    Parameters
    ----------
    list_of_dicts : list(dict)
        List of Dictionaries to look for duplicate item.
    primary_key : str
        Dictionary Key to match on.
    new_dict : dict
        Item to append.
    context : str
        Context of duplicate check. Used for error message like
        "Found duplicate objects with conflicting data while generating configuration for {context}.'
        {context_keys_from_item_a} conflicts with {context_keys_from_item_a}"
    context_keys : list[str]
        Keys to extract from new_dict and the found_dict and show in the error message.
    ignore_same_dict: bool, default=True
        Ignore the new_dict if a duplicate is found and it is an exact match.
    ignore_keys : set[str] | None
        Keys to ignore when performing the comparison for 'ignore_same_dict'.
        Often if is relevant to ignore the 'tenant' key so duplicate configs across multiple
        tenants can be ignored since tenant is not part of the output config.

    Raises:
    ------
    AristaAvdDuplicateDataError
        If a duplicate is found.
    """
    if (found_dict := get_item(list_of_dicts, primary_key, new_dict[primary_key])) is None:
        list_of_dicts.append(new_dict)
        return

    if (compare_result := compare_dicts(new_dict, found_dict, ignore_keys))[0] and ignore_same_dict:
        return

    context_keys.extend(sorted(compare_result[1]))
    context_item_a = str({context_key: get(new_dict, context_key) for context_key in context_keys})
    context_item_b = str({context_key: get(found_dict, context_key) for context_key in context_keys})
    raise AristaAvdDuplicateDataError(context, context_item_a, context_item_b)
