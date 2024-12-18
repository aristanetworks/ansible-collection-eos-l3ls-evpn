# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC, abstractmethod
from copy import deepcopy
import re
from typing import TYPE_CHECKING, Literal

from .avd_path import AvdPath

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

    from typing_extensions import Self

    from .type_vars import T_AvdBase


class AvdBase(ABC):
    """Base class used for schema-based data classes holding data loaded from AVD inputs."""

    _path: AvdPath = AvdPath()
    """Path the class in the data tree."""

    _created_from_null: bool = False
    """
    Flag to say if this data was loaded from a '<key>: null' value in YAML.

    This is used to handle inheritance and merging correctly.
    When _created_from_null we inherit nothing (we win!).
    When _created_from_null we take anything in when merging and clear the flag.
    TODO: Stop changing data in-place.

    The flag is not carried across between classes, so it should not affect anything outside the loaded inputs.
    Only exception is on _cast_as, where the flag is carried over.
    """

    _block_inheritance: bool = False
    """Flag to block inheriting further if we at some point inherited from a class with _created_from_null set."""

    @property
    def path(self) -> str:
        """Return the path of the class."""
        return str(self._path)

    @classmethod
    def get_schema_name(cls) -> str:
        """Return the schema name of the class."""
        return re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()

    def __eq__(self, other: object) -> bool:
        """Compare two instances of AvdBase by comparing their repr."""
        if isinstance(other, self.__class__):
            return repr(self) == repr(other)
        return False

    def _deepcopy(self) -> Self:
        """Return a copy including all nested models."""
        return deepcopy(self)

    @classmethod
    @abstractmethod
    def _load(cls, data: Sequence | Mapping) -> Self:
        """Returns a new instance loaded with the given data."""

    @classmethod
    def _from_null(cls) -> Self:
        """Returns a new instance with all attributes set to None. This represents the YAML input '<key>: null'."""
        new_instance = cls()
        new_instance._created_from_null = True
        return new_instance

    @abstractmethod
    def _strip_empties(self) -> None:
        """In-place update the instance to remove data matching the given strip_values."""

    @abstractmethod
    def _dump(self, include_default_values: bool = False) -> dict | list:
        """Dump data into native Python types with or without default values."""

    @abstractmethod
    def _cast_as(self, new_type: type[T_AvdBase], ignore_extra_keys: bool = False) -> T_AvdBase:
        """Recast a class instance as another similar subclass if they are compatible."""

    @abstractmethod
    def _deepmerge(self, other: Self, list_merge: Literal["append", "replace"] = "append") -> None:
        """
        Update instance by deepmerging the other instance in.

        Args:
            other: The other instance of the same type to merge on this instance.
            list_merge: Merge strategy used on any nested lists.
                - "append" will first try to deep merge on the primary key, and if not found it will append non-existing items.
                - "replace" will replace the full list.
        """

    def _deepmerged(self, other: Self, list_merge: Literal["append", "replace"] = "append") -> Self:
        """
        Return new instance with the result of the deepmerge of "other" on this instance.

        Args:
            other: The other instance of the same type to merge on this instance.
            list_merge: Merge strategy used on any nested lists.
                - "append" will first try to deep merge on the primary key, and if not found it will append non-existing items.
                - "replace" will replace the full list.
        """
        new_instance = deepcopy(self)
        new_instance._deepmerge(other=other, list_merge=list_merge)
        return new_instance
