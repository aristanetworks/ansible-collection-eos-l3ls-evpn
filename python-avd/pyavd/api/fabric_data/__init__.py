# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections import defaultdict
    from ipaddress import IPv4Address

    from pyavd._anta.models import BoundaryLocation, DeviceData, FabricScope


@dataclass(frozen=True)
class FabricData:
    """Stores fabric topology and device information with support for filtering and queries.

    Data is stored in FabricData to support:
      1. Generating test inputs that require information from other devices' structured configurations
         (e.g., peer IPs, interconnect links, fabric-wide relationships)
      2. Enabling efficient fabric-wide filtering and querying of network topology attributes
         (e.g., identifying devices by location, role, or other fabric-level characteristics)

    Device-specific configuration data that isn't needed for broader fabric relationships or testing
    remains in the device's own structured config and is used directly when generating test inputs.

    The dataclass is frozen to ensure:
      - Consistent and immutable data representation
      - Safe sharing between test input factories
      - Usage in different processes in a multiprocessing environment to avoid copying on write

    This class must be instantiated using the create() factory method rather than direct instantiation.
    The create() method requires structured configurations of all devices to build necessary indexes and relationships.
    An optional scope dictionary can be provided to define the fabric's test input generation scope.

    Example:
    ```python
    scope = {
        "boundary": "pod",           # Options: unlimited, fabric, dc, pod, rack
        "allow_bgp_vrfs": True,      # Allow BGP peers in VRFs
    }
    structured_configs = {
        "hostname1": {structured_config1},
        "hostname2": {structured_config2},
        ...
    }
    fabric_data = FabricData.create(structured_configs, scope)
    ```
    """

    # Public attributes that tests can access. More attributes can be added as needed
    scope: FabricScope
    devices: dict[str, DeviceData]
    boundary_index: defaultdict[BoundaryLocation, set[str]]

    # IP indexes. Methods are provided to access these indexes
    _loopback0_ips: dict[str, IPv4Address]
    _vtep_ips: dict[str, IPv4Address]
    _special_ips: dict[str, list[IPv4Address]]

    # Role indexes
    _vteps: set[str]
    _wan_routers: set[str]

    def __new__(cls, *_args: tuple, **_kwargs: dict) -> None:
        """Prevent direct instantiation of the FabricData class."""
        if not hasattr(cls, "_internal_create"):
            msg = "Use FabricData.create() instead of direct instantiation"
            raise TypeError(msg)
        delattr(cls, "_internal_create")
        return super().__new__(cls)

    @classmethod
    def create(cls, structured_configs: dict[str, dict[str, Any]], scope: dict | None = None) -> FabricData:
        """Factory function to create FabricData instance with computed indexes."""
        from pyavd._anta.factories import create_fabric_data

        cls._internal_create = True
        return create_fabric_data(structured_configs, scope)

    def get_devices_by_attribute(self, attr: str, value: Any) -> set[str]:
        """Get devices filtered by any attribute.

        This is a flexible filter that works with any DeviceData attribute,
        using the pre-built indexes when available for efficiency.
        """
        match attr:
            case "is_vtep":
                return self._vteps if value is True else set(self.devices) - self._vteps
            case "is_wan_router":
                return self._wan_routers if value is True else set(self.devices) - self._wan_routers
            case "boundary_location":
                if self.scope.boundary == "unlimited":
                    return set(self.devices)
                return self.boundary_index.get(value, set())
            case _:
                return {hostname for hostname, device in self.devices.items() if getattr(device, attr, None) == value}

    def get_ip_index(self, index_name: str, **filters: dict) -> dict[str, IPv4Address | list[IPv4Address]]:
        """Get an IP index for devices matching the given filters. If no filters are provided, return all IPs.

        Available indexes:
          - loopback0_ips: Loopback0 IPs
          - vtep_ips: VTEP IPs
          - special_ips: Special IPs (Loopback0 & VTEP IPs combined)
        """
        match index_name:
            case "loopback0_ips":
                ip_index = self._loopback0_ips
            case "vtep_ips":
                ip_index = self._vtep_ips
            case "special_ips":
                ip_index = self._special_ips
            case _:
                msg = f"Invalid IP index name: {index_name}. Available indexes: loopback0_ips, vtep_ips, special_ips"
                raise ValueError(msg)

        # If no filters, return the entire index
        if not filters:
            return ip_index

        # Apply filters to get matching devices
        matching_devices = set(self.devices)
        for attr, value in filters.items():
            matching_devices &= self.get_devices_by_attribute(attr, value)

        # Return filtered IP index
        return {hostname: ip_index[hostname] for hostname in matching_devices if hostname in ip_index}

    def to_dict(self) -> dict:
        """Convert FabricData to a JSON-seralizable dictionary."""
        return {
            "scope": self.scope.model_dump(mode="json"),
            "devices": {
                hostname: {
                    "hostname": device.hostname,
                    "dns_domain": device.dns_domain,
                    "is_deployed": device.is_deployed,
                    "fabric_name": device.fabric_name,
                    "dc_name": device.dc_name,
                    "pod_name": device.pod_name,
                    "rack": device.rack,
                    "boundary_location": "/".join(
                        filter(
                            None, (device.boundary_location.fabric, device.boundary_location.dc, device.boundary_location.pod, device.boundary_location.rack)
                        )
                    )
                    if self.scope.boundary != "unlimited"
                    else None,
                    "is_vtep": device.is_vtep,
                    "is_wan_router": device.is_wan_router,
                    "loopback0_ip": str(device.loopback0_ip) if device.loopback0_ip else None,
                    "vtep_ip": str(device.vtep_ip) if device.vtep_ip else None,
                    "routed_interface_ips": {intf: str(ip) for intf, ip in device.routed_interface_ips.items()},
                }
                for hostname, device in self.devices.items()
            },
            "boundary_index": {
                "/".join(filter(None, (loc.fabric, loc.dc, loc.pod, loc.rack))): sorted(devices) for loc, devices in self.boundary_index.items()
            },
            "_loopback0_ips": {device: str(ip) for device, ip in self._loopback0_ips.items()},
            "_vtep_ips": {device: str(ip) for device, ip in self._vtep_ips.items()},
            "_special_ips": {device: [str(ip) for ip in ips] for device, ips in self._special_ips.items()},
            "_vteps": sorted(self._vteps),
            "_wan_routers": sorted(self._wan_routers),
        }
