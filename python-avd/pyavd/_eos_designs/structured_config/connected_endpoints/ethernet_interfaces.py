# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import Undefined, append_if_not_duplicate, replace_or_append_item, strip_null_from_data
from pyavd.api.interface_descriptions import InterfaceDescriptionData
from pyavd.j2filters import range_expand

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigConnectedEndpoints


class EthernetInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def ethernet_interfaces(self: AvdStructuredConfigConnectedEndpoints) -> list | None:
        """
        Return structured config for ethernet_interfaces.

        Duplicate checks following these rules:
        - Silently overwrite duplicate network_ports with other network_ports.
        - Silently overwrite duplicate network_ports with connected_endpoints.
        - Do NOT overwrite connected_endpoints with other connected_endpoints. Instead we raise a duplicate error.
        """
        ethernet_interfaces = []

        # List of ethernet_interfaces used for duplicate checks.

        non_overwritable_ethernet_interfaces = []

        for network_port in self._filtered_network_ports:
            connected_endpoint = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem(name=network_port.endpoint or Undefined)
            connected_endpoint._type = "network_port"
            network_port_as_adapter = network_port._cast_as(
                EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem, ignore_extra_keys=True
            )
            network_port_as_adapter._context = network_port._context
            for ethernet_interface_name in range_expand(network_port.switch_ports):
                # Override switches and switch_ports to only render for a single interface
                network_port_as_adapter.switch_ports = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.SwitchPorts(
                    [ethernet_interface_name]
                )
                network_port_as_adapter.switches = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.Switches(
                    [self.shared_utils.hostname]
                )
                ethernet_interface = self._get_ethernet_interface_cfg(network_port_as_adapter, 0, connected_endpoint)
                replace_or_append_item(ethernet_interfaces, "name", ethernet_interface)

        for connected_endpoint in self._filtered_connected_endpoints:
            for adapter in connected_endpoint.adapters:
                for node_index, node_name in enumerate(adapter.switches):
                    if node_name != self.shared_utils.hostname:
                        continue

                    ethernet_interface = self._get_ethernet_interface_cfg(adapter, node_index, connected_endpoint)
                    append_if_not_duplicate(
                        list_of_dicts=non_overwritable_ethernet_interfaces,
                        primary_key="name",
                        new_dict=ethernet_interface,
                        context="Ethernet Interfaces defined under connected_endpoints",
                        context_keys=["name", "peer_interface"],
                    )

                    replace_or_append_item(ethernet_interfaces, "name", ethernet_interface)

        if ethernet_interfaces:
            return ethernet_interfaces

        return None

    def _update_ethernet_interface_cfg(
        self: AvdStructuredConfigConnectedEndpoints,
        adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem,
        ethernet_interface: dict,
        connected_endpoint: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem,
    ) -> dict:
        if (vlans := adapter.vlans) is not None and adapter.mode in ["access", "dot1q-tunnel"]:
            try:
                # For access ports we use the 'vlans' field (str) as 'access_vlan' (int). Attempting to convert.
                vlans = int(vlans)
            except ValueError as e:
                msg = (
                    "Adapter 'vlans' value must be a single vlan ID when mode is 'access' or 'dot1q-tunnel'. "
                    f"Got {vlans} for interface {ethernet_interface['name']}."
                )
                raise AristaAvdInvalidInputsError(msg) from e

        ethernet_interface.update(
            {
                "mtu": adapter.mtu if self.shared_utils.platform_settings.feature_support.per_interface_mtu else None,
                "l2_mtu": adapter.l2_mtu,
                "l2_mru": adapter.l2_mru,
                "switchport": {
                    "enabled": True,
                    "mode": adapter.mode,
                    "trunk": {
                        "allowed_vlan": vlans if adapter.mode == "trunk" else None,
                        "groups": self._get_adapter_trunk_groups(adapter, connected_endpoint),
                        "native_vlan_tag": adapter.native_vlan_tag,
                        "native_vlan": adapter.native_vlan,
                    },
                    "access_vlan": vlans if adapter.mode in ["access", "dot1q-tunnel"] else None,
                    "phone": self._get_adapter_phone(adapter, connected_endpoint),
                },
                "spanning_tree_portfast": adapter.spanning_tree_portfast,
                "spanning_tree_bpdufilter": adapter.spanning_tree_bpdufilter,
                "spanning_tree_bpduguard": adapter.spanning_tree_bpduguard,
                "storm_control": self._get_adapter_storm_control(adapter),
                "ptp": self._get_adapter_ptp(adapter),
                "service_profile": adapter.qos_profile,
                "sflow": self._get_adapter_sflow(adapter),
                "flow_tracker": self.shared_utils.get_flow_tracker(adapter.flow_tracking),
                "link_tracking_groups": self._get_adapter_link_tracking_groups(adapter),
            },
        )
        return strip_null_from_data(ethernet_interface, strip_values_tuple=(None, "", {}))

    def _get_ethernet_interface_cfg(
        self: AvdStructuredConfigConnectedEndpoints,
        adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem,
        node_index: int,
        connected_endpoint: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem,
    ) -> dict:
        """Return structured_config for one ethernet_interface."""
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
        ethernet_interface = {
            "name": adapter.switch_ports[node_index],
            "peer": peer,
            "peer_interface": peer_interface,
            "peer_type": connected_endpoint._type,
            "port_profile": adapter.profile,
            "description": self.shared_utils.interface_descriptions.connected_endpoints_ethernet_interface(
                InterfaceDescriptionData(
                    shared_utils=self.shared_utils,
                    interface=adapter.switch_ports[node_index],
                    peer=peer,
                    peer_interface=peer_interface,
                    peer_type=connected_endpoint._type,
                    description=interface_description,
                    port_channel_id=channel_group_id if port_channel_mode is not None else None,
                ),
            )
            or None,
            "speed": adapter.speed,
            "shutdown": not (adapter.enabled if adapter.enabled is not None else True),
            "validate_state": None if (adapter.validate_state if adapter.validate_state is not None else True) else False,
            "validate_lldp": None if (adapter.validate_lldp if adapter.validate_lldp is not None else True) else False,
            "dot1x": adapter.dot1x._as_dict() or None,
            "poe": self._get_adapter_poe(adapter),
            "eos_cli": adapter.raw_eos_cli,
        }

        if adapter.structured_config:
            self.custom_structured_configs.nested.ethernet_interfaces.obtain(adapter.switch_ports[node_index])._deepmerge(
                adapter.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )

        # Port-channel member
        if adapter.port_channel.mode:
            ethernet_interface["channel_group"] = {"id": channel_group_id, "mode": adapter.port_channel.mode}

            if (lacp_fallback_mode := adapter.port_channel.lacp_fallback.mode) == "static":
                ethernet_interface["lacp_port_priority"] = 8192 if node_index == 0 else 32768

            elif lacp_fallback_mode == "individual":
                # if fallback is set to individual a profile has to be defined
                if (profile_name := adapter.port_channel.lacp_fallback.individual.profile) is None:
                    msg = (
                        "A Port-channel which is set to lacp fallback mode 'individual' must have a 'profile' defined. Profile definition is missing for"
                        f" the connected endpoint with the name '{connected_endpoint.name}'."
                    )
                    raise AristaAvdInvalidInputsError(msg)

                profile = self.shared_utils.get_merged_port_profile(profile_name, context=f"{adapter._context}.port_channel.lacp_fallback.individual")._cast_as(
                    EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem
                )
                profile._context = adapter._context
                ethernet_interface = self._update_ethernet_interface_cfg(profile, ethernet_interface, connected_endpoint)

            if adapter.port_channel.mode != "on" and adapter.port_channel.lacp_timer.mode is not None:
                ethernet_interface["lacp_timer"] = {
                    "mode": adapter.port_channel.lacp_timer.mode,
                    "multiplier": adapter.port_channel.lacp_timer.multiplier,
                }

        else:
            ethernet_interface = self._update_ethernet_interface_cfg(adapter, ethernet_interface, connected_endpoint)
            ethernet_interface["evpn_ethernet_segment"] = self._get_adapter_evpn_ethernet_segment_cfg(
                adapter,
                short_esi,
                node_index,
                connected_endpoint,
                "auto",
                "single-active",
            )

        # More common ethernet_interface settings
        if adapter.flowcontrol.received:
            ethernet_interface["flowcontrol"] = {"received": adapter.flowcontrol.received}

        return strip_null_from_data(ethernet_interface, strip_values_tuple=(None, ""))
