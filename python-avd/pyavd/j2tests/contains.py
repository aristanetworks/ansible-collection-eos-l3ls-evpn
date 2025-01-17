# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""AVD Jinja2 test contains.

The test checks if a list contains any of the value(s) passed in test_value.
"""

from __future__ import annotations

from typing import Any

from jinja2.runtime import Undefined


def contains(value: list[Any], test_value: Any | list[Any] = None) -> bool:
    """The test checks if a list contains any of the value(s) passed in test_value.

    If 'value' is Undefined, None or not a list then the test has failed.

    Parameters
    ----------
    value :
        List to test
    test_value : single item or list of items
        Value(s) to test for in value

    Returns:
    -------
    boolean
        True if variable matches criteria, False in other cases.
    """
    # TODO: - this will fail miserably if test_value is not hashable !
    if isinstance(value, Undefined) or value is None or not isinstance(value, list):
        # Invalid value - return false
        return False
    if isinstance(test_value, Undefined) or test_value is None:
        # Invalid value - return false
        return False
    if isinstance(test_value, list) and not set(value).isdisjoint(test_value):
        # test_value is list so test if value and test_value has any common items
        return True
    return test_value in value
