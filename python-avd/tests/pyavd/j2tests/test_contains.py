# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Unit tests for pyavd.j2tests.contains."""

from __future__ import annotations

from typing import Any

import pytest
from jinja2.runtime import Undefined

from pyavd.j2tests.contains import contains

TEST_DATA = [
    pytest.param(None, "dummy", False, id="value is None"),
    pytest.param(Undefined, "dummy", False, id="value is Undefined"),
    pytest.param("value_not_a_list", "dummy", False, id="value is not a list"),
    pytest.param(["dummy"], None, False, id="test_value is None"),
    pytest.param(["dummy"], Undefined, False, id="test_value is Undefined"),
    pytest.param(["a", "b", "c"], "b", True, id="test_value single value in value"),
    pytest.param(["a", "b", "c"], ["d", "b"], True, id="test_value list contained value"),
    pytest.param([1, 42, 666], 42, True, id="test success with int"),
    pytest.param(["a", "b", "c"], "d", False, id="test_value list not contained value"),
    pytest.param(["a", "b", "c"], ["d", "e"], False, id="test_value single value not in value"),
]


class TestContainsTest:
    """Test Contains."""

    @pytest.mark.parametrize(("value", "test_value", "expected_result"), TEST_DATA)
    def test_contains(self, value: Any, test_value: Any, expected_result: bool) -> None:
        """Test the contains function."""
        assert contains(value, test_value) == expected_result
