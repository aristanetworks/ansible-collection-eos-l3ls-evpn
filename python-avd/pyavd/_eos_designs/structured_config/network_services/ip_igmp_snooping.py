# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import append_if_not_duplicate, default, get

from .utils import UtilsMixin

if TYPE_CHECKING:
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

        ip_igmp_snooping = {}
        igmp_snooping_enabled = self.shared_utils.igmp_snooping_enabled
        ip_igmp_snooping["globally_enabled"] = igmp_snooping_enabled
        if igmp_snooping_enabled is not True:
            return ip_igmp_snooping

        vlans = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant["vrfs"]:
                for svi in vrf["svis"]:
                    if vlan := self._ip_igmp_snooping_vlan(svi, tenant):
                        append_if_not_duplicate(
                            list_of_dicts=vlans,
                            primary_key="id",
                            new_dict=vlan,
                            context=f"IGMP snooping for SVIs in VRF '{vrf['name']}'",
                            context_keys=["id"],
                        )

            for l2vlan in tenant["l2vlans"]:
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

    def _ip_igmp_snooping_vlan(self: AvdStructuredConfigNetworkServices, vlan: dict, tenant: dict) -> dict:
        """
        ip_igmp_snooping logic for one vlan.

        Can be used for both svis and l2vlans
        """
        tenant_igmp_snooping_querier = tenant.get("igmp_snooping_querier", {})
        igmp_snooping_querier = vlan.get("igmp_snooping_querier", {})
        igmp_snooping_enabled = None
        igmp_snooping_querier_enabled = None
        evpn_l2_multicast_enabled = (
            default(
                get(vlan, "evpn_l2_multicast.enabled"),
                get(tenant, "evpn_l2_multicast.enabled"),
            )
            and self.shared_utils.evpn_multicast is True
        )
        if self.shared_utils.overlay_vtep and evpn_l2_multicast_enabled is True:
            # Leaving igmp_snooping_enabled unset, to avoid extra line of config as we already check
            # that global igmp snooping is enabled and igmp snooping is required for evpn_l2_multicast.

            # Forcing querier to True since evpn_l2_multicast requires
            # querier on all vteps
            igmp_snooping_querier_enabled = True

        else:
            igmp_snooping_enabled = vlan.get("igmp_snooping_enabled")
            if self.shared_utils.network_services_l3 and self.shared_utils.uplink_type in ["p2p", "p2p-vrfs"]:
                igmp_snooping_querier_enabled = default(
                    igmp_snooping_querier.get("enabled"),
                    tenant_igmp_snooping_querier.get("enabled"),
                )

        ip_igmp_snooping_vlan = {}
        if igmp_snooping_enabled is not None:
            ip_igmp_snooping_vlan["enabled"] = igmp_snooping_enabled

        if igmp_snooping_querier_enabled is not None:
            ip_igmp_snooping_vlan["querier"] = {"enabled": igmp_snooping_querier_enabled}
            if igmp_snooping_querier_enabled is True:
                address = default(igmp_snooping_querier.get("source_address"), tenant_igmp_snooping_querier.get("source_address"), self.shared_utils.router_id)
                if address is not None:
                    ip_igmp_snooping_vlan["querier"]["address"] = address

                version = default(
                    igmp_snooping_querier.get("version"),
                    tenant_igmp_snooping_querier.get("version"),
                )
                if version is not None:
                    ip_igmp_snooping_vlan["querier"]["version"] = version

        # IGMP snooping fast-leave feature is enabled only when evpn_l2_multicast is enabled
        if evpn_l2_multicast_enabled is True:
            fast_leave = default(
                igmp_snooping_querier.get("fast_leave"),
                get(tenant, "evpn_l2_multicast.fast_leave"),
            )
            if fast_leave is not None:
                ip_igmp_snooping_vlan["fast_leave"] = fast_leave

        if ip_igmp_snooping_vlan:
            return {"id": int(vlan["id"]), **ip_igmp_snooping_vlan}

        return ip_igmp_snooping_vlan
