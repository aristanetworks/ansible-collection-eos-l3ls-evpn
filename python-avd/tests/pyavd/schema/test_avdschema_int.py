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

# TODO: Test Dynamic valid values.
#       Test default value with required False.

TEST_SCHEMA = {
    "type": "dict",
    "keys": {
        "test_value": {
            "type": "int",
            "convert_types": ["bool", "str", "float"],
            "default": 11,
            "min": 2,
            "max": 20,
            "valid_values": [0, 11, 22],
            "dynamic_valid_values": ["valid_values"],  # Part of meta schema but not implemented in converter
            "required": True,
            "description": "Some integer",
            "display_name": "Integer",
        },
    },
}

TESTS = [
    # (test_value, expected_errors: tuple, expected_error_messages: tuple)
    (11, None, None),  # Valid value. No errors.
    (
        False,
        (AvdValidationError,),
        ("'Validation Error: test_value': '0' is lower than the allowed minimum of 2.",),
    ),  # False is converted to 0 which is valid but below min.
    (
        True,
        (AvdValidationError,),
        ("'Validation Error: test_value': '1' is lower than the allowed minimum of 2.", "'Validation Error: test_value': '1' is not one of [0, 11, 22]"),
    ),  # True is converted to 1 which is not valid.
    ("11", None, None),  # Converted to 11. No errors.
    (11.0123, None, None),  # Converted to 11. No errors.
    (None, (AvdValidationError,), ("'Validation Error: ': Required key 'test_value' is not set in dict.",)),  # Required is set, so None is not ignored.
    (12, (AvdValidationError,), ("'Validation Error: test_value': '12' is not one of [0, 11, 22]",)),  # Invalid value.
    ([], (AvdValidationError,), ("'Validation Error: test_value': Invalid type 'list'. Expected a 'int'.",)),  # Invalid type.
    (0, (AvdValidationError,), ("'Validation Error: test_value': '0' is lower than the allowed minimum of 2.",)),  # Valid but below min.
    (22, (AvdValidationError,), ("'Validation Error: test_value': '22' is higher than the allowed maximum of 20.",)),  # Valid but above max.
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
