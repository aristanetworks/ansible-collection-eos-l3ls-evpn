# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import default

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class RouterOspfMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_ospf(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set structured config for router_ospf.

        If we have static_routes in default VRF and not EPVN, and underlay is OSPF
        Then add redistribute static to the underlay OSPF process.
        """
        if not self.shared_utils.network_services_l3:
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if not vrf.ospf.enabled or (vrf.ospf.nodes and self.shared_utils.hostname not in vrf.ospf.nodes):
                    continue

                process_id = default(vrf.ospf.process_id, vrf.vrf_id)
                if not process_id:
                    msg = f"Missing or invalid 'ospf.process_id' or 'vrf_id' under vrf '{vrf.name}"
                    raise AristaAvdInvalidInputsError(msg)
                process = EosCliConfigGen.RouterOspf.ProcessIdsItem(
                    id=process_id, passive_interface_default=True, max_lsa=vrf.ospf.max_lsa, router_id=self.get_vrf_router_id(vrf, tenant, vrf.ospf.router_id)
                )
                self._update_ospf_interface(process, vrf)

                if vrf.name != "default":
                    process.vrf = vrf.name
                if vrf.ospf.bfd:
                    process.bfd_enable = vrf.ospf.bfd
                self._update_ospf_redistribute(process, vrf)

                self.structured_config.router_ospf.process_ids.append(process)
        # If we have static_routes in default VRF and not EPVN, and underlay is OSPF
        # Then add redistribute static to the underlay OSPF process.
        if self._vrf_default_ipv4_static_routes["redistribute_in_underlay"] and self.shared_utils.underlay_routing_protocol in ["ospf", "ospf-ldp"]:
            self.structured_config.router_ospf.process_ids.obtain(self.inputs.underlay_ospf_process_id).redistribute.static.enabled = True

    def _update_ospf_redistribute(
        self: AvdStructuredConfigNetworkServicesProtocol,
        process: EosCliConfigGen.RouterOspf.ProcessIdsItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> None:
        """
        Configures OSPF route redistribution settings for the given VRF.

        This method enables redistribution of BGP and connected routes into OSPF,
        setting the associated route maps if specified.

        Args:
            process: The OSPF process configuration object.
            vrf: The VRF object containing OSPF redistribution settings.
        """
        if vrf.ospf.redistribute_bgp.enabled:
            process.redistribute.bgp.enabled = True
            if route_map := vrf.ospf.redistribute_bgp.route_map:
                process.redistribute.bgp.route_map = route_map

        if vrf.ospf.redistribute_connected.enabled:
            process.redistribute.connected.enabled = True
            if route_map := vrf.ospf.redistribute_connected.route_map:
                process.redistribute.connected.route_map = route_map

    def _update_ospf_interface(
        self: AvdStructuredConfigNetworkServicesProtocol,
        process: EosCliConfigGen.RouterOspf.ProcessIdsItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> None:
        """
        Populates the list of OSPF-enabled interfaces for the given VRF.

        This method iterates through L3 interfaces and SVIs, adding those that have OSPF enabled.

        Args:
            process: The OSPF process configuration object.
            vrf: The VRF object containing interface OSPF settings.
        """
        for l3_interface in vrf.l3_interfaces:
            if l3_interface.ospf.enabled:
                for node_index, node in enumerate(l3_interface.nodes):
                    if node != self.shared_utils.hostname:
                        continue
                    process.no_passive_interfaces.append(l3_interface.interfaces[node_index])

        for svi in vrf.svis:
            if svi.ospf.enabled:
                interface_name = f"Vlan{svi.id}"
                process.no_passive_interfaces.append(interface_name)
