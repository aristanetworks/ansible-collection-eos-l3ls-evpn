# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import ip_interface

from anta.input_models.stun import StunClientTranslation
from anta.tests.stun import VerifyStunClientTranslation

from pyavd._anta.logs import LogMessage

from ._base_classes import AntaTestInputFactory


class VerifyStunClientTranslationInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyStunClientTranslation test.

    Required config:
      - router_path_selection.path_groups.[].local_interfaces.[].stun.server_profiles
      - ethernet_interfaces.[].ip_address (for referenced interfaces)

    Requirements:
      - Path groups have local interfaces with STUN server profiles
      - IPv4 source address for the STUN client
    """

    def create(self) -> VerifyStunClientTranslation.Input | None:
        """Create Input for the VerifyStunClientTranslation test."""
        stun_clients = []

        for path_group in self.structured_config.router_path_selection.path_groups:
            # Check if the path group has local interfaces with STUN server profiles
            stun_interfaces = [local_interface.name for local_interface in path_group.local_interfaces if local_interface.stun.server_profiles]
            if not stun_interfaces:
                self.logger.debug(LogMessage.STUN_NO_CLIENT_INTERFACE, caller=path_group.name)
                continue

            for interface in stun_interfaces:
                # Get the source IP address for the STUN client
                ip_address = (
                    self.structured_config.ethernet_interfaces[interface].ip_address if interface in self.structured_config.ethernet_interfaces else None
                )
                if ip_address is None:
                    self.logger.debug(LogMessage.INTERFACE_NO_IP, caller=interface)
                    continue
                if ip_address == "dhcp":
                    self.logger.debug(LogMessage.INTERFACE_USING_DHCP, caller=interface)
                    continue

                source_address = ip_interface(ip_address).ip
                stun_clients.append(StunClientTranslation(source_address=source_address))

        return VerifyStunClientTranslation.Input(stun_clients=stun_clients) if stun_clients else None
