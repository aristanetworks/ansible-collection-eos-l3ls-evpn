# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._utils import append_if_not_duplicate
from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from .utils import UtilsMixin

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
                    for rps in vrf_rps:
                        rps_item = EosCliConfigGen.RouterPimSparseMode.VrfsItem.Ipv4.RpAddressesItem(**rps)
                        ipv4_config.rp_addresses.append_new(address=rps_item.address, groups=rps_item.groups, access_lists=rps_item.access_lists,priority=rps_item.priority,
                                                hashmask=rps_item.hashmask, override=rps_item.override)
                    self.structured_config.router_pim_sparse_mode.vrfs.append_new(name=vrf.name, ipv4=ipv4_config)
