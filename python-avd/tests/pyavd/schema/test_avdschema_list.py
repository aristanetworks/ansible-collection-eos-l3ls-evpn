# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from sys import path
from typing import Any

import pytest

# Override global path to load schema from source instead of any installed version.
path.insert(0, str(Path(__file__).parents[3]))

from pyavd._errors import AvdValidationError
from pyavd._schema.avdschema import AvdSchema

# TODO: Test default value with required False.

TEST_SCHEMA = {
    "type": "dict",
    "keys": {
        "test_value": {
            "type": "list",
            "default": [{"pri": 1, "foo": "foo1"}, {"pri": 2, "foo": "foo2"}, {"pri": 3, "foo": "foo3"}],
            "max_length": 3,
            "min_length": 1,
            "required": True,
            "description": "Some string",
            "display_name": "String",
            "primary_key": "pri",
            "unique_keys": ["foo"],
            "items": {
                "type": "dict",
                "keys": {
                    "pri": {"type": "int", "convert_types": ["str"]},
                    "foo": {"type": "str", "convert_types": ["int"]},
                },
            },
        },
    },
}

TESTS = [
    # (test_value, expected_errors: tuple, expected_error_messages: tuple)
    ([{"pri": 1, "foo": "foo1"}, {"pri": 2, "foo": "foo2"}], None, None),  # Valid value. No errors.
    ([{"pri": "1", "foo": 123}, {"pri": 2, "foo": "234"}], None, None),  # Valid value after conversion. No errors.
    (
        [{"pri": 1, "foo": "123"}, {"pri": "1", "foo": 123}],
        (AvdValidationError,),
        (
            "'Validation Error: test_value[0].pri': The value '1' is not unique between all list items as required.",
            "'Validation Error: test_value[1].pri': The value '1' is not unique between all list items as required.",
            "'Validation Error: test_value[0].foo': The value '123' is not unique between all list items as required.",
            "'Validation Error: test_value[1].foo': The value '123' is not unique between all list items as required.",
        ),
    ),  # Collision on both primary_key and unique_keys
    (None, (AvdValidationError,), ("'Validation Error: ': Required key 'test_value' is not set in dict.",)),  # Required is set, so None is not ignored.
    ([], (AvdValidationError,), ("'Validation Error: test_value': The value is shorter (0) than the allowed minimum of 1.",)),  # Valid but below min length.
    (
        [{"pri": 1, "foo": "foo1"}, {"pri": 2, "foo": "foo2"}, {"pri": 3, "foo": "foo3"}, {"pri": 4, "foo": "foo4"}],
        (AvdValidationError,),
        ("'Validation Error: test_value': The value is longer (4) than the allowed maximum of 3.",),
    ),  # Valid but amove max length.
    ("a", (AvdValidationError,), ("'Validation Error: test_value': Invalid type 'str'. Expected a 'list'.",)),  # Invalid type.
]


@pytest.fixture(scope="module")
def avd_schema() -> AvdSchema:
    return AvdSchema(TEST_SCHEMA)


@pytest.mark.parametrize(("test_value", "expected_errors", "expected_error_messages"), TESTS)
def test_generated_schema(test_value: Any, expected_errors: tuple | None, expected_error_messages: tuple | None, avd_schema: AvdSchema) -> None:
    instance = {"test_value": test_value}
    list(avd_schema.convert(instance))
    validation_errors = list(avd_schema.validate(instance))
    if expected_errors:
        for validation_error in validation_errors:
            assert isinstance(validation_error, expected_errors)
            assert str(validation_error) in expected_error_messages

        assert len(validation_errors) == len(expected_error_messages)
    else:
        # No errors expected.
        assert not validation_errors
