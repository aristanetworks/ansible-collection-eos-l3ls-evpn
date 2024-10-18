# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from hashlib import sha256
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError
from pyavd._utils import get, get_item, short_esi_to_route_target

if TYPE_CHECKING:
    from . import AvdStructuredConfigConnectedEndpoints


class UtilsMixin:
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to a AvdStructuredConfig class or other Mixins.
    """

    @cached_property
    def _filtered_connected_endpoints(self: AvdStructuredConfigConnectedEndpoints) -> list:
        """
        Return list of endpoints defined under one of the keys in "connected_endpoints_keys" which are connected to this switch.

        Adapters are filtered to contain only the ones connected to this switch.
        """
        filtered_connected_endpoints = []
        for connected_endpoints_key in self.shared_utils.connected_endpoints_keys:
            connected_endpoints = get(self._hostvars, connected_endpoints_key["key"], default=[])
            for connected_endpoint in connected_endpoints:
                if "adapters" not in connected_endpoint:
                    continue

                filtered_adapters = []
                for adapter_index, adapter in enumerate(connected_endpoint["adapters"]):
                    adapter["context"] = f"{connected_endpoints_key['key']}[name={connected_endpoint['name']}].adapters[{adapter_index}]"
                    adapter_settings = self.shared_utils.get_merged_adapter_settings(adapter)

                    if self.shared_utils.hostname not in adapter_settings.get("switches", []):
                        continue

                    # Verify that length of all lists are the same
                    nodes_length = len(adapter_settings["switches"])
                    endpoint_ports = adapter_settings.get("endpoint_ports")
                    if len(adapter_settings["switch_ports"]) != nodes_length or (endpoint_ports is not None and len(endpoint_ports) != nodes_length):
                        msg = (
                            f"Length of lists 'switches', 'switch_ports', 'endpoint_ports' (if used) did not match on adapter {adapter_index} on"
                            f" connected_endpoint '{connected_endpoint['name']}' under '{connected_endpoints_key['key']}'."
                            " Notice that some or all of these variables could be inherited from 'port_profiles'"
                        )
                        raise AristaAvdError(msg)

                    filtered_adapters.append(adapter_settings)

                if filtered_adapters:
                    filtered_connected_endpoints.append(
                        {
                            **connected_endpoint,
                            "adapters": filtered_adapters,
                            "type": connected_endpoints_key["type"],
                        },
                    )

        return filtered_connected_endpoints

    @cached_property
    def _filtered_network_ports(self: AvdStructuredConfigConnectedEndpoints) -> list:
        """Return list of endpoints defined under "network_ports" which are connected to this switch."""
        filtered_network_ports = []
        for index, network_port in enumerate(get(self._hostvars, "network_ports", default=[])):
            network_port["context"] = f"network_ports[{index}]"
            network_port_settings = self.shared_utils.get_merged_adapter_settings(network_port)
            if not self._match_regexes(network_port_settings.get("switches"), self.shared_utils.hostname):
                continue

            filtered_network_ports.append(network_port_settings)

        return filtered_network_ports

    def _match_regexes(self: AvdStructuredConfigConnectedEndpoints, regexes: list, value: str) -> bool:
        """
        Match a list of regexes with the supplied value.

        Regex must match the full value to pass, so regex is wrapped in ^$.
        """
        return any(re.match(rf"^{regex}$", value) for regex in regexes)

    def _get_short_esi(
        self: AvdStructuredConfigConnectedEndpoints,
        adapter: dict,
        channel_group_id: int,
        short_esi: str | None = None,
        hash_extra_value: str = "",
    ) -> str | None:
        """Return short_esi for one adapter."""
        if len(set(adapter["switches"])) < 2 or not self.shared_utils.overlay_evpn or not self.shared_utils.overlay_vtep:
            # Only configure ESI for multi-homing.
            return None

        # short_esi is only set when called from sub-interface port-channels.
        if (short_esi is None) and (short_esi := get(adapter, "ethernet_segment.short_esi")) is None:
            return None

        endpoint_ports: list = adapter.get("endpoint_ports")
        short_esi = str(short_esi)
        if short_esi.lower() == "auto":
            esi_hash = sha256(
                "".join(
                    [hash_extra_value] + adapter["switches"][:2] + adapter["switch_ports"][:2] + endpoint_ports[:2] + [str(channel_group_id)],
                ).encode("UTF-8"),
            ).hexdigest()
            short_esi = re.sub(r"([0-9a-f]{4})", "\\1:", esi_hash)[:14]

        if len(short_esi.split(":")) != 3:
            msg = f"Invalid 'short_esi': '{short_esi}' on connected endpoints adapter. Must be in the format xxxx:xxxx:xxxx"
            raise AristaAvdError(msg)

        return short_esi

    def _get_adapter_trunk_groups(self: AvdStructuredConfigConnectedEndpoints, adapter: dict, connected_endpoint: dict) -> dict | None:
        """Return trunk_groups for one adapter."""
        if self.shared_utils.enable_trunk_groups and "trunk" in adapter.get("mode", ""):
            return get(
                adapter, "trunk_groups", required=True, custom_error_msg=f"'trunk_groups' for the connected_endpoint {connected_endpoint['name']} is required."
            )

        return None

    def _get_adapter_storm_control(self: AvdStructuredConfigConnectedEndpoints, adapter: dict) -> dict | None:
        """Return storm_control for one adapter."""
        if self.shared_utils.platform_settings_feature_support_interface_storm_control:
            return get(adapter, "storm_control")

        return None

    def _get_adapter_evpn_ethernet_segment_cfg(
        self: AvdStructuredConfigConnectedEndpoints,
        adapter: dict,
        short_esi: str,
        node_index: int,
        connected_endpoint: dict,
        default_df_algo: str | None = None,
        default_redundancy: str | None = None,
    ) -> dict | None:
        """Return evpn_ethernet_segment_cfg for one adapter."""
        if short_esi is None:
            return None

        adapter_ethernet_segment: dict = adapter.get("ethernet_segment", {})
        evpn_ethernet_segment = {
            "identifier": f"{self.shared_utils.evpn_short_esi_prefix}{short_esi}",
            "redundancy": adapter_ethernet_segment.get("redundancy", default_redundancy),
            "route_target": short_esi_to_route_target(short_esi),
        }
        if (designated_forwarder_algorithm := adapter_ethernet_segment.get("designated_forwarder_algorithm", default_df_algo)) is None:
            return evpn_ethernet_segment

        if designated_forwarder_algorithm == "modulus":
            evpn_ethernet_segment["designated_forwarder_election"] = {"algorithm": "modulus"}

        elif designated_forwarder_algorithm == "auto":
            auto_preferences = range((len(adapter["switches"]) - 1) * 100, -1, -100)
            evpn_ethernet_segment["designated_forwarder_election"] = {
                "algorithm": "preference",
                "preference_value": auto_preferences[node_index],
                "dont_preempt": adapter_ethernet_segment.get("dont_preempt"),
            }

        elif designated_forwarder_algorithm == "preference":
            # TODO: Add check for length of designated_forwarder_preferences
            designated_forwarder_preferences = get(
                adapter_ethernet_segment,
                "designated_forwarder_preferences",
                required=True,
                custom_error_msg=f"ethernet_segment.designated_forwarder_preferences for the connected_endpoint {connected_endpoint['name']}.",
            )
            evpn_ethernet_segment["designated_forwarder_election"] = {
                "algorithm": "preference",
                "preference_value": designated_forwarder_preferences[node_index],
                "dont_preempt": adapter_ethernet_segment.get("dont_preempt"),
            }

        return evpn_ethernet_segment

    def _get_adapter_link_tracking_groups(self: AvdStructuredConfigConnectedEndpoints, adapter: dict) -> list | None:
        """Return link_tracking_groups for one adapter."""
        if self.shared_utils.link_tracking_groups is None or get(adapter, "link_tracking.enabled") is not True:
            return None

        return [
            {
                "name": get(adapter, "link_tracking.name", default=self.shared_utils.link_tracking_groups[0]["name"]),
                "direction": "downstream",
            },
        ]

    def _get_adapter_ptp(self: AvdStructuredConfigConnectedEndpoints, adapter: dict) -> dict | None:
        """Return ptp for one adapter."""
        if get(adapter, "ptp.enabled") is not True:
            return None

        ptp_config = {}

        # Apply PTP profile config
        if (ptp_profile_name := get(adapter, "ptp.profile", default=self.shared_utils.ptp_profile_name)) is not None:
            msg = f"PTP Profile '{ptp_profile_name}' referenced under {adapter['context']} does not exist in `ptp_profiles`."
            ptp_config.update(get_item(self.shared_utils.ptp_profiles, "profile", ptp_profile_name, required=True, custom_error_msg=msg))

        ptp_config["enable"] = True

        if get(adapter, "ptp.endpoint_role") != "bmca":
            ptp_config["role"] = "master"

        ptp_config.pop("profile", None)

        return ptp_config

    def _get_adapter_poe(self: AvdStructuredConfigConnectedEndpoints, adapter: dict) -> dict | None:
        """Return poe settings for one adapter."""
        if self.shared_utils.platform_settings_feature_support_poe:
            return get(adapter, "poe")

        return None

    def _get_adapter_phone(self: AvdStructuredConfigConnectedEndpoints, adapter: dict, connected_endpoint: dict) -> dict | None:
        """Return phone settings for one adapter."""
        if (adapter_phone_vlan := get(adapter, "phone_vlan")) is None:
            return None

        # Verify that "mode" is set to "trunk phone"
        if get(adapter, "mode") != "trunk phone":
            msg = f"Setting 'phone_vlan' requires 'mode: trunk phone' to be set on connected endpoint '{connected_endpoint['name']}'."
            raise AristaAvdError(msg)

        # Verify that "vlans" is not set, since data vlan is picked up from 'native_vlan'.
        if get(adapter, "vlans") is not None:
            msg = (
                "With 'phone_vlan' and 'mode: trunk phone' the data VLAN is set via 'native_vlan' instead of 'vlans'. Found 'vlans' on connected endpoint"
                f" '{connected_endpoint['name']}'."
            )
            raise AristaAvdError(
                msg,
            )

        return {
            "vlan": adapter_phone_vlan,
            "trunk": get(adapter, "phone_trunk_mode"),
        }

    def _get_adapter_sflow(self: AvdStructuredConfigConnectedEndpoints, adapter: dict) -> dict | None:
        if (adapter_sflow := get(adapter, "sflow", default=self.shared_utils.fabric_sflow_endpoints)) is not None:
            return {"enable": adapter_sflow}

        return None

    def _get_adapter_flow_tracking(self: AvdStructuredConfigConnectedEndpoints, adapter: dict) -> dict | None:
        # Adapter flow tracking variables will be validated in _filtered_connected_endpoints
        return self.shared_utils.get_flow_tracker(adapter, "endpoints")
