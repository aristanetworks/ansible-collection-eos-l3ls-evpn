# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._anta.utils import LogMessage
from pyavd._utils import get

from ._base_classes import AntaTestInputFactory, AntaTestInputFactoryFilter
from ._constants import INTERFACE_MODELS

if TYPE_CHECKING:
    from anta.tests.interfaces import VerifyInterfacesStatus


class VerifyInterfacesStatusInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyInterfacesStatus test.

    This factory creates test inputs for interface status verification.

    It collects interfaces that should be monitored for:
      - These configured interface types: Ethernet, Port-Channel, VLAN, Loopback, DPS
      - Vxlan1 interface on VTEP devices

    The factory ensures:
      - Interface shutdown state is properly considered ('adminDown' vs 'up')
      - Only interfaces marked for validation (`validate_state: true`) are included
      - Interface collection is skipped if no interfaces are found
    """

    # TODO: Add filter class
    class Filter(AntaTestInputFactoryFilter):
        pass

    def create(self) -> VerifyInterfacesStatus.Input | None:
        """Create Input for the VerifyInterfacesStatus test."""
        inputs = []

        for interface_model in INTERFACE_MODELS:
            if (interfaces := get(self.manager.structured_config, interface_model)) is None:
                self.logger.debug(LogMessage.NO_DATA_MODEL, entity=interface_model)
                continue

            for interface in interfaces:
                self.manager.update_interface_shutdown(interface)

                # Skip interfaces that have `validate_state: false`
                if not self.manager.to_be_validated(interface):
                    self.logger.debug(LogMessage.SKIP_INTERFACE, entity=interface["name"])
                    continue

                # Find the interface status per the shutdown state
                status = "adminDown" if interface["shutdown"] else "up"

                inputs.append(
                    self.test.Input.InterfaceState(
                        name=interface["name"],
                        status=status,
                    ),
                )

        # If the device is a VTEP, add the Vxlan1 interface to the list of interfaces to check
        # TODO: Check if we want to add log here
        if self.manager.is_vtep():
            inputs.append(
                self.test.Input.InterfaceState(
                    name="Vxlan1",
                    status="up",
                ),
            )

        return self.test.Input(interfaces=inputs) if inputs else None
