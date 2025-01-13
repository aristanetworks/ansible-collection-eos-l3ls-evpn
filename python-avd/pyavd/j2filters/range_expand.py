# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# pylint: disable=cell-var-from-loop
from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass


@dataclass
class InterfaceData:
    one_range: str
    first_interface: int | None = None
    last_interface: int | None = None
    first_subinterface: int | None = None
    last_subinterface: int | None = None
    first_parent_interface: int | None = None
    last_parent_interface: int | None = None
    first_module: int | None = None
    last_module: int | None = None


def expand_subinterfaces(interface_string: str, data: InterfaceData) -> list:
    result = []
    if data.last_subinterface is not None:
        if data.first_subinterface > data.last_subinterface:
            msg = (
                f"Range {data.one_range} could not be expanded because the first subinterface {data.first_subinterface} is larger than last"
                f" subinterface {data.last_subinterface} in the range."
            )
            raise ValueError(msg)
        result.extend(f"{interface_string}.{subinterface}" for subinterface in range(data.first_subinterface, data.last_subinterface + 1))
    else:
        result.append(interface_string)
    return result


def expand_interfaces(interface_string: str, data: InterfaceData) -> list:
    result = []
    if data.first_interface > data.last_interface:
        msg = (
            f"Range {data.one_range} could not be expanded because the first interface {data.first_interface} is larger than last interface"
            f" {data.last_interface} in the range."
        )
        raise ValueError(msg)
    for interface in range(data.first_interface, data.last_interface + 1):
        result.extend(expand_subinterfaces(f"{interface_string}{interface}", data))
    return result


def expand_parent_interfaces(interface_string: str, data: InterfaceData) -> list:
    result = []
    if data.last_parent_interface is not None:
        if data.first_parent_interface > data.last_parent_interface:
            msg = (
                f"Range {data.one_range} could not be expanded because the first interface {data.first_parent_interface} is larger than last"
                f" interface {data.last_parent_interface} in the range."
            )
            raise ValueError(msg)
        for parent_interface in range(data.first_parent_interface, data.last_parent_interface + 1):
            result.extend(expand_interfaces(f"{interface_string}{parent_interface}/", data))
    else:
        result.extend(expand_interfaces(f"{interface_string}", data))
    return result


def expand_module(interface_string: str, data: InterfaceData) -> list:
    result = []
    if data.last_module is not None:
        if data.first_module > data.last_module:
            msg = (
                f"Range {data.one_range} could not be expanded because the first module {data.first_module} is larger than last module"
                f" {data.last_module} in the range."
            )
            raise ValueError(msg)
        for module in range(data.first_module, data.last_module + 1):
            result.extend(expand_parent_interfaces(f"{interface_string}{module}/", data))
    else:
        result.extend(expand_parent_interfaces(f"{interface_string}", data))
    return result


def range_expand(range_to_expand: Sequence) -> list:
    if not isinstance(range_to_expand, Sequence):
        msg = f"value must be a Sequence, got {type(range_to_expand)}"
        raise TypeError(msg)

    result = []

    # If we got a list, unpack it and run this function recursively
    if not isinstance(range_to_expand, str):
        for r in range_to_expand:
            result.extend(range_expand(r))

    # Must be a str now
    else:
        prefix = ""

        # Unpack list in string
        for one_range in range_to_expand.split(","):
            if one_range is None:
                continue

            # Find prefix (if any)
            # Ignoring SONAR hotspot regarding potential DDOS for this PR.
            regex = r"^(.*?)(((\d+)-)?(\d+)\/)?(((\d+)-)?(\d+)\/)?(((\d+)-)?(\d+))(\.((\d+)-)?(\d+))?"  # NOSONAR
            # Number of groups in this regex.
            regex_groups = 17
            # Groups one-by-one:
            # Group 1  (.*?)                                                                           matches prefix ex. Ethernet, Eth, Po, Port-Channel
            # Group 2       (((\d+)-)?(\d+)\/)?                                                        matches module(s) and slash ex. 12/, 1-3/
            # Group 3        ((\d+)-)?                                                                 matches first module and dash ex. 1-
            # Group 4         (\d+)                                                                    matches first module ex. 1
            # Group 5                 (\d+)                                                            matches last module ex. 12, 3
            # Group 6                          (((\d+)-)?(\d+)\/)?                                     matches parent interface(s) and slash ex. 47/, 1-48/
            # Group 7                           ((\d+)-)?                                              matches parent interface(s) and dash ex. 47-
            # Group 8                            (\d+)                                                 matches first parent interface ex. 1
            # Group 9                                    (\d+)                                         matches last parent interface ex. 47, 48
            # Group 10                                            (((\d+)-)?(\d+))                     matches (breakout) interface(s) ex. 1, 1-4, 1-48
            # Group 11                                             ((\d+)-)?                           matches first interfaces and dash ex. 1-, 1-
            # Group 12                                              (\d+)                              matches first interface
            # Group 13                                                      (\d+)                      matches last interface ex. 1, 4, 48
            # Group 14                                                            (\.((\d+)-)?(\d+))?  matches dot and sub-interface(s) ex. .141, .12-15
            # Group 15                                                               ((\d+)-)?         matches first sub-interface and dash ex. 12-
            # Group 16                                                                (\d+)            matches first sub-interface ex. 12
            # Group 17                                                                        (\d+)    matches last sub-interface ex. 141, 15
            # Remember that the groups() object is 0-based and the group numbers above are 1-based
            search_result = re.search(regex, one_range)
            if search_result:
                if len(search_result.groups()) == regex_groups:
                    groups = search_result.groups()
                    data = InterfaceData(one_range=one_range)
                    # Set prefix if found (otherwise use last set prefix)
                    if groups[0]:
                        prefix = groups[0]
                    if groups[4]:
                        data.last_module = int(groups[4])
                    data.first_module = int(groups[3]) if groups[3] else data.last_module
                    if groups[8]:
                        data.last_parent_interface = int(groups[8])
                    data.first_parent_interface = int(groups[7]) if groups[7] else data.last_parent_interface
                    if groups[12]:
                        data.last_interface = int(groups[12])
                    data.first_interface = int(groups[11]) if groups[11] else data.last_interface
                    if groups[16]:
                        data.last_subinterface = int(groups[16])
                    data.first_subinterface = int(groups[15]) if groups[15] else data.last_subinterface

                    result.extend(expand_module(prefix, data))

                else:
                    msg = f"Invalid range, got {one_range} and found {search_result.groups()}"
                    raise ValueError(msg)

    return result
