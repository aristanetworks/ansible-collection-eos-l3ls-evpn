# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Any

import pytest
from jinja2.runtime import Undefined

from pyavd.j2filters import default

PRIMARY_VALUE_LIST = [1, "ABC", None, Undefined, {}, {"key": "value"}, [1, 2]]
DEFAULT_VALUE_LIST = [["default"], [None, 1], [None, "abc"], [None, None, "2"], [{"key": "value"}]]


class TestDefaultFilter:
    @pytest.mark.parametrize("primary_value", PRIMARY_VALUE_LIST)
    @pytest.mark.parametrize("default_value", DEFAULT_VALUE_LIST)
    def test_default(self, primary_value: Any, default_value: Any) -> None:
        resp = default(primary_value, *default_value)
        if isinstance(primary_value, Undefined) or (primary_value is None and len(DEFAULT_VALUE_LIST) >= 1):
            for i in default_value:
                if isinstance(i, Undefined) or i is None or i == "":
                    continue
                assert i == resp
        else:
            assert resp == primary_value
