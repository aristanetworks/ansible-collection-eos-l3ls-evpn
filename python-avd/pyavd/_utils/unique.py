# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
def unique(in_list: list) -> list:
    """
    Return list of unique items from the in_list.

    Parameters
    ----------
    in_list : list

    Returns:
    -------
    list
        Unique list items
    """
    return list(set(in_list))
