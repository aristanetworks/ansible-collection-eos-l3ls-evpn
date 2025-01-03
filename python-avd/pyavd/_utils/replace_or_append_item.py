# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
def replace_or_append_item(list_of_dicts: list, key: str, replacement_dict: dict) -> int:
    """
    In-place replace or append one dictionary to a list of dictionaries by matching the given key with the value of replacement_dict[key].

    Parameters
    ----------
    list_of_dicts : list(dict)
        List of Dictionaries to get list item from
    key : any
        Dictionary Key to match on
    replacement_dict : dict
        Dictionary to replace / append.
        The value of 'key' in this dict is used to search for existing entries.

    Returns:
    -------
    int
        Index in list_of_dicts of replaced / appended entry
    """
    if key not in replacement_dict:
        msg = f"The argument 'replacement_dict' does not contain the key {key}"
        raise ValueError(msg)

    for index, list_item in enumerate(list_of_dicts):
        if not isinstance(list_item, dict):
            # List item is not a dict as required. Skip this item.
            continue
        if list_item.get(key) == replacement_dict[key]:
            # Match. Replace the item and return the index.
            list_of_dicts[index] = replacement_dict
            return index

    # No Match
    index = len(list_of_dicts)
    list_of_dicts.append(replacement_dict)
    return index
