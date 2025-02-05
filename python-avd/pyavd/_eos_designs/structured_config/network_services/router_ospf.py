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
                if not vrf.ospf.enabled:
                    continue

                if vrf.ospf.nodes and self.shared_utils.hostname not in vrf.ospf.nodes:
                    continue

                ospf_interfaces = EosCliConfigGen.RouterOspf.ProcessIdsItem.NoPassiveInterfaces()
                for l3_interface in vrf.l3_interfaces:
                    if l3_interface.ospf.enabled:
                        for node_index, node in enumerate(l3_interface.nodes):
                            if node != self.shared_utils.hostname:
                                continue
                            ospf_interfaces.append(l3_interface.interfaces[node_index])

                for svi in vrf.svis:
                    if svi.ospf.enabled:
                        interface_name = f"Vlan{svi.id}"
                        ospf_interfaces.append(interface_name)

                process_id = default(vrf.ospf.process_id, vrf.vrf_id)
                if not process_id:
                    msg = f"Missing or invalid 'ospf.process_id' or 'vrf_id' under vrf '{vrf.name}"
                    raise AristaAvdInvalidInputsError(msg)
                process = EosCliConfigGen.RouterOspf.ProcessIdsItem(id=process_id)
                if vrf.name != "default":
                    process.vrf = vrf.name
                process.passive_interface_default = True
                if vrf_router_id := self.get_vrf_router_id(vrf, vrf.ospf.router_id, tenant.name):
                    process.router_id = vrf_router_id
                process.no_passive_interfaces = ospf_interfaces
                if vrf.ospf.bfd:
                    process.bfd_enable = vrf.ospf.bfd
                process.max_lsa = vrf.ospf.max_lsa

                if vrf.ospf.redistribute_bgp.enabled:
                    process.redistribute.bgp.enabled = True
                    if route_map := vrf.ospf.redistribute_bgp.route_map:
                        process.redistribute.bgp.route_map = route_map

                if vrf.ospf.redistribute_connected.enabled:
                    process.redistribute.connected.enabled = True
                    if route_map := vrf.ospf.redistribute_connected.route_map:
                        process.redistribute.connected.route_map = route_map

                self.structured_config.router_ospf.process_ids.append(process)
        # If we have static_routes in default VRF and not EPVN, and underlay is OSPF
        # Then add redistribute static to the underlay OSPF process.
        if self._vrf_default_ipv4_static_routes["redistribute_in_underlay"] and self.shared_utils.underlay_routing_protocol in ["ospf", "ospf-ldp"]:
            process = EosCliConfigGen.RouterOspf.ProcessIdsItem(id=self.inputs.underlay_ospf_process_id)
            process.redistribute.static.enabled = True
            self.structured_config.router_ospf.process_ids.append(process)
