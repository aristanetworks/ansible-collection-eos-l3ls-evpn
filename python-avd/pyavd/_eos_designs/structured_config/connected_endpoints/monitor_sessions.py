# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import append_if_not_duplicate, groupby_obj, strip_null_from_data
from pyavd.j2filters import range_expand

from .utils import UtilsMixin

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigConnectedEndpoints


class MonitorSessionsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def monitor_sessions(self: AvdStructuredConfigConnectedEndpoints) -> list | None:
        """Return structured_config for monitor_sessions."""
        if not self._monitor_session_configs:
            return None

        monitor_sessions = []

        for session_name, session_configs in groupby_obj(self._monitor_session_configs, "name"):
            # Convert iterator to list since we can only access it once.
            session_configs_list = list(session_configs)
            merged_settings = session_configs_list[0]._deepcopy()
            for session_config in session_configs_list[1:]:
                merged_settings._deepmerge(session_config)

            if merged_settings.session_settings.access_group:
                for session in session_configs_list:
                    if session.source_settings.access_group:
                        msg = (
                            f"Cannot set an ACL for both `session_settings` and `source_settings`"
                            f" under the monitor session '{session.name}' for {session._context}."
                        )
                        raise AristaAvdInvalidInputsError(msg)

            monitor_session = {
                "name": session_name,
                "sources": [],
                "destinations": [session._interface for session in session_configs_list if session.role == "destination"],
            }
            source_sessions = [session for session in session_configs_list if session.role == "source"]
            for session in source_sessions:
                source = {
                    "name": session._interface,
                    "direction": session.source_settings.direction,
                }
                if session.source_settings.access_group.name is not None:
                    source["access_group"] = {
                        "type": session.source_settings.access_group.type,
                        "name": session.source_settings.access_group.name,
                        "priority": session.source_settings.access_group.priority,
                    }
                append_if_not_duplicate(
                    list_of_dicts=monitor_session["sources"],
                    primary_key="name",
                    new_dict=source,
                    context="Monitor session defined under connected_endpoints",
                    context_keys=["name"],
                )

            if session_settings := merged_settings.session_settings:
                monitor_session.update(session_settings._as_dict())

            monitor_sessions.append(monitor_session)

        if monitor_sessions:
            return strip_null_from_data(monitor_sessions, ([], {}, None))

        return None

    @cached_property
    def _monitor_session_configs(
        self: AvdStructuredConfigConnectedEndpoints,
    ) -> list[EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.MonitorSessionsItem]:
        """Return list of monitor session configs extracted from every interface."""
        monitor_session_configs = []
        for connected_endpoint in self._filtered_connected_endpoints:
            for adapter in connected_endpoint.adapters:
                if not adapter.monitor_sessions:
                    continue

                # Monitor session on Port-channel interface
                if adapter.port_channel.mode:
                    default_channel_group_id = int("".join(re.findall(r"\d", adapter.switch_ports[0])))
                    channel_group_id = adapter.port_channel.channel_id or default_channel_group_id

                    port_channel_interface_name = f"Port-Channel{channel_group_id}"
                    for monitor_session in adapter.monitor_sessions:
                        per_interface_monitor_session = monitor_session._deepcopy()
                        per_interface_monitor_session._interface = port_channel_interface_name
                        per_interface_monitor_session._context = adapter._context
                        monitor_session_configs.append(per_interface_monitor_session)
                    continue

                # Monitor session on Ethernet interface
                for node_index, node_name in enumerate(adapter.switches):
                    if node_name != self.shared_utils.hostname:
                        continue

                    ethernet_interface_name = adapter.switch_ports[node_index]
                    for monitor_session in adapter.monitor_sessions:
                        per_interface_monitor_session = monitor_session._deepcopy()
                        per_interface_monitor_session._interface = ethernet_interface_name
                        per_interface_monitor_session._context = adapter._context
                        monitor_session_configs.append(per_interface_monitor_session)

        for network_port in self._filtered_network_ports:
            if not network_port.monitor_sessions:
                continue

            for ethernet_interface_name in range_expand(network_port.switch_ports):
                # Monitor session on Port-channel interface
                if network_port.port_channel and network_port.port_channel.mode is not None:
                    default_channel_group_id = int("".join(re.findall(r"\d", ethernet_interface_name)))
                    channel_group_id = network_port.port_channel.channel_id or default_channel_group_id

                    port_channel_interface_name = f"Port-Channel{channel_group_id}"
                    for monitor_session in network_port.monitor_sessions:
                        per_interface_monitor_session = monitor_session._deepcopy()
                        per_interface_monitor_session._interface = port_channel_interface_name
                        per_interface_monitor_session._context = network_port._context
                        monitor_session_configs.append(per_interface_monitor_session)
                    continue

                # Monitor session on Ethernet interface
                for monitor_session in network_port.monitor_sessions:
                    per_interface_monitor_session = monitor_session._deepcopy()
                    per_interface_monitor_session._interface = ethernet_interface_name
                    per_interface_monitor_session._context = network_port._context
                    monitor_session_configs.append(per_interface_monitor_session)

        return monitor_session_configs
