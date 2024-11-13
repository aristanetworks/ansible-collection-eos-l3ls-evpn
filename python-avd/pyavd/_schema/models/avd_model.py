# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, ClassVar, Literal

from pyavd._schema.coerce_type import coerce_type
from pyavd._utils import Undefined

from .avd_base import AvdBase
from .avd_indexed_list import AvdIndexedList

if TYPE_CHECKING:
    from typing_extensions import Self

    from .type_vars import T_AvdModel


class AvdModel(AvdBase):
    _is_avd_model = True
    _allow_other_keys: bool = False
    _fields: ClassVar[dict[str, dict]]
    _required_fields: ClassVar[tuple[str, ...]]
    _field_to_key_map: ClassVar[dict[str, str]]
    """Map of field name to original dict key. Used when fields have the field_ prefix to get the original key."""
    _key_to_field_map: ClassVar[dict[str, str]]
    """Map of dict key to field name. Used when the key is names with a reserved keyword or mixed case. E.g. `Vxlan1` or `as`."""

    @classmethod
    def _from_dict(cls: type[T_AvdModel], data: Mapping, keep_extra_keys: bool = False) -> T_AvdModel:
        """
        Returns a new instance loaded with the data from the given dict.

        TODO: AVD6.0.0 remove the keep_extra_keys option so we no longer support custom keys without _ in structured config.
        """
        if not isinstance(data, Mapping):
            msg = f"Expecting 'data' as a 'Mapping' when loading data into '{cls.__name__}'. Got '{type(data)}"
            raise TypeError(msg)

        has_custom_data = "_custom_data" in cls._fields
        cls_args = {}

        for key in data:
            if not (field := cls._get_field_name(key)):
                if keep_extra_keys or (has_custom_data and str(key).startswith("_")):
                    cls_args.setdefault("_custom_data", {})[key] = data[key]
                    continue

                if cls._allow_other_keys:
                    # Ignore unknown keys.
                    continue

                msg = f"Invalid key '{key}'. Not available on '{cls.__name__}'."
                raise KeyError(msg)

            field_info = cls._fields[field]
            field_type = field_info["type"]

            value = coerce_type(data[key], field_type, list_items_type=field_info.get("items"))

            # Raise for wrong type ignoring None values - we expect the validation to have sorted out required fields.
            if value is not None and not isinstance(value, field_type):
                msg = f"Invalid type '{type(value)}. Expected '{field_type}'. Value '{value}"
                raise TypeError(msg)

            cls_args[field] = value

        return cls(**cls_args)

    @classmethod
    def _get_field_name(cls, key: str) -> str | None:
        """Returns the field name for the given key. Returns None if the key is not matching a valid field."""
        field_name = cls._key_to_field_map.get(key, key)
        return field_name if field_name in cls._fields else None

    @classmethod
    def _get_field_default_value(cls, name: str) -> Any:
        """
        Returns the default value for a field.

        We check for a default value in the _fields information and if something is there we return that.
        - For dicts, AvdModel and lists of AvdModels subclasses the default value is a callable to generate a new instance to avoid reusing a mutable object.
        - For lists of simple types like 'list[str]' the default value is a list that is copied to avoid reusing a mutable object.
        - For other types, which are immutable, the default value is taken directly.

        If there is no default value in the field info, we return the default-default depending on type.
        - For lists and dicts we return new empty list / dict.
        - For AvdModel subclasses we return a new empty instance of the class.
        - For other types we return None.
        """
        if name not in cls._fields:
            raise AttributeError("'" + cls.__name__ + "' object has no attribute '" + name + "'")
        field_info = cls._fields[name]
        field_type: type = field_info["type"]
        if field_type is list:
            if (default_value_or_function := field_info.get("default")) is None:
                return []
            if isinstance(default_value_or_function, list):
                # Create a new list
                return default_value_or_function.copy()

            # Callable default value.
            return default_value_or_function(field_info["items"])

        if issubclass(field_type, AvdBase) or field_type is dict:
            return default_function(field_type) if (default_function := field_info.get("default")) else field_type()

        return field_info.get("default")

    def __getattr__(self, name: str) -> Any:
        """
        Resolves the default value for a field, set the default value on the attribute and return the value.

        We only get here if the attribute is not set already, and next call will skip this since the attribute is set.
        """
        if name not in self._fields:
            raise AttributeError("'" + self.__class__.__name__ + "' object has no attribute '" + name + "'")

        default_value = self._get_field_default_value(name)
        setattr(self, name, default_value)
        return default_value

    def _get_defined_attr(self, name: str) -> Any | Undefined:
        """
        Get attribute or Undefined.

        Avoids the overridden __getattr__ to avoid default values.
        """
        if name not in self._fields:
            raise AttributeError("'" + self.__class__.__name__ + "' object has no attribute '" + name + "'")
        try:
            return self.__getattribute__(name)
        except AttributeError:
            return Undefined

    def __repr__(self) -> str:
        """Returns a repr with all the fields that are set including any nested models."""
        cls_name = self.__class__.__name__
        attrs = [f"{key}={getattr(self, key)!r}" for key in self._fields if self._get_defined_attr(key) is not Undefined]
        return f"<{cls_name}({', '.join(attrs)})>"

    def __bool__(self) -> bool:
        """
        Boolean check on the class to quickly determine if any parameter is set.

        Note that a falsy value will still make this True.

        The check ignores the default values and is performed recursively on any nested models.
        """
        return any(
            # First item going through the checks below will trigger the any.
            True
            for field in self._fields
            # Skipping item if Undefined
            if (value := self._get_defined_attr(field)) is not Undefined
            # Skipping value if it is not an AVD class or if it _is_ an AVD class with a falsy value
            and not (hasattr(value, "_is_avd_class") and not value)
        )

    def _as_dict(self, include_default_values: bool = False) -> dict:
        """
        Returns a dict with all the data from this model and any nested models.

        Filtered for nested None, {} and [] values.
        """
        as_dict = {}
        for field, field_info in self._fields.items() or ():
            if (value := self._get_defined_attr(field)) is Undefined:
                if not include_default_values:
                    continue

                value = self._get_field_default_value(field)
                if value in (None, [], {}):
                    continue

            if field == "_custom_data" and isinstance(value, dict) and value:
                as_dict.update(value)
                continue

            # Removing field_ prefix if needed.
            key = self._field_to_key_map.get(field, field)

            if issubclass(field_info["type"], AvdModel) and isinstance(value, AvdModel):
                value = value._as_dict(include_default_values=include_default_values)
                if value == {}:  # Keeping None values for nullified dicts.
                    continue
            elif issubclass(field_info["type"], AvdIndexedList) and isinstance(value, AvdIndexedList):
                value = value._as_list(include_default_values=include_default_values)
                if value == []:  # Keeping None values for nullified list.
                    continue

            elif field_info["type"] is list and isinstance(value, list):
                if issubclass(field_info["items"], AvdModel):
                    value = [item._as_dict(include_default_values=include_default_values) for item in value if isinstance(item, AvdModel)]
                elif issubclass(field_info["items"], AvdIndexedList):
                    value = [item._as_list(include_default_values=include_default_values) for item in value if isinstance(item, AvdIndexedList)]

            as_dict[key] = value

        return as_dict

    def _get(self, name: str, default: Any = None) -> Any:
        """
        Behave like dict.get() to get a field value only if set.

        This will not insert a default values and will return the default value (or None) if not set.
        """
        if (value := self._get_defined_attr(name)) is Undefined:
            return default
        return value

    def _update(self, other: Self) -> None:
        """Update instance by shallow merging the other instance in."""
        cls = type(self)
        if not isinstance(other, cls):
            msg = f"Unable to merge type '{type(other)}' into '{cls}'"
            raise TypeError(msg)

        for field in cls._fields:
            if new_value := other._get_defined_attr(field) is Undefined:
                continue
            old_value = self._get_defined_attr(field)
            if old_value == new_value:
                continue
            setattr(self, field, new_value)

    def _deepmerge(self, other: Self, list_merge: Literal["append", "replace"] = "append") -> None:
        """Update instance by deepmerging the other instance in."""
        cls = type(self)
        if not isinstance(other, cls):
            msg = f"Unable to merge type '{type(other)}' into '{cls}'"
            raise TypeError(msg)

        copy_of_other = other._deepcopy()
        for field, field_info in cls._fields.items():
            if (new_value := copy_of_other._get_defined_attr(field)) is Undefined:
                continue
            old_value = self._get_defined_attr(field)
            if old_value == new_value:
                continue

            if not isinstance(old_value, type(new_value)):
                # Different type so we can just replace
                setattr(self, field, new_value)
                continue

            # Merge new value
            field_type = field_info["type"]
            if field_type is list and list_merge == "append":
                setattr(self, field, old_value + new_value)
            elif issubclass(field_type, (AvdModel, AvdIndexedList)) and isinstance(old_value, field_type):
                # Merge in to the existing object
                old_value._deepmerge(new_value, list_merge=list_merge)
            else:
                setattr(self, field, new_value)

    def _deepmerged(self, other: Self, list_merge: Literal["append", "replace"] = "append") -> Self:
        """Return new instance with the result of the deepmerge of "other" on this instance."""
        new_instance = self._deepcopy()
        new_instance._deepmerge(other=other, list_merge=list_merge)
        return new_instance

    def _inherit(self, other: Self) -> None:
        """Update unset fields on this instance with fields from other instance. No merging."""
        cls = type(self)
        if not isinstance(other, cls):
            msg = f"Unable to inherit from type '{type(other)}' into '{cls}'"
            raise TypeError(msg)

        copy_of_other = other._deepcopy()
        for field in cls._fields:
            if self._get_defined_attr(field) is not Undefined:
                continue
            if (new_value := copy_of_other._get_defined_attr(field)) is Undefined:
                continue

            setattr(self, field, new_value)

    def _deepinherit(self, other: Self) -> None:
        """Update instance by recursively inheriting unset fields from other instance. Lists are not merged."""
        cls = type(self)
        if not isinstance(other, cls):
            msg = f"Unable to inherit from type '{type(other)}' into '{cls}'"
            raise TypeError(msg)

        copy_of_other = other._deepcopy()
        for field, field_info in cls._fields.items():
            if (new_value := copy_of_other._get_defined_attr(field)) is Undefined:
                continue
            old_value = self._get_defined_attr(field)
            if old_value == new_value:
                continue

            # Merge new value if it is a class.
            field_type = field_info["type"]
            if issubclass(field_type, (AvdModel, AvdIndexedList)) and isinstance(old_value, field_type):
                # Inherit into the existing object.
                old_value._deepinherit(new_value)

            # Inherit the field only if the old value is Undefined, otherwise ignore.
            if old_value is Undefined:
                setattr(self, field, new_value)

    def _deepinherited(self, other: Self) -> Self:
        """Return new instance with the result of recursively inheriting unset fields from other instance. Lists are not merged."""
        new_instance = self._deepcopy()
        new_instance._deepinherit(other=other)
        return new_instance

    def _cast_as(self, new_type: type[T_AvdModel], ignore_extra_keys: bool = False) -> T_AvdModel:
        """
        Recast a class instance as another AvdModel subclass if they are compatible.

        The classes are compatible if the fields of the new class is a superset of the current class.
        Unset fields are ignored when evaluating compatibility.

        Useful when inheriting from profiles.
        """
        cls = type(self)
        if not issubclass(new_type, AvdModel):
            msg = f"Unable to cast '{cls}' as type '{new_type}' since '{new_type}' is not an AvdModel subclass."
            raise TypeError(msg)

        new_args = {}
        for field, field_info in cls._fields.items():
            if (value := self._get_defined_attr(field)) is Undefined:
                continue
            if field not in new_type._fields:
                if ignore_extra_keys:
                    continue
                msg = f"Unable to cast '{cls}' as type '{new_type}' since the field '{field}' is missing from the new class. "
                raise TypeError(msg)
            if field_info != new_type._fields[field]:
                if field_info["type"] is list and issubclass(field_info["items"], (AvdModel, AvdIndexedList)) and isinstance(value, list):
                    # TODO: Consider using the TypeError we raise below to ensure we know the outer type.
                    # TODO: with suppress(TypeError):
                    new_args[field] = [
                        item._cast_as(new_type._fields[field]["items"], ignore_extra_keys=ignore_extra_keys)
                        for item in value
                        if isinstance(item, (AvdModel, AvdIndexedList))
                    ]
                    continue

                if issubclass(field_info["type"], (AvdModel, AvdIndexedList)) and isinstance(value, (AvdModel, AvdIndexedList)):
                    # TODO: Consider using the TypeError we raise below to ensure we know the outer type.
                    # TODO: with suppress(TypeError):
                    new_args[field] = value._cast_as(new_type._fields[field]["type"], ignore_extra_keys=ignore_extra_keys)
                    continue

                msg = f"Unable to cast '{cls}' as type '{new_type}' since the field '{field}' is incompatible. Value {value}"
                raise TypeError(msg)

            new_args[field] = value
            continue

        return new_type(**new_args)
