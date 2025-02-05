# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class RouterPimSparseModeMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_pim_sparse_mode(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Return structured config for router_pim.

        Used for to configure RPs on the VRF
        """
        if not self.shared_utils.network_services_l3:
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if vrf_rps := getattr(vrf, "_pim_rp_addresses", None):
                    ipv4_config = EosCliConfigGen.RouterPimSparseMode.VrfsItem.Ipv4()
                    rps_item = EosCliConfigGen.RouterPimSparseMode.VrfsItem.Ipv4.RpAddressesItem()
                    for rps in vrf_rps:
                        if "groups" in rps:
                            for group in rps["groups"]:
                                rps_item.groups.append_unique(group)
                        if "access_lists" in rps:
                            for access_list in rps["access_lists"]:
                                rps_item.access_lists.append_unique(access_list)
                        if "address" in rps:
                            rps_item.address = rps["address"]
                        if "priority" in rps:
                            rps_item.priority = rps["priority"]
                        if "hashmask" in rps:
                            rps_item.hashmask = rps["hashmask"]
                        if "override" in rps:
                            rps_item.override = rps["override"]
                        if "_custom_data" in rps:
                            rps_item._custom_data = rps["_custom_data"]
                        ipv4_config.rp_addresses.append_unique(rps_item)
                    self.structured_config.router_pim_sparse_mode.vrfs.append_new(name=vrf.name, ipv4=ipv4_config)
