# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol, overload

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdError, AristaAvdMissingVariableError
from pyavd._utils import Undefined, default, get, get_ip_from_ip_prefix, strip_empties_from_dict
from pyavd.j2filters import natural_sort, range_expand

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class UtilsMixin(Protocol):
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def _avd_peers(self: AvdStructuredConfigUnderlayProtocol) -> list:
        """
        Returns a list of peers.

        This cannot be loaded in shared_utils since it will not be calculated until EosDesignsFacts has been rendered
        and shared_utils are shared between EosDesignsFacts and AvdStructuredConfig classes like this one.
        """
        return natural_sort(get(self._hostvars, f"avd_topology_peers..{self.shared_utils.hostname}", separator="..", default=[]))

    @cached_property
    def _underlay_filter_peer_as_route_maps_asns(self: AvdStructuredConfigUnderlayProtocol) -> list:
        """Filtered ASNs."""
        if not self.inputs.underlay_filter_peer_as:
            return []

        # using set comprehension with `{}` to remove duplicates and then run natural_sort to convert to list.
        return natural_sort({link["peer_bgp_as"] for link in self._underlay_links if link["type"] == "underlay_p2p"})

    @cached_property
    def _underlay_links(self: AvdStructuredConfigUnderlayProtocol) -> list:
        """Returns the list of underlay links for this device."""
        underlay_links = []
        underlay_links.extend(self._uplinks)
        if self.inputs.fabric_sflow.uplinks is not None:
            for uplink in underlay_links:
                uplink.update({"sflow": {"enable": self.inputs.fabric_sflow.uplinks}})

        for uplink in underlay_links:
            uplink["flow_tracking"] = self.inputs.fabric_flow_tracking.uplinks

        downlinks_flow_tracking = self.inputs.fabric_flow_tracking.downlinks if self.inputs.fabric_flow_tracking.downlinks.enabled else None

        for peer in self._avd_peers:
            peer_facts = self.shared_utils.get_peer_facts(peer, required=True)
            for uplink in peer_facts["uplinks"]:
                if uplink["peer"] == self.shared_utils.hostname:
                    link = {
                        "interface": uplink["peer_interface"],
                        "peer": peer,
                        "peer_interface": uplink["interface"],
                        "peer_type": get(peer_facts, "type"),
                        "peer_is_deployed": peer_facts["is_deployed"],
                        "peer_bgp_as": get(peer_facts, "bgp_as"),
                        "type": get(uplink, "type", required=True),
                        "speed": get(uplink, "peer_speed", default=get(uplink, "speed")),
                        "ip_address": get(uplink, "peer_ip_address"),
                        "peer_ip_address": get(uplink, "ip_address"),
                        "prefix_length": get(uplink, "prefix_length"),
                        "channel_group_id": get(uplink, "peer_channel_group_id"),
                        "peer_channel_group_id": get(uplink, "channel_group_id"),
                        "peer_node_group": get(uplink, "node_group"),
                        "vlans": get(uplink, "vlans"),
                        "native_vlan": get(uplink, "native_vlan"),
                        "trunk_groups": get(uplink, "peer_trunk_groups"),
                        "bfd": get(uplink, "bfd"),
                        "ptp": get(uplink, "ptp"),
                        "mac_security": get(uplink, "mac_security"),
                        "short_esi": get(uplink, "peer_short_esi"),
                        "mlag": get(uplink, "peer_mlag"),
                        "underlay_multicast": get(uplink, "underlay_multicast"),
                        "ipv6_enable": get(uplink, "ipv6_enable"),
                        "sflow": {"enable": self.inputs.fabric_sflow.downlinks},
                        "flow_tracking": downlinks_flow_tracking,
                        "spanning_tree_portfast": get(uplink, "peer_spanning_tree_portfast"),
                        "structured_config": get(uplink, "structured_config"),
                    }
                    if get(peer_facts, "inband_ztp"):
                        # l2 inband ztp
                        link["inband_ztp_vlan"] = get(peer_facts, "inband_ztp_vlan")
                        link["inband_ztp_lacp_fallback_delay"] = get(peer_facts, "inband_ztp_lacp_fallback_delay")
                        # l3 inband ztp
                        link["dhcp_server"] = True

                    if (subinterfaces := get(uplink, "subinterfaces")) is not None:
                        link["subinterfaces"] = [
                            {
                                **subinterface,
                                "interface": subinterface["peer_interface"],
                                "peer_interface": subinterface["interface"],
                                "ip_address": subinterface.get("peer_ip_address"),
                                "peer_ip_address": subinterface.get("ip_address"),
                            }
                            for subinterface in subinterfaces
                        ]
                    underlay_links.append(strip_empties_from_dict(link))

        return natural_sort(underlay_links, "interface")

    @cached_property
    def _underlay_vlan_trunk_groups(self: AvdStructuredConfigUnderlayProtocol) -> list:
        """Returns a list of trunk groups to configure on the underlay link."""
        if self.inputs.enable_trunk_groups is not True:
            return []

        trunk_groups = []

        for peer in self._avd_peers:
            peer_facts = self.shared_utils.get_peer_facts(peer, required=True)
            for uplink in peer_facts["uplinks"]:
                if uplink["peer"] == self.shared_utils.hostname:
                    if (peer_trunk_groups := get(uplink, "peer_trunk_groups")) is None:
                        continue

                    trunk_groups.append(
                        {
                            "vlan_list": uplink["vlans"],
                            "trunk_groups": peer_trunk_groups,
                        },
                    )

        if trunk_groups:
            return trunk_groups

        return []

    @cached_property
    def _uplinks(self: AvdStructuredConfigUnderlayProtocol) -> list:
        return get(self._hostvars, "switch.uplinks")

    # These overloads are just here to help the type checker enforce that input type x gives output type y
    @overload
    def _get_l3_common_interface_cfg(
        self: AvdStructuredConfigUnderlayProtocol,
        l3_generic_interface: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem,
    ) -> EosCliConfigGen.EthernetInterfacesItem: ...

    @overload
    def _get_l3_common_interface_cfg(
        self: AvdStructuredConfigUnderlayProtocol,
        l3_generic_interface: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3PortChannelsItem,
    ) -> EosCliConfigGen.PortChannelInterfacesItem: ...

    def _get_l3_common_interface_cfg(
        self: AvdStructuredConfigUnderlayProtocol,
        l3_generic_interface: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem
        | EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3PortChannelsItem,
    ) -> EosCliConfigGen.EthernetInterfacesItem | EosCliConfigGen.PortChannelInterfacesItem:
        """Returns common structured_configuration for L3 interface or L3 Port-Channel."""
        # variables being set for constructing appropriate validation error
        if isinstance(l3_generic_interface, EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem):
            interface = EosCliConfigGen.EthernetInterfacesItem()
            schema_key = "l3_interfaces"
        else:
            # implies interface is "L3 Port-Channel"
            interface = EosCliConfigGen.PortChannelInterfacesItem()
            schema_key = "l3_port_channels"

        # logic below is common to l3_interface and l3_port_channel interface types

        # TODO: catch if ip_address is not valid or not dhcp
        if not l3_generic_interface.ip_address:
            msg = f"{self.shared_utils.node_type_key_data.key}.nodes[name={self.shared_utils.hostname}].{schema_key}"
            msg += f"[name={l3_generic_interface.name}].ip_address"
            raise AristaAvdMissingVariableError(msg)

        is_subinterface = "." in l3_generic_interface.name
        interface._update(
            name=l3_generic_interface.name,
            peer=l3_generic_interface.peer,
            ip_address=l3_generic_interface.ip_address,
            shutdown=not l3_generic_interface.enabled,
            service_profile=l3_generic_interface.qos_profile,
            eos_cli=l3_generic_interface.raw_eos_cli,
            flow_tracker=self.shared_utils.new_get_flow_tracker(l3_generic_interface.flow_tracking, interface.FlowTracker),
        )
        interface.switchport.enabled = False if "." not in l3_generic_interface.name else None

        if is_subinterface:
            interface.encapsulation_dot1q.vlan = default(
                l3_generic_interface.encapsulation_dot1q_vlan, int(l3_generic_interface.name.split(".", maxsplit=1)[-1])
            )

        if l3_generic_interface.ip_address == "dhcp" and l3_generic_interface.dhcp_accept_default_route:
            interface.dhcp_client_accept_default_route = True

        return interface

    def _get_l3_uplink_with_l2_as_subint(
        self: AvdStructuredConfigUnderlayProtocol, link: dict
    ) -> tuple[EosCliConfigGen.EthernetInterfacesItem, EosCliConfigGen.EthernetInterfaces]:
        """Return a tuple with main uplink interface, list of subinterfaces representing each SVI."""
        vlans = [int(vlan) for vlan in range_expand(link["vlans"])]

        # Main interface
        # Routed interface with no config unless there is an SVI matching the native-vlan, then it will contain the config for that SVI

        interfaces = EosCliConfigGen.EthernetInterfaces()
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for svi in vrf.svis:
                    # Skip any vlans not part of the link
                    if svi.id not in vlans:
                        continue

                    interfaces.append(self._get_l2_as_subint(link, svi, vrf))

        # If we have the main interface covered, we can just remove it from the list and return as main interface.
        # Otherwise we return an almost empty dict as the main interface since it was already covered by the calling function.
        if link["interface"] in interfaces:
            main_interface = interfaces[link["interface"]]
            del main_interface.description
            del interfaces[link["interface"]]
        else:
            main_interface = EosCliConfigGen.EthernetInterfacesItem(
                switchport=EosCliConfigGen.EthernetInterfacesItem.Switchport(enabled=False), mtu=self.shared_utils.p2p_uplinks_mtu
            )

        if (mtu := default(main_interface.mtu, 1500)) != self.shared_utils.p2p_uplinks_mtu:
            msg = (
                f"MTU '{self.shared_utils.p2p_uplinks_mtu}' set for 'p2p_uplinks_mtu' conflicts with MTU '{mtu}' "
                f"set on SVI for uplink_native_vlan '{link['native_vlan']}'."
                "Either adjust the MTU on the SVI or p2p_uplinks_mtu or change/remove the uplink_native_vlan setting."
            )
            raise AristaAvdError(msg)
        return main_interface, interfaces

    def _get_l2_as_subint(
        self: AvdStructuredConfigUnderlayProtocol,
        link: dict,
        svi: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> EosCliConfigGen.EthernetInterfacesItem:
        """
        Return structured config for one subinterface representing the given SVI.

        Only supports static IPs or VRRP.
        """
        is_native = svi.id == link.get("native_vlan")
        interface_name = link["interface"] if is_native else f"{link['interface']}.{svi.id}"
        subinterface = EosCliConfigGen.EthernetInterfacesItem(
            name=interface_name,
            peer=link["peer"],
            peer_interface=f"{link['peer_interface']} VLAN {svi.id}",
            peer_type=link["peer_type"],
            description=default(svi.description, svi.name),
            shutdown=not default(svi.enabled, False),  # noqa: FBT003
            switchport=EosCliConfigGen.EthernetInterfacesItem.Switchport(enabled=False) if is_native else Undefined,
            encapsulation_dot1q=EosCliConfigGen.EthernetInterfacesItem.EncapsulationDot1q(vlan=svi.id) if not is_native else Undefined,
            vrf=vrf.name if vrf.name != "default" else None,
            ip_address=svi.ip_address,
            ipv6_address=svi.ipv6_address,
            ipv6_enable=svi.ipv6_enable,
            mtu=svi.mtu if self.shared_utils.platform_settings.feature_support.per_interface_mtu else None,
            eos_cli=svi.raw_eos_cli,
        )

        if (flow_tracking := link.get("flow_tracking")) and (
            flow_tracker := self.shared_utils.new_get_flow_tracker(flow_tracking, EosCliConfigGen.EthernetInterfacesItem.FlowTracker)
        ):
            subinterface.flow_tracker = flow_tracker

        if svi.structured_config:
            self.custom_structured_configs.nested.ethernet_interfaces.obtain(interface_name)._deepmerge(
                svi.structured_config._cast_as(EosCliConfigGen.EthernetInterfacesItem, ignore_extra_keys=True),
                list_merge=self.custom_structured_configs.list_merge_strategy,
            )

        if subinterface.mtu and self.shared_utils.p2p_uplinks_mtu and subinterface.mtu > self.shared_utils.p2p_uplinks_mtu:
            msg = (
                f"MTU '{self.shared_utils.p2p_uplinks_mtu}' set for 'p2p_uplinks_mtu' must be larger or equal to MTU '{subinterface.mtu}' "
                f"set on the SVI '{svi.id}'."
                "Either adjust the MTU on the SVI or p2p_uplinks_mtu."
            )
            raise AristaAvdError(msg)

        # Only set VRRPv4 if ip_address is set
        if subinterface.ip_address:
            # TODO: in separate PR adding VRRP support for SVIs
            pass

        # Only set VRRPv6 if ipv6_address is set
        if subinterface.ipv6_address:
            # TODO: in separate PR adding VRRP support for SVIs
            pass

        # Adding IP helpers and OSPF via a common function also used for SVIs on L3 switches.
        self.shared_utils.get_additional_svi_config(subinterface, svi, vrf)

        return subinterface

    def _get_acl_for_l3_generic_interface(
        self: AvdStructuredConfigUnderlayProtocol,
        acl_name: str,
        interface: (
            EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem
            | EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3PortChannelsItem
        ),
    ) -> EosDesigns.Ipv4AclsItem:
        interface_ip = interface.dhcp_ip if (ip_address := interface.ip_address) == "dhcp" else ip_address
        if interface_ip is not None and "/" in interface_ip:
            interface_ip = get_ip_from_ip_prefix(interface_ip)

        return self.shared_utils.get_ipv4_acl(
            name=acl_name,
            interface_name=interface.name,
            interface_ip=interface_ip,
            peer_ip=interface.peer_ip,
        )
