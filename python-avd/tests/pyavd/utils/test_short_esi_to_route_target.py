# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


import pytest

from pyavd._utils import short_esi_to_route_target

ESI_TO_RT_TEST_CASES = [
    # (<short_esi>, <route_target>)
    ("0303:0202:0101", "03:03:02:02:01:01"),
    ("0303:0202:0101  ", "0303:0202:0101  "),
    ("ESI_SHORT", "ESI_SHORT"),
    ("", ""),
    ("3", "3"),
]


class TestGenerateRouteTargetFilter:
    @pytest.mark.parametrize(("short_esi", "route_target"), ESI_TO_RT_TEST_CASES)
    def test_short_esi_to_route_target(self, short_esi: str, route_target: str) -> None:
        resp = short_esi_to_route_target(short_esi)
        assert resp == route_target
