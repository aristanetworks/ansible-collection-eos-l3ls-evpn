# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections import ChainMap
from collections.abc import Generator
from re import fullmatch, match
from typing import Any, Literal, NoReturn

from pyavd._errors import AvdValidationError
from pyavd._utils import get_all, get_all_with_path, get_indices_of_duplicate_items

from .utils import get_instance_with_defaults


class AvdValidator:
    def __init__(self, schema: dict) -> None:
        self.schema = schema
        self.validators = {
            # Note type_validator is not included here since we first check that before spending energy on the rest
            "max": self.max_validator,
            "min": self.min_validator,
            "max_length": self.max_length_validator,
            "min_length": self.min_length_validator,
            "format": self.format_validator,
            "pattern": self.pattern_validator,
            "valid_values": self.valid_values_validator,
            "keys": self.keys_validator,
            "dynamic_keys": self.dynamic_keys_validator,
            "items": self.items_validator,
            "primary_key": self.primary_key_validator,
            "unique_keys": self.unique_keys_validator,
            "$ref": self.ref_validator,
        }

    def validate(self, instance: Any, schema: dict | None = None, path: list[str | int] | None = None) -> Generator:
        if schema is None:
            schema = self.schema
        if path is None:
            path = []

        type_errors = list(self.type_validator(schema["type"], instance, schema, path))
        if type_errors:
            yield from (type_error for type_error in type_errors)
            # Skip further validation since the type is wrong.
            return

        for schema_key, schema_value in schema.items():
            if (validator := self.validators.get(schema_key)) is None or schema_value is None:
                continue
            yield from validator(schema_value, instance, schema, path)

    def type_validator(self, schema_type: str, instance: Any, _schema: dict, path: list[str | int]) -> Generator:
        if not self.is_type(instance, schema_type):
            yield AvdValidationError(
                f"Invalid type '{type(instance).__name__}'. Expected a '{schema_type}'.",
                path=path,
            )

    def unique_keys_validator(self, unique_keys: list[str], instance: list, _schema: dict, path: list[str | int]) -> Generator:
        if not instance:
            return

        if not all(self.is_type(element, "dict") for element in instance):
            return

        for unique_key in unique_keys:
            if not (paths_and_values := tuple(get_all_with_path(instance, unique_key))):
                # No values matching the unique key, check the next unique_key
                continue

            # Separate all paths and values
            paths, values = zip(*paths_and_values, strict=False)

            key = unique_key.split(".")[-1]
            is_nested_key = unique_key != key

            # Find any duplicate values and emit errors for each index.
            for duplicate_value, duplicate_indices in get_indices_of_duplicate_items(values):
                for duplicate_index in duplicate_indices:
                    yield AvdValidationError(
                        f"The value '{duplicate_value}' is not unique between all {'nested ' if is_nested_key else ''}list items as required.",
                        path=[*path, *paths[duplicate_index], key],
                    )

    def primary_key_validator(self, primary_key: str, instance: list, schema: dict, path: list[str | int]) -> Generator:
        if not instance:
            return

        if not all(self.is_type(element, "dict") for element in instance):
            return

        if not all(element.get(primary_key) is not None for element in instance):
            yield AvdValidationError(f"Primary key '{primary_key}' is not set on all items as required.", path=path)

        if not schema.get("allow_duplicate_primary_key"):
            # Reusing the unique keys validator
            yield from self.unique_keys_validator([primary_key], instance, schema, path)

    def keys_validator(self, keys: dict, instance: dict, schema: dict, path: list[str | int]) -> Generator:
        """
        This function validates each key with the relevant subschema.

        It also includes various child key validations,
        which can only be implemented with access to the parent "keys" instance.
        - Expand dynamic_keys
        - Validate "allow_other_keys" (default is false)
        - Validate "required" under child keys
        - Expand "dynamic_valid_values" under child keys (don't perform validation).
        """
        # Compile schema_dynamic_keys and add to "dynamic_keys"
        schema_dynamic_keys = schema.get("dynamic_keys", {})
        dynamic_keys = {}
        for dynamic_key, childschema in schema_dynamic_keys.items():
            instance_with_defaults = get_instance_with_defaults(instance, dynamic_key, schema)
            resolved_keys = get_all(instance_with_defaults, dynamic_key)
            for resolved_key in resolved_keys:
                dynamic_keys.setdefault(resolved_key, childschema)

        all_keys = ChainMap(keys, dynamic_keys)

        # Validation of "allow_other_keys"
        if not schema.get("allow_other_keys", False):
            # Check that instance only contains the schema keys
            invalid_keys = ", ".join([key for key in instance if key not in all_keys and key[0] != "_"])
            if invalid_keys:
                yield AvdValidationError(f"Unexpected key(s) '{invalid_keys}' found in dict.", path=path)

        # Run over child keys and check for required and update child schema with dynamic valid values before
        # descending into validation of child schema.
        for key in all_keys:
            childschema = all_keys[key].copy()
            if instance.get(key) is None:
                # Validation of "required" on child keys
                if childschema.get("required"):
                    yield AvdValidationError(f"Required key '{key}' is not set in dict.", path=path)

                # Skip further validation since there is nothing to validate.
                continue

            # Expand "dynamic_valid_values" in child schema and add to "valid_values"
            if "dynamic_valid_values" in childschema:
                for dynamic_valid_value in childschema["dynamic_valid_values"]:
                    instance_with_defaults = get_instance_with_defaults(instance, dynamic_valid_value, schema)
                    childschema.setdefault("valid_values", []).extend(get_all(instance_with_defaults, dynamic_valid_value))

            # Perform regular validation of the child schema.
            yield from self.validate(
                instance[key],
                childschema,
                path=[*path, key],
            )

    def dynamic_keys_validator(self, _dynamic_keys: dict, instance: dict, schema: dict, path: list[str | int]) -> Generator:
        """This function triggers the regular "keys" validator in case only dynamic_keys is set."""
        if "keys" not in schema:
            yield from self.keys_validator({}, instance, schema, path=path)

    def items_validator(self, items: dict, instance: list, _schema: dict, path: list[str | int]) -> Generator:
        for index, item in enumerate(instance):
            yield from self.validate(item, items, path=[*path, index])

    def ref_validator(self, _ref: str, _instance: dict, _schema: dict, _path: list[str | int]) -> NoReturn:
        msg = "$ref must be resolved before using AvdValidator"
        raise NotImplementedError(msg)

    def max_validator(self, schema_max: int, instance: int, _schema: dict, path: list[str | int]) -> Generator:
        if instance > schema_max:
            yield AvdValidationError(f"'{instance}' is higher than the allowed maximum of {schema_max}.", path=path)

    def min_validator(self, schema_min: int, instance: int, _schema: dict, path: list[str | int]) -> Generator:
        if instance < schema_min:
            yield AvdValidationError(f"'{instance}' is lower than the allowed minimum of {schema_min}.", path=path)

    def max_length_validator(self, schema_max_length: int, instance: str | list, _schema: dict, path: list[str | int]) -> Generator:
        if len(instance) > schema_max_length:
            yield AvdValidationError(f"The value is longer ({len(instance)}) than the allowed maximum of {schema_max_length}.", path=path)

    def min_length_validator(self, schema_min_length: int, instance: str | list, _schema: dict, path: list[str | int]) -> Generator:
        if len(instance) < schema_min_length:
            yield AvdValidationError(f"The value is shorter ({len(instance)}) than the allowed minimum of {schema_min_length}.", path=path)

    def valid_values_validator(self, valid_values: list, instance: Any, _schema: dict, path: list[str | int]) -> Generator:
        """This function validates if the instance conforms to the "valid_values"."""
        if instance not in valid_values:
            yield AvdValidationError(f"'{instance}' is not one of {valid_values}", path=path)

    def format_validator(self, schema_format: str, instance: str, _schema: dict, path: list[str | int]) -> Generator:
        match schema_format:
            case "ipv4":
                # TODO: Figure out how to do this efficiently since ipaddress is slow
                return
            case "ipv4_cidr":
                # TODO: Figure out how to do this efficiently since ipaddress is slow
                return
            case "ipv6":
                # TODO: Figure out how to do this efficiently since ipaddress is slow
                return
            case "ipv6_cidr":
                # TODO: Figure out how to do this efficiently since ipaddress is slow
                return
            case "ip":
                # TODO: Figure out how to do this efficiently since ipaddress is slow
                return
            case "cidr":
                # TODO: Figure out how to do this efficiently since ipaddress is slow
                return
            case "mac":
                # Matching for format 01:23:45:67:89:AB
                if fullmatch(r"([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}|([0-9a-fA-F]{4}.){2}[0-9a-fA-F]{4}", instance) is None:
                    yield AvdValidationError(
                        f"The value '{instance}' is not a valid MAC address (Expecting bytes separated by colons like 01:23:45:67:89:AB).", path=path
                    )

    def pattern_validator(self, pattern: str, instance: str, _schema: dict, path: list[str | int]) -> Generator:
        if match(pattern, instance) is None:
            yield AvdValidationError(f"The value '{instance}' is not matching the pattern '{pattern}'.", path=path)

    def is_type(self, instance: Any, type_str: Literal["dict", "int", "str", "bool"]) -> bool:
        match type_str:
            case "int":
                return isinstance(instance, int)
            case "str":
                return isinstance(instance, str)
            case "bool":
                return isinstance(instance, bool)
            case "dict":
                return isinstance(instance, (dict, ChainMap))
            case "list":
                return isinstance(instance, list)

        msg = f"Unable to check type '{type_str}'"
        raise NotImplementedError(msg)
