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

# TODO: Test dynamic valid values.
#       Test formats once that is implemented - replacing format.
#       Test format
#       Test default value with required False.

TEST_SCHEMA = {
    "type": "dict",
    "keys": {
        "test_value": {
            "type": "str",
            "convert_types": ["bool", "int", "float"],
            "default": "foo",
            "valid_values": ["a", "foo", "zoo", "baaar", "1.0", "42", "true"],
            "convert_to_lower_case": True,
            "max_length": 4,
            "min_length": 2,
            "dynamic_valid_values": ["valid_strings"],  # Part of meta schema but not implemented in converter
            "pattern": "[abf14t].*",
            "required": True,
            "description": "Some string",
            "display_name": "String",
        },
    },
}

TESTS = [
    # (test_value, expected_errors: tuple, expected_error_messages: tuple)
    ("foo", None, None),  # Valid value. No errors.
    ("FoO", None, None),  # Lowered to "foo" which is valid.
    (True, None, None),  # True is converted and lowered to "true" which is valid.
    (
        False,
        (AvdValidationError,),
        (
            "'Validation Error: test_value': 'false' is not one of ['a', 'foo', 'zoo', 'baaar', '1.0', '42', 'true']",
            "'Validation Error: test_value': The value is longer (5) than the allowed maximum of 4.",
        ),
    ),  # False is converted and lowered to "false" which is not valid.
    (42, None, None),  # Converted to "42". No errors.
    (1.000, None, None),  # Converted to "1.0". No errors.
    (
        None,
        (AvdValidationError,),
        ("'Validation Error: ': Required key 'test_value' is not set in dict.",),
    ),  # Required is set, so None is not ignored.
    ([], (AvdValidationError,), ("'Validation Error: test_value': Invalid type 'list'. Expected a 'str'.",)),  # Invalid type.
    ("a", (AvdValidationError,), ("'Validation Error: test_value': The value is shorter (1) than the allowed minimum of 2.",)),  # Valid but below min length.
    (
        "baaar",
        (AvdValidationError,),
        ("'Validation Error: test_value': The value is longer (5) than the allowed maximum of 4.",),
    ),  # Valid but below min length.
    (
        22,
        (AvdValidationError,),
        (
            "'Validation Error: test_value': '22' is not one of ['a', 'foo', 'zoo', 'baaar', '1.0', '42', 'true']",
            "'Validation Error: test_value': The value '22' is not matching the pattern '[abf14t].*'.",
        ),
    ),  # Converted to "22" which is not valid.
    (
        "zoo",
        (AvdValidationError,),
        ("'Validation Error: test_value': The value 'zoo' is not matching the pattern '[abf14t].*'.",),
    ),  # Valid value but does not match pattern.
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
