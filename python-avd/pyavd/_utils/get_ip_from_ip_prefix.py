# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


def get_ip_from_ip_prefix(ip_prefix: str) -> str:
    """Return the ip part of an ip/mask prefix."""
    return ip_prefix.split("/", maxsplit=1)[0]
