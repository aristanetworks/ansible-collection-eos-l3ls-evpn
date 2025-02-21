# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import get, short_esi_to_route_target
from pyavd.api.interface_descriptions import InterfaceDescriptionData
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigUnderlayProtocol


class PortChannelInterfacesMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def port_channel_interfaces(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set structured config for port_channel_interfaces."""
        # Port channel set is used to avoid creating the same underlay port-channel multiple times.
        port_channel_set = set()
        for link in self._underlay_links:
            if link["type"] != "underlay_l2" or link.get("channel_group_id") is None:
                continue

            if (channel_group_id := link.get("channel_group_id")) in port_channel_set:
                continue

            port_channel_set.add(channel_group_id)

            port_channel_name = f"Port-Channel{link['channel_group_id']}"

            description = self.shared_utils.interface_descriptions.underlay_port_channel_interface(
                InterfaceDescriptionData(
                    shared_utils=self.shared_utils,
                    interface=port_channel_name,
                    link_type="underlay_l2",
                    peer=link["peer"],
                    peer_interface=f"Port-Channel{link['peer_channel_group_id']}",
                    peer_channel_group_id=link["peer_channel_group_id"],
                    port_channel_id=link["channel_group_id"],
                    peer_node_group=link.get("peer_node_group"),
                )
            )
            port_channel_interface = EosCliConfigGen.PortChannelInterfacesItem(
                name=port_channel_name,
                description=description or None,
                shutdown=False,
                service_profile=self.inputs.p2p_uplinks_qos_profile,
                flow_tracker=self.shared_utils.new_get_flow_tracker(link.get("flow_tracking"), EosCliConfigGen.PortChannelInterfacesItem.FlowTracker),
                spanning_tree_portfast=link.get("spanning_tree_portfast"),
            )
            port_channel_interface.switchport._update(enabled=True, mode="trunk")
            port_channel_interface.switchport.trunk.native_vlan = link.get("native_vlan")

            if (trunk_groups := link.get("trunk_groups")) is not None:
                port_channel_interface.switchport.trunk.groups.extend(trunk_groups)
            elif (vlans := link.get("vlans")) is not None:
                port_channel_interface.switchport.trunk.allowed_vlan = vlans

            if sflow := link.get("sflow"):
                port_channel_interface.sflow.enable = sflow["enable"]

            if link_tracking_groups := link.get("link_tracking_groups"):
                for link_tracking_group in link_tracking_groups:
                    port_channel_interface.link_tracking_groups.append_new(
                        name=link_tracking_group["name"],
                        direction=link_tracking_group["direction"],
                    )

            # Configure MLAG on MLAG switches if either 'mlag_on_orphan_port_channel_downlink' or 'link.mlag' is True
            if self.shared_utils.mlag is True and any([self.inputs.mlag_on_orphan_port_channel_downlink, link.get("mlag", True)]):
                port_channel_interface.mlag = int(channel_group_id)

            if (short_esi := link.get("short_esi")) is not None:
                port_channel_interface.evpn_ethernet_segment._update(
                    identifier=f"{self.inputs.evpn_short_esi_prefix}{short_esi}",
                    route_target=short_esi_to_route_target(short_esi),
                )
                port_channel_interface.lacp_id = short_esi.replace(":", ".")

            # PTP
            if get(link, "ptp.enable") is True:
                # Apply PTP profile config if using the new ptp config style
                if self.shared_utils.ptp_enabled:
                    # Create a copy and removes the .profile attribute since the target model has a .profile key with a different schema.
                    ptp_profile_config = self.shared_utils.ptp_profile._deepcopy()
                    delattr(ptp_profile_config, "profile")
                    port_channel_interface.ptp = ptp_profile_config._cast_as(EosCliConfigGen.PortChannelInterfacesItem.Ptp, ignore_extra_keys=True)

                port_channel_interface.ptp.enable = True

            # Inband ZTP Port-Channel LACP Fallback
            if get(link, "inband_ztp_vlan"):
                port_channel_interface._update(lacp_fallback_mode="individual", lacp_fallback_timeout=get(link, "inband_ztp_lacp_fallback_delay"))

            # Structured Config
            if structured_config := link.get("structured_config"):
                self.custom_structured_configs.nested.port_channel_interfaces.obtain(port_channel_name)._deepmerge(
                    EosCliConfigGen.PortChannelInterfacesItem._from_dict(structured_config), list_merge=self.custom_structured_configs.list_merge_strategy
                )

            self.structured_config.port_channel_interfaces.append(port_channel_interface)

        # Support l3_port_channels including sub-interfaces
        subif_parent_port_channel_names = set()
        regular_l3_port_channel_names = set()
        for l3_port_channel in self.shared_utils.node_config.l3_port_channels:
            interface_name = l3_port_channel.name
            is_subinterface = "." in interface_name
            if not is_subinterface:
                # This is a regular Port-Channel (not sub-interface)
                regular_l3_port_channel_names.add(interface_name)
                continue
            # This is a subinterface for a port-channel interface.
            # We need to ensure that parent port-channel interface is also included explicitly
            # within list of Port-Channel interfaces.
            parent_port_channel_name = interface_name.split(".", maxsplit=1)[0]
            subif_parent_port_channel_names.add(parent_port_channel_name)
            if l3_port_channel.member_interfaces:
                msg = f"L3 Port-Channel sub-interface '{interface_name}' has 'member_interfaces' set. This is not a valid setting."
                raise AristaAvdInvalidInputsError(msg)
            if l3_port_channel._get("mode"):
                # implies 'mode' is set when not applicable for a sub-interface
                msg = f"L3 Port-Channel sub-interface '{interface_name}' has 'mode' set. This is not a valid setting."
                raise AristaAvdInvalidInputsError(msg)

        # Sanity check if there are any sub-interfaces for which parent Port-channel is not explicitly specified
        if missing_parent_port_channels := subif_parent_port_channel_names.difference(regular_l3_port_channel_names):
            msg = (
                f"One or more L3 Port-Channels '{', '.join(natural_sort(missing_parent_port_channels))}' "
                "need to be specified as they have sub-interfaces referencing them."
            )
            raise AristaAvdInvalidInputsError(msg)

        # Now that validation is complete, we can make another pass at all l3_port_channels
        # (subinterfaces or otherwise) and generate their structured config.
        for l3_port_channel in self.shared_utils.node_config.l3_port_channels:
            self._set_l3_port_channel(l3_port_channel)

        # WAN HA interface for direct connection
        self._set_direct_ha_port_channel_interface()

    def _set_l3_port_channel(
        self: AvdStructuredConfigUnderlayProtocol, l3_port_channel: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3PortChannelsItem
    ) -> None:
        """Set structured_configuration for one L3 Port-Channel."""
        # build common portion of the interface cfg
        interface = self._get_l3_common_interface_cfg(l3_port_channel)

        interface_description = l3_port_channel.description
        if not interface_description:
            interface_description = self.shared_utils.interface_descriptions.underlay_port_channel_interface(
                InterfaceDescriptionData(
                    shared_utils=self.shared_utils,
                    interface=l3_port_channel.name,
                    peer=l3_port_channel.peer,
                    peer_interface=l3_port_channel.peer_port_channel,
                    wan_carrier=l3_port_channel.wan_carrier,
                    wan_circuit_id=l3_port_channel.wan_circuit_id,
                ),
            )
        interface._update(description=interface_description, peer_type="l3_port_channel", peer_interface=l3_port_channel.peer_port_channel)

        if l3_port_channel.ipv4_acl_in:
            acl = self._get_acl_for_l3_generic_interface(l3_port_channel.ipv4_acl_in, l3_port_channel)
            interface.access_group_in = acl.name
            self._set_ipv4_acl(acl)

        if l3_port_channel.ipv4_acl_out:
            acl = self._get_acl_for_l3_generic_interface(l3_port_channel.ipv4_acl_out, l3_port_channel)
            interface.access_group_out = acl.name
            self._set_ipv4_acl(acl)

        if l3_port_channel.structured_config:
            self.custom_structured_configs.nested.port_channel_interfaces.obtain(l3_port_channel.name)._deepmerge(
                l3_port_channel.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )

        if (
            self.shared_utils.is_wan_router
            and (wan_carrier_name := l3_port_channel.wan_carrier) is not None
            and interface.access_group_in is None
            and (wan_carrier_name not in self.inputs.wan_carriers or not self.inputs.wan_carriers[wan_carrier_name].trusted)
        ):
            msg = (
                "'ipv4_acl_in' must be set on WAN interfaces where 'wan_carrier' is set, unless the carrier is configured as 'trusted' "
                f"under 'wan_carriers'. 'ipv4_acl_in' is missing on L3 Port-Channel '{l3_port_channel.name}'."
            )
            raise AristaAvdError(msg)

        self.structured_config.port_channel_interfaces.append(interface)

    def _set_direct_ha_port_channel_interface(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Return a dict containing the port-channel interface for direct HA."""
        if not self.shared_utils.use_port_channel_for_direct_ha:
            return

        direct_wan_ha_links_flow_tracker = self.shared_utils.new_get_flow_tracker(
            self.shared_utils.node_config.wan_ha.flow_tracking, EosCliConfigGen.PortChannelInterfacesItem.FlowTracker
        )
        port_channel_name = f"Port-Channel{self.shared_utils.wan_ha_port_channel_id}"
        description = self.shared_utils.interface_descriptions.wan_ha_port_channel_interface(
            InterfaceDescriptionData(
                shared_utils=self.shared_utils,
                interface=port_channel_name,
                peer=self.shared_utils.wan_ha_peer,
                peer_interface=port_channel_name,
            ),
        )

        self.structured_config.port_channel_interfaces.append_new(
            name=port_channel_name,
            switchport=EosCliConfigGen.PortChannelInterfacesItem.Switchport(enabled=False),
            peer_type="l3_interface",
            # TODO: if different interfaces used across nodes it will fail just like for mlag.
            peer_interface=port_channel_name,
            peer=self.shared_utils.wan_ha_peer,
            shutdown=False,
            description=description,
            ip_address=self.shared_utils.wan_ha_ip_addresses[0],
            flow_tracker=direct_wan_ha_links_flow_tracker,
            mtu=self.shared_utils.node_config.wan_ha.mtu,
        )
