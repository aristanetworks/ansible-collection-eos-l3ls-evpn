# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import re
from ipaddress import IPv4Network, IPv6Network

import pytest

from pyavd._errors import AristaAvdError
from pyavd._utils import get_ipv4_networks_from_pool, get_ipv6_networks_from_pool, get_networks_from_pool


def test_get_networks_from_pool() -> None:
    pool = "2001:db8:1:2::0-2001:db8:1:3::1, 192.168.0.0/24, 2001:db8::/64, 192.168.1.0-192.168.1.2"
    expected_networks = [
        IPv6Network("2001:db8:1:2::/64"),
        IPv6Network("2001:db8:1:3::/127"),
        IPv4Network("192.168.0.0/24"),
        IPv6Network("2001:db8::/64"),
        IPv4Network("192.168.1.0/31"),
        IPv4Network("192.168.1.2/32"),
    ]
    result = list(get_networks_from_pool(pool))
    assert result == expected_networks


def test_get_ipv4_networks_from_pool() -> None:
    pool = "192.168.0.0/24, 192.168.1.0-192.168.1.2"
    expected_networks = [IPv4Network("192.168.0.0/24"), IPv4Network("192.168.1.0/31"), IPv4Network("192.168.1.2/32")]
    result = list(get_ipv4_networks_from_pool(pool))
    assert result == expected_networks


def test_get_ipv6_networks_from_pool() -> None:
    pool = "2001:db8::/64, 2001:db8:1:2::0-2001:db8:1:3::1"
    expected_networks = [IPv6Network("2001:db8::/64"), IPv6Network("2001:db8:1:2::/64"), IPv6Network("2001:db8:1:3::/127")]
    result = list(get_ipv6_networks_from_pool(pool))
    assert result == expected_networks


def test_get_ipv4_networks_from_pool_negative() -> None:
    pool = "2001:db8:1:2::0-2001:db8:1:3::1, 192.168.0.0/24, 2001:db8::/64, 192.168.1.0-192.168.1.2"
    with pytest.raises(AristaAvdError, match=re.escape(f"Invalid IP pool(s) '{pool}': Expected IPv4Network but got IPv6Network.")):
        list(get_ipv4_networks_from_pool(pool))


def test_get_ipv6_networks_from_pool_negative() -> None:
    pool = "2001:db8:1:2::0-2001:db8:1:3::1, 192.168.0.0/24, 2001:db8::/64, 192.168.1.0-192.168.1.2"
    with pytest.raises(AristaAvdError, match=re.escape(f"Invalid IP pool(s) '{pool}': Expected IPv6Network but got IPv4Network.")):
        list(get_ipv6_networks_from_pool(pool))
