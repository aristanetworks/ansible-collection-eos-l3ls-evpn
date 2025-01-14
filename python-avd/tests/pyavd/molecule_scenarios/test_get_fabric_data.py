# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from copy import deepcopy
from ipaddress import IPv4Address

import pytest

from pyavd import get_fabric_data
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
