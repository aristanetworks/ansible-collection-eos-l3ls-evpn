# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


import re
from collections.abc import Generator
from contextlib import contextmanager

import pytest

from pyavd._errors import AristaAvdError
from pyavd._utils import get


@contextmanager
def does_not_raise() -> Generator:
    yield


GET_DATA = [
    {  # normal case
        "dictionary": {"avd_switch_facts": {"host1": {"id": 42}}},
        "key": "avd_switch_facts.host1.id",
        "default": None,
        "required": False,
        "org_key": None,
        "separator": ".",
        "expected_result": 42,
        "expected_exception": does_not_raise(),
    },
    {  # not required and no default - return None
        "dictionary": {"avd_switch_facts": {"host1": {"id": 42}}},
        "key": "avd_switch_facts.host1.missing",
        "default": None,
        "required": False,
        "org_key": None,
        "separator": ".",
        "expected_result": None,
        "expected_exception": does_not_raise(),
    },
    {  # default value
        "dictionary": {"avd_switch_facts": {"host1": {"id": 42}}},
        "key": "avd_switch_facts.host1.missing_default",
        "default": 666,
        "required": False,
        "org_key": None,
        "separator": ".",
        "expected_result": 666,
        "expected_exception": does_not_raise(),
    },
    {  # default value - present
        "dictionary": {"avd_switch_facts": {"host1": {"id": 42, "present_default": 1000}}},
        "key": "avd_switch_facts.host1.present_default",
        "default": 666,
        "required": False,
        "org_key": None,
        "separator": ".",
        "expected_result": 1000,
        "expected_exception": does_not_raise(),
    },
    {  # required - missing
        "dictionary": {"avd_switch_facts": {"host1": {"id": 42}}},
        "key": "avd_switch_facts.host1.missing_required",
        "default": None,
        "required": True,
        "org_key": None,
        "separator": ".",
        "expected_result": None,
        "expected_exception": pytest.raises(AristaAvdError, match="avd_switch_facts.host1.missing_required"),
    },
    {  # custom separator - hostname with a "."
        "dictionary": {"avd_switch_facts": {"host1.test": {"id": 42}}},
        "key": "avd_switch_facts..host1.test..id",
        "default": None,
        "required": False,
        "org_key": None,
        "separator": "..",
        "expected_result": 42,
        "expected_exception": does_not_raise(),
    },
    {  # org_key as exception message
        "dictionary": {"avd_switch_facts": {"host1.test": {"id": 42}}},
        "key": "avd_switch_facts..host1.test..missing_required",
        "default": None,
        "required": True,
        "org_key": "avd_switch_facts.(host1.test).missing_required",
        "separator": "..",
        "expected_result": None,
        "expected_exception": pytest.raises(AristaAvdError, match=re.escape("avd_switch_facts.(host1.test).missing_required")),
    },
]


class TestUtils:
    @pytest.mark.parametrize("data", GET_DATA)
    def test_get(self, data: dict) -> None:
        with data["expected_exception"]:
            res = get(data["dictionary"], data["key"], data["default"], data["required"], data["org_key"], data["separator"])
            assert res == data["expected_result"]
