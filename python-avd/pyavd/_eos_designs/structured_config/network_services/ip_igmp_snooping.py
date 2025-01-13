# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import append_if_not_duplicate, default, strip_empties_from_dict

from .utils import UtilsMixin

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServices


class IpIgmpSnoopingMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def ip_igmp_snooping(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """Return structured config for ip_igmp_snooping."""
        if not self.shared_utils.network_services_l2:
            return None

        igmp_snooping_enabled = self.shared_utils.igmp_snooping_enabled
        ip_igmp_snooping = {"globally_enabled": igmp_snooping_enabled}
        if not igmp_snooping_enabled:
            return ip_igmp_snooping

        vlans = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for svi in vrf.svis:
                    if vlan := self._ip_igmp_snooping_vlan(svi, tenant):
                        append_if_not_duplicate(
                            list_of_dicts=vlans,
                            primary_key="id",
                            new_dict=vlan,
                            context=f"IGMP snooping for SVIs in VRF '{vrf.name}'",
                            context_keys=["id"],
                        )

            for l2vlan in tenant.l2vlans:
                if vlan := self._ip_igmp_snooping_vlan(l2vlan, tenant):
                    append_if_not_duplicate(
                        list_of_dicts=vlans,
                        primary_key="id",
                        new_dict=vlan,
                        context="IGMP snooping for L2VLANs",
                        context_keys=["id"],
                    )

        if vlans:
            ip_igmp_snooping["vlans"] = vlans

        return ip_igmp_snooping

    def _ip_igmp_snooping_vlan(
        self: AvdStructuredConfigNetworkServices,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> dict:
        """
        ip_igmp_snooping logic for one vlan.

        Can be used for both svis and l2vlans
        """
        igmp_snooping_enabled = None
        igmp_snooping_querier_enabled = None
        evpn_l2_multicast_enabled = bool(default(vlan.evpn_l2_multicast.enabled, tenant.evpn_l2_multicast.enabled)) and self.shared_utils.evpn_multicast
        if self.shared_utils.overlay_vtep and evpn_l2_multicast_enabled:
            # Leaving igmp_snooping_enabled unset, to avoid extra line of config as we already check
            # that global igmp snooping is enabled and igmp snooping is required for evpn_l2_multicast.

            # Forcing querier to True since evpn_l2_multicast requires
            # querier on all vteps
            igmp_snooping_querier_enabled = True

        else:
            igmp_snooping_enabled = vlan.igmp_snooping_enabled
            if self.shared_utils.network_services_l3 and self.shared_utils.uplink_type in ["p2p", "p2p-vrfs"]:
                igmp_snooping_querier_enabled = default(vlan.igmp_snooping_querier.enabled, tenant.igmp_snooping_querier.enabled)

        ip_igmp_snooping_vlan = strip_empties_from_dict(
            {
                "enabled": igmp_snooping_enabled,
                "querier": {
                    "enabled": igmp_snooping_querier_enabled,
                    "address": (
                        default(vlan.igmp_snooping_querier.source_address, tenant.igmp_snooping_querier.source_address, self.shared_utils.router_id)
                        if igmp_snooping_querier_enabled
                        else None
                    ),
                    "version": default(vlan.igmp_snooping_querier.version, tenant.igmp_snooping_querier.version) if igmp_snooping_querier_enabled else None,
                },
                # IGMP snooping fast-leave feature is enabled only when evpn_l2_multicast is enabled
                "fast_leave": default(vlan.igmp_snooping_querier.fast_leave, tenant.evpn_l2_multicast.fast_leave) if evpn_l2_multicast_enabled else None,
            }
        )

        if ip_igmp_snooping_vlan:
            return {"id": vlan.id, **ip_igmp_snooping_vlan}

        return ip_igmp_snooping_vlan
