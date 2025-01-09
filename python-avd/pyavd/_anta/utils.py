# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Utility functions used by PyAVD for ANTA."""

from __future__ import annotations

from ipaddress import IPv4Address, ip_interface
from json import dumps
from logging import getLogger
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from anta.catalog import AntaCatalog

    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
    from pyavd.api.fabric_data import FabricData

LOGGER = getLogger(__name__)


def get_device_special_ips(structured_config: EosCliConfigGen) -> tuple[IPv4Address | None, IPv4Address | None]:
    """Extract Loopback0 and VTEP IP addresses from the structured configuration."""
    loopback0_ip = structured_config.loopback_interfaces["Loopback0"].ip_address if "Loopback0" in structured_config.loopback_interfaces else None

    vxlan_source_intf = structured_config.vxlan_interface.vxlan1.vxlan.source_interface
    if vxlan_source_intf:
        interface_model = structured_config.dps_interfaces if "Dps" in vxlan_source_intf else structured_config.loopback_interfaces
        vtep_ip = interface_model[vxlan_source_intf].ip_address if vxlan_source_intf in interface_model else None
    else:
        vtep_ip = None

    return (
        ip_interface(loopback0_ip).ip if loopback0_ip else None,
        ip_interface(vtep_ip).ip if vtep_ip else None,
    )


def get_device_roles(structured_config: EosCliConfigGen) -> tuple[bool, bool]:
    """Extract device roles from the structured configuration."""
    vxlan_source_intf = structured_config.vxlan_interface.vxlan1.vxlan.source_interface
    is_vtep = bool(vxlan_source_intf)
    is_wan_router = is_vtep and "Dps" in vxlan_source_intf

    return is_vtep, is_wan_router


def get_device_routed_interface_ips(structured_config: EosCliConfigGen) -> dict[str, IPv4Address]:
    """Extract routed ethernet interface IPs from the structured configuration. Interface in DHCP mode are excluded."""
    routed_interface_ips = {}
    for interface in structured_config.ethernet_interfaces:
        if interface.ip_address and interface.ip_address != "dhcp" and interface.switchport.enabled is False:
            routed_interface_ips[interface.name] = ip_interface(interface.ip_address).ip

    return routed_interface_ips


def dump_anta_catalog(hostname: str, catalog: AntaCatalog, catalog_dir: str) -> None:
    """Dump the ANTA catalog for a device to the provided catalog directory.

    The catalog will be saved as a JSON file named after the device: `<device>.json`.
    """
    catalog_path = Path(catalog_dir) / f"{hostname}.json"
    catalog_dump = catalog.dump()

    LOGGER.debug("<%s> dumping ANTA catalog at %s", hostname, catalog_path)
    with catalog_path.open(mode="w", encoding="UTF-8") as stream:
        stream.write(catalog_dump.to_json())


def dump_fabric_data(filename: str | Path, fabric_data: FabricData) -> None:
    """Dump a FabricData instance to a JSON file."""
    fabric_data_path = Path(filename)
    fabric_data_json = dumps(fabric_data.to_dict(), indent=2)

    LOGGER.debug("dumping FabricData at %s", fabric_data_path)
    with fabric_data_path.open(mode="w", encoding="UTF-8") as stream:
        stream.write(fabric_data_json)
