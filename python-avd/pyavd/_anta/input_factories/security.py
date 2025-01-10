# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import ip_interface

from anta.input_models.security import IPSecPeer
from anta.tests.security import VerifySpecificIPSecConn

from pyavd._anta.logs import LogMessage

from ._base_classes import AntaTestInputFactory


class VerifySpecificIPSecConnInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifySpecificIPSecConn test.

    This factory generates test inputs for verifying IPsec connections.

    It collects `static_peers` IP addresses from the dynamic path selection
    `path_groups` to build the list of IPSec connections to verify.

    It deduplicates connections and always uses the default VRF.
    """

    def create(self) -> VerifySpecificIPSecConn.Input | None:
        """Create Input for the VerifySpecificIPSecConn test."""
        ip_security_connections = []

        added_peers = set()
        for path_group in self.structured_config.router_path_selection.path_groups:
            # Check if the path group has static peers
            if not path_group.static_peers:
                self.logger.debug(LogMessage.STUN_NO_STATIC_PEERS, caller=path_group.name)
                continue

            # Add static peers to the list of IP security connections
            for static_peer in path_group.static_peers:
                peer_ip = ip_interface(static_peer.router_ip).ip
                if (static_peer.router_ip, "default") not in added_peers:
                    ip_security_connections.append(
                        IPSecPeer(
                            peer=peer_ip,
                            vrf="default",
                        ),
                    )
                    added_peers.add((static_peer.router_ip, "default"))

        return VerifySpecificIPSecConn.Input(ip_security_connections=ip_security_connections) if ip_security_connections else None
