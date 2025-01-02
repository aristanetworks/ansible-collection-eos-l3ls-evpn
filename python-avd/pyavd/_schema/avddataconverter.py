# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pyavd._errors import AvdDeprecationWarning
from pyavd._utils import get, get_all

from .utils import get_instance_with_defaults

SCHEMA_TO_PY_TYPE_MAP = {
    "str": str,
    "int": int,
    "bool": bool,
    "float": float,
    "dict": dict,
    "list": list,
}
SIMPLE_CONVERTERS = {
    "str": str,
    "int": int,
    "bool": bool,
}

if TYPE_CHECKING:
    from collections.abc import Generator


class AvdDataConverter:
    """AvdDataConverter is used to convert AVD Data Types based on schema options."""

    def __init__(self, schema: dict) -> None:
        self.schema = schema

        # We run through all the regular keys first, to ensure that all data has been converted
        # in case some of it is referenced in "dynamic_keys" below
        self.converters = {
            "items": self.convert_items,
            "keys": self.convert_keys,
            "dynamic_keys": self.convert_dynamic_keys,
            "deprecation": self.deprecation,
        }

    def convert_data(self, data: Any, schema: dict | None = None, path: list[str | int] | None = None, parent_dict: dict | None = None) -> Generator:
        """
        Perform in-place conversion of data according to the provided schema.

        Main entry function which is recursively called from the child functions performing the actual conversion of keys/items.
        """
        if schema is None:
            schema = self.schema
        if path is None:
            path = []

        for key, converter in self.converters.items():
            if key not in schema:
                # Ignore keys not in schema
                continue

            # Converters will do inplace update of data. Any returns will be yielded conversion messages.
            yield from converter(schema[key], data, schema, path, parent_dict)

    def convert_keys(self, keys: dict, data: dict, _schema: dict, path: list[str | int], _parent_dict: dict | None) -> Generator:
        """This function performs conversion on each key with the relevant subschema."""
        if not isinstance(data, dict):
            return

        for key, childschema in keys.items():
            if key not in data:
                # Skip key since there is nothing to convert if the key is not set in data
                continue

            # Perform type conversion of the data for the child key if required based on "convert_types"
            if "convert_types" in childschema:
                self.convert_types(childschema["convert_types"], data, key, childschema, [*path, key])

            # Convert to lower case if set in schema and value is a string
            if childschema.get("convert_to_lower_case") and isinstance(data[key], str):
                data[key] = data[key].lower()

            yield from self.convert_data(data[key], childschema, [*path, key], data)

    def convert_dynamic_keys(self, dynamic_keys: dict, data: dict, schema: dict, path: list[str | int], parent_dict: dict | None) -> Generator:
        """
        This function resolves "dynamic_keys" by looking in the actual data.

        Then calls convert_keys to performs conversion on each resolved key with the relevant subschema.
        """
        if not isinstance(data, dict):
            return

        # Resolve "keys" from schema "dynamic_keys" by looking for the dynamic key in data.
        keys = {}
        for dynamic_key, childschema in dynamic_keys.items():
            data_with_defaults = get_instance_with_defaults(data, dynamic_key, schema)
            resolved_keys = get_all(data_with_defaults, dynamic_key)
            for resolved_key in resolved_keys:
                keys.setdefault(resolved_key, childschema)

        # Reuse convert_keys to perform the actual conversion on the resolved dynamic keys
        yield from self.convert_keys(keys, data, schema, path, parent_dict)

    def convert_items(self, items: dict, data: list, _schema: dict, path: list[str | int], parent_dict: dict | None) -> Generator:
        """This function performs conversion on each item with the items subschema."""
        if not isinstance(data, list):
            return

        for index, item in enumerate(data):
            # Perform type conversion of the items data if required based on "convert_types"
            if "convert_types" in items:
                self.convert_types(items["convert_types"], data, index, items, [*path, index])

            # Convert to lower case if set in schema and item is a string
            if items.get("convert_to_lower_case") and isinstance(item, str):
                data[index] = item.lower()

            # Dive in to child items/schema
            yield from self.convert_data(item, items, [*path, index], parent_dict)

    def convert_types(self, convert_types: list, data: dict | list, index: str | int, schema: dict, _path: list[str | int]) -> None:
        """
        This function performs type conversion if necessary on a single data instance.

        It is invoked for child keys during "keys" conversion and for child items during
        "items" conversion.

        "data" is either the parent dict or the parent list.
        "index" is either the key of the parent dict or the index of the parent list.

        Conversion is performed in-place using the provided "data" and "index"

        Any conversion errors are ignored and the original value is returned
        """
        schema_type = schema.get("type")

        # Get value from input data
        value = data[index]

        # For simple conversions, skip conversion if the value is of the correct type
        # Avoid corner case where we want to convert bool to int. Bool is a subclass of Int so it passes the check above.
        if (
            schema_type in SIMPLE_CONVERTERS
            and isinstance(value, SCHEMA_TO_PY_TYPE_MAP.get(schema_type))
            and not (schema_type == "int" and isinstance(value, bool))
        ):
            return

        for convert_type in convert_types:
            if isinstance(value, SCHEMA_TO_PY_TYPE_MAP.get(convert_type)) and schema_type in SIMPLE_CONVERTERS:
                try:
                    data[index] = SIMPLE_CONVERTERS[schema_type](value)
                except Exception:  # pylint: disable=broad-exception-caught
                    # Ignore errors
                    # TODO: Log message
                    return

    def deprecation(
        self, deprecation: dict, _data: Any, _schema: dict, path: list[str | int], parent_dict: dict | None
    ) -> Generator[AvdDeprecationWarning, None, None]:
        """
        deprecation.

          warning: bool, default = True
          new_key: str
          removed: bool
          remove_in_version: str
          remove_after_date: str
          url: str

            Yields AvdDeprecationWarning

        """
        if not deprecation.get("warning", True):
            return

        new_key = deprecation.get("new_key")
        removed = deprecation.get("removed", False)

        # If new_key set, we can check for collision where both new and old key are set.
        # If we have a space in the new_key, we will skip the check and just produce the deprecation warning with new_key.
        # New key is assumed to be relative to the parent dict.
        conflict = False
        if not removed and new_key and parent_dict is not None:
            for one_new_key in new_key.split(" or "):
                if " " in one_new_key:
                    continue
                if get(parent_dict, one_new_key) is not None:
                    conflict = True
                    # Overriding new_key to direct the error message to the relevant key in case the original new_key contained multiple keys.
                    new_key = one_new_key
                    break

        deprecation_warning = AvdDeprecationWarning(
            key=path,
            new_key=new_key,
            remove_in_version=deprecation.get("remove_in_version"),
            remove_after_date=deprecation.get("remove_after_date"),
            url=deprecation.get("url"),
            removed=removed,
            conflict=conflict,
        )

        yield deprecation_warning
