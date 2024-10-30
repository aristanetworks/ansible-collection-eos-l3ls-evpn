# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from collections import ChainMap
from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import append_if_not_duplicate, default, get, replace_or_append_item, strip_null_from_data
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
            connected_endpoint = {
                "name": network_port.get("endpoint"),
                "type": "network_port",
            }
            for ethernet_interface_name in range_expand(network_port["switch_ports"]):
                # Override switches and switch_ports to only render for a single interface
                tmp_network_port = ChainMap(
                    {
                        "switch_ports": [ethernet_interface_name],
                        "switches": [self.shared_utils.hostname],
                    },
                    network_port,
                )
                ethernet_interface = self._get_ethernet_interface_cfg(tmp_network_port, 0, connected_endpoint)
                replace_or_append_item(ethernet_interfaces, "name", ethernet_interface)

        for connected_endpoint in self._filtered_connected_endpoints:
            for adapter in connected_endpoint["adapters"]:
                for node_index, node_name in enumerate(adapter["switches"]):
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
        self: AvdStructuredConfigConnectedEndpoints, adapter: dict | ChainMap, ethernet_interface: dict, connected_endpoint: dict
    ) -> dict:
        ethernet_interface.update(
            {
                "mtu": adapter.get("mtu") if self.shared_utils.platform_settings_feature_support_per_interface_mtu else None,
                "l2_mtu": adapter.get("l2_mtu"),
                "l2_mru": adapter.get("l2_mru"),
                "switchport": {
                    "enabled": True,
                    "mode": adapter.get("mode"),
                    "trunk": {
                        "allowed_vlan": adapter.get("vlans") if adapter.get("mode") == "trunk" else None,
                        "groups": self._get_adapter_trunk_groups(adapter, connected_endpoint),
                        "native_vlan_tag": adapter.get("native_vlan_tag"),
                        "native_vlan": adapter.get("native_vlan"),
                    },
                    "access_vlan": adapter.get("vlans") if adapter.get("mode") in ["access", "dot1q-tunnel"] else None,
                    "phone": self._get_adapter_phone(adapter, connected_endpoint),
                },
                "spanning_tree_portfast": adapter.get("spanning_tree_portfast"),
                "spanning_tree_bpdufilter": adapter.get("spanning_tree_bpdufilter"),
                "spanning_tree_bpduguard": adapter.get("spanning_tree_bpduguard"),
                "storm_control": self._get_adapter_storm_control(adapter),
                "ptp": self._get_adapter_ptp(adapter),
                "service_profile": adapter.get("qos_profile"),
                "sflow": self._get_adapter_sflow(adapter),
                "flow_tracker": self._get_adapter_flow_tracking(adapter),
                "link_tracking_groups": self._get_adapter_link_tracking_groups(adapter),
            },
        )
        return strip_null_from_data(ethernet_interface, strip_values_tuple=(None, "", {}))

    def _get_ethernet_interface_cfg(self: AvdStructuredConfigConnectedEndpoints, adapter: dict | ChainMap, node_index: int, connected_endpoint: dict) -> dict:
        """Return structured_config for one ethernet_interface."""
        peer = connected_endpoint["name"]
        endpoint_ports: list = default(
            adapter.get("endpoint_ports"),
            [],
        )
        peer_interface = endpoint_ports[node_index] if node_index < len(endpoint_ports) else None
        default_channel_group_id = int("".join(re.findall(r"\d", adapter["switch_ports"][0])))
        channel_group_id = get(adapter, "port_channel.channel_id", default=default_channel_group_id)
        short_esi = self._get_short_esi(adapter, channel_group_id)
        port_channel_mode = get(adapter, "port_channel.mode")

        # check lengths of lists
        nodes_length = len(adapter["switches"])
        if len(adapter["switch_ports"]) != nodes_length or ("descriptions" in adapter and len(adapter["descriptions"]) != nodes_length):
            msg = (
                f"Length of lists 'switches', 'switch_ports', and 'descriptions' (if used) must match for adapter. Check configuration for {peer}, adapter"
                f" switch_ports {adapter['switch_ports']}."
            )
            raise AristaAvdError(
                msg,
            )

        # if 'descriptions' is set, it is preferred
        if (interface_descriptions := adapter.get("descriptions")) is not None:
            interface_description = interface_descriptions[node_index]
        else:
            interface_description = get(adapter, "description")

        # Common ethernet_interface settings
        ethernet_interface = {
            "name": adapter["switch_ports"][node_index],
            "peer": peer,
            "peer_interface": peer_interface,
            "peer_type": connected_endpoint["type"],
            "port_profile": adapter.get("profile"),
            "description": self.shared_utils.interface_descriptions.connected_endpoints_ethernet_interface(
                InterfaceDescriptionData(
                    shared_utils=self.shared_utils,
                    interface=adapter["switch_ports"][node_index],
                    peer=peer,
                    peer_interface=peer_interface,
                    peer_type=connected_endpoint["type"],
                    description=interface_description,
                    port_channel_id=channel_group_id if port_channel_mode is not None else None,
                ),
            )
            or None,
            "speed": adapter.get("speed"),
            "shutdown": not adapter.get("enabled", True),
            "validate_state": None if adapter.get("validate_state", True) else False,
            "dot1x": adapter.get("dot1x"),
            "poe": self._get_adapter_poe(adapter),
            "eos_cli": adapter.get("raw_eos_cli"),
            "struct_cfg": adapter.get("structured_config"),
        }

        # Port-channel member
        if port_channel_mode is not None:
            ethernet_interface["channel_group"] = {
                "id": channel_group_id,
                "mode": port_channel_mode,
            }

            if get(adapter, "port_channel.lacp_fallback.mode") == "static":
                ethernet_interface["lacp_port_priority"] = 8192 if node_index == 0 else 32768

            elif get(adapter, "port_channel.lacp_fallback.mode") == "individual":
                # if fallback is set to individual a profile has to be defined
                if (profile_name := get(adapter, "port_channel.lacp_fallback.individual.profile")) is None:
                    msg = (
                        "A Port-channel which is set to lacp fallback mode 'individual' must have a 'profile' defined. Profile definition is missing for"
                        f" the connected endpoint with the name '{connected_endpoint['name']}'."
                    )
                    raise AristaAvdInvalidInputsError(msg)

                profile = self.shared_utils.get_merged_port_profile(profile_name, context=f"{adapter['context']}.port_channel.lacp_fallback.individual")
                profile["context"] = adapter["context"]

                ethernet_interface = self._update_ethernet_interface_cfg(profile, ethernet_interface, connected_endpoint)

            if port_channel_mode != "on" and get(adapter, "port_channel.lacp_timer") is not None:
                ethernet_interface["lacp_timer"] = {
                    "mode": get(adapter, "port_channel.lacp_timer.mode"),
                    "multiplier": get(adapter, "port_channel.lacp_timer.multiplier"),
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
        if (flowcontrol_received := get(adapter, "flowcontrol.received")) is not None:
            ethernet_interface["flowcontrol"] = {"received": flowcontrol_received}

        return strip_null_from_data(ethernet_interface, strip_values_tuple=(None, ""))
