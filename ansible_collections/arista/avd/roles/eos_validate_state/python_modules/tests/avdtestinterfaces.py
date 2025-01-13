# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

LOGGER = logging.getLogger(__name__)


class AvdTestInterfacesState(AvdTestBase):
    """AvdTestInterfacesState class for interfaces state tests."""

    anta_module = "anta.tests.interfaces"
    interfaces_to_test = (
        "ethernet_interfaces",
        "port_channel_interfaces",
        "vlan_interfaces",
        "loopback_interfaces",
        "dps_interfaces",
    )

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all interfaces state tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """
        anta_tests = []

        required_keys = ["name", "shutdown"]

        for interface_model in self.interfaces_to_test:
            interfaces = self.structured_config.get(interface_model, default=[])

            for idx, interface in enumerate(interfaces):
                self.update_interface_shutdown(interface)
                if not self.validate_data(data=interface, data_path=f"{interface_model}.[{idx}]", required_keys=required_keys):
                    continue

                if interface.get("validate_state", True) is False:
                    LOGGER.info("Interface '%s' variable 'validate_state' is set to False. %s is skipped.", interface["name"], self.__class__.__name__)
                    continue

                status = "adminDown" if interface["shutdown"] else "up"

                intf_description = interface.get("description")
                custom_field = str(interface["name"]) if not intf_description else f"{interface['name']} - {intf_description}"
                custom_field = f"Interface {custom_field} = '{status}'"

                anta_tests.append(
                    {
                        "VerifyInterfacesStatus": {
                            "interfaces": [
                                {
                                    "name": interface["name"],
                                    "status": status,
                                },
                            ],
                            "result_overwrite": {"custom_field": custom_field},
                        },
                    },
                )

        # Add Vxlan1 interface state test if it exists
        # TODO: Remove the support of Vxlan1 in AVD 6.0.0 version
        if default(get(self.structured_config, "vxlan_interface.vxlan1"), get(self.structured_config, "vxlan_interface.Vxlan1")) is not None:
            anta_tests.append(
                {
                    "VerifyInterfacesStatus": {
                        "interfaces": [
                            {
                                "name": "Vxlan1",
                                "status": "up",
                            },
                        ],
                        "result_overwrite": {"custom_field": "Interface Vxlan1 = 'up'"},
                    },
                },
            )

        return {self.anta_module: anta_tests} if anta_tests else None
