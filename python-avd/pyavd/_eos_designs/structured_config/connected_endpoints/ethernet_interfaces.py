# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import Undefined
from pyavd.api.interface_descriptions import InterfaceDescriptionData
from pyavd.j2filters import range_expand

if TYPE_CHECKING:
    from . import AvdStructuredConfigConnectedEndpointsProtocol


class EthernetInterfacesMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def ethernet_interfaces(self: AvdStructuredConfigConnectedEndpointsProtocol) -> None:
        """
        Return structured config for ethernet_interfaces.

        Duplicate checks following these rules:
        - Silently overwrite duplicate network_ports with other network_ports.
        - Silently overwrite duplicate network_ports with connected_endpoints.
        - Do NOT overwrite connected_endpoints with other connected_endpoints. Instead we raise a duplicate error.
        """
        for connected_endpoint in self._filtered_connected_endpoints:
            for adapter in connected_endpoint.adapters:
                for node_index, node_name in enumerate(adapter.switches):
                    if node_name != self.shared_utils.hostname:
                        continue

                    ethernet_interface = self._get_ethernet_interface_cfg(adapter, node_index, connected_endpoint)
                    self.structured_config.ethernet_interfaces.append(ethernet_interface)
                    if adapter.structured_config:
                        self.custom_structured_configs.nested.ethernet_interfaces.obtain(ethernet_interface.name)._deepmerge(
                            adapter.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
                        )

        # Temporary dict of ethernet interfaces to be added by network ports.
        # We need this since network ports can override each other, so the last one "wins"
        # Values are the real structured config and the custom structured config for this interface.
        network_ports_ethernet_interfaces: dict[str, tuple[EosCliConfigGen.EthernetInterfacesItem, EosCliConfigGen.EthernetInterfacesItem]] = {}
        for network_port in self._filtered_network_ports:
            connected_endpoint = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem(name=network_port.endpoint or Undefined)
            connected_endpoint._internal_data.type = "network_port"
            network_port_as_adapter = network_port._cast_as(
                EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem, ignore_extra_keys=True
            )
            network_port_as_adapter._internal_data.context = network_port._internal_data.context
            for ethernet_interface_name in range_expand(network_port.switch_ports):
                # Skip the interface if it was already created by some other feature like connected endpoints or uplinks etc.
                if ethernet_interface_name in self.structured_config.ethernet_interfaces:
                    continue

                # Override switches and switch_ports to only render for a single interface
                network_port_as_adapter.switch_ports = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.SwitchPorts(
                    [ethernet_interface_name]
                )
                network_port_as_adapter.switches = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.Switches(
                    [self.shared_utils.hostname]
                )

                # Using __setitem__ to replace any previous network_port.
                ethernet_interface = self._get_ethernet_interface_cfg(network_port_as_adapter, 0, connected_endpoint)
                network_ports_ethernet_interfaces[ethernet_interface_name] = ethernet_interface, network_port_as_adapter.structured_config

        # Now insert into the actual structured config and custom structured config
        for ethernet_interface, structured_config in network_ports_ethernet_interfaces.values():
            self.structured_config.ethernet_interfaces.append(ethernet_interface)
            if structured_config:
                self.custom_structured_configs.nested.ethernet_interfaces.obtain(ethernet_interface.name)._deepmerge(
                    structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
                )

    def _update_ethernet_interface_cfg(
        self: AvdStructuredConfigConnectedEndpointsProtocol,
        adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem,
        ethernet_interface: EosCliConfigGen.EthernetInterfacesItem,
        connected_endpoint: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem,
    ) -> None:
        ethernet_interface._update(
            mtu=adapter.mtu if self.shared_utils.platform_settings.feature_support.per_interface_mtu else None,
            l2_mtu=adapter.l2_mtu,
            l2_mru=adapter.l2_mru,
            spanning_tree_portfast=adapter.spanning_tree_portfast,
            spanning_tree_bpdufilter=adapter.spanning_tree_bpdufilter,
            spanning_tree_bpduguard=adapter.spanning_tree_bpduguard,
            storm_control=self._get_adapter_storm_control(adapter, output_type=EosCliConfigGen.EthernetInterfacesItem.StormControl),
            ptp=self._get_adapter_ptp(adapter, output_type=EosCliConfigGen.EthernetInterfacesItem.Ptp),
            service_profile=adapter.qos_profile,
            sflow=self._get_adapter_sflow(adapter, output_type=EosCliConfigGen.EthernetInterfacesItem.Sflow),
            flow_tracker=self.shared_utils.new_get_flow_tracker(adapter.flow_tracking, output_type=EosCliConfigGen.EthernetInterfacesItem.FlowTracker),
            link_tracking_groups=self._get_adapter_link_tracking_groups(adapter, output_type=EosCliConfigGen.EthernetInterfacesItem.LinkTrackingGroups),
        )
        ethernet_interface.switchport._update(
            enabled=True,
            mode=adapter.mode,
            phone=self._get_adapter_phone(adapter, connected_endpoint, output_type=EosCliConfigGen.EthernetInterfacesItem.Switchport.Phone),
        )
        if adapter.mode in ["access", "dot1q-tunnel"] and adapter.vlans is not None:
            try:
                # For access ports we use the 'vlans' field (str) as 'access_vlan' (int). Attempting to convert.
                ethernet_interface.switchport.access_vlan = int(adapter.vlans)
            except ValueError as e:
                msg = (
                    "Adapter 'vlans' value must be a single vlan ID when mode is 'access' or 'dot1q-tunnel'. "
                    f"Got {adapter.vlans} for interface {ethernet_interface.name}."
                )
                raise AristaAvdInvalidInputsError(msg) from e

        elif adapter.mode in ["trunk", "trunk phone"]:
            ethernet_interface.switchport.trunk._update(
                allowed_vlan=adapter.vlans if adapter.mode == "trunk" else None,
                groups=self._get_adapter_trunk_groups(adapter, connected_endpoint, output_type=EosCliConfigGen.EthernetInterfacesItem.Switchport.Trunk.Groups),
                native_vlan_tag=adapter.native_vlan_tag,
                native_vlan=adapter.native_vlan,
            )

    def _get_ethernet_interface_cfg(
        self: AvdStructuredConfigConnectedEndpointsProtocol,
        adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem,
        node_index: int,
        connected_endpoint: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem,
    ) -> EosCliConfigGen.EthernetInterfacesItem:
        """
        Return structured configuration for one ethernet interface.

        Args:
            adapter: The adapter configuration item.
            node_index: The index of the node in the list of nodes.
            connected_endpoint: The connected endpoint configuration item.

        Returns:
            The structured configuration for the ethernet interface.

        Raises:
            AristaAvdError: If the lengths of the lists 'switches', 'switch_ports', and 'descriptions' (if used) do not match.
            AristaAvdInvalidInputsError: If a port-channel set to LACP fallback mode 'individual' does not have a 'profile' defined.
        """
        peer = connected_endpoint.name
        endpoint_ports = adapter.endpoint_ports
        peer_interface = endpoint_ports[node_index] if node_index < len(endpoint_ports) else None
        default_channel_group_id = int("".join(re.findall(r"\d", adapter.switch_ports[0])))
        channel_group_id = adapter.port_channel.channel_id or default_channel_group_id
        short_esi = self._get_short_esi(adapter, channel_group_id)
        port_channel_mode = adapter.port_channel.mode

        # check lengths of lists
        nodes_length = len(adapter.switches)
        if len(adapter.switch_ports) != nodes_length or (adapter.descriptions and len(adapter.descriptions) != nodes_length):
            msg = (
                f"Length of lists 'switches', 'switch_ports', and 'descriptions' (if used) must match for adapter. Check configuration for {peer}, adapter"
                f" switch_ports {adapter.switch_ports._as_list()}."
            )
            raise AristaAvdError(msg)

        # if 'descriptions' is set, it is preferred
        interface_description = adapter.descriptions[node_index] if adapter.descriptions else adapter.description

        # Common ethernet_interface settings
        ethernet_interface = EosCliConfigGen.EthernetInterfacesItem(
            name=adapter.switch_ports[node_index],
            peer=peer,
            peer_interface=peer_interface,
            peer_type=connected_endpoint._internal_data.type,
            port_profile=adapter.profile,
            description=self.shared_utils.interface_descriptions.connected_endpoints_ethernet_interface(
                InterfaceDescriptionData(
                    shared_utils=self.shared_utils,
                    interface=adapter.switch_ports[node_index],
                    peer=peer,
                    peer_interface=peer_interface,
                    peer_type=connected_endpoint._internal_data.type,
                    description=interface_description,
                    port_channel_id=channel_group_id if port_channel_mode is not None else None,
                ),
            )
            or None,
            speed=adapter.speed,
            shutdown=not (adapter.enabled if adapter.enabled is not None else True),
            validate_state=None if (adapter.validate_state if adapter.validate_state is not None else True) else False,
            validate_lldp=None if (adapter.validate_lldp if adapter.validate_lldp is not None else True) else False,
            dot1x=adapter.dot1x,
            poe=self._get_adapter_poe(adapter),
            eos_cli=adapter.raw_eos_cli,
        )

        # Port-channel member
        if adapter.port_channel.mode:
            ethernet_interface.channel_group.id = channel_group_id
            ethernet_interface.channel_group.mode = adapter.port_channel.mode

            if (lacp_fallback_mode := adapter.port_channel.lacp_fallback.mode) == "static":
                ethernet_interface.lacp_port_priority = 8192 if node_index == 0 else 32768

            elif lacp_fallback_mode == "individual":
                # if fallback is set to individual a profile has to be defined
                if (profile_name := adapter.port_channel.lacp_fallback.individual.profile) is None:
                    msg = (
                        "A Port-channel which is set to lacp fallback mode 'individual' must have a 'profile' defined. Profile definition is missing for"
                        f" the connected endpoint with the name '{connected_endpoint.name}'."
                    )
                    raise AristaAvdInvalidInputsError(msg)

                profile = self.shared_utils.get_merged_port_profile(
                    profile_name, context=f"{adapter._internal_data.context}.port_channel.lacp_fallback.individual"
                )._cast_as(EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem)
                self._update_ethernet_interface_cfg(profile, ethernet_interface, connected_endpoint)

            if adapter.port_channel.mode != "on" and adapter.port_channel.lacp_timer.mode is not None:
                ethernet_interface.lacp_timer.mode = adapter.port_channel.lacp_timer.mode
                ethernet_interface.lacp_timer.multiplier = adapter.port_channel.lacp_timer.multiplier

        else:
            self._update_ethernet_interface_cfg(adapter, ethernet_interface, connected_endpoint)
            if evpn_ethernet_segment := self._get_adapter_evpn_ethernet_segment_cfg(
                adapter,
                short_esi,
                node_index,
                connected_endpoint,
                output_type=EosCliConfigGen.EthernetInterfacesItem.EvpnEthernetSegment,
                default_df_algo="auto",
                default_redundancy="single-active",
            ):
                ethernet_interface.evpn_ethernet_segment = evpn_ethernet_segment

        # More common ethernet_interface settings
        if adapter.flowcontrol:
            ethernet_interface.flowcontrol = adapter.flowcontrol

        return ethernet_interface
