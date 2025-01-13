# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


from typing import Any

import pytest

from pyavd._utils import strip_null_from_data

STRIP_EMPTIES_LIST = {
    "None": ["string1", "string2", "string3", None],
    "empty_string": ["", "string1", "string2"],
    "empty_list": [[], ["string1", "string2"]],
    "empty_dict": [{}, {"key1": "value1", "key2": "value2"}],
    "None_in_nested_list": [[None, 1, 2, 3], [], 1, 2, 3],
    "None_in_nested_dict": [{"key1": None, "key2": "value2", "key3": [None, 1, 2, 3]}, 1, 2, 3],
}

STRIP_EMPTIES_DICT = {
    "None": {"key1": None, "key2": "value2", "key3": "value3"},
    "empty_string": {"key1": "", "key2": "value2", "key3": "value3"},
    "empty_list": {"key1": [], "key2": "value2", "key3": "value3"},
    "empty_dict": {"key1": {}, "key2": "value2", "key3": "value3"},
    "None_in_nested_list": {"key1": [1, 2, 3, None], "key2": [{"key3": "value3"}, {"key4": "value4"}]},
    "None_in_nested_dict": {"key1": [1, 2, 3, {}], "key2": [{"key3": "value3", "key4": None}]},
}

STRIP_EMPTIES = {"None": None, "empty_string": "", "valid_string": "string1", "valid_number": 4}


class TestStripEmpties:
    def strip_empties_checks(self, output: Any) -> None:
        assert None not in output
        assert "" not in output
        assert [] not in output
        assert {} not in output
        for entry in output:
            if isinstance(entry, list):
                self.strip_empties_checks(entry)
            if isinstance(entry, dict):
                self.strip_empties_checks(entry.values())

    @pytest.mark.parametrize("data", STRIP_EMPTIES.values(), ids=STRIP_EMPTIES.keys())
    def test_strip_empties_string(self, data: Any) -> None:
        output = strip_null_from_data(data)
        assert output == data

    @pytest.mark.parametrize("data", STRIP_EMPTIES_LIST.values(), ids=STRIP_EMPTIES_LIST.keys())
    def test_strip_empties_list(self, data: Any) -> None:
        output = strip_null_from_data(
            data,
            strip_values_tuple=(
                None,
                "",
                [],
                {},
            ),
        )
        self.strip_empties_checks(output)

    @pytest.mark.parametrize("data", STRIP_EMPTIES_DICT.values(), ids=STRIP_EMPTIES_DICT.keys())
    def test_strip_empties_dict(self, data: Any) -> None:
        output = strip_null_from_data(
            data,
            strip_values_tuple=(
                None,
                "",
                [],
                {},
            ),
        )
        self.strip_empties_checks(output.values())
