# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import defaultdict
from ipaddress import ip_interface
from typing import TYPE_CHECKING

from pyavd._utils import get, get_item

if TYPE_CHECKING:
    from logging import Logger


class FabricData:
    """FabricData class.

    Class to store the structured configs and mappings for the fabric devices. Used to generate the test inputs.

    Attributes:
    ----------
    structured_configs : dict[str, dict]
        The structured configurations of the devices in the fabric.
        The key is the device name and the value is the structured config.
    loopback0_mapping : dict[str, IPv4Address]
        The mapping of the Loopback0 IP addresses for each device.
    vtep_mapping : dict[str, IPv4Address]
        The mapping of the VTEP IP addresses for each device.
    combined_mapping : defaultdict[str, list[IPv4Address]]
        The combined mapping of the Loopback0 and VTEP IP addresses for each device.
    logger : Logger
        The logger object to use for logging messages.
    """

    def __init__(self, structured_configs: dict[str, dict], logger: Logger) -> None:
        """Initialize the FabricData instance."""
        self.structured_configs = structured_configs
        self.loopback0_mapping = {}
        self.vtep_mapping = {}
        self.combined_mapping = defaultdict(list)
        self.logger = logger

        # Generate the mappings and populate the attributes
        self._generate_mappings()

    def _generate_mappings(self) -> None:
        """Generate the mappings."""
        for device, config in self.structured_configs.items():
            self._process_loopback0(device, config)
            self._process_vtep(device, config)

    def _process_loopback0(self, device: str, structured_config: dict) -> None:
        """Process the loopback0 mapping.

        Populates the loopback0_mapping and combined_mapping attributes.

        Parameters
        ----------
            device: The device name.
            structured_config: The structured configuration of the device.
        """
        loopback_interfaces = get(structured_config, "loopback_interfaces", default=[])
        if (loopback0 := get_item(loopback_interfaces, "name", "Loopback0")) is not None and (loopback_ip := get(loopback0, "ip_address")) is not None:
            ip_obj = ip_interface(loopback_ip).ip
            self.loopback0_mapping[device] = ip_obj
            self.combined_mapping[device].append(ip_obj)
        else:
            self.logger.warning("<%s>: Loopback0 or IP missing. Some tests will be skipped.", device)

    def _process_vtep(self, device: str, structured_config: dict) -> None:
        """Process the vtep mapping.

        Populates the vtep_mapping and combined_mapping attributes.

        Parameters
        ----------
            device: The device name.
            structured_config: The structured configuration of the device.
        """
        loopback_interfaces = get(structured_config, "loopback_interfaces", default=[])
        vtep_interface = get(structured_config, "vxlan_interface.Vxlan1.vxlan.source_interface")

        # NOTE: For now we exclude WAN VTEPs from the vtep_mapping
        if vtep_interface is not None and "Dps" not in vtep_interface:
            if (loopback_interface := get_item(loopback_interfaces, "name", vtep_interface)) is not None and (
                loopback_ip := get(loopback_interface, "ip_address")
            ) is not None:
                ip_obj = ip_interface(loopback_ip).ip
                self.vtep_mapping[device] = ip_obj
                self.combined_mapping[device].append(ip_obj)
            else:
                self.logger.warning("<%s>: VTEP source %s or IP missing. Some VTEP tests will be skipped.", device, vtep_interface)
        else:
            self.logger.info("<%s>: Not in VTEP mapping. Not a VTEP or is WAN VTEP.", device)
