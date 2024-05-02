# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

from ansible_collections.arista.avd.plugins.plugin_utils.utils.range_expand import range_expand

VALID_INPUTS = [
    (
        "Ethernet1",
        ["Ethernet1"],
    ),
    (
        "Ethernet1-2",
        ["Ethernet1", "Ethernet2"],
    ),
    (
        "Eth 3-5,7-8",
        ["Eth 3", "Eth 4", "Eth 5", "Eth 7", "Eth 8"],
    ),
    (
        "et2-6,po1-2",
        ["et2", "et3", "et4", "et5", "et6", "po1", "po2"],
    ),
    (
        ["Ethernet1"],
        ["Ethernet1"],
    ),
    (
        ["Ethernet 1-2", "Eth3-5", "7-8"],
        ["Ethernet 1", "Ethernet 2", "Eth3", "Eth4", "Eth5", "7", "8"],
    ),
    (
        ["Ethernet2-6", "Port-channel1-2"],
        ["Ethernet2", "Ethernet3", "Ethernet4", "Ethernet5", "Ethernet6", "Port-channel1", "Port-channel2"],
    ),
    (
        ["Ethernet1/1-2", "Eth1-2/3-5,5/1-2"],
        ["Ethernet1/1", "Ethernet1/2", "Eth1/3", "Eth1/4", "Eth1/5", "Eth2/3", "Eth2/4", "Eth2/5", "Eth5/1", "Eth5/2"],
    ),
    (
        ["Eth1.1,9-10.1", "Eth2.2-3", "Eth3/1-2.3-4"],
        ["Eth1.1", "Eth9.1", "Eth10.1", "Eth2.2", "Eth2.3", "Eth3/1.3", "Eth3/1.4", "Eth3/2.3", "Eth3/2.4"],
    ),
    (
        "1-3",
        ["1", "2", "3"],
    ),
    (
        ["1", "2", "3"],
        ["1", "2", "3"],
    ),
    (
        "vlan1-3",
        ["vlan1", "vlan2", "vlan3"],
    ),
    (
        "Et1-2/3-4/5-6",
        ["Et1/3/5", "Et1/3/6", "Et1/4/5", "Et1/4/6", "Et2/3/5", "Et2/3/6", "Et2/4/5", "Et2/4/6"],
    ),
    (
        "65100.0",
        ["65100.0"],
    ),
    (
        "65100.0-4",
        ["65100.0", "65100.1", "65100.2", "65100.3", "65100.4"],
    ),
    (
        "65100.0-2,65200.1-2",
        ["65100.0", "65100.1", "65100.2", "65200.1", "65200.2"],
    ),
    (
        "1-2.0-1",
        ["1.0", "1.1", "2.0", "2.1"],
    ),
    (
        "Ethernet{1}",
        ["Ethernet1"],
    ),
    (
        "Ethernet{1, 2,3 }",
        ["Ethernet1", "Ethernet2", "Ethernet3"],
    ),
    (
        "Ethernet{1}/{4,5}",
        ["Ethernet1/4", "Ethernet1/5"],
    ),
    (
        "{1,2}",
        ["1", "2"],
    ),
    (
        "1,{2,3}/5",
        ["1", "2/5", "3/5"],
    ),
    (
        "Eth{10-14}",
        ["Eth10", "Eth11", "Eth12", "Eth13", "Eth14"],
    ),
    (
        "Eth{101-103}/{5,7}",
        ["Eth101/5", "Eth101/7", "Eth102/5", "Eth102/7", "Eth103/5", "Eth103/7"],
    ),
    # (
    #     "Eth{1,2",
    #     ["Eth{1", "Eth2"],
    # ),
    # ("Eth{1,2}/3,4}", ["Eth1/3", "Eth2/3", "Eth4}"],), # Exception need to fix regex_commas_outside_parentheses regex in range_expand.
    # ("1  -  2  -  3", ["1  -  2  -  3"],), # Exception for regex regex_hyphen_range (more than multiple one spaces not supported)
    #                                               lookbehind does not support quantifier.
    (
        "Eth{1, 2}/3, 4",
        ["Eth1/3", "Eth2/3", "Eth4"],
    ),
    (
        "Eth{4}/{2-3}/{1,32}/4.{200-202,300}",
        [
            "Eth4/2/1/4.200",
            "Eth4/2/1/4.201",
            "Eth4/2/1/4.202",
            "Eth4/2/1/4.300",
            "Eth4/2/32/4.200",
            "Eth4/2/32/4.201",
            "Eth4/2/32/4.202",
            "Eth4/2/32/4.300",
            "Eth4/3/1/4.200",
            "Eth4/3/1/4.201",
            "Eth4/3/1/4.202",
            "Eth4/3/1/4.300",
            "Eth4/3/32/4.200",
            "Eth4/3/32/4.201",
            "Eth4/3/32/4.202",
            "Eth4/3/32/4.300",
        ],
    ),
    (
        ["{1-5}", "{2,3,4}", "14-16"],
        ["1", "2", "3", "4", "5", "2", "3", "4", "14", "15", "16"],
    ),
    (
        ["Ethernet 1-2/{3-5}", "Eth3-5/{3,4,5}", "7-8/{3,4,5}"],
        [
            "Ethernet 1/3",
            "Ethernet 1/4",
            "Ethernet 1/5",
            "Ethernet 2/3",
            "Ethernet 2/4",
            "Ethernet 2/5",
            "Eth3/3",
            "Eth3/4",
            "Eth3/5",
            "Eth4/3",
            "Eth4/4",
            "Eth4/5",
            "Eth5/3",
            "Eth5/4",
            "Eth5/5",
            "7/3",
            "7/4",
            "7/5",
            "8/3",
            "8/4",
            "8/5",
        ],
    ),
    (
        ["Et {3 ,4,5}.1", "Et4/{3,4,5}.1", "Et5.200", "Et{4-6}.200"],
        ["Et 3.1", "Et 4.1", "Et 5.1", "Et4/3.1", "Et4/4.1", "Et4/5.1", "Et5.200", "Et4.200", "Et5.200", "Et6.200"],
    ),
    (
        "{65000}.1",
        ["65000.1"],
    ),
    (
        ["Pt{600, 7000}/2.1", "Pt{ 600, 7000}/2.1", "Pt{600, 7000 }/2.1"],
        ["Pt600/2.1", "Pt7000/2.1", "Pt600/2.1", "Pt7000/2.1", "Pt600/2.1", "Pt7000/2.1"],
    ),
    (
        "eth1- 5,{7,9, 11-13}",
        ["eth1", "eth2", "eth3", "eth4", "eth5", "eth7", "eth9", "eth11", "eth12", "eth13"],
    ),
    (
        "eth{7,9,11-13},21,26",
        ["eth7", "eth9", "eth11", "eth12", "eth13", "eth21", "eth26"],
    ),
    (
        "eth{7,9,11-13}/1,21/1,26/1",
        ["eth7/1", "eth9/1", "eth11/1", "eth12/1", "eth13/1", "eth21/1", "eth26/1"],
    ),
    # (
    #     ["eth{-2}"],
    #     ["eth{-2}"],
    # ),
    (
        "eth{12,0-5}, 14",
        ["eth12", "eth0", "eth1", "eth2", "eth3", "eth4", "eth5", "eth14"],
    ),
    (
        ["{10-15,2}"],
        ["10", "11", "12", "13", "14", "15", "2"],
    ),
]


@pytest.mark.parametrize(["input_range", "expected_output"], VALID_INPUTS)
def test_range_expand_valid_input(input_range, expected_output: list):
    assert range_expand(input_range) == expected_output
