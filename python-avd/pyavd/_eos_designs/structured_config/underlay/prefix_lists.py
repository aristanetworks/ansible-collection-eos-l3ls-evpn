# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlay


class PrefixListsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def prefix_lists(self: AvdStructuredConfigUnderlay) -> list | None:
        """Return structured config for prefix_lists."""
        if self.shared_utils.underlay_bgp is not True and not self.shared_utils.is_wan_router:
            return None

        if self.shared_utils.overlay_routing_protocol == "none":
            return None

        if not self.shared_utils.underlay_filter_redistribute_connected:
            return None

        # IPv4 - PL-LOOPBACKS-EVPN-OVERLAY
        sequence_numbers = [{"sequence": 10, "action": f"permit {self.shared_utils.loopback_ipv4_pool} eq 32"}]

        if self.shared_utils.overlay_vtep and self.shared_utils.vtep_loopback.lower() != "loopback0" and not self.shared_utils.is_wan_router:
            sequence_numbers.append({"sequence": 20, "action": f"permit {self.shared_utils.vtep_loopback_ipv4_pool} eq 32"})

        if self.shared_utils.vtep_vvtep_ip is not None and self.shared_utils.network_services_l3 is True and not self.shared_utils.is_wan_router:
            sequence_numbers.append({"sequence": 30, "action": f"permit {self.shared_utils.vtep_vvtep_ip}"})

        prefix_lists = [{"name": "PL-LOOPBACKS-EVPN-OVERLAY", "sequence_numbers": sequence_numbers}]

        if self.shared_utils.underlay_multicast_rp_interfaces is not None:
            sequence_numbers = [
                {"sequence": (index + 1) * 10, "action": f"permit {interface['ip_address']}"}
                for index, interface in enumerate(self.shared_utils.underlay_multicast_rp_interfaces)
            ]
            prefix_lists.append({"name": "PL-LOOPBACKS-PIM-RP", "sequence_numbers": sequence_numbers})

        # For now only configure it with eBGP towards LAN.
        if self.shared_utils.wan_ha and self.shared_utils.use_uplinks_for_wan_ha and self.shared_utils.underlay_routing_protocol == "ebgp":
            sequence_numbers = [
                {"sequence": 10 * (index + 1), "action": f"permit {ipaddress.ip_network(ip_address, strict=False)}"}
                for index, ip_address in enumerate(self.shared_utils.wan_ha_ip_addresses)
            ]

            if sequence_numbers:
                prefix_lists.append({"name": "PL-WAN-HA-PREFIXES", "sequence_numbers": sequence_numbers})

            sequence_numbers = [
                {"sequence": 10 * (index + 1), "action": f"permit {ipaddress.ip_network(ip_address, strict=False)}"}
                for index, ip_address in enumerate(self.shared_utils.wan_ha_peer_ip_addresses)
            ]

            if sequence_numbers:
                prefix_lists.append({"name": "PL-WAN-HA-PEER-PREFIXES", "sequence_numbers": sequence_numbers})

        return prefix_lists

    @cached_property
    def ipv6_prefix_lists(self: AvdStructuredConfigUnderlay) -> list | None:
        """Return structured config for IPv6 prefix_lists."""
        if self.shared_utils.underlay_bgp is not True:
            return None

        if self.shared_utils.underlay_ipv6 is not True:
            return None

        if self.shared_utils.overlay_routing_protocol == "none" and not self.shared_utils.is_wan_router:
            return None

        if not self.shared_utils.underlay_filter_redistribute_connected:
            return None

        # IPv6 - PL-LOOPBACKS-EVPN-OVERLAY-V6
        return [
            {"name": "PL-LOOPBACKS-EVPN-OVERLAY-V6", "sequence_numbers": [{"sequence": 10, "action": f"permit {self.shared_utils.loopback_ipv6_pool} eq 128"}]},
        ]
