# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdError, AristaAvdMissingVariableError
from pyavd._utils import Undefined, get
from pyavd.api.interface_descriptions import InterfaceDescriptionData
from pyavd.j2filters import encrypt, natural_sort

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigUnderlayProtocol


class EthernetInterfacesMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def ethernet_interfaces(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set structured config for ethernet_interfaces."""
        for link in self._underlay_links:
            # common values
            description = self.shared_utils.interface_descriptions.underlay_ethernet_interface(
                InterfaceDescriptionData(
                    shared_utils=self.shared_utils,
                    interface=link["interface"],
                    link_type=link["type"],
                    peer=link["peer"],
                    peer_interface=link["peer_interface"],
                ),
            )
            ethernet_interface = EosCliConfigGen.EthernetInterfacesItem(
                name=link["interface"],
                peer=link["peer"],
                peer_interface=link["peer_interface"],
                peer_type=link["peer_type"],
                description=description or None,
                speed=link.get("speed", Undefined),
                shutdown=self.inputs.shutdown_interfaces_towards_undeployed_peers and not link["peer_is_deployed"],
            )

            # L3 interface
            # Used for p2p uplinks as well as main interface for p2p-vrfs.
            if link["type"] == "underlay_p2p":
                ethernet_interface._update(
                    mtu=self.shared_utils.p2p_uplinks_mtu,
                    service_profile=self.inputs.p2p_uplinks_qos_profile,
                    ipv6_enable=link.get("ipv6_enable", Undefined),
                    flow_tracker=self.shared_utils.new_get_flow_tracker(
                        link.get("flow_tracking"), output_type=EosCliConfigGen.EthernetInterfacesItem.FlowTracker
                    ),
                )
                ethernet_interface.switchport.enabled = False
                if mac_security := link.get("mac_security"):
                    ethernet_interface.mac_security.profile = mac_security["profile"]

                if link_tracking_groups := link.get("link_tracking_groups"):
                    for link_tracking_group in link_tracking_groups:
                        ethernet_interface.link_tracking_groups.append_new(
                            name=link_tracking_group["name"],
                            direction=link_tracking_group["direction"],
                        )
                if sflow := link.get("sflow"):
                    ethernet_interface.sflow.enable = sflow["enable"]

                # PTP
                if get(link, "ptp.enable") is True:
                    # Apply PTP profile config if using the new ptp config style
                    if self.shared_utils.ptp_enabled:
                        # Create a copy and removes the .profile attribute since the target model has a .profile key with a different schema.
                        ptp_profile_config = self.shared_utils.ptp_profile._deepcopy()
                        delattr(ptp_profile_config, "profile")
                        ethernet_interface.ptp = ptp_profile_config._cast_as(EosCliConfigGen.EthernetInterfacesItem.Ptp, ignore_extra_keys=True)

                    ethernet_interface.ptp.enable = True

                # MPLS
                if self.shared_utils.underlay_mpls:
                    ethernet_interface.mpls.ip = True
                    if self.shared_utils.underlay_ldp is True:
                        ethernet_interface.mpls.ldp._update(interface=True, igp_sync=True)

                # IP address
                if link.get("ip_address") is not None:
                    if "unnumbered" in link["ip_address"].lower():
                        ethernet_interface.ip_address = link["ip_address"]
                    else:
                        ethernet_interface.ip_address = f"{link['ip_address']}/{link['prefix_length']}"

                if self.shared_utils.underlay_ospf is True:
                    ethernet_interface.ospf_network_point_to_point = True
                    ethernet_interface.ospf_area = self.inputs.underlay_ospf_area
                    ospf_authentication = self.inputs.underlay_ospf_authentication.enabled
                    ospf_message_digest_keys = self.inputs.underlay_ospf_authentication.message_digest_keys
                    if ospf_authentication:
                        if not ospf_message_digest_keys:
                            msg = "'underlay_ospf_authentication.enabled' is True but no message-digest keys with both key and ID are defined."
                            raise AristaAvdError(msg)

                        ethernet_interface.ospf_authentication = "message-digest"
                        for ospf_key in ospf_message_digest_keys:
                            ethernet_interface.ospf_message_digest_keys.append_new(
                                id=ospf_key.id,
                                hash_algorithm=ospf_key.hash_algorithm,
                                key=encrypt(
                                    ospf_key.key,
                                    passwd_type="ospf_message_digest",  # NOSONAR # noqa: S106
                                    key=ethernet_interface.name,
                                    hash_algorithm=ospf_key.hash_algorithm,
                                    key_id=ospf_key.id,
                                ),
                            )

                if self.shared_utils.underlay_isis is True:
                    ethernet_interface._update(
                        isis_enable=self.shared_utils.isis_instance_name,
                        isis_bfd=self.inputs.underlay_isis_bfd or None,
                        isis_metric=self.inputs.isis_default_metric,
                        isis_network_point_to_point=True,
                        isis_circuit_type=self.inputs.isis_default_circuit_type,
                    )
                    if self.inputs.underlay_isis_authentication_mode:
                        ethernet_interface.isis_authentication.both.mode = self.inputs.underlay_isis_authentication_mode

                    if self.inputs.underlay_isis_authentication_key is not None:
                        ethernet_interface.isis_authentication.both._update(key=self.inputs.underlay_isis_authentication_key, key_type="7")

                if link.get("underlay_multicast") is True:
                    ethernet_interface.pim.ipv4.sparse_mode = True

                # DHCP server settings (primarily used for ZTP)
                if link.get("ip_address") is not None and "unnumbered" not in link["ip_address"].lower() and link.get("dhcp_server"):
                    ethernet_interface.dhcp_server_ipv4 = True

                # Structured Config
                if structured_config := link.get("structured_config"):
                    self.custom_structured_configs.nested.ethernet_interfaces.obtain(link["interface"])._deepmerge(
                        EosCliConfigGen.EthernetInterfacesItem._from_dict(structured_config), list_merge=self.custom_structured_configs.list_merge_strategy
                    )

                self.structured_config.ethernet_interfaces.append(ethernet_interface)

            # L2 interface
            elif link["type"] == "underlay_l2":
                if self.shared_utils.network_services_l2_as_subint:
                    # Render L3 subinterfaces for each SVI.
                    # The peer will just render a regular trunk.
                    main_interface, ethernet_subinterfaces = self._get_l3_uplink_with_l2_as_subint(link)
                    ethernet_interface._deepmerge(main_interface)
                    self.structured_config.ethernet_interfaces.extend(ethernet_subinterfaces)

                elif (channel_group_id := link.get("channel_group_id")) is not None:
                    # Render port-channel member
                    ethernet_interface.channel_group._update(id=int(channel_group_id), mode="active")
                    if get(link, "inband_ztp_vlan"):
                        ethernet_interface.switchport._update(enabled=True, mode="access", access_vlan=link["inband_ztp_vlan"])
                else:
                    # Render trunk interface
                    ethernet_interface.switchport._update(enabled=True, mode="trunk")
                    ethernet_interface.switchport.trunk._update(
                        allowed_vlan=link["vlans"],
                        native_vlan=link.get("native_vlan", Undefined),
                    )
                    ethernet_interface._update(
                        service_profile=self.inputs.p2p_uplinks_qos_profile,
                        spanning_tree_portfast=link.get("spanning_tree_portfast", Undefined),
                        flow_tracker=self.shared_utils.new_get_flow_tracker(
                            link.get("flow_tracking"), output_type=EosCliConfigGen.EthernetInterfacesItem.FlowTracker
                        ),
                    )
                    if link_tracking_groups := link.get("link_tracking_groups"):
                        for link_tracking_group in link_tracking_groups:
                            ethernet_interface.link_tracking_groups.append_new(
                                name=link_tracking_group["name"],
                                direction=link_tracking_group["direction"],
                            )

                self.structured_config.ethernet_interfaces.append(ethernet_interface)

            # Adding subinterfaces for each VRF after the main interface.
            if link["type"] == "underlay_p2p" and "subinterfaces" in link:
                for subinterface in get(link, "subinterfaces", default=[]):
                    description = self.shared_utils.interface_descriptions.underlay_ethernet_interface(
                        InterfaceDescriptionData(
                            shared_utils=self.shared_utils,
                            interface=subinterface["interface"],
                            link_type=link["type"],
                            peer=link["peer"],
                            peer_interface=subinterface["peer_interface"],
                            vrf=subinterface["vrf"],
                        ),
                    )
                    ethernet_subinterface = EosCliConfigGen.EthernetInterfacesItem(
                        name=subinterface["interface"],
                        peer=link["peer"],
                        peer_interface=subinterface["peer_interface"],
                        peer_type=link["peer_type"],
                        vrf=subinterface["vrf"],
                        # TODO: - for now reusing the encapsulation as it is hardcoded to the VRF ID which is used as
                        # subinterface name
                        description=description or None,
                        shutdown=self.inputs.shutdown_interfaces_towards_undeployed_peers and not link["peer_is_deployed"],
                        ipv6_enable=subinterface.get("ipv6_enable", Undefined),
                        mtu=self.shared_utils.p2p_uplinks_mtu,
                        flow_tracker=self.shared_utils.new_get_flow_tracker(link.get("flow_tracking"), EosCliConfigGen.EthernetInterfacesItem.FlowTracker),
                    )
                    ethernet_subinterface.encapsulation_dot1q.vlan = subinterface["encapsulation_dot1q_vlan"]

                    if sflow := link.get("sflow"):
                        ethernet_subinterface.sflow.enable = sflow["enable"]

                    if subinterface.get("ip_address") is not None:
                        ethernet_subinterface.ip_address = f"{subinterface['ip_address']}/{subinterface['prefix_length']}"

                    self.structured_config.ethernet_interfaces.append(ethernet_subinterface)

        # Support l3_interface as sub interfaces
        subif_parent_interface_names = set()
        for l3_interface in self.shared_utils.l3_interfaces:
            if "." in l3_interface.name:
                # This is a subinterface so we need to ensure that the parent is created
                parent_interface_name, _ = l3_interface.name.split(".", maxsplit=1)
                subif_parent_interface_names.add(parent_interface_name)

            self._set_l3_interface(l3_interface)

        subif_parent_interface_names = subif_parent_interface_names.difference(self.structured_config.ethernet_interfaces.keys())
        if subif_parent_interface_names:
            for interface_name in natural_sort(subif_parent_interface_names):
                self.structured_config.ethernet_interfaces.append_new(
                    name=interface_name,
                    switchport=EosCliConfigGen.EthernetInterfacesItem.Switchport(enabled=False),
                    peer_type="l3_interface",
                    shutdown=False,
                )

        # WAN HA interface(s) for direct connection
        self._set_direct_ha_ethernet_interfaces()

        # Member ethernet ports for Port-Channel interface
        for l3_port_channel in self.shared_utils.node_config.l3_port_channels:
            # sub-interface for l3_port_channel cannot have member eth ports
            # skip any logic to generate member port config for such sub-interfaces
            if "." in l3_port_channel.name:
                continue
            self._set_l3_port_channel_member_ports(l3_port_channel)

    def _set_l3_interface(
        self: AvdStructuredConfigUnderlayProtocol, l3_interface: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem
    ) -> None:
        """Set structured_configuration for one L3 interface."""
        # build common portion of the interface cfg
        interface = self._get_l3_common_interface_cfg(l3_interface)

        interface_description = l3_interface.description
        if not interface_description:
            interface_description = self.shared_utils.interface_descriptions.underlay_ethernet_interface(
                InterfaceDescriptionData(
                    shared_utils=self.shared_utils,
                    interface=l3_interface.name,
                    peer=l3_interface.peer,
                    peer_interface=l3_interface.peer_interface,
                    wan_carrier=l3_interface.wan_carrier,
                    wan_circuit_id=l3_interface.wan_circuit_id,
                ),
            )
        interface._update(
            description=interface_description or None,
            peer_type="l3_interface",
            peer_interface=l3_interface.peer_interface,
            speed=l3_interface.speed,
        )
        if l3_interface.ipv4_acl_in:
            acl = self._get_acl_for_l3_generic_interface(l3_interface.ipv4_acl_in, l3_interface)
            interface.access_group_in = acl.name
            self._set_ipv4_acl(acl)

        if l3_interface.ipv4_acl_out:
            acl = self._get_acl_for_l3_generic_interface(l3_interface.ipv4_acl_out, l3_interface)
            interface.access_group_out = acl.name
            self._set_ipv4_acl(acl)

        if l3_interface.structured_config:
            self.custom_structured_configs.nested.ethernet_interfaces.obtain(l3_interface.name)._deepmerge(
                l3_interface.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )
        if self.inputs.fabric_sflow.l3_interfaces is not None:
            interface.sflow.enable = self.inputs.fabric_sflow.l3_interfaces

        if (
            self.shared_utils.is_wan_router
            and (wan_carrier_name := l3_interface.wan_carrier) is not None
            and interface.access_group_in is None
            and (wan_carrier_name not in self.inputs.wan_carriers or not self.inputs.wan_carriers[wan_carrier_name].trusted)
        ):
            msg = (
                "'ipv4_acl_in' must be set on WAN interfaces where 'wan_carrier' is set, unless the carrier is configured as 'trusted' "
                f"under 'wan_carriers'. 'ipv4_acl_in' is missing on L3 interface '{l3_interface.name}'."
            )
            raise AristaAvdError(msg)

        self.structured_config.ethernet_interfaces.append(interface)

    def _set_l3_port_channel_member_ports(
        self: AvdStructuredConfigUnderlayProtocol, l3_port_channel: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3PortChannelsItem
    ) -> None:
        """
        Returns structured_configuration (list of ethernet interfaces) representing member ports for one L3 Port-Channel.

        only being called for l3_port_channel which is not a sub-interface
        """
        channel_group_id = l3_port_channel.name.split("Port-Channel")[-1]
        for member_intf in l3_port_channel.member_interfaces:
            interface_description = member_intf.description
            # derive values for peer from parent L3 port-channel
            # if not defined explicitly for member interface
            peer = member_intf.peer if member_intf.peer else l3_port_channel.peer
            if not interface_description:
                interface_description = self.shared_utils.interface_descriptions.underlay_ethernet_interface(
                    InterfaceDescriptionData(
                        shared_utils=self.shared_utils,
                        interface=member_intf.name,
                        peer=peer,
                        peer_interface=member_intf.peer_interface,
                    ),
                )
            self.structured_config.ethernet_interfaces.append_new(
                name=member_intf.name,
                description=interface_description or None,
                peer_type="l3_port_channel_member",
                peer=peer,
                peer_interface=member_intf.peer_interface,
                shutdown=not l3_port_channel.enabled,
                speed=member_intf.speed if member_intf.speed else None,
                channel_group=EosCliConfigGen.EthernetInterfacesItem.ChannelGroup(id=int(channel_group_id), mode=l3_port_channel.mode),
            )
            if member_intf.structured_config:
                self.custom_structured_configs.nested.ethernet_interfaces.obtain(member_intf.name)._deepmerge(
                    member_intf.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
                )

    def _set_direct_ha_ethernet_interfaces(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """
        Set ethernet interfaces to be configured for WAN direct HA.

        Caters for the scenarii where either a port-channel is used or a single l3_interface.
        """
        if self.shared_utils.use_uplinks_for_wan_ha:
            return

        direct_wan_ha_links_flow_tracker = self.shared_utils.new_get_flow_tracker(
            self.shared_utils.node_config.wan_ha.flow_tracking, EosCliConfigGen.EthernetInterfacesItem.FlowTracker
        )

        if not self.shared_utils.node_config.wan_ha.ha_interfaces:
            msg = "wan_ha.ha_interfaces"
            raise AristaAvdMissingVariableError(msg)

        for index, interface in enumerate(self.shared_utils.node_config.wan_ha.ha_interfaces):
            description = self.shared_utils.interface_descriptions.wan_ha_ethernet_interface(
                InterfaceDescriptionData(
                    shared_utils=self.shared_utils,
                    interface=interface,
                    peer=self.shared_utils.wan_ha_peer,
                    peer_interface=interface,
                ),
            )
            if self.shared_utils.use_port_channel_for_direct_ha:
                self.structured_config.ethernet_interfaces.append_new(
                    name=interface,
                    peer_type="wan_ha_peer",
                    peer_interface=interface,
                    peer=self.shared_utils.wan_ha_peer,
                    description=description or None,
                    shutdown=False,
                    channel_group=EosCliConfigGen.EthernetInterfacesItem.ChannelGroup(id=self.shared_utils.wan_ha_port_channel_id, mode="active"),
                    # TODO: do we need speed?
                    mtu=self.shared_utils.node_config.wan_ha.mtu,
                )
            else:
                # Using direct l3 interface
                self.structured_config.ethernet_interfaces.append_new(
                    name=interface,
                    switchport=EosCliConfigGen.EthernetInterfacesItem.Switchport(enabled=False),
                    peer_type="l3_interface",
                    peer=self.shared_utils.wan_ha_peer,
                    shutdown=False,
                    description=description or None,
                    ip_address=self.shared_utils.wan_ha_ip_addresses[index],
                    flow_tracker=direct_wan_ha_links_flow_tracker,
                    mtu=self.shared_utils.node_config.wan_ha.mtu,
                )
