# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections.abc import Iterable
from copy import deepcopy
from ipaddress import IPv4Address

import pytest

from pyavd import get_device_anta_catalog, get_fabric_data
from tests.models import MoleculeScenario


@pytest.mark.molecule_scenarios("anta_runner")
def test_get_fabric_data(molecule_scenario: MoleculeScenario) -> None:
    """Test get_fabric_data."""
    structured_configs = {host.name: deepcopy(host.structured_config) for host in molecule_scenario.hosts}
    fabric_data = get_fabric_data(structured_configs)

    # Test basic fabric data properties
    assert fabric_data.scope.boundary == "unlimited"
    assert len(fabric_data.boundary_index) == 0
    assert len(fabric_data.devices) == len(molecule_scenario.hosts)

    # Test special_ips is a superset of other IP indexes
    special_ips = fabric_data.get_ip_index(index_name="special_ips")
    loopback_ips = fabric_data.get_ip_index(index_name="loopback0_ips")
    vtep_ips = fabric_data.get_ip_index(index_name="vtep_ips")
    for device in special_ips:
        if device in loopback_ips:
            assert loopback_ips[device] == special_ips[device][0]
        if device in vtep_ips:
            assert vtep_ips[device] == special_ips[device][1]

    # Test VTEP role and IP consistency
    vtep_devices = fabric_data.get_devices_by_attribute(attr="is_vtep", value=True)
    assert all(device in vtep_ips for device in vtep_devices)
    non_vtep_devices = fabric_data.get_devices_by_attribute(attr="is_vtep", value=False)
    assert all(device not in vtep_ips for device in non_vtep_devices)

    # Test WAN router integrity
    wan_routers = fabric_data.get_devices_by_attribute(attr="is_wan_router", value=True)
    wan_vteps = {device for device in wan_routers if device in vtep_ips}
    assert all(fabric_data.devices[device].is_wan_router for device in wan_routers)
    assert all(fabric_data.devices[device].vtep_ip for device in wan_vteps)

    # Test VTEP and special IPs relationships for non-WAN routers
    non_wan_vteps = {device for device in vtep_devices if not fabric_data.devices[device].is_wan_router}
    non_wan_special_ips = fabric_data.get_ip_index(index_name="special_ips", is_wan_router=False)

    # Each non-WAN VTEP should have both loopback0 and VTEP IPs
    for device in non_wan_vteps:
        if device in non_wan_special_ips:
            assert len(non_wan_special_ips[device]) == 2

    # Test routed interface consistency
    for device, data in fabric_data.devices.items():
        for intf_name, ip in data.routed_interface_ips.items():
            assert isinstance(ip, IPv4Address)
            # Test that the interface exists in structured config
            assert any(intf["name"] == intf_name for intf in structured_configs[device].get("ethernet_interfaces", []))

    # Test filtering consistency
    for attr in ["is_deployed", "fabric_name", "dc_name", "pod_name", "rack"]:
        for device, data in fabric_data.devices.items():
            value = getattr(data, attr, None)
            if value is not None:
                matching_devices = fabric_data.get_devices_by_attribute(attr, value)
                assert device in matching_devices

    # TODO: When https://github.com/aristanetworks/avd/pull/4827 is merged:
    # Test boundary relationships (boundary != unlimited):
    #   - Verify all devices belong to a boundary
    #   - Test boundary hierarchy (rack -> pod -> dc)
    #   - Validate proper boundary nesting (racks in pods, pods in DCs)


@pytest.mark.molecule_scenarios("anta_runner")
@pytest.mark.parametrize(
    "run_config",
    [
        {
            "catalog_attr": "anta_catalog_default",
            "fabric_scope": None,
        },
        {"catalog_attr": "anta_catalog_allow_bgp_vrfs", "fabric_scope": {"allow_bgp_vrfs": True}},
    ],
)
def test_get_device_anta_catalog(molecule_scenario: MoleculeScenario, run_config: dict) -> None:
    """Test get_device_anta_catalog with different run configurations."""
    structured_configs = {host.name: deepcopy(host.structured_config) for host in molecule_scenario.hosts}
    assert len(structured_configs) == len(molecule_scenario.hosts)
    fabric_data = get_fabric_data(structured_configs, scope=run_config["fabric_scope"])

    # TODO: We could simplify this by having equality implemented in AntaCatalog
    for host in molecule_scenario.hosts:
        generated_catalog = get_device_anta_catalog(host.name, structured_configs[host.name], fabric_data)
        reference_catalog = getattr(host, run_config["catalog_attr"])
        assert len(generated_catalog.tests) == len(reference_catalog.tests)

        # Input checks for each test
        for gen_test, ref_test in zip(generated_catalog.tests, reference_catalog.tests, strict=True):
            # Check the test classes match
            assert gen_test.test == ref_test.test

            exclusions = {"exclude": {"result_overwrite", "filters"}, "exclude_unset": True, "exclude_defaults": True, "exclude_none": True}
            gen_test_inputs = gen_test.inputs.model_dump(**exclusions)
            ref_test_inputs = ref_test.inputs.model_dump(**exclusions)
            for field_name, field_value in gen_test_inputs.items():
                assert field_name in ref_test_inputs
                if isinstance(field_value, Iterable):
                    assert len(field_value) == len(ref_test_inputs[field_name])
                else:
                    assert field_value == ref_test_inputs[field_name]
