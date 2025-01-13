# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

from typing import Any

import pytest

from pyavd.j2filters import range_expand

RANGE_TO_EXPAND_INVALID_VALUES = [
    pytest.param(True, TypeError, "value must be a Sequence, got <class 'bool'>", id="Wrong input type - bool"),
    pytest.param({"key": "value"}, TypeError, "value must be a Sequence, got <class 'dict'>", id="Wrong input type - dict"),
    pytest.param(33, TypeError, "", id="Wrong input type - int"),
    pytest.param(
        "Ethernet4-2",
        ValueError,
        "Range Ethernet4-2 could not be expanded because the first interface 4 is larger than last interface 2 in the range.",
        id="Wrong interface range",
    ),
    pytest.param(
        "Ethernet1,51-3/2",
        ValueError,
        "Range 51-3/2 could not be expanded because the first module 51 is larger than last module 3 in the range.",
        id="Wrong module range",
    ),
    pytest.param(
        "Ethernet1.42-21",
        ValueError,
        "Range Ethernet1.42-21 could not be expanded because the first subinterface 42 is larger than last subinterface 21 in the range.",
        id="Wrong subinterface range",
    ),
    pytest.param(
        "Ethernet4/2-1/4",
        ValueError,
        "Range Ethernet4/2-1/4 could not be expanded because the first interface 2 is larger than last interface 1 in the range.",
        id="Wrong parent interface range",
    ),
]

RANGE_TO_EXPAND_VALID_TESTS = [
    # (<input>, <expected_output>)
    pytest.param("Ethernet1", ["Ethernet1"]),
    pytest.param("Ethernet1-2", ["Ethernet1", "Ethernet2"]),
    pytest.param("Eth 3-5,7-8", ["Eth 3", "Eth 4", "Eth 5", "Eth 7", "Eth 8"]),
    pytest.param("et2-6,po1-2", ["et2", "et3", "et4", "et5", "et6", "po1", "po2"]),
    pytest.param(["Ethernet1"], ["Ethernet1"]),
    pytest.param(["Ethernet 1-2", "Eth3-5", "7-8"], ["Ethernet 1", "Ethernet 2", "Eth3", "Eth4", "Eth5", "7", "8"]),
    pytest.param(["Ethernet2-6", "Port-channel1-2"], ["Ethernet2", "Ethernet3", "Ethernet4", "Ethernet5", "Ethernet6", "Port-channel1", "Port-channel2"]),
    pytest.param(
        ["Ethernet1/1-2", "Eth1-2/3-5,5/1-2"], ["Ethernet1/1", "Ethernet1/2", "Eth1/3", "Eth1/4", "Eth1/5", "Eth2/3", "Eth2/4", "Eth2/5", "Eth5/1", "Eth5/2"]
    ),
    pytest.param(
        ["Eth1.1,9-10.1", "Eth2.2-3", "Eth3/1-2.3-4"], ["Eth1.1", "Eth9.1", "Eth10.1", "Eth2.2", "Eth2.3", "Eth3/1.3", "Eth3/1.4", "Eth3/2.3", "Eth3/2.4"]
    ),
    pytest.param("1-3", ["1", "2", "3"]),
    pytest.param(["1", "2", "3"], ["1", "2", "3"]),
    pytest.param("vlan1-3", ["vlan1", "vlan2", "vlan3"]),
    pytest.param("Et1-2/3-4/5-6", ["Et1/3/5", "Et1/3/6", "Et1/4/5", "Et1/4/6", "Et2/3/5", "Et2/3/6", "Et2/4/5", "Et2/4/6"]),
    pytest.param("65100.0", ["65100.0"]),
    pytest.param("65100.0-4", ["65100.0", "65100.1", "65100.2", "65100.3", "65100.4"]),
    pytest.param("65100.0-2,65200.1-2", ["65100.0", "65100.1", "65100.2", "65200.1", "65200.2"]),
    pytest.param("1-2.0-1", ["1.0", "1.1", "2.0", "2.1"]),
    pytest.param("Gi1/0/1-2", ["Gi1/0/1", "Gi1/0/2"]),
]


class TestRangeExpandFilter:
    @pytest.mark.parametrize(("input_value", "expected_raise", "expected_raise_message"), RANGE_TO_EXPAND_INVALID_VALUES)
    def test_range_expand_invalid(self, input_value: Any, expected_raise: Exception, expected_raise_message: str) -> None:
        with pytest.raises(expected_raise, match=expected_raise_message):
            range_expand(input_value)

    @pytest.mark.parametrize(("range_to_expand", "expected_output"), RANGE_TO_EXPAND_VALID_TESTS)
    def test_range_expand_valid(self, range_to_expand: list | str, expected_output: list) -> None:
        resp = range_expand(range_to_expand)
        assert resp == expected_output
