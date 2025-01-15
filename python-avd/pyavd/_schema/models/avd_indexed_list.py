# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from collections.abc import Iterable, Iterator, Sequence
from typing import TYPE_CHECKING, ClassVar, Generic, Literal, cast

from pyavd._errors import AristaAvdDuplicateDataError
from pyavd._schema.coerce_type import coerce_type
from pyavd._utils import Undefined, UndefinedType

from .avd_base import AvdBase
from .input_path import InputPath, PathIndexedListKey
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
    def _load(cls, data: Sequence, data_source: InputPath | None = None) -> Self:
        """Returns a new instance loaded with the data from the given list."""
        return cls._from_list(data, data_source=data_source)

    @classmethod
    def _from_list(cls, data: Sequence, data_source: InputPath | None = None) -> Self:
        """Returns a new instance loaded with the data from the given list."""
        data_source = data_source or InputPath()
        if not isinstance(data, Sequence):
            msg = f"Expecting 'data' as a 'Sequence' when loading data into '{cls.__name__}'. Got '{type(data)}"
            raise TypeError(msg)

        cls_items = []
        # Handle _DynamicKeys slightly differently
        for index, item in enumerate(data):
            # Need to retrieve the key from the data not from the model.
            item_key = cls._item_type._field_to_key_map.get(cls._primary_key, cls._primary_key)
            child_data_source = (
                InputPath(item[item_key])
                if cls.__name__.startswith("Dynamic")
                else data_source.create_descendant(PathIndexedListKey(index, item_key, item[item_key]))
            )
            cls_items.append(cast(Iterable[T_AvdModel], (coerce_type(item, cls._item_type, data_source=child_data_source))))

        cls_instance = cls(cls_items)
        cls_instance._source = data_source
        return cls_instance

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

    def obtain(self, key: T_PrimaryKey) -> T_AvdModel:
        """Return item with given primary key, autocreating if missing."""
        if key not in self._items:
            item_type = cast(T_AvdModel, self._item_type)
            self._items[key] = item_type._from_dict({self._primary_key: key})
        return self._items[key]

    def append(self, item: T_AvdModel, ignore_fields: tuple[str, ...] = ()) -> None:
        if (primary_key := getattr(item, self._primary_key)) in self._items:
            # Found existing entry using the same primary key. Ignore if it is the exact same content.
            if item._compare(existing_item := self._items[primary_key], ignore_fields):
                # Ignore identical item.
                return
            raise AristaAvdDuplicateDataError(type(self).__name__, str(item), str(existing_item))

        self._items[primary_key] = item

    if TYPE_CHECKING:
        append_new: type[T_AvdModel]

    else:

        def append_new(self, *args: Any, **kwargs: Any) -> T_AvdModel:
            """
            Create a new instance with the given arguments and append to the list.

            Returns the new item, or in case of an identical duplicate item it returns the existing item.
            """
            new_item = self._item_type(*args, **kwargs)
            self.append(new_item)
            return self._items[kwargs[self._primary_key]]

    def extend(self, items: Iterable[T_AvdModel]) -> None:
        self._items.update({getattr(item, self._primary_key): item for item in items})

    def _strip_empties(self) -> None:
        """In-place update the instance to remove data matching the given strip_values."""
        [item._strip_empties() for item in self._items.values()]
        self._items = {primary_key: item for primary_key, item in self._items.items() if item}

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

    def _deepmerge(self, other: Self, list_merge: Literal["append_unique", "append", "replace", "keep", "prepend", "prepend_unique"] = "append_unique") -> None:
        """
        Update instance by deepmerging the other instance in.

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
            # Clear the flag and set list_merge to replace so we overwrite with data from other below.
            self._created_from_null = other._created_from_null
            list_merge = "replace"

        match list_merge:
            case "replace":
                # Replace with the "other" list.
                self._items = other._items.copy()
                return
            case "keep":
                # We only get here if there was a defined instance of the old list, so we "keep" the existing list as-is.
                return
            case _:
                # For the other strategies we need to merge on primary key for existing items and otherwise append/prepend.
                # There is no difference for _unique for indexed lists since it can only hold one item per primary key.
                pass

        prepend_items = {}
        for primary_key, new_item in other.items():
            if new_item._created_from_null:
                # Remove the complete item when merging in a Null item.
                self._items.pop(primary_key, None)
                continue

            if self.get(primary_key) is Undefined:
                # New item so we can just append/prepend.
                if list_merge.startswith("prepend"):
                    # Prepending requires us to rebuild the internal dict to maintain the correct order.
                    # We do that at the end to maintain the order of <new-list> + <old-list>. If we prepended per item we would reverse the new list.
                    prepend_items[primary_key] = new_item
                    continue

                # Appending the new item.
                self[primary_key] = new_item
                continue

            # Existing item of same type, so deepmerge.
            self[primary_key]._deepmerge(new_item, list_merge=list_merge)

        if prepend_items:
            self._items = {**prepend_items, **self._items}

    def _deepinherit(self, other: Self) -> None:
        """Update instance by recursively inheriting from other instance for all existing items. New items are *not* added."""
        cls = type(self)
        if not isinstance(other, cls):
            msg = f"Unable to inherit from type '{type(other)}' into '{cls}'"
            raise TypeError(msg)

        if self._created_from_null or self._block_inheritance:
            # Null always wins, so no inheritance.
            return

        if other._created_from_null:
            # Nothing to inherit, and we set the special block flag to prevent inheriting from something else later.
            self._block_inheritance = True
            return

        for primary_key, new_item in other.items():
            if self.get(primary_key) is Undefined:
                # New item so we can just append
                self[primary_key] = new_item
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

        new_instance = new_type([item._cast_as(new_type._item_type, ignore_extra_keys=ignore_extra_keys) for item in self])

        # Pass along the internal flags
        new_instance._created_from_null = self._created_from_null
        new_instance._block_inheritance = self._block_inheritance
        # Copy the source
        new_instance._source = self._source

        return new_instance
