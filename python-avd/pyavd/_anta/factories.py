# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Factory functions used by PyAVD for ANTA."""

from __future__ import annotations

from collections import defaultdict
from logging import getLogger
from time import perf_counter
from typing import TYPE_CHECKING

from anta.catalog import AntaCatalog, AntaTestDefinition
from anta.models import AntaTest

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._utils import get, get_v2

from .constants import StructuredConfigKey
from .logs import LogMessage, TestLoggerAdapter
from .models import BoundaryLocation, DeviceData, ExtendedDeviceData, FabricScope
from .utils import get_device_location_metadata, get_device_roles, get_device_routed_interface_ips, get_device_special_ips

if TYPE_CHECKING:
    from ipaddress import IPv4Address

    from pyavd.api.anta_test_spec import TestSpec
    from pyavd.api.fabric_data import FabricData


LOGGER = getLogger(__name__)


def create_fabric_data(structured_configs: dict, scope: dict | None = None) -> FabricData:
    """Factory function to create a FabricData instance from device structured configurations."""
    from pyavd.api.fabric_data import FabricData

    devices: dict[str, DeviceData] = {}
    # TODO: Might need to handle Pydantic validation errors more gracefully
    scope_obj = FabricScope(**scope) if scope is not None else FabricScope()
    boundary_index: defaultdict[BoundaryLocation, set[str]] = defaultdict(set)

    loopback0_ips: dict[str, IPv4Address] = {}
    vtep_ips: dict[str, IPv4Address] = {}
    special_ips: defaultdict[str, list[IPv4Address]] = defaultdict(list)

    vteps: set[str] = set()
    wan_routers: set[str] = set()

    start_time = perf_counter()
    LOGGER.debug("creating FabricData object with scope %s", scope)

    # Build all the indexes
    for hostname, structured_config in structured_configs.items():
        device_data = create_device_data(hostname, structured_config, scope_obj.boundary)
        devices[hostname] = device_data

        if scope_obj.boundary != "unlimited" and getattr(device_data.boundary_location, scope_obj.boundary) is None:
            field = "rack" if scope_obj.boundary == "rack" else f"{scope_obj.boundary}_name"
            msg = f"Device {hostname} is missing required metadata field '{field}' for boundary '{scope_obj.boundary}'"
            raise ValueError(msg)

        # Build boundary index
        if scope_obj.boundary != "unlimited":
            boundary_index[device_data.boundary_location].add(hostname)

        # Build IP indexes
        if device_data.loopback0_ip:
            loopback0_ips[hostname] = device_data.loopback0_ip
            special_ips[hostname].append(device_data.loopback0_ip)
        else:
            LOGGER.debug("<%s>: skipped Loopback0 IP mapping - IP not found", hostname)

        if device_data.vtep_ip:
            vtep_ips[hostname] = device_data.vtep_ip
            special_ips[hostname].append(device_data.vtep_ip)
        else:
            LOGGER.debug("<%s>: skipped VTEP IP mapping - IP not found", hostname)

        # Build role indexes
        if device_data.is_vtep:
            vteps.add(hostname)
        if device_data.is_wan_router:
            wan_routers.add(hostname)

    fabric_data = FabricData(
        devices=devices,
        scope=scope_obj,
        boundary_index=boundary_index,
        _loopback0_ips=loopback0_ips,
        _vtep_ips=vtep_ips,
        _special_ips=special_ips,
        _vteps=vteps,
        _wan_routers=wan_routers,
    )

    stop_time = perf_counter()
    LOGGER.debug("created FabricData object in %.8f seconds", stop_time - start_time)

    return fabric_data


def create_device_data(hostname: str, structured_config: dict, boundary: str) -> DeviceData:
    """Create the DeviceData object for the given hostname."""
    fabric_name, dc_name, pod_name, rack = get_device_location_metadata(structured_config)
    boundary_location = create_device_boundary_location(fabric_name, dc_name, pod_name, rack, boundary)
    is_vtep, is_wan_router = get_device_roles(structured_config)
    loopback0_ip, vtep_ip = get_device_special_ips(structured_config)
    routed_interface_ips = get_device_routed_interface_ips(structured_config)

    return DeviceData(
        hostname=hostname,
        dns_domain=get(structured_config, "dns_domain"),
        is_deployed=get(structured_config, "is_deployed", default=True),
        fabric_name=fabric_name,
        dc_name=dc_name,
        pod_name=pod_name,
        rack=rack,
        boundary_location=boundary_location,
        is_vtep=is_vtep,
        is_wan_router=is_wan_router,
        loopback0_ip=loopback0_ip,
        vtep_ip=vtep_ip,
        routed_interface_ips=routed_interface_ips,
    )


