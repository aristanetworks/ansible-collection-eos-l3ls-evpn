# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest

from pyavd.j2filters.natural_sort import convert, natural_sort


class TestNaturalSortFilter:
    @pytest.mark.parametrize(
        ("item_to_convert", "converted_item", "ignore_case"),
        [
            ("100", 100, True),
            ("200", 200, True),
            ("ABC", "abc", True),
            ("ABC", "ABC", False),
        ],
    )
    def test_convert(self, item_to_convert: str, converted_item: int | str, ignore_case: bool) -> None:
        resp = convert(item_to_convert, ignore_case)
        assert resp == converted_item

    @pytest.mark.parametrize(
        ("item_to_natural_sort", "sort_key", "strict", "ignore_case", "sorted_list", "expected_raise"),
        [
            pytest.param(None, None, False, True, [], does_not_raise(), id="None"),
            pytest.param([], None, False, True, [], does_not_raise(), id="empty-list"),
            pytest.param({}, "", False, True, [], does_not_raise(), id="empty-dict"),
            pytest.param("", "", False, True, [], does_not_raise(), id="empty-string"),
            pytest.param("access_list", None, False, True, ["_", "a", "c", "c", "e", "i", "l", "s", "s", "s", "t"], does_not_raise(), id="string-input"),
            pytest.param(
                ["1,2,3,4", "11,2,3,4", "5.6.7.8"],  # NOSONAR, IP is just test data
                None,
                False,
                True,
                ["1,2,3,4", "5.6.7.8", "11,2,3,4"],  # NOSONAR, IP is just test data
                does_not_raise(),
                id="list-of-integers",
            ),
            pytest.param({"a1": 123, "a10": 333, "a2": 2, "a11": 4456}, None, False, True, ["a1", "a2", "a10", "a11"], does_not_raise(), id="dict"),
            pytest.param(
                [
                    {"name": "ACL-10", "counters_per_entry": True},
                    {"name": "ACL-01", "counters_per_entry": True},
                    {"name": "ACL-05", "counters_per_entry": False},
                ],
                "name",
                False,
                True,
                [
                    {"name": "ACL-01", "counters_per_entry": True},
                    {"name": "ACL-05", "counters_per_entry": False},
                    {"name": "ACL-10", "counters_per_entry": True},
                ],
                does_not_raise(),
                id="list-of-dict-with-sort-key",
            ),
            pytest.param(
                [
                    {"name": "ACL-10", "counters_per_entry": True},
                    {"sequence_numbers": {"sequence": 10}},
                    {"counters_per_entry": False},
                    {"name": "ACL-05", "counters_per_entry": False},
                ],
                "name",
                False,
                True,
                [
                    {"name": "ACL-05", "counters_per_entry": False},
                    {"name": "ACL-10", "counters_per_entry": True},
                    {"counters_per_entry": False},
                    {"sequence_numbers": {"sequence": 10}},
                ],
                does_not_raise(),
                id="list-of-dict-with-sort-key-some-entries-dont-have-the-key",
            ),
            pytest.param(
                [
                    {"sequence_numbers": {"sequence": 10}},
                    {"counters_per_entry": False},
                    {"action": "action_command"},
                ],
                "name",
                False,
                True,
                [
                    {"action": "action_command"},
                    {"counters_per_entry": False},
                    {"sequence_numbers": {"sequence": 10}},
                ],
                does_not_raise(),
                id="list-of-dict-with-sort-key-all-entries-dont-have-the-key",
            ),
            pytest.param(
                [
                    {"name": "default"},
                    {"name": "D"},
                    {"name": "E"},
                ],
                "name",
                False,
                True,
                [
                    {"name": "D"},
                    {"name": "default"},
                    {"name": "E"},
                ],
                does_not_raise(),
                id="list-of-dict-with-sort-key-ignore-case",
            ),
            pytest.param(
                [
                    {"name": "default"},
                    {"name": "D"},
                    {"name": "E"},
                ],
                "name",
                False,
                False,
                [
                    {"name": "D"},
                    {"name": "E"},
                    {"name": "default"},
                ],
                does_not_raise(),
                id="list-of-dict-with-sort-key-respect-case",
            ),
            pytest.param(
                [
                    {"name": "ACL-10", "counters_per_entry": True},
                    {"counters_per_entry": False},
                    {"name": "ACL-05", "counters_per_entry": False},
                ],
                "name",
                True,
                True,
                None,
                pytest.raises(Exception, match="Missing key 'name' in item to sort "),
                id="list-of-dict-with-sort-key-strict-mode",
            ),
        ],
    )
    def test_natural_sort(
        self,
        item_to_natural_sort: Any,
        sort_key: str | None,
        strict: bool,
        ignore_case: bool,
        sorted_list: list | None,
        expected_raise: AbstractContextManager,
    ) -> None:
        with expected_raise:
            resp = natural_sort(item_to_natural_sort, sort_key, strict=strict, ignore_case=ignore_case)
            assert resp == sorted_list
