# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from itertools import islice
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable


def batch(iterable: Iterable, size: int) -> Generator[Iterable]:
    """Returns a Generator of lists containing 'size' items. The final list may be shorter."""
    iterator = iter(iterable)
    while batch := list(islice(iterator, size)):
        yield batch
