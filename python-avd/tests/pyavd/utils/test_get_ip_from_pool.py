# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest

from pyavd._errors import AristaAvdError
from pyavd._utils import get_ip_from_pool

# default values for testcases

POOL, PREFIXLEN, SUBNET_OFFSET, IP_OFFSET = ("1.2.3.4/24", 32, 1, 0)


@pytest.mark.parametrize(
    ("pool", "prefixlen", "subnet_offset", "ip_offset", "expected"),
    [
        ("1.2.3.0/32", PREFIXLEN, SUBNET_OFFSET, IP_OFFSET, f"Unable to get {SUBNET_OFFSET + 1} /{PREFIXLEN} subnets from pool 1.2.3.0/32"),
        (POOL, 8, SUBNET_OFFSET, IP_OFFSET, "Prefix length 8 is smaller than pool network prefix length"),
        (POOL, PREFIXLEN, 256, IP_OFFSET, f"Unable to get 257 /{PREFIXLEN} subnets from pool {POOL}"),
        (POOL, PREFIXLEN, SUBNET_OFFSET, 1, "Unable to get 2 hosts in subnet"),
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
    ],
)
def test_get_ip_from_pool_valid(pool: str, prefixlen: int, subnet_offset: int, ip_offset: int, expected: str) -> None:
    """Valid cases for get_ip_from_pool with default values."""
    resp = get_ip_from_pool(pool, prefixlen, subnet_offset, ip_offset)
    assert resp == expected
