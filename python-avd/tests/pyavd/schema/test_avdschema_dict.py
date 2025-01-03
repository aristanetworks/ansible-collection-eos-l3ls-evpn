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
#       Test dynamic keys

TEST_SCHEMA = {
    "type": "dict",
    "keys": {
        "test_value": {
            "type": "dict",
            "default": {"pri": 1, "foo": "foo1"},
            "required": True,
            "description": "Some string",
            "display_name": "String",
            "keys": {
                "pri": {"type": "int", "convert_types": ["str"]},
                "foo": {"type": "str", "convert_types": ["int"]},
            },
        },
    },
}

TESTS = [
    # (test_value, expected_errors: tuple, expected_error_messages: tuple)
    ({"pri": 1, "foo": "foo1"}, None, None),  # Valid value. No errors.
    ({"pri": "1", "foo": 123}, None, None),  # Valid value after conversion. No errors.
    ({}, None, None),  # Valid value. No errors.
    (
        None,
        (AvdValidationError,),
        ("'Validation Error: ': Required key 'test_value' is not set in dict.",),
    ),  # Required is set, so None is not ignored.
    ("a", (AvdValidationError,), ("'Validation Error: test_value': Invalid type 'str'. Expected a 'dict'.",)),  # Invalid type.
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
