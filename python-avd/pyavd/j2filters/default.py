# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import TypeVar

from jinja2.runtime import Undefined

T = TypeVar("T")


def default(*values: list[T]) -> T | None:
    """
    Default will test value if defined and is not none.

    Arista.avd.default will test if the first value is defined and is not none.
    If true return value else repeat for the next value.
    If we run out of values we return None.

    Example when used as a jinja filter
    -------
    priority: {{ spanning_tree_priority | arista.avd.default("32768") }}

    Args:
        *values: One or more values to test.

    Returns:
        First value that is defined and not None. Otherwise returns None.
    """
    for value in values:
        if value is not None and not isinstance(value, Undefined):
            return value

    return None
