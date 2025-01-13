# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import pytest

from pyavd.j2filters import is_in_filter

HOSTNAME_VALID = "test1.aristanetworks.com"
HOSTNAME_INVALID = "test1.bsn.com"
HOSTNAME_FILTER_VALID = ["arista", "aristanetworks"]
HOSTNAME_FILTER_INVALID = "aristanetworks"

IS_IN_FILTER_TEST_CASES = [
    # (<hostname>, <hostname_filter>, <res_is_in_filter>)
    (HOSTNAME_VALID, None, True),  # default filter
    (HOSTNAME_VALID, HOSTNAME_FILTER_VALID, True),  # valid hostname
    (HOSTNAME_INVALID, HOSTNAME_FILTER_VALID, False),  # invalid hostname
    # TODO: Check if this is a valid testcase. Add a type check?
    (HOSTNAME_VALID, HOSTNAME_FILTER_INVALID, True),  # invalid filter
]


class TestIsInFilter:
    @pytest.mark.parametrize(("hostname", "hostname_filter", "res_is_in_filter"), IS_IN_FILTER_TEST_CASES)
    def test_is_in_filter(self, hostname: str, hostname_filter: list | str, res_is_in_filter: bool) -> None:
        res = is_in_filter(hostname=hostname, hostname_filter=hostname_filter)
        assert res == res_is_in_filter
