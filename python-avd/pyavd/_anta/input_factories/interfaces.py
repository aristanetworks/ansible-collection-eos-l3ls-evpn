# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from itertools import chain

from anta.input_models.interfaces import InterfaceState
from anta.tests.interfaces import VerifyInterfacesStatus

from pyavd._anta.logs import LogMessage

from ._base_classes import AntaTestInputFactory


class VerifyInterfacesStatusInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyInterfacesStatus test.

    Ethernet/Port-Channel interfaces:
    - Required config:
      * validate_state != False
    - Requirements:
      * Interface exists in config
      * Interface is not shutdown

    VLAN/Loopback/DPS interfaces:
    - Requirements:
      * Interface exists in config
      * Interface is not shutdown

    Vxlan1 interface:
    - Requirements:
      * Device is VTEP

    Notes:
      - Expected status is 'adminDown' when the interface is shutdown, 'up' otherwise
      - Ethernet interfaces can consider `interface_defaults.ethernet.shutdown`
    """

    def create(self) -> VerifyInterfacesStatus.Input | None:
        """Create Input for the VerifyInterfacesStatus test."""
        interfaces = []

        # Add Ethernet interfaces, considering `validate_state` knob and interface defaults
        for intf in self.structured_config.ethernet_interfaces:
            if intf.validate_state is False:
                self.logger.debug(LogMessage.INTERFACE_VALIDATION_DISABLED, caller=intf.name)
                continue
            status = "adminDown" if intf.shutdown or self.structured_config.interface_defaults.ethernet.shutdown else "up"
            interfaces.append(InterfaceState(name=intf.name, status=status))

        # Add Port-Channel interfaces, considering `validate_state` knob
        for intf in self.structured_config.port_channel_interfaces:
            if intf.validate_state is False:
                self.logger.debug(LogMessage.INTERFACE_VALIDATION_DISABLED, caller=intf.name)
                continue
            interfaces.append(InterfaceState(name=intf.name, status="adminDown" if intf.shutdown else "up"))

        # Add VLAN, Loopback, and DPS interfaces
        interfaces.extend(
            [
                InterfaceState(name=intf.name, status="adminDown" if intf.shutdown else "up")
                for intf in chain(self.structured_config.vlan_interfaces, self.structured_config.loopback_interfaces, self.structured_config.dps_interfaces)
            ]
        )

        # If the device is a VTEP, add the Vxlan1 interface to the list
        if self.device.is_vtep:
            interfaces.append(InterfaceState(name="Vxlan1", status="up"))

        return VerifyInterfacesStatus.Input(interfaces=interfaces) if interfaces else None
