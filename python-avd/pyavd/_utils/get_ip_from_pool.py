# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import ipaddress
import re
from collections.abc import Iterator
from functools import partial

from pyavd._errors import AristaAvdError
from pyavd._utils import ensure_type

# Not using f-strings since more {} in there would just make it harder to follow.
# These do not match valid IP addresses, but just something that looks like an IP at first glance.
LAZY_IPV4_ADDRESS_PATTERN = r"(\d{1,3}\.){3}\d{1,3}"
LAZY_IPV4_PREFIX_PATTERN = LAZY_IPV4_ADDRESS_PATTERN + r"/\d{1,2}"
LAZY_IPV4_RANGE_PATTERN = LAZY_IPV4_ADDRESS_PATTERN + r"-" + LAZY_IPV4_ADDRESS_PATTERN
LAZY_IPV6_ADDRESS_PATTERN = r"([A-Fa-f0-9]{0,4}::?){0,7}(?<=:)([A-Fa-f0-9]{1,4})?"
LAZY_IPV6_PREFIX_PATTERN = LAZY_IPV6_ADDRESS_PATTERN + r"/\d{1,3}"
LAZY_IPV6_RANGE_PATTERN = LAZY_IPV6_ADDRESS_PATTERN + r"-" + LAZY_IPV6_ADDRESS_PATTERN
PREFIX_PATTERN = r"(" + LAZY_IPV4_PREFIX_PATTERN + r"|" + LAZY_IPV6_PREFIX_PATTERN + r")"
RANGE_PATTERN = r"(" + LAZY_IPV4_RANGE_PATTERN + r"|" + LAZY_IPV6_RANGE_PATTERN + r")"
POOLS_AND_RANGES_PATTERN = re.compile(r"((?P<prefix>" + PREFIX_PATTERN + r")|(?P<range>" + RANGE_PATTERN + r"))([,\ ]+|$)")

# The following are imported by schema validation, but it is easier to maintain in one place.
# TODO: Move to some centralized constants.
FULLMATCH_IP_POOLS_AND_RANGES_PATTERN = re.compile(rf"({POOLS_AND_RANGES_PATTERN.pattern})+")
FULLMATCH_IPV4_POOLS_AND_RANGES_PATTERN = re.compile(r"((" + LAZY_IPV4_PREFIX_PATTERN + r"|" + LAZY_IPV4_RANGE_PATTERN + r")([,\ ]+|$))+")
FULLMATCH_IPV6_POOLS_AND_RANGES_PATTERN = re.compile(r"((" + LAZY_IPV6_PREFIX_PATTERN + r"|" + LAZY_IPV6_RANGE_PATTERN + r")([,\ ]+|$))+")


def get_ip_from_pool(pool: str, prefixlen: int, subnet_offset: int, ip_offset: int) -> str:
    """
    get_ip_from_pool returns one IP address from a subnet of the given prefix length size from the given pool.

    The "pool" string is lazily evaluated, so an invalid IP address may be allowed if we never need to parse it.
    E.g. if you ask for offset 1 and the first pool is valid, but the pool for offset 256 is invalid.

    Args:
        pool: IP pool(s) and/or IP range(s) in string format, example: "192.168.0.0/24, 10.10.10.10-10.10.10.20"
        prefixlen: Prefix length for subnet to fetch from the pool
        subnet_offset: Offset this many subnets of 'prefixlen' size into the pool.
        ip_offset: Offset this many IP addresses into the subnet to get the IP.

    Returns:
        IP address without mask

    Raises:
        AristaAvdError: If the pool string is invalid or if the requested offset is not available in the pool.
    """
    subnet = None
    remaining_subnet_offset = subnet_offset
    for pool_network in get_networks_from_pool(pool):
        # Storing these since they involve calculations:
        pool_network_size = pool_network.num_addresses
        prefixlen_diff = prefixlen - pool_network.prefixlen

        # Since _pools_from_str may generate multiple smaller networks when given a range, this will fail if the first or last
        # IP does not match the subnet boundaries.
        try:
            subnet_size = (int(pool_network.hostmask) + 1) >> prefixlen_diff
        except ValueError as e:
            msg = (
                f"Invalid IP pool(s) '{pool}'. Each pool and range must be larger than the prefix length of each subnet: {prefixlen}."
                "IP ranges must also start and end on proper subnet boundaries for this prefix length size."
            )
            raise AristaAvdError(msg) from e

        if (remaining_subnet_offset + 1) * subnet_size > pool_network_size:
            # This pool does not have enough addresses to allocate the requested offset. Subtract the size and try the next pool.
            remaining_subnet_offset -= 2**prefixlen_diff
            continue

        # Everything went well so we can take a subnet from this pool.
        subnet = ipaddress.ip_network((int(pool_network.network_address) + remaining_subnet_offset * subnet_size, prefixlen))
        break

    if not subnet:
        msg = f"Unable to get {subnet_offset + 1} /{prefixlen} subnets from pool {pool}"
        raise AristaAvdError(msg)

    try:
        if subnet_size > 2:
            # This is a regular subnet. Skip the network address and raise if we hit the broadcast address.
            # >= because ip_offset is 0-based.
            if ip_offset >= (subnet_size - 2):
                raise IndexError  # noqa: TRY301
            ip = subnet[ip_offset + 1]
        else:
            # This is a linknet (/31 or /127) or a single IP (/32 or /128)
            ip = subnet[ip_offset]

    except IndexError as e:
        msg = f"Unable to get {ip_offset + 1} hosts in subnet {subnet} taken from pool {pool}"
        raise AristaAvdError(msg) from e

    return str(ip)


