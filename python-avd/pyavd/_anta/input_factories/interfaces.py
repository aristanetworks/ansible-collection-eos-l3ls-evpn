# Copyright (c) 2023-2025 Arista Networks, Inc.
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

    This factory generates test inputs for verifying the status of interfaces.

    The following interfaces are considered:
    - Ethernet interfaces - `ethernet_interfaces`
    - Port-Channel interfaces - `port_channel_interfaces`
    - VLAN interfaces - `vlan_interfaces`
    - Loopback interfaces - `loopback_interfaces`
    - DPS interfaces - `dps_interfaces`
    - Vxlan1 interface, if the device is a VTEP

    The expected status is 'adminDown' when the interface is shutdown, 'up' otherwise.

    For Ethernet and Port-Channel interfaces, state validation depends on the `validate_state` knob (default: True).

    For Ethernet interfaces, `interface_defaults.ethernet.shutdown` is considered when `shutdown` is not set
    """

    def create(self) -> VerifyInterfacesStatus.Input | None:
        """Create Input for the VerifyInterfacesStatus test."""
        interfaces = []

        # Add Ethernet interfaces, considering `validate_state` knob and interface defaults
        for intf in self.structured_config.ethernet_interfaces:
            if intf.validate_state is False:
                self.logger.debug(LogMessage.INTERFACE_VALIDATION_DISABLED, caller=intf.name)
                continue
            status = "adminDown" if intf.shutdown or (intf.shutdown is None and self.structured_config.interface_defaults.ethernet.shutdown) else "up"
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
