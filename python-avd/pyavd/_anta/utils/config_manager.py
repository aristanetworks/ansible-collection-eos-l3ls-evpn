# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError
from pyavd._utils import default, get, get_item

if TYPE_CHECKING:
    from pyavd.api.fabric_data import FabricData

    from .constants import StructuredConfigKey


class ConfigManager:
    """Configuration manager class used to generate test inputs based on the structured configuration of a device.

    It has access to the FabricData instance containing the structured configurations and mappings
    such as loopback0 and VTEP mappings of all devices in the fabric.

    It must be initialized per device.
    """

    def __init__(self, device_name: str, fabric_data: FabricData) -> None:
        """Initialize the ConfigManager instance.

        Parameters
        ----------
            device_name: The device name for which the configuration manager is being initialized.
            fabric_data: The FabricData object containing the structured configurations and mappings of all devices in the fabric.
        """
        self.device_name = device_name
        self.fabric_data = fabric_data
        self.structured_config = get(fabric_data.structured_configs, device_name, default={})
        if not self.structured_config:
            raise AristaAvdError(message=f"Device '{device_name}' structured configuration not found in the provided fabric data.")

    def verify_keys(self, keys: list[StructuredConfigKey]) -> bool:
        """Verify that all provided keys are present in the structured configuration of the device.

        Parameters
        ----------
            keys: List of keys to verify. Must be Enum members from StructuredConfigKey.

        Returns:
        -------
            bool: True if all keys are present, False otherwise
        """
        return all(get(self.structured_config, key.value) for key in keys)

    def is_peer_available(self, peer: str) -> bool:
        """Check if a peer is deployed by looking at his `is_deployed` key.

        Parameters
        ----------
            peer: The peer to verify.

        Returns:
        -------
            bool: True if the peer is deployed, False otherwise.
        """
        return peer in self.fabric_data.structured_configs and get(self.fabric_data.structured_configs[peer], "is_deployed", True)

    def update_interface_shutdown(self, interface: dict) -> None:
        """Update the interface shutdown key, considering EOS default.

        For Ethernet interfaces:
        - If the interface `shutdown` key is not set, the host `interface_defaults.ethernet.shutdown` key is used.
        - If the host `interface_defaults.ethernet.shutdown` key is not set, the interface `shutdown` key is set to False.

        For other interfaces, the `shutdown` key is updated using the interface `shutdown` key if available or set to False.

        Parameters
        ----------
            interface: The interface to verify.
        """
        default_state = False
        if "Ethernet" in interface["name"]:
            interface["shutdown"] = default(get(interface, "shutdown"), get(self.structured_config, "interface_defaults.ethernet.shutdown"), default_state)
        else:
            interface["shutdown"] = get(interface, "shutdown", default=default_state)

    def get_interface_ip(self, interface_model: str, interface_name: str, device: str | None = None) -> str | None:
        """Retrieve the IP address of a specified device interface.

        Parameters
        ----------
            interface_model: Interface model in the structured configuration (e.g., ethernet_interfaces).
            interface_name: Interface name to retrieve the IP.
            device: Device to verify. Defaults to the device running the test.

        Returns:
        -------
            str | None: IP address of the device interface or None if unavailable.
        """
        device_struct_cfg = get(self.fabric_data.structured_configs, device, default={}) if device else self.structured_config
        interfaces = get(device_struct_cfg, interface_model, default=[])
        interface = get_item(interfaces, "name", interface_name, default={})
        return get(interface, "ip_address")

    def is_wan_vtep(self) -> bool:
        """Check if the device is a WAN VTEP by looking at the presence of a DPS VXLAN source interface.

        Returns:
        -------
            bool: True if the device is a WAN VTEP, False otherwise.
        """
        return "Dps" in get(self.structured_config, "vxlan_interface.Vxlan1.vxlan.source_interface")

    def is_vtep(self) -> bool:
        """Check if the device is a VTEP by looking at the presence of a VXLAN source interface.

        Returns:
        -------
            bool: True if the device is a VTEP, False otherwise.
        """
        return bool(get(self.structured_config, "vxlan_interface.Vxlan1.vxlan.source_interface"))

    @staticmethod
    def to_be_validated(interface: dict) -> bool:
        """Check if an interface is to be validated by looking at the `validate_state` key.

        Returns:
        -------
            bool: True if the interface is to be validated, False otherwise. Defaults to True.
        """
        return get(interface, "validate_state", default=True)

    @staticmethod
    def is_subinterface(interface: dict) -> bool:
        """Check if the interface is a subinterface.

        Parameters
        ----------
            interface: The interface to verify.

        Returns:
        -------
            bool: True if the interface is a subinterface, False otherwise.
        """
        return "." in interface["name"]
