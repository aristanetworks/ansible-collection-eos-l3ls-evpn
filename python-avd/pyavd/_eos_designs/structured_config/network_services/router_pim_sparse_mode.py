# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._utils import get

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
        Set structured config for router_pim.

        Used for to configure RPs on the VRF
        """
        if not self.shared_utils.network_services_l3:
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if vrf_rps := getattr(vrf._internal_data, "pim_rp_addresses", None):
                    ipv4_config = EosCliConfigGen.RouterPimSparseMode.VrfsItem.Ipv4()
                    for rps in vrf_rps:
                        rpaddress = EosCliConfigGen.RouterPimSparseMode.VrfsItem.Ipv4.RpAddressesItem()
                        rpaddress.address = rps["address"]
                        for group in get(rps, "groups", []):
                            rpaddress.groups.append(group)
                        for access_list in get(rps, "access_lists", []):
                            rpaddress.access_lists.append(access_list)
                        ipv4_config.rp_addresses.append_unique(rpaddress)
                    self.structured_config.router_pim_sparse_mode.vrfs.append_new(name=vrf.name, ipv4=ipv4_config)
