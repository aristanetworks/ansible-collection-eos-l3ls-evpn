# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property
from ipaddress import ip_network
from typing import TYPE_CHECKING

from pyavd._utils import get

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

        if not self.inputs.underlay_filter_redistribute_connected:
            return None

        # IPv4 - PL-LOOPBACKS-EVPN-OVERLAY
        sequence_numbers = [{"sequence": 10, "action": f"permit {self.shared_utils.loopback_ipv4_pool} eq 32"}]

        if self.shared_utils.overlay_vtep and self.shared_utils.vtep_loopback.lower() != "loopback0" and not self.shared_utils.is_wan_router:
            sequence_numbers.append({"sequence": 20, "action": f"permit {self.shared_utils.vtep_loopback_ipv4_pool} eq 32"})

        if self.inputs.vtep_vvtep_ip is not None and self.shared_utils.network_services_l3 is True and not self.shared_utils.is_wan_router:
            sequence_numbers.append({"sequence": 30, "action": f"permit {self.inputs.vtep_vvtep_ip}"})

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

        # P2P-LINKS needed for L3 inband ZTP
        p2p_links_sequence_numbers = []
        sequence_number = 0
        for peer in self._avd_peers:
            peer_facts = self.shared_utils.get_peer_facts(peer, required=True)
            for uplink in peer_facts["uplinks"]:
                if (
                    uplink["peer"] == self.shared_utils.hostname
                    and uplink["type"] == "underlay_p2p"
                    and uplink.get("ip_address")
                    and "unnumbered" not in uplink["ip_address"]
                    and get(peer_facts, "inband_ztp")
                ):
                    sequence_number += 10
                    subnet = str(ip_network(f"{uplink['ip_address']}/{uplink['prefix_length']}", strict=False))
                    p2p_links_sequence_numbers.append({"sequence": sequence_number, "action": f"permit {subnet}"})
        if p2p_links_sequence_numbers:
            prefix_lists.append({"name": "PL-P2P-LINKS", "sequence_numbers": p2p_links_sequence_numbers})

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

        if not self.inputs.underlay_filter_redistribute_connected:
            return None

        # IPv6 - PL-LOOPBACKS-EVPN-OVERLAY-V6
        return [
            {"name": "PL-LOOPBACKS-EVPN-OVERLAY-V6", "sequence_numbers": [{"sequence": 10, "action": f"permit {self.shared_utils.loopback_ipv6_pool} eq 128"}]},
        ]
