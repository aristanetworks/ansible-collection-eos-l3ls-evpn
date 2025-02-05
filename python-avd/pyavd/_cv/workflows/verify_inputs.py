# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.client.exceptions import CVDuplicatedDevices
from pyavd._utils import groupby_obj

if TYPE_CHECKING:
    from .models import CVDevice

LOGGER = getLogger(__name__)


def verify_device_inputs(*, devices: list[CVDevice], tolerate_duplicated_devices: bool, warnings: list[Exception]) -> None:
    """
    Verify device inputs from structured config files.

    This includes:
        - Checking for presence of the duplicated `serial_number` or `metadata.system_mac_address` values.
    """
    # List object to hold info regaridng devices with duplicated serial_number
    duplicated_serial_number: list[dict[str, str | list[str]]] = []
    # List object to hold info regaridng devices with duplicated system_mac_address
    duplicated_system_mac_address: list[dict[str, str | list[str]]] = []
    # Set object to track IDs of unique CVDevice objects
    unique_device_ids: set[str] = set()
    # List object to hold unique CVDevice objects from original `devices`
    unique_devices: list[CVDevice] = []

    # Deduplicate CVDevice objects as original `devices` list may contain duplicated items
    for device in devices:
        if (device_id := id(device)) not in unique_device_ids:
            unique_device_ids.add(device_id)
            unique_devices.append(device)

    # Group devices based on <CVDevice>.serial_number as long as it's not None
    devices_grouped_by_serial_number = groupby_obj(
        list_of_objects=[device for device in unique_devices if device.serial_number is not None], attr="serial_number"
    )

    # Group devices based on <CVDevice>.system_mac_address as long as it's not None
    devices_grouped_by_system_mac_address = groupby_obj(
        list_of_objects=[device for device in unique_devices if device.system_mac_address is not None], attr="system_mac_address"
    )

    for current_serial_number, device_iterator_object in devices_grouped_by_serial_number:
        if len(devices_with_current_serial_number := list(device_iterator_object)) > 1:
            duplicated_serial_number.append(
                {"duplicated_serial_number": current_serial_number, "devices_with_duplicated_serial_number": devices_with_current_serial_number}
            )

    for current_system_mac_address, device_iterator_object in devices_grouped_by_system_mac_address:
        if len(devices_with_current_system_mac_address := list(device_iterator_object)) > 1:
            duplicated_system_mac_address.append(
                {
                    "duplicated_system_mac_address": current_system_mac_address,
                    "devices_with_duplicated_system_mac_address": devices_with_current_system_mac_address,
                }
            )

    if duplicated_serial_number or duplicated_system_mac_address:
        warnings.append(
            duplicated_devices_handler(
                duplicated_serial_number=duplicated_serial_number,
                duplicated_system_mac_address=duplicated_system_mac_address,
                tolerate_duplicated_devices=tolerate_duplicated_devices,
            )
        )


def duplicated_devices_handler(
    *,
    duplicated_serial_number: list[dict[str, str | list[str]]],
    duplicated_system_mac_address: list[dict[str, str | list[str]]],
    tolerate_duplicated_devices: bool,
) -> Exception:
    """
    Handle input devices with duplicated `serial_number`s or `metadata.system_mac_address`es.

      - Raise an exception if tolerate_duplicated_devices is set to False.
      - Return an Exception if tolerate_duplicated_devices is set to True.
    """
    exception = CVDuplicatedDevices("Duplicated devices found in inventory", duplicated_serial_number, duplicated_system_mac_address)
    if not tolerate_duplicated_devices:
        raise exception
    if duplicated_serial_number:
        LOGGER.warning(
            "verify_inputs: Devices with duplicated serial_number discovered in inventory (structured config): %s",
            duplicated_serial_number,
        )
    if duplicated_system_mac_address:
        LOGGER.warning(
            "verify_inputs: Devices with duplicated system_mac_address discovered in inventory (structured config): %s",
            duplicated_system_mac_address,
        )
    return exception
