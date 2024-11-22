# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._anta.utils import LogMessage
from pyavd._utils import get, validate_dict

if TYPE_CHECKING:
    from anta.tests.security import VerifySpecificIPSecConn

    from pyavd._anta.utils import TestLoggerAdapter
    from pyavd._anta.utils.config_manager import ConfigManager

class VerifySpecificIPSecConnInputFactory:
    """Input factory class for the VerifySpecificIPSecConn test.

    This factory creates test inputs for IP security connections verification.

    It collects IP security connections for:
      - Router path-selection path groups configured with static-peers.
      - static-peers configured with router_ip.

    The factory ensures:
      - IP security collection is skipped for missing required key `router_path_selection.path_groups[].static_peers[].router_ip`

    """

    @classmethod
    def create(cls, test: type[VerifySpecificIPSecConn], manager: ConfigManager, logger: TestLoggerAdapter) -> VerifySpecificIPSecConn.Input | None:
        """Create Input for the VerifySpecificIPSecConn test."""

        connections = []

        path_groups = get(manager.structured_config, "router_path_selection.path_groups")
        added_peers = set()
        # Check if there are any path groups with static peers
        for path_group in path_groups:
            is_valid, issues = validate_dict(path_group, required_keys=["static_peers"])
            if not is_valid:
                logger.debug(LogMessage.INELIGIBLE_DATA, entity=path_group["name"], issues=issues)
                continue
            # Check if there are any static peer with router_ip
            for peer in path_group["static_peers"]:
                is_valid, issues = validate_dict(peer, required_keys=["router_ip"])
                if not is_valid:
                    logger.debug(LogMessage.INELIGIBLE_DATA, entity=peer["name"], issues=issues)
                    continue
                peer_address = peer["router_ip"]
                vrf = "default"  # TODO: Keeping the vrf name static for now. We may need to change later on.
                if (peer_address, vrf) not in added_peers:
                    connections.append(
                test.Input.IPSecPeers(
                    peer=peer_address,
                    vrf=vrf,
                ),
            )
                    added_peers.add((peer_address, vrf))

        return test.Input(ip_security_connections=connections) if connections else None
