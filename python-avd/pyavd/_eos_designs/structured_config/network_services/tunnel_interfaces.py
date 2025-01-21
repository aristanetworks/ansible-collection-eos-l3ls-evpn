# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import append_if_not_duplicate

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class TunnelInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def tunnel_interfaces(self: AvdStructuredConfigNetworkServices) -> list | None:
        """
        Return structured config for tunnel_interfaces.

        Only used for CV Pathfinder edge routers today
        """
        if not self._filtered_internet_exit_policies_and_connections:
            return None

        tunnel_interfaces = []

        for internet_exit_policy, connections in self._filtered_internet_exit_policies_and_connections:
            for connection in connections:
                if connection["type"] == "tunnel":
                    tunnel_interface = {
                        "name": f"Tunnel{connection['tunnel_id']}",
                        "description": connection["description"],
                        "mtu": 1394,  # TODO: do not hardcode
                        "ip_address": connection["tunnel_ip_address"],
                        "tunnel_mode": "ipsec",  # TODO: do not hardcode
                        "source_interface": connection["source_interface"],
                        "destination": connection["tunnel_destination_ip"],
                        "ipsec_profile": connection["ipsec_profile"],
                    }

                    if internet_exit_policy.type == "zscaler":
                        tunnel_interface["nat_profile"] = self.get_internet_exit_nat_profile_name(internet_exit_policy.type)

                    append_if_not_duplicate(
                        list_of_dicts=tunnel_interfaces,
                        primary_key="name",
                        new_dict=tunnel_interface,
                        context="Tunnel interface for Internet Exit policy",
                        context_keys=["name"],
                    )

        if tunnel_interfaces:
            return tunnel_interfaces

        return None
