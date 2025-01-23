# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest

from pyavd._errors import AristaAvdError
from pyavd._utils import get_ip_from_pool

# default values for testcases

POOL, PREFIXLEN, SUBNET_OFFSET, IP_OFFSET = ("1.2.3.4/24", 32, 1, 0)
POOLS_AND_RANGES = "10.10.10.0/24, 10.20.20.20-10.20.20.29"


@pytest.mark.parametrize(
    ("pool", "prefixlen", "subnet_offset", "ip_offset", "expected"),
    [
        (
            "1.3.0/32",
            PREFIXLEN,
            SUBNET_OFFSET,
            IP_OFFSET,
            (
                "Invalid format of IP pool(s) '1.3.0/32'. "
                "Must be one or more prefixes (like 10.10.10.0/24) and/or ranges (like 10.10.10.10-10.10.10.20) separated by commas."
            ),
        ),
        (
            "10.10.10.10 - 10.10.10.20",  # No spaces allowed for ranges
            PREFIXLEN,
            SUBNET_OFFSET,
            IP_OFFSET,
            (
                "Invalid format of IP pool(s) '10.10.10.10 - 10.10.10.20'. "
                "Must be one or more prefixes (like 10.10.10.0/24) and/or ranges (like 10.10.10.10-10.10.10.20) separated by commas."
            ),
        ),
        ("1.2.3.0/32", PREFIXLEN, SUBNET_OFFSET, IP_OFFSET, f"Unable to get {SUBNET_OFFSET + 1} /{PREFIXLEN} subnets from pool 1.2.3.0/32"),
        (
            POOL,
            8,
            SUBNET_OFFSET,
            IP_OFFSET,
            (
                f"Invalid IP pool(s) '{POOL}'. Each pool and range must be larger than the prefix length of each subnet: 8."
                "IP ranges must also start and end on proper subnet boundaries for this prefix length size."
            ),
        ),
        (POOL, PREFIXLEN, 256, IP_OFFSET, f"Unable to get 257 /{PREFIXLEN} subnets from pool {POOL}"),
        (POOL, PREFIXLEN, SUBNET_OFFSET, 1, "Unable to get 2 hosts in subnet"),
        (
            "300.300.300.300/32",
            PREFIXLEN,
            SUBNET_OFFSET,
            IP_OFFSET,
            (
                "Invalid IP pool(s) '300.300.300.300/32'. Unable to load '300.300.300.300/32' as an IP prefix: "
                "'300.300.300.300/32' does not appear to be an IPv4 or IPv6 network"
            ),
        ),
        (
            "1.1.1.1-0.0.0.0",
            PREFIXLEN,
            SUBNET_OFFSET,
            IP_OFFSET,
            "Invalid IP pool(s) '1.1.1.1-0.0.0.0'. Unable to load '1.1.1.1-0.0.0.0' as an IP range: last IP address must be greater than first",
        ),
        (POOLS_AND_RANGES, PREFIXLEN, 266, IP_OFFSET, f"Unable to get 267 /{PREFIXLEN} subnets from pool {POOLS_AND_RANGES}"),
        (
            "10.0.0.0/24,1.1.1.1-0.0.0.0",
            24,
            1,
            IP_OFFSET,
            "Invalid IP pool(s) '10.0.0.0/24,1.1.1.1-0.0.0.0'. Unable to load '1.1.1.1-0.0.0.0' as an IP range: last IP address must be greater than first",
        ),
        (
            "10.10.10.10-20",
            24,
            1,
            IP_OFFSET,
            (
                "Invalid format of IP pool(s) '10.10.10.10-20'. "
                "Must be one or more prefixes (like 10.10.10.0/24) and/or ranges (like 10.10.10.10-10.10.10.20) separated by commas."
            ),
        ),
    ],
)
def test_get_ip_from_pool_invalid(pool: str, prefixlen: int, subnet_offset: int, ip_offset: int, expected: str) -> None:
    """Invalid cases for get_ip_from_pool."""
    with pytest.raises(AristaAvdError) as exc_info:
        get_ip_from_pool(pool, prefixlen, subnet_offset, ip_offset)
    assert expected in str(exc_info.value)


@pytest.mark.parametrize(
    ("pool", "prefixlen", "subnet_offset", "ip_offset", "expected"),
    [
        ("1.2.3.0/31", PREFIXLEN, SUBNET_OFFSET, IP_OFFSET, "1.2.3.1"),
        (POOL, 25, SUBNET_OFFSET, IP_OFFSET, "1.2.3.129"),
        (POOL, PREFIXLEN, 0, IP_OFFSET, "1.2.3.0"),
        (POOL, PREFIXLEN, 255, IP_OFFSET, "1.2.3.255"),
        (POOL, 31, SUBNET_OFFSET, 1, "1.2.3.3"),
        (POOLS_AND_RANGES, PREFIXLEN, 256, IP_OFFSET, "10.20.20.20"),
        (POOLS_AND_RANGES, PREFIXLEN, 265, IP_OFFSET, "10.20.20.29"),
        # Notice this will not raise even when the range is invalid, since the pools are lazily evaluated.
        ("10.0.0.0/24,1.1.1.1-0.0.0.0", PREFIXLEN, SUBNET_OFFSET, IP_OFFSET, "10.0.0.1"),
    ],
)
def test_get_ip_from_pool_valid(pool: str, prefixlen: int, subnet_offset: int, ip_offset: int, expected: str) -> None:
    """Valid cases for get_ip_from_pool with default values."""
    resp = get_ip_from_pool(pool, prefixlen, subnet_offset, ip_offset)
    assert resp == expected
