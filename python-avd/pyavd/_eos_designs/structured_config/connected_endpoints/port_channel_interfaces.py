# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import Undefined, append_if_not_duplicate, get, short_esi_to_route_target, strip_null_from_data
from pyavd.api.interface_descriptions import InterfaceDescriptionData
from pyavd.j2filters import range_expand

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigConnectedEndpoints


class PortChannelInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def port_channel_interfaces(self: AvdStructuredConfigConnectedEndpoints) -> list | None:
        """
        Return structured config for port_channel_interfaces.

        Duplicate checks following these rules:
        - Silently ignore duplicate port-channels if they contain _exactly_ the same configuration
        - Raise a duplicate error for any other duplicate port-channel interface
        """
        port_channel_interfaces = []
        for connected_endpoint in self._filtered_connected_endpoints:
            for adapter in connected_endpoint.adapters:
                if not adapter.port_channel or not adapter.port_channel.mode:
                    continue

                default_channel_group_id = int("".join(re.findall(r"\d", adapter.switch_ports[0])))
                channel_group_id = adapter.port_channel.channel_id or default_channel_group_id

                port_channel_interface_name = f"Port-Channel{channel_group_id}"
                port_channel_config = self._get_port_channel_interface_cfg(adapter, port_channel_interface_name, channel_group_id, connected_endpoint)
                append_if_not_duplicate(
                    list_of_dicts=port_channel_interfaces,
                    primary_key="name",
                    new_dict=port_channel_config,
                    context="Port-channel Interfaces defined under connected_endpoints",
                    context_keys=["name"],
                )

                for subinterface in adapter.port_channel.subinterfaces:
                    if not subinterface.number:
                        continue

                    port_channel_subinterface_name = f"Port-Channel{channel_group_id}.{subinterface.number}"
                    port_channel_subinterface_config = self._get_port_channel_subinterface_cfg(
                        subinterface,
                        adapter,
                        port_channel_subinterface_name,
                        channel_group_id,
                    )
                    append_if_not_duplicate(
                        list_of_dicts=port_channel_interfaces,
                        primary_key="name",
                        new_dict=port_channel_subinterface_config,
                        context="Port-channel Interfaces defined under connected_endpoints",
                        context_keys=["name"],
                    )

        for network_port in self._filtered_network_ports:
            if not network_port.port_channel.mode:
                continue

            connected_endpoint = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem(name=network_port.endpoint or Undefined)
            connected_endpoint._type = "network_port"
            network_port_as_adapter = network_port._cast_as(
                EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem, ignore_extra_keys=True
            )
            for ethernet_interface_name in range_expand(network_port.switch_ports):
                # Override switches and switch_ports to only render for a single interface
                # The blank extra switch is only inserted to work around port_channel validations
                # This also means that port-channels defined with network_ports data model will be single-port per switch.
                # Caveat: "short_esi: auto" and "designated_forwarder_algorithm: auto" will not work correctly.
                network_port_as_adapter.switch_ports = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.SwitchPorts(
                    [ethernet_interface_name, ""]
                )
                network_port_as_adapter.switches = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.Switches(
                    [self.shared_utils.hostname, ""]
                )

                default_channel_group_id = int("".join(re.findall(r"\d", ethernet_interface_name)))
                channel_group_id = network_port_as_adapter.port_channel.channel_id or default_channel_group_id

                port_channel_interface_name = f"Port-Channel{channel_group_id}"

                port_channel_config = self._get_port_channel_interface_cfg(
                    network_port_as_adapter, port_channel_interface_name, channel_group_id, connected_endpoint
                )
                append_if_not_duplicate(
                    list_of_dicts=port_channel_interfaces,
                    primary_key="name",
                    new_dict=port_channel_config,
                    context="Port-channel Interfaces defined under connected_endpoints",
                    context_keys=["name"],
                )

        if port_channel_interfaces:
            return port_channel_interfaces

        return None

    def _get_port_channel_interface_cfg(
        self: AvdStructuredConfigConnectedEndpoints,
        adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem,
        port_channel_interface_name: str,
        channel_group_id: int,
        connected_endpoint: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem,
    ) -> dict:
        """Return structured_config for one port_channel_interface."""
        peer = connected_endpoint.name
        adapter_description = adapter.description
        port_channel_description = adapter.port_channel.description
        port_channel_mode = adapter.port_channel.mode
        peer_interface = adapter.port_channel.endpoint_port_channel
        node_index = adapter.switches.index(self.shared_utils.hostname)

        # if 'descriptions' is set, it is preferred
        adapter_description = interface_descriptions[node_index] if (interface_descriptions := adapter.descriptions) else adapter.description

        # Common port_channel_interface settings
        port_channel_interface = {
            "name": port_channel_interface_name,
            "description": self.shared_utils.interface_descriptions.connected_endpoints_port_channel_interface(
                InterfaceDescriptionData(
                    shared_utils=self.shared_utils,
                    interface=port_channel_interface_name,
                    peer=peer,
                    peer_interface=peer_interface,
                    peer_type=connected_endpoint._type,
                    description=adapter_description,
                    port_channel_id=channel_group_id,
                    port_channel_description=port_channel_description,
                ),
            ),
            "shutdown": not (adapter.port_channel.enabled if adapter.port_channel.enabled is not None else True),
            "mtu": adapter.mtu if self.shared_utils.platform_settings.feature_support.per_interface_mtu else None,
            "service_profile": adapter.qos_profile,
            "link_tracking_groups": self._get_adapter_link_tracking_groups(adapter),
            "ptp": self._get_adapter_ptp(adapter),
            "sflow": self._get_adapter_sflow(adapter),
            "flow_tracker": self.shared_utils.get_flow_tracker(adapter.flow_tracking),
            "validate_state": None if (adapter.validate_state if adapter.validate_state is not None else True) else False,
            "validate_lldp": None if (adapter.validate_lldp if adapter.validate_lldp is not None else True) else False,
            "eos_cli": adapter.port_channel.raw_eos_cli,
        }
        if adapter.port_channel.structured_config:
            self.custom_structured_configs.nested.port_channel_interfaces.obtain(port_channel_interface_name)._deepmerge(
                adapter.port_channel.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )

        if adapter.port_channel.subinterfaces:
            port_channel_interface.update({"switchport": {"enabled": False}})
        else:
            # switchport
            if (vlans := adapter.vlans) is not None and adapter.mode in ["access", "dot1q-tunnel"]:
                try:
                    # For access ports we use the 'vlans' field (str) as 'access_vlan' (int). Attempting to convert.
                    vlans = int(vlans)
                except ValueError as e:
                    msg = (
                        "Adapter 'vlans' value must be a single vlan ID when mode is 'access' or 'dot1q-tunnel'. "
                        f"Got {vlans} for interface {port_channel_interface['name']}."
                    )
                    raise AristaAvdInvalidInputsError(msg) from e

            port_channel_interface.update(
                {
                    "switchport": {
                        "enabled": True,
                        "mode": adapter.mode,
                        "trunk": {
                            "allowed_vlan": vlans if adapter.mode == "trunk" else None,
                            "groups": self._get_adapter_trunk_groups(adapter, connected_endpoint),
                            "native_vlan_tag": adapter.native_vlan_tag,
                            "native_vlan": adapter.native_vlan,
                        },
                        "phone": self._get_adapter_phone(adapter, connected_endpoint),
                        "access_vlan": vlans if adapter.mode in ["access", "dot1q-tunnel"] else None,
                    },
                    "l2_mtu": adapter.l2_mtu,
                    "l2_mru": adapter.l2_mru,
                    "spanning_tree_portfast": adapter.spanning_tree_portfast,
                    "spanning_tree_bpdufilter": adapter.spanning_tree_bpdufilter,
                    "spanning_tree_bpduguard": adapter.spanning_tree_bpduguard,
                    "storm_control": self._get_adapter_storm_control(adapter),
                },
            )

        # EVPN A/A
        if (short_esi := self._get_short_esi(adapter, channel_group_id)) is not None:
            port_channel_interface["evpn_ethernet_segment"] = self._get_adapter_evpn_ethernet_segment_cfg(adapter, short_esi, node_index, connected_endpoint)
            if port_channel_mode == "active":
                port_channel_interface["lacp_id"] = short_esi.replace(":", ".")

        # Set MLAG ID on port-channel if connection is multi-homed and this switch is running MLAG
        elif self.shared_utils.mlag and len(set(adapter.switches)) > 1:
            if get(port_channel_interface, "ptp.enable") is True and adapter.port_channel.ptp_mpass:
                port_channel_interface["ptp"]["mpass"] = True
            port_channel_interface["mlag"] = channel_group_id

        # LACP Fallback
        if port_channel_mode in ["active", "passive"] and (lacp_fallback_mode := adapter.port_channel.lacp_fallback.mode) in ["static", "individual"]:
            port_channel_interface.update(
                {
                    "lacp_fallback_mode": lacp_fallback_mode,
                    "lacp_fallback_timeout": adapter.port_channel.lacp_fallback.timeout or 90,
                },
            )

        return strip_null_from_data(port_channel_interface, strip_values_tuple=(None, "", {}))

    def _get_port_channel_subinterface_cfg(
        self: AvdStructuredConfigConnectedEndpoints,
        subinterface: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.PortChannel.SubinterfacesItem,
        adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem,
        port_channel_subinterface_name: str,
        channel_group_id: int,
    ) -> dict:
        """Return structured_config for one port_channel_interface (subinterface)."""
        # Common port_channel_interface settings
        port_channel_interface = {
            "name": port_channel_subinterface_name,
            "vlan_id": subinterface.vlan_id or subinterface.number,
            "encapsulation_vlan": {
                "client": {
                    "encapsulation": "dot1q",
                    "vlan": subinterface.encapsulation_vlan.client_dot1q or subinterface.number,
                },
                "network": {
                    "encapsulation": "client",
                },
            },
        }

        # EVPN A/A
        if (
            short_esi := self._get_short_esi(adapter, channel_group_id, short_esi=subinterface.short_esi, hash_extra_value=str(subinterface.number))
        ) is not None:
            port_channel_interface["evpn_ethernet_segment"] = {
                "identifier": f"{self.inputs.evpn_short_esi_prefix}{short_esi}",
                "route_target": short_esi_to_route_target(short_esi),
            }

        return strip_null_from_data(port_channel_interface, strip_values_tuple=(None, ""))
