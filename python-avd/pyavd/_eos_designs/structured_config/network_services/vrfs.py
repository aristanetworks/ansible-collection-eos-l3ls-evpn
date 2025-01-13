# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import append_if_not_duplicate

from .utils import UtilsMixin

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServices


class VrfsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def vrfs(self: AvdStructuredConfigNetworkServices) -> list | None:
        """
        Return structured config for vrfs.

        Used for creating VRFs except VRF "default".

        This function also detects duplicate vrfs and raise an error in case of duplicates between
        all Tenants deployed on this device.
        """
        if not self.shared_utils.network_services_l3:
            return None

        vrfs = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                vrf_name = vrf.name
                if vrf_name == "default":
                    continue

                new_vrf = {
                    "name": vrf_name,
                    "tenant": tenant.name,
                }

                # MLAG IBGP Peering VLANs per VRF
                if self.inputs.overlay_mlag_rfc5549 and self._mlag_ibgp_peering_enabled(vrf, tenant):
                    new_vrf["ip_routing_ipv6_interfaces"] = True
                    new_vrf["ipv6_routing"] = True
                else:
                    new_vrf["ip_routing"] = True

                if self._has_ipv6(vrf):
                    new_vrf["ipv6_routing"] = True

                if vrf.description:
                    new_vrf["description"] = vrf.description

                append_if_not_duplicate(
                    list_of_dicts=vrfs,
                    primary_key="name",
                    new_dict=new_vrf,
                    context="VRFs defined under network services",
                    context_keys=["name", "tenant"],
                    ignore_keys={"tenant"},
                )

        if vrfs:
            return vrfs

        return None

    def _has_ipv6(self: AvdStructuredConfigNetworkServices, vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem) -> bool:
        """
        Return bool if IPv6 is configured in the given VRF.

        Expects a VRF definition coming from filtered_tenants, where all keys have been set and filtered
        """
        return any(svi.ipv6_address or svi.ipv6_address_virtuals for svi in vrf.svis)
