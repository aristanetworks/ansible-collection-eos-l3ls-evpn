# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._anta.utils import LogMessage
from pyavd._utils import get

from .constants import INTERFACE_MODELS

if TYPE_CHECKING:
    from anta.tests.interfaces import VerifyInterfacesStatus

    from pyavd._anta.utils import ConfigManager, TestLoggerAdapter


class VerifyInterfacesStatusInputFactory:
    """Input factory class for the VerifyInterfacesStatus test."""

    @classmethod
    def create(cls, test: type[VerifyInterfacesStatus], manager: ConfigManager, logger: TestLoggerAdapter) -> VerifyInterfacesStatus.Input | None:
        """Create Input for the VerifyInterfacesStatus test."""
        inputs = []

        for interface_model in INTERFACE_MODELS:
            if (interfaces := get(manager.structured_config, interface_model)) is None:
                logger.info(LogMessage.NO_DATA_MODEL, entity=interface_model)
                continue

            for interface in interfaces:
                manager.update_interface_shutdown(interface)

                if not manager.to_be_validated(interface):
                    logger.info(LogMessage.SKIP_INTERFACE, entity=interface["name"])
                    continue

                status = "adminDown" if interface["shutdown"] else "up"

                inputs.append(
                    test.Input.InterfaceState(
                        name=interface["name"],
                        status=status,
                    ),
                )

        # If the device is a VTEP, add the Vxlan1 interface to the list of interfaces to check
        # TODO: Check if we want to add log here
        if manager.is_vtep():
            inputs.append(
                test.Input.InterfaceState(
                    name="Vxlan1",
                    status="up",
                ),
            )

        return test.Input(interfaces=inputs) if inputs else None
