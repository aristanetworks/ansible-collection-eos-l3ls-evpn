# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd.j2filters.natural_sort import natural_sort

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigBase


class IpNameServersMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def dns_settings(self: AvdStructuredConfigBase) -> None:
        """
        Parse "dns_settings" data-model and set ip_name_servers, ip_domain_lookup, dns_domain accordingly.

        Servers in the new data model may have management VRFs dynamically set.

        This will not be set together with any of the deprecated models (enforced by schema).
        """
        if not self.inputs.dns_settings:
            return

        if self.inputs.dns_settings.domain:
            self.structured_config.dns_domain = self.inputs.dns_settings.domain

        has_mgmt_ip = bool(self.shared_utils.node_config.mgmt_ip or self.shared_utils.node_config.ipv6_mgmt_ip)
        vrf_source_interface_map = {}
        for server in self.inputs.dns_settings.servers:
            # Initialize a set with vrf defined under the server
            vrfs = set()
            if server.vrf:
                vrfs.add(server.vrf)
            if server.use_mgmt_interface_vrf and has_mgmt_ip:
                vrf = self.inputs.mgmt_interface_vrf
                vrfs.add(vrf)
                vrf_source_interface_map[vrf] = self.shared_utils.mgmt_interface

            if server.use_inband_mgmt_vrf and self.shared_utils.inband_mgmt_interface:
                # self.shared_utils.inband_mgmt_vrf returns None for the default VRF, but here we need "default" to avoid duplicates.
                vrf = self.shared_utils.inband_mgmt_vrf or "default"
                vrfs.add(vrf)
                vrf_source_interface_map[vrf] = self.shared_utils.inband_mgmt_interface

            if not any([vrfs, server.use_mgmt_interface_vrf, server.use_inband_mgmt_vrf]):
                # If no VRFs are defined (and we are not just ignoring missing mgmt config), try to apply the default mgmt protocol if set, else "default".
                vrf = self.shared_utils.default_mgmt_protocol_vrf or "default"
                vrfs.add(vrf)
                vrf_source_interface_map[vrf] = self.shared_utils.default_mgmt_protocol_interface

            # Ensure default VRF is added first
            if "default" in vrfs:
                vrfs.remove("default")
                # Add server without VRF field
                self.structured_config.ip_name_servers.append_new(ip_address=server.ip_address, priority=server.priority, vrf="default")

            for vrf in natural_sort(vrfs):
                # Add server with VRF field.
                self.structured_config.ip_name_servers.append_new(ip_address=server.ip_address, priority=server.priority, vrf=vrf)

        # Setting source interface here to avoid parsing the server list multiple times.
        for vrf, source_interface in vrf_source_interface_map.items():
            self.structured_config.ip_domain_lookup.source_interfaces.append_new(name=source_interface, vrf=vrf if vrf != "default" else None)

    @cached_property
    def ip_domain_lookup(self: AvdStructuredConfigBase) -> dict | None:
        """
        ip_domain_lookup set based on the deprecated "source_interfaces.domain_lookup" input data-model.

        This will not be set together with dns_settings (enforced by schema).

        TODO: Remove support in AVD 6.0.0
        """
        if self.inputs.source_interfaces.domain_lookup:
            for source_interface in self._build_source_interfaces(
                self.inputs.source_interfaces.domain_lookup.mgmt_interface,
                self.inputs.source_interfaces.domain_lookup.inband_mgmt_interface,
                "IP Domain Lookup",
            ):
                self.structured_config.ip_domain_lookup.source_interfaces.append_new(name=source_interface["name"], vrf=source_interface.get("vrf"))

    @cached_property
    def ip_name_servers(self: AvdStructuredConfigBase) -> None:
        """
        ip_name_servers set based on the deprecated "name_servers" input data-model.

        This will not be set together with dns_settings (enforced by schema).

        TODO: Remove support in AVD 6.0.0
        """
        if self.inputs.name_servers:
            self.structured_config.ip_name_servers.extend(
                [EosCliConfigGen.IpNameServersItem(ip_address=name_server, vrf=self.inputs.mgmt_interface_vrf) for name_server in self.inputs.name_servers]
            )
