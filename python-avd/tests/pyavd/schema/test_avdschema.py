# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from typing import Any

import pytest
import yaml
from deepmerge import always_merger

from pyavd._errors import AvdValidationError
from pyavd._schema.avdschema import DEFAULT_SCHEMA, AvdSchema

script_dir = Path(__file__).parent
with Path(script_dir, "access_lists.schema.yml").open(encoding="utf-8") as schema_file:
    acl_schema = yaml.load(schema_file, Loader=yaml.CSafeLoader)
with Path(script_dir, "ipv6_standard_access_lists.schema.yml").open(encoding="utf-8") as schema_file:
    ipv6_acl_schema = yaml.load(schema_file, Loader=yaml.CSafeLoader)
with Path(script_dir, "combined.schema.yml").open(encoding="utf-8") as schema_file:
    combined_schema = yaml.load(schema_file, Loader=yaml.CSafeLoader)
with Path(script_dir, "acl.yml").open(encoding="utf-8") as data_file:
    acl_test_data = yaml.load(data_file, Loader=yaml.CSafeLoader)
with Path(script_dir, "ipv6-access-lists.yml").open(encoding="utf-8") as data_file:
    ipv6_acl_test_data = yaml.load(data_file, Loader=yaml.CSafeLoader)

VALID_TEST_SCHEMAS = [DEFAULT_SCHEMA, acl_schema, ipv6_acl_schema, combined_schema]

combined_data = {}
always_merger.merge(combined_data, acl_test_data)
always_merger.merge(combined_data, ipv6_acl_test_data)

TEST_DATA_SETS = [{}, acl_test_data, ipv6_acl_test_data, combined_data]

TEST_DATA_PATHS = [
    [],
    ["access_lists", "name"],
    ["access_lists", "sequence_numbers", "action"],
]

# Expected responses for .subschema() when tested with TEST_DATA_PATHS
EXPECTED_SUBSCHEMAS = {
    "_empty": combined_schema,
    "access_lists.name": acl_schema["keys"]["access_lists"]["items"]["keys"]["name"],
    "access_lists.sequence_numbers.action": acl_schema["keys"]["access_lists"]["items"]["keys"]["sequence_numbers"]["items"]["keys"]["action"],
}

# Testing invalid data for "access-lists" data model
INVALID_ACL_DATA = [
    # Wrong data type (string instead of dict)
    "String",
    # Wrong data type (None instead of dict)
    None,
    # Wrong item type (None instead of dict)
    {"access_lists": [None]},
    # Missing Multiple Required keys ("name", "sequence_numbers")
    {"access_lists": [{}]},
    # Missing One Required key ("sequence_numbers")
    {"access_lists": [{"name": "name"}]},
    # Wrong type for deeply nested key (int instead of str)
    {"access_lists": [{"name": "name", "sequence_numbers": [{"sequence": 10, "action": 123}]}]},
    # Unexpected key (extra_key)
    {"access_lists": [{"extra_key": "extra_value", "name": "name", "sequence_numbers": [{"sequence": 10, "action": "permit ip any any"}]}]},
    # Duplicate primary key values (two sequence:10)
    {"access_lists": [{"name": "name", "sequence_numbers": [{"sequence": 10, "action": "permit ip any any"}, {"sequence": 10, "action": "deny ip any any"}]}]},
    # Primary key not set on one list item.
    {"access_lists": [{"name": "name", "sequence_numbers": [{"sequence": 10, "action": "permit ip any any"}, {"action": "deny ip any any"}]}]},
]


UNIQUE_KEYS_SCHEMAS = [
    {
        "type": "list",
        "unique_keys": ["key", "nested_list.nested_list_key"],
        "items": {
            "type": "dict",
            "keys": {"key": {"type": "str"}, "nested_list": {"type": "list", "items": {"type": "dict", "keys": {"nested_list_key": {"type": "int"}}}}},
        },
    }
]

UNIQUE_KEYS_VALID_DATA = [
    [
        {"key": "a", "nested_list": [{"nested_list_key": 1}, {"nested_list_key": 2}]},
        {"key": "b", "nested_list": [{"nested_list_key": 3}, {"nested_list_key": 4}]},
    ],
    [
        {"key": "a", "nested_list": [{"nested_list_key": 1}, {}]},
        {"nested_list": [{"nested_list_key": 3}, {"nested_list_key": 4}]},
    ],
    [],
    [{}],
    [{"nested_list": []}],
]

