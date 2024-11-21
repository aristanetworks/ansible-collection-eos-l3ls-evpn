# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from collections.abc import Iterable, Iterator, Sequence
from copy import deepcopy
from typing import TYPE_CHECKING, ClassVar, Generic, Literal

from pyavd._schema.coerce_type import coerce_type
from pyavd._utils import Undefined, UndefinedType

from .avd_base import AvdBase
from .type_vars import T_AvdModel, T_PrimaryKey

if TYPE_CHECKING:
    from typing_extensions import Self

    from .avd_model import AvdModel
    from .type_vars import T, T_AvdIndexedList

NATURAL_SORT_PATTERN = re.compile(r"(\d+)")


class AvdIndexedList(Sequence[T_AvdModel], Generic[T_PrimaryKey, T_AvdModel], AvdBase):
    """
    Base class used for schema-based data classes holding lists-of-dictionaries-with-primary-key loaded from AVD inputs.

    Other lists are *not* using this model.
    """

    _item_type: ClassVar[type[AvdModel]]
    """Type of items. This is used instead of inspecting the type-hints to improve performance significantly."""
    _primary_key: ClassVar[str]
    """The name of the primary key to be used in the items."""
    _items: dict[T_PrimaryKey, T_AvdModel]
    """
    Internal attribute holding the actual data. Using a dict keyed by the primary key value of each item to improve performance
    significantly when searching for a specific item.
    """

    @classmethod
    def _load(cls, data: Sequence) -> Self:
        """Returns a new instance loaded with the data from the given list."""
        return cls._from_list(data)

    @classmethod
    def _from_list(cls, data: Sequence) -> Self:
        """Returns a new instance loaded with the data from the given list."""
        if not isinstance(data, Sequence):
            msg = f"Expecting 'data' as a 'Sequence' when loading data into '{cls.__name__}'. Got '{type(data)}"
            raise TypeError(msg)

        cls_items = [coerce_type(item, cls._item_type) for item in data]
        return cls(cls_items)

    def __init__(self, items: Iterable[T_AvdModel] | UndefinedType = Undefined) -> None:
        """
        AvdIndexedList subclass.

        Args:
            items: Iterable holding items of the correct type to be loaded into the indexed list.
        """
        if isinstance(items, UndefinedType):
            self._items = {}
        else:
            self._items = {getattr(item, self._primary_key): item for item in items}

    def __repr__(self) -> str:
        """Returns a repr with all the items including any nested models."""
        cls_name = self.__class__.__name__
        attrs = [f"{item!r}" for item in (self._items.values())]
        return f"<{cls_name}([{', '.join(attrs)}])>"

    def __bool__(self) -> bool:
        """Boolean check on the class to quickly determine if any items are set."""
        return bool(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __contains__(self, key: T_PrimaryKey) -> bool:
        return key in self._items

    def __iter__(self) -> Iterator[T_AvdModel]:
        return iter(self._items.values())

    def __getitem__(self, key: T_PrimaryKey) -> T_AvdModel:
        return self._items[key]

    def __setitem__(self, key: T_PrimaryKey, value: T_AvdModel) -> None:
        self._items[key] = value

    def get(self, key: T_PrimaryKey, default: T | UndefinedType = Undefined) -> T_AvdModel | T | UndefinedType:
        return self._items.get(key, default)

    def items(self) -> Iterable[tuple[T_PrimaryKey, T_AvdModel]]:
        return self._items.items()

    def keys(self) -> Iterable[T_PrimaryKey]:
        return self._items.keys()

    def values(self) -> Iterable[T_AvdModel]:
        return self._items.values()

    def append(self, item: T_AvdModel) -> None:
        self._items[getattr(item, self._primary_key)] = item

    def extend(self, items: Iterable[T_AvdModel]) -> None:
        self._items.update({getattr(item, self._primary_key): item for item in items})

    def _as_list(self, include_default_values: bool = False) -> list[dict]:
        """Returns a list with all the data from this model and any nested models."""
        return [item._as_dict(include_default_values=include_default_values) for item in self._items.values()]

    def _dump(self, include_default_values: bool = False) -> list[dict]:
        return self._as_list(include_default_values=include_default_values)

    def _natural_sorted(self, ignore_case: bool = True) -> Self:
        """Return new instance where the items are natural sorted by primary key."""

        def convert(text: str) -> int | str:
            if text.isdigit():
                return int(text)
            return text.lower() if ignore_case else text

        def key(value: T_AvdModel) -> list[int | str]:
            primary_key = getattr(value, self._primary_key)
            return [convert(c) for c in re.split(NATURAL_SORT_PATTERN, str(primary_key))]

        cls = type(self)
        return cls(sorted(self.values(), key=key))

    def _deepmerge(self, other: Self, list_merge: Literal["append", "replace"] = "append") -> None:
        """
        Update instance by deepmerging the other instance in.

        Args:
            other: The other instance of the same type to merge into this instance.
            list_merge: Merge strategy used on this and any nested lists.
                - "append" will first try to deep merge on the primary key, and if not found it will append non-existing items.
                - "replace" will replace the full list.
        """
        cls = type(self)
        if not isinstance(other, cls):
            msg = f"Unable to merge type '{type(other)}' into '{cls}'"
            raise TypeError(msg)

        if list_merge == "replace":
            self._items = deepcopy(other._items)
            return

        for primary_key, new_item in other.items():
            old_value = self.get(primary_key)
            if old_value is Undefined or not isinstance(old_value, type(new_item)):
                # New item or different type so we can just replace
                self[primary_key] = deepcopy(new_item)
                continue

            # Existing item of same type, so deepmerge.
            self[primary_key]._deepmerge(new_item, list_merge=list_merge)

    def _deepinherit(self, other: Self) -> None:
        """Update instance by recursively inheriting from other instance for all existing items. New items are *not* added."""
        cls = type(self)
        if not isinstance(other, cls):
            msg = f"Unable to inherit from type '{type(other)}' into '{cls}'"
            raise TypeError(msg)

        for primary_key, new_item in other.items():
            old_value = self.get(primary_key)
            if old_value is Undefined:
                # New item so we can just append
                self[primary_key] = deepcopy(new_item)
                continue

            # Existing item, so deepinherit.
            self[primary_key]._deepinherit(new_item)

    def _cast_as(self, new_type: type[T_AvdIndexedList], ignore_extra_keys: bool = False) -> T_AvdIndexedList:
        """
        Recast a class instance as another AvdIndexedList subclass if they are compatible.

        The classes are compatible if the items of the new class is a superset of the current class.

        Useful when inheriting from profiles.
        """
        cls = type(self)
        if not issubclass(new_type, AvdIndexedList):
            msg = f"Unable to cast '{cls}' as type '{new_type}' since '{new_type}' is not an AvdIndexedList subclass."
            raise TypeError(msg)

        return new_type([item._cast_as(new_type._item_type, ignore_extra_keys=ignore_extra_keys) for item in self])
