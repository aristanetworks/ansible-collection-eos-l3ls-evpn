# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

LOGGER = logging.getLogger(__name__)


class AvdTestAPIHttpsSSL(AvdTestBase):
    """AvdTestAPIHttpsSSL class for eAPI HTTPS SSL tests."""

    anta_module = "anta.tests.security"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all eAPI HTTPS SSL tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """
        anta_tests = []

        if (profile := get(self.structured_config, "management_api_http.https_ssl_profile")) is None:
            LOGGER.info("No https ssl profile found. %s is skipped.", self.__class__.__name__)
            return None

        anta_tests.append({"VerifyAPIHttpsSSL": {"profile": profile, "result_overwrite": {"custom_field": f"eAPI HTTPS SSL Profile: {profile}"}}})

        return {self.anta_module: anta_tests}


class AvdTestIPSecurity(AvdTestBase):
    """
    AvdTestIPSecurity class for IP security connection tests.

    It validates the state of IPv4 security connections for a specified peer, ensuring they are established.
    It specifically focuses on IPv4 security connections within the default VRF.
    In its current state, the test validates only IPsec connections defined as static peers under the `router path-selection` section of the configuration.

    """

    anta_module = "anta.tests.security"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all IP security connection tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """
        anta_tests = []

        # Check if there are any path groups with static peers
        if (path_groups := get(self.structured_config, "router_path_selection.path_groups")) is None:
            LOGGER.info("No router path-group configured to collect the static peer. %s is skipped.", self.__class__.__name__)
            return None

        added_peers = set()
        for group_idx, path_group in enumerate(path_groups):
            if not self.validate_data(data=path_group, data_path=f"router_path_selection.path_groups.[{group_idx}]", required_keys="static_peers"):
                continue

            for peer_idx, peer in enumerate(path_group["static_peers"]):
                if self.validate_data(
                    data=peer,
                    data_path=f"router_path_selection.path_groups.[{group_idx}].static_peers.[{peer_idx}]",
                    required_keys="router_ip",
                ):
                    peer_address = peer["router_ip"]
                    vrf = "default"  # TODO: Keeping the vrf name static for now. We may need to change later on.
                    if (peer_address, vrf) not in added_peers:
                        anta_tests.append(
                            {
                                "VerifySpecificIPSecConn": {
                                    "ip_security_connections": [{"peer": peer_address, "vrf": vrf}],
                                    "result_overwrite": {"custom_field": f"IPv4 Peer: {peer_address} VRF: {vrf}"},
                                },
                            },
                        )
                        added_peers.add((peer_address, vrf))

        return {self.anta_module: anta_tests} if anta_tests else None
