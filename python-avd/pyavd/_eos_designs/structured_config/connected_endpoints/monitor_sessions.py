# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import append_if_not_duplicate, get, groupby, merge, strip_null_from_data
from pyavd.j2filters import range_expand

from .utils import UtilsMixin

if TYPE_CHECKING:
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

        for session_name, session_configs in groupby(self._monitor_session_configs, "name"):
            # Convert iterator to list since we can only access it once.
            session_configs_list = list(session_configs)
            merged_settings = merge({}, session_configs_list, destructive_merge=False)

            if get(merged_settings, "session_settings.access_group"):
                for session in session_configs_list:
                    if get(session, "source_settings.access_group"):
                        msg = (
                            f"Cannot set an ACL for both `session_settings` and `source_settings`"
                            f" under the monitor session '{session['name']}' for {session['context']}."
                        )
                        raise AristaAvdInvalidInputsError(msg)

            monitor_session = {
                "name": session_name,
                "sources": [],
                "destinations": [session["interface"] for session in session_configs_list if session.get("role") == "destination"],
            }
            source_sessions = [session for session in session_configs_list if session.get("role") == "source"]
            for session in source_sessions:
                source = {
                    "name": session["interface"],
                    "direction": get(session, "source_settings.direction"),
                }

                if (access_group := get(session, "source_settings.access_group")) is not None:
                    source["access_group"] = {
                        "type": access_group.get("type"),
                        "name": access_group.get("name"),
                        "priority": access_group.get("priority"),
                    }
                append_if_not_duplicate(
                    list_of_dicts=monitor_session["sources"],
                    primary_key="name",
                    new_dict=source,
                    context="Monitor session defined under connected_endpoints",
                    context_keys=["name"],
                )

            if (session_settings := merged_settings.get("session_settings")) is not None:
                monitor_session.update(session_settings)

            monitor_sessions.append(monitor_session)

        if monitor_sessions:
            return strip_null_from_data(monitor_sessions, ([], {}, None))

        return None

    @cached_property
    def _monitor_session_configs(self: AvdStructuredConfigConnectedEndpoints) -> list:
        """Return list of monitor session configs extracted from every interface."""
        monitor_session_configs = []
        for connected_endpoint in self._filtered_connected_endpoints:
            for adapter in connected_endpoint["adapters"]:
                if "monitor_sessions" not in adapter:
                    continue

                # Monitor session on Port-channel interface
                if get(adapter, "port_channel.mode") is not None:
                    default_channel_group_id = int("".join(re.findall(r"\d", adapter["switch_ports"][0])))
                    channel_group_id = get(adapter, "port_channel.channel_id", default=default_channel_group_id)

                    port_channel_interface_name = f"Port-Channel{channel_group_id}"
                    monitor_session_configs.extend(
                        [
                            dict(monitor_session, interface=port_channel_interface_name, context=adapter["context"])
                            for monitor_session in adapter["monitor_sessions"]
                        ],
                    )
                    continue

                # Monitor session on Ethernet interface
                for node_index, node_name in enumerate(adapter["switches"]):
                    if node_name != self.shared_utils.hostname:
                        continue

                    ethernet_interface_name = adapter["switch_ports"][node_index]
                    monitor_session_configs.extend(
                        [
                            dict(monitor_session, interface=ethernet_interface_name, context=adapter["context"])
                            for monitor_session in adapter["monitor_sessions"]
                        ],
                    )

        for network_port in self._filtered_network_ports:
            if "monitor_sessions" not in network_port:
                continue

            for ethernet_interface_name in range_expand(network_port["switch_ports"]):
                # Monitor session on Port-channel interface
                if get(network_port, "port_channel.mode") is not None:
                    default_channel_group_id = int("".join(re.findall(r"\d", ethernet_interface_name)))
                    channel_group_id = get(network_port, "port_channel.channel_id", default=default_channel_group_id)

                    port_channel_interface_name = f"Port-Channel{channel_group_id}"
                    monitor_session_configs.extend(
                        [
                            dict(monitor_session, interface=port_channel_interface_name, context=network_port["context"])
                            for monitor_session in network_port["monitor_sessions"]
                        ],
                    )
                    continue

                # Monitor session on Ethernet interface
                monitor_session_configs.extend(
                    [
                        dict(monitor_session, interface=ethernet_interface_name, context=network_port["context"])
                        for monitor_session in network_port["monitor_sessions"]
                    ],
                )

        return monitor_session_configs
