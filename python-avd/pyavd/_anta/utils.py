# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Utility functions used by PyAVD for ANTA."""

from __future__ import annotations

from ipaddress import IPv4Address, ip_interface
from pathlib import Path
from typing import TYPE_CHECKING

from pyavd._utils import get, get_item

if TYPE_CHECKING:
    from anta.catalog import AntaCatalog


def get_device_location_metadata(structured_config: dict) -> tuple[str | None, str | None, str | None, str | None]:
    """Extract the location metadata from the structured configuration."""
    return (
        get(structured_config, "metadata.fabric_name"),
        get(structured_config, "metadata.dc_name"),
        get(structured_config, "metadata.pod_name"),
        get(structured_config, "metadata.rack"),
    )


def get_device_special_ips(structured_config: dict) -> tuple[IPv4Address | None, IPv4Address | None]:
    """Extract Loopback0 and VTEP IP addresses from the structured configuration."""
    loopback0_ip = get(get_item(get(structured_config, "loopback_interfaces", []), "name", "Loopback0", default={}), "ip_address")
    if "Dps" in get(structured_config, "vxlan_interface.vxlan1.vxlan.source_interface", ""):
        interface_model = get(structured_config, "dps_interfaces", default=[])
    else:
        interface_model = get(structured_config, "loopback_interfaces", default=[])
    vtep_ip = get(get_item(interface_model, "name", get(structured_config, "vxlan_interface.vxlan1.vxlan.source_interface", ""), default={}), "ip_address")

    return (
        ip_interface(loopback0_ip).ip if loopback0_ip else None,
        ip_interface(vtep_ip).ip if vtep_ip else None,
    )


def get_device_roles(structured_config: dict) -> tuple[bool, bool]:
    """Extract device roles from the structured configuration."""
    is_vtep = get(structured_config, "vxlan_interface") is not None
    is_wan_router = is_vtep and "Dps" in get(structured_config, "vxlan_interface.vxlan1.vxlan.source_interface", "")

    return is_vtep, is_wan_router


def get_device_ip_by_interface(structured_config: dict) -> dict[str, IPv4Address]:
    """Extract IP ethernet interfaces from the structured configuration."""
    ip_by_interface = {}
    for interface in get(structured_config, "ethernet_interfaces", default=[]):
        if (ip_address := get(interface, "ip_address")) is not None and ip_address != "dhcp" and get(interface, "switchport.enabled") is False:
            ip_by_interface[interface["name"]] = ip_interface(ip_address).ip
    return ip_by_interface


def dump_anta_catalog(hostname: str, catalog: AntaCatalog, catalog_dir: str) -> None:
    """Dump the ANTA catalog for a device to the provided catalog directory.

    The catalog will be saved as a JSON file named after the device: `<device>.json`.
    """
    catalog_path = Path(catalog_dir) / f"{hostname}.json"
    catalog_dump = catalog.dump()

    with catalog_path.open(mode="w", encoding="UTF-8") as stream:
        stream.write(catalog_dump.to_json())
