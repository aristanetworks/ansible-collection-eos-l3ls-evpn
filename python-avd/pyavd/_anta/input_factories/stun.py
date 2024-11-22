# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import ip_interface
from typing import TYPE_CHECKING

from pyavd._anta.utils import LogMessage
from pyavd._utils import get, validate_dict

if TYPE_CHECKING:
    from anta.tests.stun import VerifyStunClient

    from pyavd._anta.utils import TestLoggerAdapter
    from pyavd._anta.utils.config_manager import ConfigManager


class VerifyStunClientInputFactory:
    """Input factory class for the VerifyStunClient test.

    This factory creates test inputs for STUN client settings verification.

    It collects STUN client local interfaces for:
      - Router path-selection path groups configured with local_interfaces.
      - local_interfaces configured with stun.server_profiles.

    The factory ensures:
      - Only explicitly stun.server_profiles configured stun local interfaces are tested
      - Only explicitly ip address configured stun local interfaces are tested

    """

    @classmethod
    def create(cls, test: type[VerifyStunClient], manager: ConfigManager, logger: TestLoggerAdapter) -> VerifyStunClient.Input | None:
        """Create Input for the VerifyStunClient test."""
        stun_clients = []

        # Check if there are any path groups with STUN configuration
        path_groups = get(manager.structured_config, "router_path_selection.path_groups")
        # Get the interfaces with STUN configuration
        stun_interfaces = []
        for path_group in path_groups:
            is_valid, issues = validate_dict(path_group, required_keys=["local_interfaces"])
            if not is_valid:
                logger.debug(LogMessage.INELIGIBLE_DATA, entity=path_group["name"], issues=issues)
                continue
            for local_interface in path_group["local_interfaces"]:
                is_valid, issues = validate_dict(local_interface, required_keys=["stun.server_profiles"])

                if not is_valid:
                    logger.debug(LogMessage.INELIGIBLE_DATA, entity=local_interface["name"], issues=issues)
                    continue

                stun_interfaces.append(local_interface["name"])
        if not stun_interfaces:
            logger.debug(LogMessage.NOT_STUN_CLIENT_INTERFACE)
            return None

        # Generate the ANTA tests for each identified local interface.
        for source_interface in stun_interfaces:
            if (ip_address := manager.get_interface_ip("ethernet_interfaces", source_interface)) is None:
                continue
            source_address = str(ip_interface(ip_address).ip)
            source_port = 4500
            stun_clients.append(test.Input.ClientAddress(source_address=source_address, source_port=source_port))

        return test.Input(stun_clients=stun_clients) if stun_clients else None
