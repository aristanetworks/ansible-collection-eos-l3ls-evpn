# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from copy import deepcopy
from functools import cached_property
from ipaddress import ip_network
from itertools import islice
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import default, get, get_item, merge

if TYPE_CHECKING:
    from . import AvdStructuredConfigCoreInterfacesAndL3Edge


class UtilsMixin:
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def _p2p_links_profiles(self: AvdStructuredConfigCoreInterfacesAndL3Edge) -> list:
        return get(self._hostvars, f"{self.data_model}.p2p_links_profiles", default=[])

    @cached_property
    def _p2p_links_ip_pools(self: AvdStructuredConfigCoreInterfacesAndL3Edge) -> list:
        return get(self._hostvars, f"{self.data_model}.p2p_links_ip_pools", default=[])

    @cached_property
    def _p2p_links(self: AvdStructuredConfigCoreInterfacesAndL3Edge) -> list:
        return get(self._hostvars, f"{self.data_model}.p2p_links", default=[])

    @cached_property
    def _p2p_links_sflow(self: AvdStructuredConfigCoreInterfacesAndL3Edge) -> bool | None:
        return get(self._hostvars, f"fabric_sflow.{self.data_model}")

    @cached_property
    def _filtered_p2p_links(self: AvdStructuredConfigCoreInterfacesAndL3Edge) -> list:
        """
        Returns a filtered list of p2p_links, which only contains links with our hostname.

        For each links any referenced profiles are applied and IP addresses are resolved
        from pools or subnets.
        """
        if not (p2p_links := self._p2p_links):
            return []

        # Apply p2p_profiles if set. Silently ignoring missing profile.
        if self._p2p_links_profiles:
            p2p_links = [self._apply_p2p_links_profile(p2p_link) for p2p_link in p2p_links]

        # Filter to only include p2p_links with our hostname under "nodes"
        p2p_links = [p2p_link for p2p_link in p2p_links if self.shared_utils.hostname in p2p_link.get("nodes", [])]
        if not p2p_links:
            return []

        # Resolve IPs from subnet or p2p_pools.
        p2p_links = [self._resolve_p2p_ips(p2p_link) for p2p_link in p2p_links]

        # Parse P2P data model and add simplified data
        [p2p_link.update({"data": self._get_p2p_data(p2p_link)}) for p2p_link in p2p_links]

        return p2p_links

    def _apply_p2p_links_profile(self: AvdStructuredConfigCoreInterfacesAndL3Edge, target_dict: dict) -> dict:
        """Apply a profile to a p2p_link."""
        if "profile" not in target_dict:
            # Nothing to do
            return target_dict

        profile = deepcopy(get_item(self._p2p_links_profiles, "name", target_dict["profile"], default={}))
        merged_dict: dict = merge(profile, target_dict, list_merge="replace", destructive_merge=False)
        merged_dict.pop("name", None)
        return merged_dict

    def _resolve_p2p_ips(self: AvdStructuredConfigCoreInterfacesAndL3Edge, p2p_link: dict) -> dict:
        if "ip" in p2p_link:
            # ip already set, so nothing to do
            return p2p_link

        if "subnet" in p2p_link:
            # Resolve ip from subnet
            subnet = ip_network(p2p_link["subnet"], strict=False)

        elif "ip_pool" not in p2p_link or "id" not in p2p_link or not self._p2p_links_ip_pools:
            # Subnet not set and not possible to resolve from pool. Returning original
            return p2p_link
        else:
            # Resolving subnet from pool
            ip_pool = get_item(self._p2p_links_ip_pools, "name", p2p_link["ip_pool"], default={})
            ip_pool_subnet = ip_pool.get("ipv4_pool")
            if not ip_pool_subnet:
                return p2p_link
            prefix_size = int(ip_pool.get("prefix_size", 31))
            link_id = int(p2p_link["id"])
            subnet = next(iter(islice(ip_network(ip_pool_subnet).subnets(new_prefix=prefix_size), link_id - 1, link_id)))

        # hosts() return an iterator of all hosts in subnet.
        # islice() return a generator with only the first two iterations of hosts.
        # List comprehension runs through the generator creating string from each.
        p2p_link["ip"] = [f"{ip}/{subnet.prefixlen}" for ip in islice(subnet.hosts(), 2)]
        return p2p_link

    def _get_p2p_data(self: AvdStructuredConfigCoreInterfacesAndL3Edge, p2p_link: dict) -> dict:
        """
        Parses p2p_link data model and extracts information which is easier to parse.

        Returns:
        {
            peer: <peer name>
            peer_type: <type of peer>
            interface: <interface on this node>
            peer_interface: <interface on peer>
            port_channel_id: <id on this node | None>
            port_channel_members:
              - interface: <interface on this node>
                peer_interface: <interface on peer>
            ip: <ip if set | None>
            peer_ip: <peer ip if set | None>
            bgp_as: <as if set | None>
            peer_bgp_as: <peer as if set | None>
        }
        """
        index = p2p_link["nodes"].index(self.shared_utils.hostname)
        peer_index = (index + 1) % 2
        peer = p2p_link["nodes"][peer_index]
        peer_facts = self.shared_utils.get_peer_facts(peer, required=False)
        peer_type = "other" if peer_facts is None else peer_facts.get("type", "other")

        # Set ip or fallback to list with None values
        ip = get(p2p_link, "ip", default=[None, None])
        # Set bgp_as or fallback to list with None values
        bgp_as = get(p2p_link, "as", default=[None, None])
        # Set descriptions or fallback to list with None values
        descriptions = get(p2p_link, "descriptions", default=[None, None])

        data = {
            "peer": peer,
            "peer_type": peer_type,
            "ip": ip[index],
            "peer_ip": ip[peer_index],
            "bgp_as": str(bgp_as[index]) if index < len(bgp_as) and bgp_as[index] else None,
            "peer_bgp_as": str(bgp_as[peer_index]) if peer_index < len(bgp_as) and bgp_as[peer_index] else None,
            "description": descriptions[index],
        }

        node_child_interfaces = get(p2p_link, "port_channel.nodes_child_interfaces")
        if (node_data := get_item(node_child_interfaces, "node", self.shared_utils.hostname)) is not None and (
            member_interfaces := node_data.get("interfaces")
        ):
            # Port-channel
            default_channel_id = int("".join(re.findall(r"\d", member_interfaces[0])))
            portchannel_id = node_data.get("channel_id", default_channel_id)

            peer = get_item(
                node_child_interfaces,
                "node",
                peer,
                var_name=f"{peer} under {self.data_model}.p2p_links.[].port_channel.nodes_child_interfaces",
            )
            peer_member_interfaces = peer["interfaces"]
            default_peer_channel_id = int("".join(re.findall(r"\d", peer_member_interfaces[0])))
            peer_id = peer.get("channel_id", default_peer_channel_id)

            data.update(
                {
                    "interface": f"Port-Channel{portchannel_id}",
                    "peer_interface": f"Port-Channel{peer_id}",
                    "port_channel_id": portchannel_id,
                    "peer_port_channel_id": peer_id,
                    "port_channel_description": get(p2p_link, "port_channel.description"),
                    "port_channel_members": [
                        {
                            "interface": interface,
                            "peer_interface": peer_member_interfaces[index],
                        }
                        for index, interface in enumerate(member_interfaces)
                    ],
                },
            )
            return data

        if "interfaces" in p2p_link:
            # Ethernet
            data.update(
                {
                    "interface": p2p_link["interfaces"][index],
                    "peer_interface": p2p_link["interfaces"][peer_index],
                    "port_channel_id": None,
                    "peer_port_channel_id": None,
                    "port_channel_description": None,
                    "port_channel_members": [],
                },
            )
            return data

        msg = f"{self.data_model}.p2p_links must have either 'interfaces' or 'port_channel' with correct members set."
        raise AristaAvdInvalidInputsError(msg)

    def _get_common_interface_cfg(self: AvdStructuredConfigCoreInterfacesAndL3Edge, p2p_link: dict) -> dict:
        """
        Return partial structured_config for one p2p_link.

        Covers common config that is applicable to both port-channels and ethernet interfaces.
        This config will only be used on the main interface - so not port-channel members.
        """
        index = p2p_link["nodes"].index(self.shared_utils.hostname)
        interface_cfg = {
            "name": p2p_link["data"]["interface"],
            "peer": p2p_link["data"]["peer"],
            "peer_interface": p2p_link["data"]["peer_interface"],
            "peer_type": p2p_link["data"]["peer_type"],
            "switchport": {"enabled": False},
            "shutdown": False,
            "mtu": p2p_link.get("mtu", self.shared_utils.p2p_uplinks_mtu) if self.shared_utils.platform_settings_feature_support_per_interface_mtu else None,
            "service_profile": p2p_link.get("qos_profile", self.shared_utils.p2p_uplinks_qos_profile),
            "eos_cli": p2p_link.get("raw_eos_cli"),
            "struct_cfg": get(p2p_link, "structured_config"),
        }

        if (ip := get(p2p_link, "ip")) is not None:
            interface_cfg["ip_address"] = ip[index]

        if p2p_link.get("include_in_underlay_protocol", True) is True:
            if p2p_link.get("underlay_multicast", False) and self.shared_utils.underlay_multicast is True:
                interface_cfg["pim"] = {"ipv4": {"sparse_mode": True}}

            if (self.shared_utils.underlay_rfc5549 and p2p_link.get("routing_protocol") != "ebgp") or p2p_link.get("ipv6_enable") is True:
                interface_cfg["ipv6_enable"] = True

            if self.shared_utils.underlay_ospf:
                interface_cfg.update(
                    {
                        "ospf_network_point_to_point": True,
                        "ospf_area": self.shared_utils.underlay_ospf_area,
                    },
                )

            if self.shared_utils.underlay_isis:
                interface_cfg.update(
                    {
                        "isis_enable": self.shared_utils.isis_instance_name,
                        "isis_bfd": get(self._hostvars, "underlay_isis_bfd"),
                        "isis_metric": default(p2p_link.get("isis_metric"), self.shared_utils.isis_default_metric),
                        "isis_network_point_to_point": p2p_link.get("isis_network_type", "point-to-point") == "point-to-point",
                        "isis_hello_padding": p2p_link.get("isis_hello_padding", True),
                        "isis_circuit_type": default(p2p_link.get("isis_circuit_type"), self.shared_utils.isis_default_circuit_type),
                        "isis_authentication_mode": p2p_link.get("isis_authentication_mode"),
                        "isis_authentication_key": p2p_link.get("isis_authentication_key"),
                    },
                )

        if p2p_link.get("macsec_profile"):
            interface_cfg["mac_security"] = {
                "profile": p2p_link["macsec_profile"],
            }

        if (p2p_link_sflow := get(p2p_link, "sflow", default=self._p2p_links_sflow)) is not None:
            interface_cfg["sflow"] = {"enable": p2p_link_sflow}

        if (p2p_link_flow_tracking := self.shared_utils.get_flow_tracker(p2p_link, self.data_model)) is not None:
            interface_cfg["flow_tracker"] = p2p_link_flow_tracking

        if self.shared_utils.mpls_lsr and p2p_link.get("mpls_ip", True) is True:
            interface_cfg["mpls"] = {"ip": True}
            if p2p_link.get("include_in_underlay_protocol", True) is True and self.shared_utils.underlay_ldp and p2p_link.get("mpls_ldp", True) is True:
                interface_cfg["mpls"].update(
                    {
                        "ldp": {
                            "interface": True,
                            "igp_sync": True,
                        },
                    },
                )

        return interface_cfg

    def _get_ethernet_cfg(self: AvdStructuredConfigCoreInterfacesAndL3Edge, p2p_link: dict) -> dict:
        """
        Return partial structured_config for one p2p_link.

        Covers config that is only applicable to ethernet interfaces.
        This config will only be used on both main interfaces and port-channel members.
        """
        ethernet_cfg = {"speed": p2p_link.get("speed")}

        if get(p2p_link, "ptp.enabled") is not True:
            return ethernet_cfg

        ptp_config = {}

        # Apply PTP profile config
        if self.shared_utils.ptp_enabled:
            ptp_config.update(self.shared_utils.ptp_profile)

        ptp_config["enable"] = True
        ptp_config.pop("profile", None)
        ethernet_cfg["ptp"] = ptp_config

        return ethernet_cfg

    def _get_port_channel_member_cfg(self: AvdStructuredConfigCoreInterfacesAndL3Edge, p2p_link: dict, member: dict) -> dict:
        """
        Return partial structured_config for one p2p_link.

        Covers config for ethernet interfaces that are port-channel members.
        """
        return {
            "name": member["interface"],
            "peer": p2p_link["data"]["peer"],
            "peer_interface": member["peer_interface"],
            "peer_type": p2p_link["data"]["peer_type"],
            "shutdown": False,
            "channel_group": {
                "id": p2p_link["data"]["port_channel_id"],
                "mode": get(p2p_link, "port_channel.mode", default="active"),
            },
        }
