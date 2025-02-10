# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class MonitorConnectivityMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def monitor_connectivity(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set the structured config for monitor_connectivity.

        Only used for CV Pathfinder edge routers today
        """
        if not self._filtered_internet_exit_policies_and_connections:
            return

        for _policy, connections in self._filtered_internet_exit_policies_and_connections:
            for connection in connections:
                interface_name = f"Tunnel{connection['tunnel_id']}" if connection["type"] == "tunnel" else connection["source_interface"]

                interface_set_name = f"SET-{self.shared_utils.sanitize_interface_name(interface_name)}"
                self.structured_config.monitor_connectivity.interface_sets.append_new(name=interface_set_name, interfaces=interface_name)

                self.structured_config.monitor_connectivity.hosts.append_new(
                    name=connection["monitor_name"],
                    description=connection["description"],
                    ip=connection["monitor_host"],
                    local_interfaces=interface_set_name,
                    address_only=False,
                    url=connection.get("monitor_url"),
                )

        if self.structured_config.monitor_connectivity:
            self.structured_config.monitor_connectivity.shutdown = False
