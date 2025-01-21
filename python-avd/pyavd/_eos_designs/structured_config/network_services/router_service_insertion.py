# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class RouterServiceInsertionMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_service_insertion(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """
        Return structured config for router_service_insertion.

        Only used for CV Pathfinder edge routers today
        """
        if not self._filtered_internet_exit_policies_and_connections:
            return None

        service_connections = []

        for _policy, connections in self._filtered_internet_exit_policies_and_connections:
            for connection in connections:
                service_connection = {
                    "name": connection["name"],
                    "monitor_connectivity_host": connection["monitor_name"],
                }

                if connection["type"] == "tunnel":
                    service_connection["tunnel_interface"] = {
                        "primary": f"Tunnel{connection['tunnel_id']}",
                    }
                elif connection["type"] == "ethernet":
                    service_connection["ethernet_interface"] = {
                        "name": connection["source_interface"],
                        "next_hop": connection["next_hop"],
                    }

                service_connections.append(service_connection)

        if service_connections:
            return {"enabled": True, "connections": service_connections}

        return None