def get_ipv4_networks_from_pool(pool: str) -> Iterator[ipaddress.IPv4Network]:
    """
    Get IPv4 networks from a pool string.

    Args:
        pool: Comma separated string of IPv4 pools and ranges.

    Returns:
        Iterator of IPv4Network objects.

    Raises:
        AristaAvdError: If the pool string is invalid.
    """
    ensure_ipv4_type = partial(ensure_type, item_type=ipaddress.IPv4Network)
    try:
        yield from map(ensure_ipv4_type, get_networks_from_pool(pool))
    except TypeError as e:
        msg = f"Invalid IP pool(s) '{pool}': {e}"
        raise AristaAvdError(msg) from e


def get_ipv6_networks_from_pool(pool: str) -> Iterator[ipaddress.IPv6Network]:
    """
    Get IPv6 networks from a pool string.

    Args:
        pool: Comma separated string of IPv6 pools and ranges.

    Returns:
        Iterator of IPv6Network objects.

    Raises:
        AristaAvdError: If the pool string is invalid.
    """
    ensure_ipv6_type = partial(ensure_type, item_type=ipaddress.IPv6Network)
    try:
        yield from map(ensure_ipv6_type, get_networks_from_pool(pool))
    except TypeError as e:
        msg = f"Invalid IP pool(s) '{pool}': {e}"
        raise AristaAvdError(msg) from e


def get_networks_from_pool(pool: str) -> Iterator[ipaddress.IPv4Network | ipaddress.IPv6Network]:
    """
    Get IP networks from a pool string.

    Args:
        pool: Comma separated string of IP pools and ranges.

    Returns:
        Iterator of IPv4Network and/or IPv6Network objects.

    Raises:
        AristaAvdError: If the pool string is invalid.
    """
    counter = 0
    matches = re.finditer(POOLS_AND_RANGES_PATTERN, pool)
    for match in matches:
        counter += 1
        match_dict = match.groupdict()
        ip_prefix = match_dict["prefix"]
        ip_range = match_dict["range"]
        if ip_prefix:
            try:
                yield ipaddress.ip_network(ip_prefix, strict=False)
            except ValueError as e:
                msg = f"Invalid IP pool(s) '{pool}'. Unable to load '{ip_prefix}' as an IP prefix: {e}"
                raise AristaAvdError(msg) from e

        if ip_range:
            try:
                yield from ipaddress.summarize_address_range(*(ipaddress.ip_address(ip) for ip in ip_range.split("-")))
            except (TypeError, ValueError) as e:
                msg = f"Invalid IP pool(s) '{pool}'. Unable to load '{ip_range}' as an IP range: {e}"
                raise AristaAvdError(msg) from e

    if not counter:
        msg = (
            f"Invalid format of IP pool(s) '{pool}'. "
            "Must be one or more prefixes (like 10.10.10.0/24) and/or ranges (like 10.10.10.10-10.10.10.20) separated by commas."
        )
        raise AristaAvdError(msg)
