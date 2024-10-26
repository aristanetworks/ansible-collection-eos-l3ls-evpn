# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import AvdStringFormatter, append_if_not_duplicate
from pyavd.j2filters import natural_sort

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class VlansMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def vlans(self: AvdStructuredConfigNetworkServices) -> list | None:
        """
        Return structured config for vlans.

        Consist of svis, mlag peering vlans and l2vlans from filtered tenants.

        This function also detects duplicate vlans and raise an error in case of duplicates between
        SVIs in all VRFs and L2VLANs deployed on this device.
        """
        if not self.shared_utils.network_services_l2:
            return None

        vlans = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant["vrfs"]:
                for svi in vrf["svis"]:
                    vlan = self._get_vlan_config(svi)
                    append_if_not_duplicate(
                        list_of_dicts=vlans,
                        primary_key="id",
                        new_dict=vlan,
                        context=f"SVIs in VRF '{vrf['name']}'",
                        context_keys=["id", "name", "tenant"],
                        ignore_keys={"tenant"},
                    )

                # MLAG IBGP Peering VLANs per VRF
                # Continue to next VRF if mlag vlan_id is not set
                if (vlan_id := self._mlag_ibgp_peering_vlan_vrf(vrf, tenant)) is None:
                    continue

                vlan = {
                    "id": vlan_id,
                    "name": AvdStringFormatter().format(
                        self.shared_utils.mlag_peer_l3_vrf_vlan_name, mlag_peer=self.shared_utils.mlag_peer, vlan=vlan_id, vrf=vrf["name"]
                    ),
                    "trunk_groups": [self._trunk_groups_mlag_l3_name],
                    "tenant": tenant["name"],
                }
                append_if_not_duplicate(
                    list_of_dicts=vlans,
                    primary_key="id",
                    new_dict=vlan,
                    context=f"MLAG Peering VLAN in VRF '{vrf['name']}' (check for duplicate VRF VNI/ID)",
                    context_keys=["id", "name", "tenant"],
                    ignore_keys={"tenant"},
                )

            # L2 Vlans per Tenant
            for l2vlan in tenant["l2vlans"]:
                vlan = self._get_vlan_config(l2vlan)
                append_if_not_duplicate(
                    list_of_dicts=vlans,
                    primary_key="id",
                    new_dict=vlan,
                    context="L2VLANs",
                    context_keys=["id", "name", "tenant"],
                    ignore_keys={"tenant"},
                )

        if vlans:
            return vlans

        return None

    def _get_vlan_config(self: AvdStructuredConfigNetworkServices, vlan: dict) -> dict:
        """
        Return structured config for one given vlan.

        Can be used for svis and l2vlans
        """
        vlans_vlan = {
            "id": int(vlan["id"]),
            "name": vlan["name"],
            "tenant": vlan["tenant"],
        }
        if self.shared_utils.enable_trunk_groups:
            trunk_groups = vlan.get("trunk_groups", [])
            if self.shared_utils.only_local_vlan_trunk_groups:
                trunk_groups = list(self._local_endpoint_trunk_groups.intersection(trunk_groups))
            if self.shared_utils.mlag:
                trunk_groups.append(self._trunk_groups_mlag_name)
            if self.shared_utils.uplink_type == "port-channel":
                trunk_groups.append(self._trunk_groups_uplink_name)
            vlans_vlan["trunk_groups"] = natural_sort(trunk_groups)

        return vlans_vlan
