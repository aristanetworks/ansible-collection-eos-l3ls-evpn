# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC, abstractmethod
from copy import deepcopy
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

    from typing_extensions import Self

    from .type_vars import T_AvdBase


class InternalData:
    __slots__ = (
        "context",
        "evpn_l3_multicast_enabled",
        "evpn_l3_multicast_evpn_peg_transit",
        "evpn_l3_multicast_group_ip",
        "interface",
        "interfaces",
        "pim_rp_addresses",
        "type",
    )

    context: str
    evpn_l3_multicast_enabled: bool | None
    evpn_l3_multicast_evpn_peg_transit: bool | None
    evpn_l3_multicast_group_ip: str | None
    interface: str
    interfaces: list
    pim_rp_addresses: list[dict]
    type: str | None


class AvdBase(ABC):
    """Base class used for schema-based data classes holding data loaded from AVD inputs."""

    __slots__ = ("_block_inheritance", "_created_from_null", "_internal_data_instance")

    _created_from_null: bool
    """
    Flag to say if this data was loaded from a '<key>: null' value in YAML.

    This is used to handle inheritance and merging correctly.
    When _created_from_null we inherit nothing (we win!).
    When _created_from_null we take anything in when merging and clear the flag.
    TODO: Stop changing data in-place.

    The flag is not carried across between classes, so it should not affect anything outside the loaded inputs.
    Only exception is on _cast_as, where the flag is carried over.
    """

    _block_inheritance: bool
    """Flag to block inheriting further if we at some point inherited from a class with _created_from_null set."""

    _internal_data_instance: InternalData
    """Placeholder for Internal data used for storing internal context on data objects, without affecting other logic."""

    def __init__(self) -> None:
        """Setting default values since these are slots."""
        self._created_from_null = False
        self._block_inheritance = False

    def _deepcopy(self) -> Self:
        """Return a copy including all nested models."""
        return deepcopy(self)

    @property
    def _internal_data(self) -> InternalData:
        """Internal data used for storing internal context on data objects, without affecting other logic."""
        # Creating the instance on first access to avoid creating unused instances of this class.
        try:
            return self._internal_data_instance
        except AttributeError:
            self._internal_data_instance = InternalData()
            return self._internal_data_instance

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
    def _deepmerge(self, other: Self, list_merge: Literal["append_unique", "append", "replace", "keep", "prepend", "prepend_unique"] = "append_unique") -> None:
        """
        Update instance by deepmerging the other instance in.

        Args:
            other: The other instance of the same type to merge on this instance.
            list_merge: Merge strategy used on any nested lists.

        List merge strategies:
        - "append_unique" will first try to deep merge on the primary key, and if not found it will append non-existing items.
        - "append" will first try to deep merge on the primary key, and if not found it will append all other items (including duplicates).\
            (For AvdIndexedList this works the same as append_unique)
        - "replace" will replace the full list.
        - "keep" will only use the new list if there is no existing list or existing list is `None`.
        - "prepend_unique" will first try to deep merge on the primary key, and if not found it will prepend non-existing items.
        - "prepend" will first try to deep merge on the primary key, and if not found it will prepend all other items (including duplicates).\
            (For AvdIndexedList this works the same as prepend_unique)
        """

    @abstractmethod
    def _compare(self, other: Self) -> bool:
        """Compare two instances. Optionally ignoring fields for the outermost AvdModel."""

    def _deepmerged(
        self, other: Self, list_merge: Literal["append_unique", "append", "replace", "keep", "prepend", "prepend_unique"] = "append_unique"
    ) -> Self:
        """
        Return new instance with the result of the deepmerge of "other" on this instance.

        Args:
            other: The other instance of the same type to merge on this instance.
            list_merge: Merge strategy used on any nested lists.

        List merge strategies:
        - "append_unique" will first try to deep merge on the primary key, and if not found it will append non-existing items.
        - "append" will first try to deep merge on the primary key, and if not found it will append all other items (including duplicates).\
            (For AvdIndexedList this works the same as append_unique)
        - "replace" will replace the full list.
        - "keep" will only use the new list if there is no existing list or existing list is `None`.
        - "prepend_unique" will first try to deep merge on the primary key, and if not found it will prepend non-existing items.
        - "prepend" will first try to deep merge on the primary key, and if not found it will prepend all other items (including duplicates).\
            (For AvdIndexedList this works the same as prepend_unique)
        """
        new_instance = deepcopy(self)
        new_instance._deepmerge(other=other, list_merge=list_merge)
        return new_instance