UNIQUE_KEYS_INVALID_DATA = [
    [
        {"key": "a", "nested_list": [{"nested_list_key": 1}, {"nested_list_key": 2}]},
        {"key": "b", "nested_list": [{"nested_list_key": 3}, {"nested_list_key": 3}]},
    ],
    [
        {"key": "a", "nested_list": [{"nested_list_key": 1}, {"nested_list_key": 2}]},
        {"key": "b", "nested_list": [{"nested_list_key": 1}, {"nested_list_key": 4}]},
    ],
    [
        {"key": "a", "nested_list": [{"nested_list_key": 1}, {"nested_list_key": 2}]},
        {"key": "a", "nested_list": [{"nested_list_key": 3}, {"nested_list_key": 4}]},
    ],
]


class TestAvdSchema:
    def test_avd_schema_init_without_schema(self) -> None:
        avdschema = AvdSchema()
        assert isinstance(avdschema, AvdSchema)
        assert avdschema._schema == DEFAULT_SCHEMA

    @pytest.mark.parametrize("test_schema", VALID_TEST_SCHEMAS)
    def test_avd_schema_init_with_schema(self, test_schema: dict) -> None:
        avdschema = AvdSchema(test_schema)
        assert isinstance(avdschema, AvdSchema)
        assert avdschema._schema == test_schema

    @pytest.mark.parametrize("test_data", TEST_DATA_SETS)
    def test_avd_schema_validate_without_schema(self, test_data: Any) -> None:
        validation_errors = list(AvdSchema().validate(test_data))
        assert not validation_errors

    @pytest.mark.parametrize("test_schema", VALID_TEST_SCHEMAS)
    @pytest.mark.parametrize("test_data", TEST_DATA_SETS)
    def test_avd_schema_validate_with_loaded_schema(self, test_schema: dict, test_data: Any) -> None:
        validation_errors = list(AvdSchema(test_schema).validate(test_data))
        assert not validation_errors

    @pytest.mark.parametrize("invalid_data", INVALID_ACL_DATA)
    def test_avd_schema_validate_with_invalid_data(self, invalid_data: Any) -> None:
        validation_errors = list(AvdSchema(combined_schema).validate(invalid_data))
        assert len(validation_errors) > 0
        for validation_error in validation_errors:
            assert isinstance(validation_error, AvdValidationError)

    @pytest.mark.parametrize("test_schema", VALID_TEST_SCHEMAS)
    def test_avd_schema_load_valid_schema(self, test_schema: dict) -> None:
        avdschema = AvdSchema()
        avdschema.load_schema(test_schema)
        assert avdschema._schema == test_schema

    @pytest.mark.parametrize("test_path", TEST_DATA_PATHS)
    def test_avd_schema_subschema_with_loaded_schema(self, test_path: list) -> None:
        avdschema = AvdSchema(combined_schema)
        subschema = avdschema.subschema(test_path)

        if len(test_path) == 0:
            assert subschema == EXPECTED_SUBSCHEMAS["_empty"]
        else:
            assert subschema == EXPECTED_SUBSCHEMAS[".".join(test_path)]

    @pytest.mark.parametrize("test_schema", UNIQUE_KEYS_SCHEMAS)
    @pytest.mark.parametrize("test_data", UNIQUE_KEYS_VALID_DATA)
    def test_avd_schema_validate_unique_keys_valid_data(self, test_schema: dict, test_data: Any) -> None:  # NOSONAR
        validation_errors = list(AvdSchema(test_schema).validate(test_data))
        assert not validation_errors

    @pytest.mark.parametrize("test_schema", UNIQUE_KEYS_SCHEMAS)
    @pytest.mark.parametrize("invalid_data", UNIQUE_KEYS_INVALID_DATA)
    def test_avd_schema_validate_unique_keys_invalid_data(self, test_schema: dict, invalid_data: Any) -> None:  # NOSONAR
        validation_errors = list(AvdSchema(test_schema).validate(invalid_data))
        assert len(validation_errors) > 0
        for validation_error in validation_errors:
            assert isinstance(validation_error, AvdValidationError)
