# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._utils import AvdStringFormatter
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class VlansMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def vlans(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Return structured config for vlans.

        Consist of svis, mlag peering vlans and l2vlans from filtered tenants.

        This function also detects duplicate vlans and raise an error in case of duplicates between
        SVIs in all VRFs and L2VLANs deployed on this device.
        """
        if not self.shared_utils.network_services_l2:
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for svi in vrf.svis:
                    self.structured_config.vlans.append(self._get_vlan_config(svi, tenant), ignore_fields=("tenant",))

                # MLAG IBGP Peering VLANs per VRF
                # Continue to next VRF if mlag vlan_id is not set
                if (vlan_id := self._mlag_ibgp_peering_vlan_vrf(vrf, tenant)) is None:
                    continue

                vlan = EosCliConfigGen.VlansItem(
                    id=vlan_id,
                    name=AvdStringFormatter().format(self.inputs.mlag_peer_l3_vrf_vlan_name, mlag_peer=self.shared_utils.mlag_peer, vlan=vlan_id, vrf=vrf.name),
                    trunk_groups=EosCliConfigGen.VlansItem.TrunkGroups([self.inputs.trunk_groups.mlag_l3.name]),
                    tenant=tenant.name,
                )
                self.structured_config.vlans.append(vlan, ignore_fields=("tenant",))

            # L2 Vlans per Tenant
            for l2vlan in tenant.l2vlans:
                self.structured_config.vlans.append(self._get_vlan_config(l2vlan, tenant), ignore_fields=("tenant",))

    def _get_vlan_config(
        self: AvdStructuredConfigNetworkServicesProtocol,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> EosCliConfigGen.VlansItem:
        """
        Return structured config for one given vlan.

        Can be used for svis and l2vlans
        """
        vlans_vlan = EosCliConfigGen.VlansItem(
            id=vlan.id,
            name=vlan.name,
            tenant=tenant.name,
        )
        if self.inputs.enable_trunk_groups:
            trunk_groups = vlan.trunk_groups
            if self.shared_utils.only_local_vlan_trunk_groups:
                trunk_groups = list(self._local_endpoint_trunk_groups.intersection(trunk_groups))
            if self.shared_utils.mlag:
                trunk_groups.append(self.inputs.trunk_groups.mlag.name)
            if self.shared_utils.uplink_type == "port-channel":
                trunk_groups.append(self.inputs.trunk_groups.uplink.name)
            vlans_vlan.trunk_groups.extend(natural_sort(trunk_groups))

        return vlans_vlan
