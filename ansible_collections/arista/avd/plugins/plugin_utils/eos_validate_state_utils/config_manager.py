# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from collections.abc import Mapping
from functools import cached_property
from ipaddress import ip_interface

from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse

PLUGIN_NAME = "arista.avd.eos_validate_state"

try:
    from pyavd._errors import AristaAvdError
    from pyavd._utils import default, get, get_item
except ImportError as e:
    AristaAvdError = RaiseOnUse(
        AnsibleActionFail(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )

LOGGER = logging.getLogger(__name__)


class ConfigManager:
    """Configuration manager class for the eos_validate_state tests.

    This class is used to manage the structured configuration of the devices and to generate variables for the eos_validate_state tests.

    It should be initialized per device and the instance should be passed to the AvdTestBase class.
    """

    def __init__(self, device_name: str, hostvars: Mapping) -> None:
        """Initialize the ConfigManager class.

        Args:
        ----
            device_name (str): The current device name for which the plugin is being run.
            hostvars (Mapping): A mapping that contains a key for each device with a value of the structured_config.
                                      When using Ansible, this is the `task_vars['hostvars']` object.
        """
        self.device_name = device_name
        self.hostvars = hostvars
        self.structured_config = self.get_host_structured_config(host=device_name)
        self.loopback0_mapping = self.get_loopback0_mapping()
        self.vtep_mapping = self.get_vtep_mapping()
        self.dps_mapping = self.get_dps_mapping()

    def get_host_structured_config(self, host: str) -> Mapping:
        """Get a specified host's structured configuration from the hostvars.

        Args:
        ----
            host (str): Hostname to retrieve the structured_config.

        Returns:
        -------
            dict: Structured configuration for the host.

        Raises:
        ------
            AristaAvdError: If host is not in hostvars or if its structured_config is not a mapping object.
        """
        if host not in self.hostvars:
            raise AristaAvdError(message=f"Host '{host}' is missing from the hostvars.")
        struct_cfg = self.hostvars[host]

        # Check if struct_cfg is a mapping object (e.g. Ansible 'hostvars' object or regular dict)
        if not isinstance(struct_cfg, Mapping):
            raise AristaAvdError(message=f"Host '{host}' structured_config is not a dictionary or dictionary-like object.")

        return struct_cfg

    def get_loopback0_mapping(self) -> list[tuple[str, str]]:
        """Get the loopback0_mapping list."""
        return self._get_loopback_mappings["loopback0_mapping"]

    def get_vtep_mapping(self) -> list[tuple[str, str]]:
        """Get the vtep_mapping list."""
        return self._get_loopback_mappings["vtep_mapping"]

    def get_dps_mapping(self) -> list[tuple[str, str]]:
        """Get the dps_mapping list."""
        return self._get_loopback_mappings["dps_mapping"]

    def _get_ip_address(self, host: str, interfaces: list, vtep_interface: str) -> tuple[str, str] | None:
        """Retrieve the IP address for a given VTEP interface on a host.

        Parameters
        ----------
        host: str
            The hostname of the device.
        interfaces: list
            List of interface dictionaries.
        vtep_interface: str
            The name of the VTEP interface.

        Returns:
        -------
        tuple | None
            A tuple containing the hostname and IP address if found, else None.
        """
        if (loopback_interface := get_item(interfaces, "name", vtep_interface)) is None:
            LOGGER.warning("Host '%s' interface '%s' is missing.", host, vtep_interface)
        elif (loopback_ip := loopback_interface.get("ip_address")) is None:
            LOGGER.warning("Host '%s' variable 'ip_address' of interface '%s' is missing.", host, vtep_interface)
        else:
            return (host, str(ip_interface(loopback_ip).ip))
        return None  # Ensure a value is always returned

    @cached_property
    def _get_loopback_mappings(self) -> dict:
        """Generate the loopback mappings for the eos_validate_state tests, which are used in AvdTestBase subclasses.

        Returns:
        -------
            dict: A dictionary containing:
            - "loopback0_mapping": A list of tuples where each tuple contains a hostname and its Loopback0 IP address.
            - "vtep_mapping": A list of tuples where each tuple contains a hostname and its VTEP IP address if `Vxlan1` is the source_interface.
            - "dps_mapping": A list of tuples where each tuple contains a hostname and its VTEP IP address if `Dps` is in the source_interface.
        """
        results = {"loopback0_mapping": [], "vtep_mapping": [], "dps_mapping": []}

        for host in self.hostvars:
            host_struct_cfg = self.get_host_structured_config(host)
            loopback_interfaces = host_struct_cfg.get("loopback_interfaces", [])
            dps_interfaces = host_struct_cfg.get("dps_interfaces", [])

            # Handle Loopback0 interface
            if (loopback0 := get_item(loopback_interfaces, "name", "Loopback0")) is not None:
                if (loopback_ip := loopback0.get("ip_address")) is None:
                    LOGGER.warning("Host '%s' variable 'ip_address' of interface 'Loopback0' is missing.", host)
                else:
                    results["loopback0_mapping"].append((host, str(ip_interface(loopback_ip).ip)))

            # If the host is a VTEP, add the VTEP IP to the mapping
            # TODO: Remove the support of Vxlan1 in AVD 6.0.0 version
            vtep_interface = default(
                get(host_struct_cfg, "vxlan_interface.vxlan1.vxlan.source_interface"), get(host_struct_cfg, "vxlan_interface.Vxlan1.vxlan.source_interface")
            )
            if vtep_interface is None:
                continue

            # Determine the correct mapping based on the interface name
            if "Dps" in vtep_interface:
                ip_address = self._get_ip_address(host, dps_interfaces, vtep_interface)
                if ip_address:
                    results["dps_mapping"].append(ip_address)
            else:
                ip_address = self._get_ip_address(host, loopback_interfaces, vtep_interface)
                if ip_address:
                    results["vtep_mapping"].append(ip_address)

        return results
