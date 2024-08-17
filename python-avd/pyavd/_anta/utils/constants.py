# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from enum import Enum


class StructuredConfigKey(Enum):
    """Enumeration of AVD structured configuration keys used to conditionally run tests. Supports dot notation for nested keys."""

    ETHERNET_INTERFACES = "ethernet_interfaces"
    HTTPS_SSL_PROFILE = "management_api_http.https_ssl_profile"
    MLAG_CONFIGURATION = "mlag_configuration"
    ROUTER_BGP = "router_bgp"

    @classmethod
    def to_string_list(cls, keys: list[StructuredConfigKey]) -> list[str]:
        """Convert a list of StructuredConfigKey to a list of strings."""
        return [key.value for key in keys]
