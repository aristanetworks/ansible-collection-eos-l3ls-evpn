# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from hashlib import sha256
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import default, get_v2, short_esi_to_route_target

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigConnectedEndpoints


class UtilsMixin:
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to a AvdStructuredConfig class or other Mixins.
    """

    @cached_property
    def _filtered_connected_endpoints(
        self: AvdStructuredConfigConnectedEndpoints,
    ) -> list[EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem]:
        """
        Return list of endpoints defined under one of the keys in "connected_endpoints_keys" which are connected to this switch.

        Adapters are filtered to contain only the ones connected to this switch.
        """
        filtered_connected_endpoints = []
        for connected_endpoints_key in self.inputs._dynamic_keys.connected_endpoints:
            for connected_endpoint in connected_endpoints_key.value:
                filtered_adapters = []
                for adapter_index, adapter in enumerate(connected_endpoint.adapters):
                    adapter_settings = self.shared_utils.get_merged_adapter_settings(adapter)
                    if not adapter_settings.switches or self.shared_utils.hostname not in adapter_settings.switches:
                        continue

                    # Verify that length of all lists are the same
                    nodes_length = len(adapter_settings.switches)
                    endpoint_ports = adapter_settings.endpoint_ports
                    if len(adapter_settings.switch_ports) != nodes_length or (endpoint_ports and len(endpoint_ports) != nodes_length):
                        msg = (
                            f"Length of lists 'switches' ({len(adapter.switches)}), 'switch_ports' ({len(adapter.switch_ports)}), "
                            f"'endpoint_ports' ({len(endpoint_ports) or '-'}) (if used) did not match on adapter {adapter_index} on"
                            f" connected_endpoint '{connected_endpoint.name}' under '{connected_endpoints_key.key}'."
                            " Notice that some or all of these variables could be inherited from 'port_profiles'"
                        )
                        raise AristaAvdError(msg)

                    filtered_adapters.append(adapter_settings)

                if filtered_adapters:
                    # The object was deepcopied inside "get_merged_adapter_settings" so we can modify it here.
                    connected_endpoint.adapters = filtered_adapters
                    connected_endpoint._type = self.inputs.connected_endpoints_keys[connected_endpoints_key.key].type
                    filtered_connected_endpoints.append(connected_endpoint)

        return filtered_connected_endpoints

    @cached_property
    def _filtered_network_ports(self: AvdStructuredConfigConnectedEndpoints) -> list[EosDesigns.NetworkPortsItem]:
        """Return list of endpoints defined under "network_ports" which are connected to this switch."""
        filtered_network_ports = []
        for network_port in self.inputs.network_ports:
            network_port_settings = self.shared_utils.get_merged_adapter_settings(network_port)
            if not self._match_regexes(network_port_settings.switches, self.shared_utils.hostname):
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
        adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem,
        channel_group_id: int,
        short_esi: str | None = None,
        hash_extra_value: str = "",
    ) -> str | None:
        """Return short_esi for one adapter."""
        if len(set(adapter.switches)) < 2 or not self.shared_utils.overlay_evpn or not self.shared_utils.overlay_vtep:
            # Only configure ESI for multi-homing.
            return None

        # short_esi is only set when called from sub-interface port-channels.
        if (short_esi is None) and (short_esi := adapter.ethernet_segment.short_esi) is None:
            return None

        endpoint_ports: list = getattr(adapter, "endpoint_ports", [])
        short_esi = str(short_esi)
        if short_esi.lower() == "auto":
            esi_hash = sha256(
                "".join(
                    [hash_extra_value] + adapter.switches[:2] + adapter.switch_ports[:2] + endpoint_ports[:2] + [str(channel_group_id)],
                ).encode("UTF-8"),
            ).hexdigest()
            short_esi = re.sub(r"([0-9a-f]{4})", "\\1:", esi_hash)[:14]

        if len(short_esi.split(":")) != 3:
            msg = f"Invalid 'short_esi': '{short_esi}' on connected endpoints adapter. Must be in the format xxxx:xxxx:xxxx"
            raise AristaAvdError(msg)

        return short_esi

    def _get_adapter_trunk_groups(
        self: AvdStructuredConfigConnectedEndpoints,
        adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem,
        connected_endpoint: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem,
    ) -> list | None:
        """Return trunk_groups for one adapter."""
        if not self.inputs.enable_trunk_groups or adapter.mode not in ["trunk", "trunk phone"]:
            return None

        if adapter._get("trunk_groups") is None:
            msg = f"'trunk_groups' for the connected_endpoint {connected_endpoint.name} is required."
            raise AristaAvdInvalidInputsError(msg)

        return adapter.trunk_groups._as_list()

    def _get_adapter_storm_control(
        self: AvdStructuredConfigConnectedEndpoints,
        adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem,
    ) -> dict | None:
        """Return storm_control for one adapter."""
        if self.shared_utils.platform_settings.feature_support.interface_storm_control:
            return adapter.storm_control._as_dict()

        return None

    def _get_adapter_evpn_ethernet_segment_cfg(
        self: AvdStructuredConfigConnectedEndpoints,
        adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem,
        short_esi: str | None,
        node_index: int,
        connected_endpoint: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem,
        default_df_algo: str | None = None,
        default_redundancy: str | None = None,
    ) -> dict | None:
        """Return evpn_ethernet_segment_cfg for one adapter."""
        if short_esi is None:
            return None

        evpn_ethernet_segment = {
            "identifier": f"{self.inputs.evpn_short_esi_prefix}{short_esi}",
            "redundancy": adapter.ethernet_segment.redundancy or default_redundancy,
            "route_target": short_esi_to_route_target(short_esi),
        }
        if (designated_forwarder_algorithm := adapter.ethernet_segment.designated_forwarder_algorithm or default_df_algo) is None:
            return evpn_ethernet_segment

        if designated_forwarder_algorithm == "modulus":
            evpn_ethernet_segment["designated_forwarder_election"] = {"algorithm": "modulus"}

        elif designated_forwarder_algorithm == "auto":
            auto_preferences = range((len(adapter.switches) - 1) * 100, -1, -100)
            evpn_ethernet_segment["designated_forwarder_election"] = {
                "algorithm": "preference",
                "preference_value": auto_preferences[node_index],
                "dont_preempt": adapter.ethernet_segment.dont_preempt,
            }

        elif designated_forwarder_algorithm == "preference":
            # TODO: Add check for length of designated_forwarder_preferences
            designated_forwarder_preferences = get_v2(
                adapter.ethernet_segment,
                "designated_forwarder_preferences",
                required=True,
                custom_error_msg=f"ethernet_segment.designated_forwarder_preferences for the connected_endpoint {connected_endpoint.name}.",
            )
            evpn_ethernet_segment["designated_forwarder_election"] = {
                "algorithm": "preference",
                "preference_value": designated_forwarder_preferences[node_index],
                "dont_preempt": adapter.ethernet_segment.dont_preempt,
            }

        return evpn_ethernet_segment

    def _get_adapter_link_tracking_groups(
        self: AvdStructuredConfigConnectedEndpoints,
        adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem,
    ) -> list | None:
        """Return link_tracking_groups for one adapter."""
        if self.shared_utils.link_tracking_groups is None or not adapter.link_tracking.enabled:
            return None

        return [
            {
                "name": adapter.link_tracking.name or self.shared_utils.link_tracking_groups[0]["name"],
                "direction": "downstream",
            },
        ]

    def _get_adapter_ptp(
        self: AvdStructuredConfigConnectedEndpoints, adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem
    ) -> dict | None:
        """Return ptp for one adapter."""
        if not adapter.ptp.enabled:
            return None

        ptp_config = {}

        # Apply PTP profile config
        if (ptp_profile_name := adapter.ptp.profile or self.shared_utils.ptp_profile_name) is not None:
            if ptp_profile_name not in self.inputs.ptp_profiles:
                msg = f"PTP Profile '{ptp_profile_name}' referenced under {adapter._source} does not exist in `ptp_profiles`."
                raise AristaAvdInvalidInputsError(msg)

            ptp_config.update(self.inputs.ptp_profiles[ptp_profile_name]._as_dict(include_default_values=True))

        ptp_config["enable"] = True

        if adapter.ptp.endpoint_role not in ["dynamic", "bmca"]:
            ptp_config["role"] = "master"

        ptp_config.pop("profile", None)

        return ptp_config

    def _get_adapter_poe(
        self: AvdStructuredConfigConnectedEndpoints,
        adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem,
    ) -> dict | None:
        """Return poe settings for one adapter."""
        if self.shared_utils.platform_settings.feature_support.poe:
            return adapter.poe._as_dict() or None

        return None

    def _get_adapter_phone(
        self: AvdStructuredConfigConnectedEndpoints,
        adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem,
        connected_endpoint: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem,
    ) -> dict | None:
        """Return phone settings for one adapter."""
        if not adapter.phone_vlan:
            return None

        # Verify that "mode" is set to "trunk phone"
        if adapter.mode != "trunk phone":
            msg = f"Setting 'phone_vlan' requires 'mode: trunk phone' to be set on connected endpoint '{connected_endpoint.name}'."
            raise AristaAvdError(msg)

        # Verify that "vlans" is not set, since data vlan is picked up from 'native_vlan'.
        if adapter.vlans:
            msg = (
                "With 'phone_vlan' and 'mode: trunk phone' the data VLAN is set via 'native_vlan' instead of 'vlans'. Found 'vlans' on connected endpoint"
                f" '{connected_endpoint.name}'."
            )
            raise AristaAvdError(msg)

        return {
            "vlan": adapter.phone_vlan,
            "trunk": adapter.phone_trunk_mode,
        }

    def _get_adapter_sflow(
        self: AvdStructuredConfigConnectedEndpoints,
        adapter: EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem,
    ) -> dict | None:
        if (adapter_sflow := default(adapter.sflow, self.inputs.fabric_sflow.endpoints)) is not None:
            return {"enable": adapter_sflow}

        return None