def create_device_boundary_location(fabric_name: str | None, dc_name: str | None, pod_name: str | None, rack: str | None, boundary: str) -> BoundaryLocation:
    """Create a BoundaryLocation object for the location of a device up to the specified boundary level."""
    match boundary:
        case "unlimited":
            return BoundaryLocation()
        case "fabric":
            return BoundaryLocation(fabric=fabric_name)
        case "dc":
            return BoundaryLocation(fabric=fabric_name, dc=dc_name)
        case "pod":
            return BoundaryLocation(fabric=fabric_name, dc=dc_name, pod=pod_name)
        case "rack":
            return BoundaryLocation(fabric=fabric_name, dc=dc_name, pod=pod_name, rack=rack)
        case _:
            msg = f"Invalid boundary level: {boundary} - must be one of: unlimited, fabric, dc, pod, rack"
            raise ValueError(msg)


def create_catalog(hostname: str, structured_config: dict, fabric_data: FabricData, test_specs: list[TestSpec]) -> AntaCatalog:
    """Create an ANTA catalog for a device from the provided test specs."""
    # TODO: Remove this temporary workaround once the metadata is added in the structured config
    temporary_keys_to_remove = ["fabric_name", "dc_name", "pod_name", "rack"]
    for key in temporary_keys_to_remove:
        structured_config.get("metadata", {}).pop(key, None)

    device_data = ExtendedDeviceData(
        hostname=hostname,
        fabric_data=fabric_data,
        structured_config=EosCliConfigGen._load(structured_config),
    )

    test_definitions: list[AntaTestDefinition] = []
    for test in test_specs:
        test_logger = TestLoggerAdapter.create(device=hostname, test=test.test_class.name, logger=LOGGER)
        test_definition = create_test_definition(test, device_data, test_logger)

        # Skip the test if we couldn't create the test definition. Logging is done in the TestSpec class
        if test_definition is None:
            continue

        # Tag the test with the device name for the final catalog and add metadata
        test_definition.inputs.filters = AntaTest.Input.Filters(tags={hostname})
        test_definition.inputs.result_overwrite = AntaTest.Input.ResultOverwrite(custom_field="Generated by AVD")
        test_definitions.append(test_definition)

    # Sort by module and test name for consistent output
    # TODO: Add a proper sort method in the AntaCatalog class to also sort the inputs
    test_definitions.sort(key=lambda x: (x.test.__module__, x.test.name))
    return AntaCatalog(tests=test_definitions)


def create_test_definition(test_spec: TestSpec, device_data: ExtendedDeviceData, logger: TestLoggerAdapter) -> AntaTestDefinition | None:
    """Create the AntaTestDefinition from this TestSpec instance."""
    # Skip the test if the conditional keys are not present in the structured config
    if test_spec.conditional_keys and not all(get_v2(device_data.structured_config, key.value) for key in test_spec.conditional_keys):
        keys = StructuredConfigKey.to_string_list(test_spec.conditional_keys)
        logger.debug(LogMessage.INPUT_NO_DATA_MODEL, caller=", ".join(keys))
        return None

    # AntaTestDefinition takes `inputs=None` if the test does not require input
    inputs = None

    # Create the AntaTest.Input instance from the input dict if available
    if test_spec.input_dict:
        logger.debug(LogMessage.INPUT_RENDERING, caller="input dictionary")
        rendered_inputs = {}
        for input_field, structured_config_key in test_spec.input_dict.items():
            field_value = get_v2(device_data.structured_config, structured_config_key.value)
            if field_value is not None:
                rendered_inputs[input_field] = field_value
            else:
                logger.debug(LogMessage.INPUT_NO_DATA_MODEL, caller=structured_config_key.value)
                return None
        logger.debug(LogMessage.INPUT_RENDERED, inputs=rendered_inputs)
        inputs = test_spec.test_class.Input(**rendered_inputs)

    # Else create the AntaTest.Input instance from the input factory if available
    elif test_spec.input_factory:
        logger.debug(LogMessage.INPUT_RENDERING, caller="input factory")
        factory = test_spec.input_factory(device_data, logger)  # pylint: disable=not-callable
        inputs = factory.create()
        if inputs is None:
            logger.debug(LogMessage.INPUT_NONE_FOUND)
            return None

    return AntaTestDefinition(test=test_spec.test_class, inputs=inputs)
