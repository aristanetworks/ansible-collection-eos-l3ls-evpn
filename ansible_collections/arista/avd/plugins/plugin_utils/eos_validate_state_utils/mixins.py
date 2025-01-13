# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging

from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse
from ansible_collections.arista.avd.plugins.plugin_utils.utils import log_message

PLUGIN_NAME = "arista.avd.eos_validate_state"

try:
    from pyavd._utils import default, get, get_item
except ImportError as e:
    get = get_item = default = RaiseOnUse(
        AnsibleActionFail(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )

LOGGER = logging.getLogger(__name__)


class DeviceUtilsMixin:
    """Mixin class for the eos_validate_state tests.

    This class provides utility methods for handling and manipulating device-related data.

    It should only be used as a mixin class in the AvdTestBase classes.
    """

    def update_interface_shutdown(self, interface: dict, host: str | None = None) -> None:
        """Update the interface shutdown key, considering EOS default.

        For Ethernet interfaces:
        - If the interface `shutdown` key is not set, the host `interface_defaults.ethernet.shutdown` key is used.
        - If the host `interface_defaults.ethernet.shutdown` key is not set, the interface `shutdown` key is set to False.

        For other interfaces, the `shutdown` key is updated using the interface `shutdown` key if available or set to False.

        Args:
        ----
            interface (dict): The interface to verify.
            host (str): Host to verify. Defaults to the host running the test.
        """
        host_struct_cfg = self.config_manager.get_host_structured_config(host=host) if host else self.structured_config
        if "Ethernet" in get(interface, "name", ""):
            interface["shutdown"] = default(get(interface, "shutdown"), get(host_struct_cfg, "interface_defaults.ethernet.shutdown"), False)  # noqa: FBT003
        else:
            interface["shutdown"] = get(interface, "shutdown", default=False)

    def is_peer_available(self, peer: str) -> bool:
        """Check if a peer is deployed by looking at his `is_deployed` key.

        Args:
        ----
            peer (str): The peer to verify.

        Returns:
        -------
            bool: True if the peer is deployed, False otherwise.
        """
        if peer not in self.hostvars:
            log_msg = f"Peer '{peer}' is not configured by AVD. {self.__class__.__name__} is skipped."
            LOGGER.info(log_msg)
            return False
        if not get(self.hostvars[peer], "is_deployed", True):
            log_msg = f"Peer '{peer}' is marked as not deployed. {self.__class__.__name__} is skipped."
            LOGGER.info(log_msg)
            return False
        return True

    def get_interface_ip(self, interface_model: str, interface_name: str, host: str | None = None) -> str | None:
        """Retrieve the IP address of a specified host interface.

        Args:
        ----
            interface_model (str): Interface model in the structured config (e.g., ethernet_interfaces).
            interface_name (str): Interface name to retrieve the IP.
            host (str): Host to verify. Defaults to the host running the test.

        Returns:
        -------
            str | None: IP address of the host interface or None if unavailable.
        """
        host_struct_cfg = self.config_manager.get_host_structured_config(host=host) if host else self.structured_config
        interfaces = get(host_struct_cfg, interface_model, default=[])
        interface = get_item(interfaces, "name", interface_name, default={})
        ip_address = get(interface, "ip_address")
        if ip_address is None or ip_address == "dhcp":
            log_msg = f"Host '{host or self.device_name}' interface '{interface_name}' IP address is unavailable. {self.__class__.__name__} is skipped."
            LOGGER.warning(log_msg)
            return None

        return ip_address

    def is_dhcp_interface(self, interface: dict) -> bool:
        """Check if the interface is a DHCP interface.

        Args:
        ----
            interface (dict): The interface to verify.

        Returns:
        -------
            bool: True if the interface is a DHCP interface, False otherwise.
        """
        return interface["ip_address"] == "dhcp"

    def is_subinterface(self, interface: dict) -> bool:
        """Check if the interface is a subinterface.

        Args:
        ----
            interface (dict): The interface to verify.

        Returns:
        -------
            bool: True if the interface is a subinterface, False otherwise.
        """
        return "." in interface.get("name", "")

    def is_vtep(self) -> bool:
        """Check if the host is a VTEP by verifying the presence of a VXLAN interface."""
        return get(self.structured_config, "vxlan_interface") is not None

    def is_wan_vtep(self) -> bool:
        """Check if the host is a WAN VTEP by verifying the presence of a VXLAN interface and Dps in the source interface."""
        return self.is_vtep() and "Dps" in get(
            self.structured_config,
            "vxlan_interface.vxlan1.vxlan.source_interface",
            (get(self.structured_config, "vxlan_interface.Vxlan1.vxlan.source_interface", "")),
        )


class ValidationMixin:
    """Mixin class for the eos_validate_state tests.

    This class provides validation methods for the structured configuration data.

    It should be used as a mixin class in the AvdTestBase classes.
    """

    # TODO: @carl-baillargeon: Split the validate_data method into two methods: one for expected key-value pairs and one for required keys.
    def validate_data(
        self,
        data: dict | None = None,
        data_path: str | None = None,
        host: str | None = None,
        required_keys: str | list[str] | None = None,
        logging_level: str = "INFO",
        **kwargs: dict,
    ) -> bool:
        """Validate data based on given requirements such as expected key-value pairs and required keys.

        In the context of the eos_validate_state tests, if the data is not valid, the test is skipped.

        Args:
        ----
            data (dict | None): A data dictionary to be validated. Defaults to the structured_config of the device running the test.
            data_path (str | None): The data path in dot notation. Used for logging purposes. Index or primary key can be used for lists.
            host (str | None): The host from which data should be retrieved. Defaults to the device running the test.
            required_keys (str | list[str] | None): The keys that are expected to be in the data.
            logging_level (str): The logging level to use for the log message. Defaults to "INFO".
            **kwargs: Expected key-value pairs in the data.

        Returns:
        -------
            bool: True if the data meets all validation requirements, otherwise False.

        Example:
        -------
            >>> validate_data(data={"a": 1, "b": 2}, data_path="some.path", required_keys=["a", "b"], c=3)

            In this case, the function will log a warning message because the key 'c' with value '3' is not found,
            and it will return False as the data doesn't meet all validation requirements.
        """
        message = f"{self.__class__.__name__} is skipped"

        data = data or (self.config_manager.get_host_structured_config(host=host) if host else self.structured_config)
        valid = True

        # Check the expected key/value pairs first
        for key, value in kwargs.items():
            actual_value = get(data, key)
            if actual_value is None:
                log_message(key=key, key_path=data_path, message=message, log_level=logging_level)
                valid = False
            elif actual_value != value:
                log_message(key=key, value=value, key_path=data_path, message=message, log_level=logging_level)
                valid = False

        # Return False if any of the expected values are missing or not matching
        if not valid:
            return False

        # Check the required keys
        if required_keys:
            required_keys = [required_keys] if isinstance(required_keys, str) else required_keys
            for key in required_keys:
                if get(data, key) is None:
                    log_message(key=key, key_path=data_path, message=message, log_level=logging_level)
                    valid = False
        return valid
