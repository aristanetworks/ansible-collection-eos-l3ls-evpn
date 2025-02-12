# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.client.exceptions import CVInactiveDevices, CVWorkspaceSubmitInactiveDevices

if TYPE_CHECKING:
    from .models import CVDevice, CVEosConfig

LOGGER = getLogger(__name__)


def verify_devices_streaming(
    *,
    deployed_configs: list[CVEosConfig],
    warnings: list[Exception],
    force: bool,
) -> None:
    """
    Verify streaming status of devices.

    Raise an exception if there is at least one targeted inactive device and force is not True.
    Else - append exception to warnings.
    """
    serial_numbers_of_appended_devices: set[str] = set()
    inactive_devices: list[CVDevice] = []
    # Form the list of CVDevice objects which will cause a failure of a Workspace submission due to
    #   - Attempt to update configuration of inactive device
    #   - TODO: Attempt to update image of inactive device
    for deployed_config in deployed_configs:
        if not deployed_config.device._streaming and deployed_config.device.serial_number not in serial_numbers_of_appended_devices:
            serial_numbers_of_appended_devices.add(deployed_config.device.serial_number)
            inactive_devices.append(deployed_config.device)

    if inactive_devices:
        warnings.append(
            inactive_devices_handler(
                inactive_devices=inactive_devices,
                force=force,
            )
        )


def inactive_devices_handler(*, inactive_devices: list[CVDevice], force: bool) -> Exception:
    """
    Handle usecase when inactive devices present in CV are targeted for configuration change.

    Generate an exception when Workspace submission is not forced.
    Otherwise - append exception to warnings.
    """
    if not force:
        exception = CVWorkspaceSubmitInactiveDevices(CVWorkspaceSubmitInactiveDevices.__doc__, inactive_devices)
        raise exception
    exception = CVInactiveDevices(CVInactiveDevices.__doc__, inactive_devices)

    LOGGER.warning(
        "verify_devices_streaming: %s %s",
        CVInactiveDevices.__doc__,
        inactive_devices,
    )

    return exception
