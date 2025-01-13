# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeVar

    # TODO: Once we drop 3.10 support this can be imported from typing.
    from typing_extensions import Unpack

    T = TypeVar("T")


def default(*values: Unpack[tuple[Unpack[tuple[T | None, ...]], T]]) -> T:
    """
    Accepts any number of arguments. Return the first value which is not None.

    Last resort is to return None.

    Args:
        *values: Optional values to test
        final_value: Final value to test

    Returns:
        First value which is not None
    """
    for value in values:
        if value is not None:
            return value
    return None  # Type hint does not allow this, but it will only happen if all values are None, hence T should include None
