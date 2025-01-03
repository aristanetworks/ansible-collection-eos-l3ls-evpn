# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Any

from pyavd._errors import AristaAvdInvalidInputsError, AristaAvdMissingVariableError


def get_item(
    list_of_dicts: list,
    key: Any,
    value: Any,
    default: Any = None,
    *,
    required: bool = False,
    _case_sensitive: bool = False,
    var_name: str | None = None,
    custom_error_msg: str | None = None,
) -> Any:
    """
    Get one dictionary from a list of dictionaries by matching the given key and value.

    Returns the supplied default value or None if there is no match and "required" is False.

    Will return the first matching item if there are multiple matching items.

    Parameters
    ----------
    list_of_dicts : list(dict)
        List of Dictionaries to get list item from
    key : any
        Dictionary Key to match on
    value : any
        Value that must match
    default : any
        Default value returned if the key and value is not found
    required : bool
        Fail if there is no match
    case_sensitive : bool
        If the search value is a string, the comparison will ignore case by default (TODO)
    var_name : str
        String used for raising exception with the full variable name
    custom_error_msg : str
        Custom error message to raise when required is True and the value is not found

    Returns:
    -------
    any
        Dict or default value

    Raises:
    ------
    AristaAvdMissingVariableError
        If the key and value is not found and "required" == True
    """
    if var_name is None:
        var_name = key

    if (not isinstance(list_of_dicts, list)) or list_of_dicts == [] or value is None or key is None:
        if required is True:
            if custom_error_msg:
                raise AristaAvdInvalidInputsError(custom_error_msg)
            raise AristaAvdMissingVariableError(var_name)
        return default

    for list_item in list_of_dicts:
        if not isinstance(list_item, dict):
            # List item is not a dict as required. Skip this item
            continue
        if list_item.get(key) == value:
            # Match. Return this item
            return list_item

    # No Match
    if required is True:
        if custom_error_msg:
            raise AristaAvdInvalidInputsError(custom_error_msg)
        raise AristaAvdMissingVariableError(var_name)
    return default
