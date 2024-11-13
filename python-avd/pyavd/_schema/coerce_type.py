# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any, TypeVar

from .constants import ACCEPTED_COERCION_MAP

if TYPE_CHECKING:
    from typing import TypeVar

    from pyavd._schema.models.type_vars import T_AvdBase

    T = TypeVar("T")
    TT = TypeVar("TT")


def nullifiy_class(cls: type[T_AvdBase]) -> type:
    """
    Returns a subclass of the given class with overrides for "null" values.

    This class is used when the input for a dict or a list is None/null/none,
    to be able to signal to the deepmerge/inherit methods that this is not the same as an unset variable.
    """

    class NullifiedCls(cls):
        def _as_dict(self, *_args: Any, **_kwargs: Any) -> None:
            return None

        def _as_list(self, *_args: Any, **_kwargs: Any) -> None:
            return None

        def __repr__(self) -> str:
            return f"<NullifiedCls[{cls.__name__}]>"

        def _deepinherit(self, _other: T_AvdBase, *_args: Any, **_kwargs: Any) -> None:
            pass

        def _inherit(self, _other: T_AvdBase, *_args: Any, **_kwargs: Any) -> None:
            pass

        def _deepmerge(self, other: T_AvdBase, *_args: Any, **_kwargs: Any) -> T_AvdBase:
            return other._deepcopy()

    return NullifiedCls


def coerce_type(value: Any, target_type: type[T], list_items_type: type[TT] | None = None) -> T | list[TT]:
    """
    Return a coerced variant of the given value to the target_type or for lists a list of the the list_items_type.

    If the value is already of the correct type the value will be returned untouched.

    If coercion cannot be done, the original value will be returned. The calling function should catch the wrong type if necessary.
    """
    if value is None and (target_type is list or hasattr(target_type, "_is_avd_class")):
        # None values are sometimes used to overwrite inherited profiles.
        # This ensures we still follow the type hint of the class.
        return nullifiy_class(target_type)()

    # Special handling for lists since we need to check every item
    if target_type is list:
        if not isinstance(value, list) or list_items_type is None:
            # Wrong type so we cannot coerce or just expecting a plain list so nothing to coerce.
            return value

        # We got a type with items types like list[str] so we coerce every list item accordingly and return as a new list.
        return [coerce_type(item_value, list_items_type) for item_value in value]

    if target_type is Any or isinstance(value, target_type):
        pass

    elif target_type in ACCEPTED_COERCION_MAP and isinstance(value, ACCEPTED_COERCION_MAP[target_type]):
        try:
            return target_type(value)
        except ValueError:
            # Returns original value (too many returns triggers linting violation)
            pass

    # Identify subclass of AvdModel without importing AvdModel (circular import)
    elif hasattr(target_type, "_is_avd_model") and isinstance(value, Mapping):
        return target_type._from_dict(value)

    # Identify subclass of AvdIndexedList without importing AvdIndexedList (circular import)
    elif hasattr(target_type, "_is_avd_collection") and isinstance(value, Sequence):
        return target_type._from_list(value)

    # Giving up and just returning the original value.
    return value
