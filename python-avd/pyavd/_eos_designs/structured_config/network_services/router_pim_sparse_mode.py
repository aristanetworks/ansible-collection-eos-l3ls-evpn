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
                    rpaddresses = EosCliConfigGen.RouterPimSparseMode.VrfsItem.Ipv4.RpAddresses()

                    for rps in vrf_rps:
                        rpaddress = EosCliConfigGen.RouterPimSparseMode.VrfsItem.Ipv4.RpAddressesItem()
                        if "address" in rps:
                            rpaddress.address = rps["address"]
                        if "groups" in rps:
                            for group in rps["groups"]:
                                rpaddress.groups.append(group)
                        if "access_lists" in rps:
                            for access_list in rps["access_lists"]:
                                rpaddress.access_lists.append(access_list)
                        rpaddresses.append_unique(rpaddress)
                    ipv4_config.rp_addresses = rpaddresses
                    self.structured_config.router_pim_sparse_mode.vrfs.append_new(name=vrf.name, ipv4=ipv4_config)
