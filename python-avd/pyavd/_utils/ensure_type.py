# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, TypeVar

    T = TypeVar("T")


def ensure_type(item: Any, item_type: type[T]) -> T:
    """
    Ensure that the item is of the specified type.

    Args:
        item: The item to check.
        item_type: The type to check against.

    Returns:
        The item if it is of the correct type.

    Raises:
        TypeError: If the item is not of the correct type.
    """
    if not isinstance(item, item_type):
        msg = f"Expected {item_type.__name__} but got {type(item).__name__}."
        raise TypeError(msg)
    return item
