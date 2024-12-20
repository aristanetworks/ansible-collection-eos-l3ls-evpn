# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from ipaddress import ip_network
from itertools import islice
from typing import TYPE_CHECKING, TypeVar

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils import default

if TYPE_CHECKING:
    from . import AvdStructuredConfigCoreInterfacesAndL3Edge

T_P2pLinksItem = TypeVar("T_P2pLinksItem", EosDesigns.CoreInterfaces.P2pLinksItem, EosDesigns.L3Edge.P2pLinksItem)
T_P2pLinksProfiles = TypeVar("T_P2pLinksProfiles", EosDesigns.CoreInterfaces.P2pLinksProfiles, EosDesigns.L3Edge.P2pLinksProfiles)


class UtilsMixin:
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def _p2p_links_sflow(self: AvdStructuredConfigCoreInterfacesAndL3Edge) -> bool | None:
        return self.inputs.fabric_sflow.core_interfaces if self.data_model == "core_interfaces" else self.inputs.fabric_sflow.l3_edge

    @cached_property
    def _filtered_p2p_links(self: AvdStructuredConfigCoreInterfacesAndL3Edge) -> list[tuple[T_P2pLinksItem, dict]]:
        """
        Returns a filtered list of p2p_links, which only contains links with our hostname.

        For each links any referenced profiles are applied and IP addresses are resolved
        from pools or subnets.
        """
        if not (p2p_links := self.inputs_data.p2p_links):
            return []

        # Apply p2p_profiles if set. Silently ignoring missing profile.
        p2p_links: list[T_P2pLinksItem] = [self._apply_p2p_links_profile(p2p_link) for p2p_link in p2p_links]

        # Filter to only include p2p_links with our hostname under "nodes"
        p2p_links = [p2p_link for p2p_link in p2p_links if self.shared_utils.hostname in p2p_link.nodes]
        if not p2p_links:
            return []

        # Resolve IPs from subnet or p2p_pools.
        p2p_links = [self._resolve_p2p_ips(p2p_link) for p2p_link in p2p_links]

        # Parse P2P data model and create simplified data
        return [(p2p_link, self._get_p2p_data(p2p_link)) for p2p_link in p2p_links]

    def _apply_p2p_links_profile(self: AvdStructuredConfigCoreInterfacesAndL3Edge, p2p_link: T_P2pLinksItem) -> T_P2pLinksItem:
        """Apply a profile to a p2p_link. Always returns a new instance. TODO: Raise if profile is missing."""
        if not p2p_link.profile or p2p_link.profile not in self.inputs_data.p2p_links_profiles:
            # Nothing to do
            return p2p_link._deepcopy()

        profile_as_p2p_link_item = self.inputs_data.p2p_links_profiles[p2p_link.profile]._cast_as(type(p2p_link), ignore_extra_keys=True)
        return p2p_link._deepinherited(profile_as_p2p_link_item)

    def _resolve_p2p_ips(self: AvdStructuredConfigCoreInterfacesAndL3Edge, p2p_link: T_P2pLinksItem) -> T_P2pLinksItem:
        if p2p_link.ip:
            # ip already set, so nothing to do
            return p2p_link

        if p2p_link.subnet:
            # Resolve ip from subnet
            subnet = ip_network(p2p_link.subnet, strict=False)

        elif not p2p_link.ip_pool or not p2p_link.id or not self.inputs_data.p2p_links_ip_pools:
            # Subnet not set and not possible to resolve from pool. Returning original
            return p2p_link
        else:
            # Resolving subnet from pool
            if p2p_link.ip_pool not in self.inputs_data.p2p_links_ip_pools:
                return p2p_link
            ip_pool = self.inputs_data.p2p_links_ip_pools[p2p_link.ip_pool]
            if not ip_pool.ipv4_pool:
                return p2p_link
            subnet = next(iter(islice(ip_network(ip_pool.ipv4_pool).subnets(new_prefix=ip_pool.prefix_size), p2p_link.id - 1, p2p_link.id)))

        # hosts() return an iterator of all hosts in subnet.
        # islice() return a generator with only the first two iterations of hosts.
        # List comprehension runs through the generator creating string from each.
        p2p_link.ip = [f"{ip}/{subnet.prefixlen}" for ip in islice(subnet.hosts(), 2)]
        return p2p_link

    def _get_p2p_data(self: AvdStructuredConfigCoreInterfacesAndL3Edge, p2p_link: T_P2pLinksItem) -> dict:
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
        index = p2p_link.nodes.index(self.shared_utils.hostname)
        peer_index = (index + 1) % 2
        peer = p2p_link.nodes[peer_index]
        peer_facts = self.shared_utils.get_peer_facts(peer, required=False)
        peer_type = "other" if peer_facts is None else peer_facts.get("type", "other")

        # Set ip or fallback to list with None values
        ip = p2p_link.ip or [None, None]
        # Set bgp_as or fallback to list with None values
        bgp_as = p2p_link.field_as or [None, None]
        # Set descriptions or fallback to list with None values
        descriptions = p2p_link.descriptions or [None, None]

        data = {
            "peer": peer,
            "peer_type": peer_type,
            "ip": ip[index],
            "peer_ip": ip[peer_index],
            "bgp_as": str(bgp_as[index]) if index < len(bgp_as) and bgp_as[index] else None,
            "peer_bgp_as": str(bgp_as[peer_index]) if peer_index < len(bgp_as) and bgp_as[peer_index] else None,
            "description": descriptions[index],
        }

        if (
            self.shared_utils.hostname in p2p_link.port_channel.nodes_child_interfaces
            and p2p_link.port_channel.nodes_child_interfaces[self.shared_utils.hostname].interfaces
        ):
            node_data = p2p_link.port_channel.nodes_child_interfaces[self.shared_utils.hostname]
            # Port-channel
            default_channel_id = int("".join(re.findall(r"\d", node_data.interfaces[0])))
            portchannel_id = node_data.channel_id or default_channel_id

            if peer not in p2p_link.port_channel.nodes_child_interfaces:
                msg = f"{peer} under {self.data_model}.p2p_links.[].port_channel.nodes_child_interfaces"
                raise AristaAvdMissingVariableError(msg)

            peer_data = p2p_link.port_channel.nodes_child_interfaces[peer]
            default_peer_channel_id = int("".join(re.findall(r"\d", peer_data.interfaces[0])))
            peer_id = peer_data.channel_id or default_peer_channel_id

            data.update(
                {
                    "interface": f"Port-Channel{portchannel_id}",
                    "peer_interface": f"Port-Channel{peer_id}",
                    "port_channel_id": portchannel_id,
                    "peer_port_channel_id": peer_id,
                    "port_channel_description": p2p_link.port_channel.description,
                    "port_channel_members": [
                        {
                            "interface": interface,
                            "peer_interface": peer_data.interfaces[index],
                        }
                        for index, interface in enumerate(node_data.interfaces)
                    ],
                },
            )
            return data

        if p2p_link.interfaces:
            # Ethernet
            data.update(
                {
                    "interface": p2p_link.interfaces[index],
                    "peer_interface": p2p_link.interfaces[peer_index],
                    "port_channel_id": None,
                    "peer_port_channel_id": None,
                    "port_channel_description": None,
                    "port_channel_members": [],
                },
            )
            return data

        msg = f"{self.data_model}.p2p_links must have either 'interfaces' or 'port_channel' with correct members set."
        raise AristaAvdInvalidInputsError(msg)

    def _get_common_interface_cfg(self: AvdStructuredConfigCoreInterfacesAndL3Edge, p2p_link: T_P2pLinksItem, p2p_link_data: dict) -> dict:
        """
        Return partial structured_config for one p2p_link.

        Covers common config that is applicable to both port-channels and ethernet interfaces.
        This config will only be used on the main interface - so not port-channel members.
        """
        index = p2p_link.nodes.index(self.shared_utils.hostname)
        interface_cfg = {
            "name": p2p_link_data["interface"],
            "peer": p2p_link_data["peer"],
            "peer_interface": p2p_link_data["peer_interface"],
            "peer_type": p2p_link_data["peer_type"],
            "switchport": {"enabled": False},
            "shutdown": False,
            "mtu": p2p_link._get("mtu", self.shared_utils.p2p_uplinks_mtu) if self.shared_utils.platform_settings.feature_support.per_interface_mtu else None,
            "service_profile": p2p_link._get("qos_profile", self.inputs.p2p_uplinks_qos_profile),
            "eos_cli": p2p_link.raw_eos_cli,
        }

        if p2p_link.structured_config:
            if str(interface_name := p2p_link_data["interface"]).lower().startswith("p"):
                # Port-channel
                self.custom_structured_configs.nested.port_channel_interfaces.obtain(interface_name)._deepmerge(
                    EosCliConfigGen.PortChannelInterfacesItem._from_dict(p2p_link.structured_config),
                    list_merge=self.custom_structured_configs.list_merge_strategy,
                )
            else:
                # Ethernet
                self.custom_structured_configs.nested.ethernet_interfaces.obtain(interface_name)._deepmerge(
                    EosCliConfigGen.EthernetInterfacesItem._from_dict(p2p_link.structured_config),
                    list_merge=self.custom_structured_configs.list_merge_strategy,
                )

        if p2p_link.ip:
            interface_cfg["ip_address"] = p2p_link.ip[index]

        if p2p_link.ptp.enabled:
            ptp_config = {}

            if self.shared_utils.ptp_enabled:
                # Apply PTP profile config from node settings when profile is not defined on p2p_link
                if not p2p_link.ptp.profile:
                    ptp_config.update(self.shared_utils.ptp_profile._as_dict(include_default_values=True))

                # Apply PTP profile defined for the p2p_link
                elif p2p_link.ptp.profile not in self.inputs.ptp_profiles:
                    msg = f"PTP Profile '{p2p_link.ptp.profile}' referenced under {self.data_model}.p2p_links does not exist in `ptp_profiles`."
                    raise AristaAvdInvalidInputsError(msg)

                else:
                    ptp_config.update(self.inputs.ptp_profiles[p2p_link.ptp.profile]._as_dict(include_default_values=True))

            node_index = p2p_link.nodes._as_list().index(self.shared_utils.hostname)  # TODO: Implement .index() method on AvdList and AvdIndexedList class.
            if len(p2p_link.ptp.roles) > node_index and p2p_link.ptp.roles[node_index] == "master":
                ptp_config["role"] = "master"

            ptp_config["enable"] = True
            ptp_config.pop("profile", None)

            interface_cfg["ptp"] = ptp_config

        if p2p_link.include_in_underlay_protocol:
            if p2p_link.underlay_multicast and self.shared_utils.underlay_multicast:
                interface_cfg["pim"] = {"ipv4": {"sparse_mode": True}}

            if (self.inputs.underlay_rfc5549 and p2p_link.routing_protocol != "ebgp") or p2p_link.ipv6_enable is True:
                interface_cfg["ipv6_enable"] = True

            if self.shared_utils.underlay_ospf:
                interface_cfg.update(
                    {
                        "ospf_network_point_to_point": True,
                        "ospf_area": self.inputs.underlay_ospf_area,
                    },
                )

            if self.shared_utils.underlay_isis:
                interface_cfg.update(
                    {
                        "isis_enable": self.shared_utils.isis_instance_name,
                        "isis_bfd": self.inputs.underlay_isis_bfd or None,
                        "isis_metric": default(p2p_link.isis_metric, self.inputs.isis_default_metric),
                        "isis_network_point_to_point": p2p_link.isis_network_type == "point-to-point",
                        "isis_hello_padding": p2p_link.isis_hello_padding,
                        "isis_circuit_type": default(p2p_link.isis_circuit_type, self.inputs.isis_default_circuit_type),
                    },
                )
                if isis_authentication_mode := default(p2p_link.isis_authentication_mode, self.inputs.underlay_isis_authentication_mode):
                    interface_cfg.setdefault("isis_authentication", {}).setdefault("both", {})["mode"] = isis_authentication_mode

                if (isis_authentication_key := default(p2p_link.isis_authentication_key, self.inputs.underlay_isis_authentication_key)) is not None:
                    interface_cfg.setdefault("isis_authentication", {}).setdefault("both", {}).update(
                        {
                            "key": isis_authentication_key,
                            "key_type": "7",
                        }
                    )

        if p2p_link.macsec_profile:
            interface_cfg["mac_security"] = {"profile": p2p_link.macsec_profile}

        if (p2p_link_sflow := default(p2p_link.sflow, self._p2p_links_sflow)) is not None:
            interface_cfg["sflow"] = {"enable": p2p_link_sflow}

        if (p2p_link_flow_tracking := self.shared_utils.get_flow_tracker(p2p_link.flow_tracking)) is not None:
            interface_cfg["flow_tracker"] = p2p_link_flow_tracking

        if self.shared_utils.mpls_lsr and default(p2p_link.mpls_ip, True):  # noqa: FBT003
            interface_cfg["mpls"] = {"ip": True}
            if p2p_link.include_in_underlay_protocol is True and self.shared_utils.underlay_ldp and default(p2p_link.mpls_ldp, True):  # noqa: FBT003
                interface_cfg["mpls"]["ldp"] = {"interface": True, "igp_sync": True}

        return interface_cfg

    def _get_ethernet_cfg(self: AvdStructuredConfigCoreInterfacesAndL3Edge, p2p_link: T_P2pLinksItem) -> dict:
        """
        Return partial structured_config for one p2p_link.

        Covers config that is only applicable to ethernet interfaces.
        This config will only be used on both main interfaces and port-channel members.
        """
        return {"speed": p2p_link.speed}

    def _get_port_channel_member_cfg(self: AvdStructuredConfigCoreInterfacesAndL3Edge, p2p_link: T_P2pLinksItem, p2p_link_data: dict, member: dict) -> dict:
        """
        Return partial structured_config for one p2p_link.

        Covers config for ethernet interfaces that are port-channel members.
        """
        return {
            "name": member["interface"],
            "peer": p2p_link_data["peer"],
            "peer_interface": member["peer_interface"],
            "peer_type": p2p_link_data["peer_type"],
            "shutdown": False,
            "channel_group": {
                "id": p2p_link_data["port_channel_id"],
                "mode": p2p_link.port_channel.mode,
            },
        }
