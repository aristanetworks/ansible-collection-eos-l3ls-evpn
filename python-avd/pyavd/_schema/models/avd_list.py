# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from typing import TYPE_CHECKING, Any, ClassVar, Generic, Literal, cast

from pyavd._schema.coerce_type import coerce_type
from pyavd._utils import Undefined, UndefinedType

from .avd_base import AvdBase
from .avd_model import AvdModel
from .type_vars import T, T_AvdList, T_ItemType

if TYPE_CHECKING:
    from typing_extensions import Self

NATURAL_SORT_PATTERN = re.compile(r"(\d+)")


class AvdList(Sequence[T_ItemType], Generic[T_ItemType], AvdBase):
    """
    Base class used for schema-based data classes holding lists-of-dictionaries-with-primary-key loaded from AVD inputs.

    Other lists are *not* using this model.
    """

    _item_type: ClassVar[type]
    """Type of items. This is used instead of inspecting the type-hints to improve performance significantly."""
    _items: list[T_ItemType]
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

        item_type = cls._item_type
        if item_type is Any:
            return cls(data)

        cls_items = [coerce_type(item, item_type) for item in data]
        return cls(cls_items)

    def __init__(self, items: Iterable[T_ItemType] | UndefinedType = Undefined) -> None:
        """
        AvdList subclass.

        Args:
            items: Iterable holding items of the correct type to be loaded into the list.
        """
        if isinstance(items, UndefinedType):
            self._items = []
        else:
            self._items = list(items)

    def __repr__(self) -> str:
        """Returns a repr with all the items including any nested models."""
        cls_name = self.__class__.__name__
        items = [f"{item!r}" for item in (self._items)]
        return f"<{cls_name}([{', '.join(items)}])>"

    def __bool__(self) -> bool:
        """Boolean check on the class to quickly determine if any items are set."""
        return bool(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __contains__(self, item: T_ItemType) -> bool:
        return item in self._items

    def __iter__(self) -> Iterator[T_ItemType]:
        return iter(self._items)

    def __getitem__(self, index: int) -> T_ItemType:
        return self._items[index]

    def __setitem__(self, index: int, value: T_ItemType) -> None:
        self._items[index] = value

    def get(self, index: int, default: T | UndefinedType = Undefined) -> T_ItemType | T | UndefinedType:
        return self._items[index] if index < len(self._items) else default

    def append(self, item: T_ItemType) -> None:
        self._items.append(item)

    def append_unique(self, item: T_ItemType) -> None:
        """Append the item if not there already. Otherwise ignore."""
        if item not in self._items:
            self._items.append(item)

    if TYPE_CHECKING:
        append_new: type[T_ItemType]
    else:

        def append_new(self, *args: Any, **kwargs: Any) -> T_ItemType:
            """Create a new instance with the given arguments and append to the list. Returns the new item."""
            new_item = self._item_type(*args, **kwargs)
            self.append(new_item)
            return new_item

    def extend(self, items: Iterable[T_ItemType]) -> None:
        self._items.extend(items)

    def _strip_empties(self) -> None:
        """In-place update the instance to remove data matching the given strip_values."""
        if issubclass(self._item_type, AvdBase):
            items = cast(list[AvdBase], self._items)
            [item._strip_empties() for item in items]
            self._items = [item for item in self._items if item]
            return

        self._items = [item for item in self._items if item is not None]

    def _as_list(self, include_default_values: bool = False) -> list:
        """Returns a list with all the data from this model and any nested models."""
        if issubclass(self._item_type, AvdBase):
            items = cast(list[AvdBase], self._items)
            return [item._dump(include_default_values=include_default_values) for item in items]

        return list(self._items)

    def _dump(self, include_default_values: bool = False) -> list:
        return self._as_list(include_default_values=include_default_values)

    def _natural_sorted(self, sort_key: str | None = None, ignore_case: bool = True) -> Self:
        """Return new instance where the items are natural sorted by the given sort key or by the item itself."""

        def convert(text: str) -> int | str:
            if text.isdigit():
                return int(text)
            return text.lower() if ignore_case else text

        def key(value: T_ItemType) -> list[int | str]:
            if sort_key is not None:
                if isinstance(value, AvdModel):
                    sort_value = str(value._get(sort_key, default=value))
                elif isinstance(value, Mapping):
                    sort_value = str(value.get(sort_key, value))
            else:
                sort_value = str(value)
            return [convert(c) for c in re.split(NATURAL_SORT_PATTERN, sort_value)]

        cls = type(self)
        return cls(sorted(self._items, key=key))

    def _filtered(self, function: Callable[[T_ItemType], bool]) -> Self:
        cls = type(self)
        return cls(filter(function, self._items))

    def _deepmerge(self, other: Self, list_merge: Literal["append_unique", "append", "replace", "keep", "prepend", "prepend_unique"] = "append_unique") -> None:
        """
        Update instance by appending or replacing the items from the other instance.

        Args:
            other: The other instance of the same type to merge into this instance.
            list_merge: Merge strategy used on this and any nested lists.

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
        cls = type(self)
        if not isinstance(other, cls):
            msg = f"Unable to merge type '{type(other)}' into '{cls}'"
            raise TypeError(msg)

        if self._created_from_null or other._created_from_null:
            # Set the flag to the value of other and set list_merge to replace so we overwrite with data from other below.
            self._created_from_null = other._created_from_null
            list_merge = "replace"

        match list_merge:
            case "append_unique":
                # Append non-existing items.
                self._items.extend(new_item for new_item in other._items if new_item not in self._items)
            case "append":
                # Append all items.
                self._items.extend(other._items)
            case "replace":
                # Replace with the "other" list.
                self._items = other._items.copy()
                return
            case "keep":
                # We only get here if there was a defined instance of the old list, so we "keep" the existing list as-is.
                return
            case "prepend_unique":
                # Prepend non-existing items.
                self._items[:0] = [new_item for new_item in other._items if new_item not in self._items]
            case "prepend":
                self._items[:0] = other._items

    def _cast_as(self, new_type: type[T_AvdList], ignore_extra_keys: bool = False) -> T_AvdList:
        """
        Recast a class instance as another AvdList subclass if they are compatible.

        The classes are compatible if the items of the new class is a superset of the current class.

        Useful when inheriting from profiles.
        """
        cls = type(self)
        if not issubclass(new_type, AvdList):
            msg = f"Unable to cast '{cls}' as type '{new_type}' since '{new_type}' is not an AvdList subclass."
            raise TypeError(msg)

        if issubclass(self._item_type, AvdBase):
            items = cast(list[AvdBase], self._items)
            return new_type([item._cast_as(new_type._item_type, ignore_extra_keys=ignore_extra_keys) for item in items])

        if self._item_type != new_type._item_type:
            msg = f"Unable to cast '{cls}' as type '{new_type}' since they have incompatible item types."
            raise TypeError(msg)

        new_instance = new_type(self._items)

        # Pass along the _created_from_null flag
        new_instance._created_from_null = self._created_from_null

        return new_instance
