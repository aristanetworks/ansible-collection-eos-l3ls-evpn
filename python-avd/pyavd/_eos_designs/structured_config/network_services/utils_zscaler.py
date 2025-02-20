# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import asyncio
from functools import cached_property
from logging import getLogger
from typing import TYPE_CHECKING, Protocol

from pyavd._cv.client import CVClient
from pyavd._cv.workflows.models import CVDevice
from pyavd._cv.workflows.verify_devices_on_cv import verify_devices_in_cloudvision_inventory
from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from pyavd._cv.api.arista.swg.v1 import Location, VpnEndpoint

    from . import AvdStructuredConfigNetworkServicesProtocol

LOGGER = getLogger(__name__)


class UtilsZscalerMixin(Protocol):
    """
    Mixin Class with internal functions for Zscaler.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def _zscaler_endpoints(self: AvdStructuredConfigNetworkServicesProtocol) -> EosDesigns.ZscalerEndpoints:
        """
        Returns zscaler_endpoints data model built via CloudVision API calls, unless they are provided in the input variables.

        Should only be called for CV Pathfinder Client devices.
        """
        return self.inputs.zscaler_endpoints or asyncio.run(self._generate_zscaler_endpoints())

    async def _generate_zscaler_endpoints(self: AvdStructuredConfigNetworkServicesProtocol) -> EosDesigns.ZscalerEndpoints:
        """
        Call CloudVision SWG APIs to generate the zscaler_endpoints model.

        Should only be called for CV Pathfinder Client devices.

        TODO: Add support for cv_verify_certs
        """
        context = "The WAN Internet-exit integration with Zscaler fetches information from CloudVision"
        if not (cv_server := self.inputs.cv_server):
            msg = f"{context} and requires 'cv_server' to be set."
            raise AristaAvdInvalidInputsError(msg)
        if not (cv_token := self.inputs.cv_token):
            msg = f"{context} and requires 'cv_token' to be set."
            raise AristaAvdInvalidInputsError(msg)

        if self.shared_utils.wan_site is None or not self.shared_utils.wan_site.location:
            region_key = f"name={self.shared_utils.wan_region.name}" if self.shared_utils.wan_region is not None else ""
            site_key = f"name={self.shared_utils.wan_site.name}" if self.shared_utils.wan_site is not None else ""
            msg = f"{context} and requires 'cv_pathfinder_regions[{region_key}].sites[{site_key}].location' to be set."
            raise AristaAvdInvalidInputsError(msg)

        wan_site_location = self.shared_utils.wan_site.location

        async with CVClient(servers=[cv_server], token=cv_token) as cv_client:
            cv_device = CVDevice(self.shared_utils.hostname, self.shared_utils.serial_number, self.shared_utils.system_mac_address)
            cv_inventory_devices: list[CVDevice] = await verify_devices_in_cloudvision_inventory(
                devices=[cv_device],
                skip_missing_devices=True,
                warnings=[],
                cv_client=cv_client,
            )
            if not cv_inventory_devices:
                msg = f"{context} but could not find '{self.shared_utils.hostname}' on the server '{cv_server}'."
                raise AristaAvdError(msg)
            if len(cv_inventory_devices) > 1:
                msg = (
                    f"{context} but found more than one device named '{self.shared_utils.hostname}' on the server '{cv_server}'. "
                    "Set 'serial_number' for the device in AVD vars, to ensure a unique match."
                )
                raise AristaAvdError(msg)
            device_id: str = cv_inventory_devices[0].serial_number
            request_time, _ = await cv_client.set_swg_device(device_id=device_id, service="zscaler", location=wan_site_location)
            cv_endpoint_status = await cv_client.wait_for_swg_endpoint_status(device_id=device_id, service="zscaler", start_time=request_time)

        device_location: Location = cv_endpoint_status.device_location

        zscaler_endpoints = EosDesigns.ZscalerEndpoints(
            cloud_name=cv_endpoint_status.cloud_name,
            device_location=EosDesigns.ZscalerEndpoints.DeviceLocation(city=device_location.city, country=device_location.country),
        )
        if not getattr(cv_endpoint_status, "vpn_endpoints", None) or not getattr(cv_endpoint_status.vpn_endpoints, "values", None):
            msg = f"{context} but did not get any IPsec Tunnel endpoints back from the Zscaler API."
            raise AristaAvdError(msg)

        for key, cls in (
            ("primary", EosDesigns.ZscalerEndpoints.Primary),
            ("secondary", EosDesigns.ZscalerEndpoints.Secondary),
            ("tertiary", EosDesigns.ZscalerEndpoints.Tertiary),
        ):
            if key in cv_endpoint_status.vpn_endpoints.values:
                vpn_endpoint: VpnEndpoint = cv_endpoint_status.vpn_endpoints.values[key]
                location: Location = vpn_endpoint.endpoint_location
                setattr(
                    zscaler_endpoints,
                    key,
                    cls(
                        ip_address=vpn_endpoint.ip_address.value,
                        datacenter=vpn_endpoint.datacenter,
                        city=location.city,
                        country=location.country,
                        region=location.region,
                        latitude=location.latitude,
                        longitude=location.longitude,
                    ),
                )

        return zscaler_endpoints
