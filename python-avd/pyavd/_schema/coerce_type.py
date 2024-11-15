# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any, NoReturn, TypeVar

from pyavd._schema.models.avd_base import AvdBase

from .constants import ACCEPTED_COERCION_MAP

if TYPE_CHECKING:
    from typing import TypeVar

    from pyavd._schema.models.type_vars import T_AvdBase

    T = TypeVar("T")


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


def coerce_type(value: Any, target_type: type[T]) -> T | None:
    """
    Return a coerced variant of the given value to the target_type.

    If the value is already of the correct type the value will be returned untouched.

    If coercion cannot be done this will raise a TypeError.
    """
    if value is None:
        if issubclass(target_type, AvdBase):
            # None values are sometimes used to overwrite inherited profiles.
            # This ensures we still follow the type hint of the class.
            return nullifiy_class(target_type)()

        # Other None values are left untouched.
    elif target_type is Any or isinstance(value, target_type):
        pass

    elif target_type in ACCEPTED_COERCION_MAP and isinstance(value, ACCEPTED_COERCION_MAP[target_type]):
        try:
            return target_type(value)
        except ValueError as exception:
            raise_coerce_error(value, target_type, exception)

    # Identify subclass of AvdModel without importing AvdModel (circular import)
    elif issubclass(target_type, AvdBase):
        try:
            return target_type._load(data=value)
        except TypeError as exception:
            raise_coerce_error(value, target_type, exception)

    else:
        raise_coerce_error(value, target_type)

    # All the pass brings us here to return the original value.
    return value


def raise_coerce_error(value: Any, target_type: type, exception: Exception | None = None) -> NoReturn:
    # Not possible to coerce value.
    msg = f"Invalid type '{type(value)}'. Unable to coerce to type '{target_type}' for the value: {value}"
    if exception is not None:
        raise TypeError(msg) from exception
    raise TypeError(msg)
