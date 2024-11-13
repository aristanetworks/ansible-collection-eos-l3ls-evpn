# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


class AvdBase:
    """Base class used for schema-based data classes holding data loaded from AVD inputs."""

    def __eq__(self, other: object) -> bool:
        """Compare two instances of AvdBase by comparing their repr."""
        if isinstance(other, self.__class__):
            return repr(self) == repr(other)
        return False

    def _deepcopy(self) -> Self:
        """Return a copy including all nested models."""
        return deepcopy(self)
