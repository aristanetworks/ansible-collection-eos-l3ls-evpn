# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class TunnelInterfacesMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def tunnel_interfaces(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set structured config for tunnel_interfaces.

        Only used for CV Pathfinder edge routers today
        """
        if not self._filtered_internet_exit_policies_and_connections:
            return

        for internet_exit_policy, connections in self._filtered_internet_exit_policies_and_connections:
            for connection in connections:
                if connection["type"] == "tunnel":
                    tunnel_interface = EosCliConfigGen.TunnelInterfacesItem(
                        name=f"Tunnel{connection['tunnel_id']}",
                        description=connection["description"],
                        mtu=1394,  # TODO: do not hardcode
                        ip_address=connection["tunnel_ip_address"],
                        tunnel_mode="ipsec",  # TODO: do not hardcode
                        source_interface=connection["source_interface"],
                        destination=connection["tunnel_destination_ip"],
                        ipsec_profile=connection["ipsec_profile"],
                    )

                    if internet_exit_policy.type == "zscaler":
                        tunnel_interface.nat_profile = self.get_internet_exit_nat_profile_name(internet_exit_policy.type)

                    self.structured_config.tunnel_interfaces.append(tunnel_interface)
