# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._cv.api.arista.inventory.v1 import Device, DeviceKey, DeviceServiceStub, DeviceStreamRequest
from pyavd._cv.api.arista.time import TimeBounds

from .constants import DEFAULT_API_TIMEOUT
from .exceptions import get_cv_client_exception

if TYPE_CHECKING:
    from datetime import datetime

    from . import CVClientProtocol


class InventoryMixin(Protocol):
    """Only to be used as mixin on CVClient class."""

    inventory_api_version: Literal["v1"] = "v1"

    async def get_inventory_devices(
        self: CVClientProtocol,
        devices: list[tuple[str, str, str]] | None = None,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[Device]:
        """
        Get Devices using arista.inventory.v1.DeviceService.GetAll API.

        If 'devices' is set to None, all devices will be returned.

        Parameters:
            devices: List of tuples where each tuple is in the format (serial number, system_mac_address, hostname)
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            Device objects.
        """
        request = DeviceStreamRequest(partial_eq_filter=[], time=TimeBounds(start=None, end=time))
        if devices:
            for serial_number, system_mac_address, hostname in devices:
                request.partial_eq_filter.append(
                    Device(
                        key=DeviceKey(device_id=serial_number),
                        system_mac_address=system_mac_address,
                        hostname=hostname,
                    ),
                )
        client = DeviceServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            inventory_devices = [response.value async for response in responses]
        except Exception as e:
            raise get_cv_client_exception(e, f"devices '{devices}'") or e

        return inventory_devices
