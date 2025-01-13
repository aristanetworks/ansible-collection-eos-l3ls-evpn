# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations


def is_in_filter(hostname: str, hostname_filter: list | None) -> bool:
    """
    Check if device is part of the filter or not.

    Parameters
    ----------
    hostname : str
        Device hostname to compare against filter.
    hostname_filter : list, optional
        Device filter, by default ['all']

    Returns:
    -------
    boolean
        True if device hostname is part of filter. False if not.
    """
    if hostname_filter is None:
        hostname_filter = ["all"]
    if "all" in hostname_filter:
        return True
    return any(element in hostname for element in hostname_filter)
