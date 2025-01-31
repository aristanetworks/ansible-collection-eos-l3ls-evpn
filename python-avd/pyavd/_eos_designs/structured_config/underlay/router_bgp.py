# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._utils import get

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class RouterBgpMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_bgp(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Return the structured config for router_bgp."""
        if not self.shared_utils.underlay_bgp:
            return

        peer_group = EosCliConfigGen.RouterBgp.PeerGroupsItem(
            name=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
            type="ipv4",
            password=self.inputs.bgp_peer_groups.ipv4_underlay_peers.password,
            bfd=self.inputs.bgp_peer_groups.ipv4_underlay_peers.bfd or None,
            maximum_routes=12000,
            send_community="all",
        )

        if self.inputs.bgp_peer_groups.ipv4_underlay_peers.structured_config:
            self.custom_structured_configs.nested.router_bgp.peer_groups.obtain(self.inputs.bgp_peer_groups.ipv4_underlay_peers.name)._deepmerge(
                self.inputs.bgp_peer_groups.ipv4_underlay_peers.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )

        if self.shared_utils.overlay_routing_protocol == "ibgp" and self.shared_utils.is_cv_pathfinder_router:
            peer_group.route_map_in = "RM-BGP-UNDERLAY-PEERS-IN"
            if self.shared_utils.wan_ha:
                peer_group.route_map_out = "RM-BGP-UNDERLAY-PEERS-OUT"
                if self.shared_utils.use_uplinks_for_wan_ha:
                    # For HA need to add allowas_in 1
                    peer_group.allowas_in._update(enabled=True, times=1)

        self.structured_config.router_bgp.peer_groups.append(peer_group)

        # Address Families
        # TODO: - see if it makes sense to extract logic in method
        address_family_ipv4_peer_group = EosCliConfigGen.RouterBgp.AddressFamilyIpv4.PeerGroupsItem(
            name=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name, activate=True
        )

        if self.inputs.underlay_rfc5549 is True:
            address_family_ipv4_peer_group.next_hop.address_family_ipv6._update(enabled=True, originate=True)

        self.structured_config.router_bgp.address_family_ipv4.peer_groups.append(address_family_ipv4_peer_group)

        if self.shared_utils.underlay_ipv6 is True:
            self.structured_config.router_bgp.address_family_ipv6.peer_groups.append_new(
                name=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name, activate=True
            )

        # Neighbor Interfaces and VRF Neighbor Interfaces
        if self.inputs.underlay_rfc5549 is True:
            for link in self._underlay_links:
                if link["type"] != "underlay_p2p":
                    continue

                self.structured_config.router_bgp.neighbor_interfaces.append_new(
                    name=link["interface"],
                    peer_group=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
                    remote_as=link["peer_bgp_as"],
                    peer=link["peer"],
                    description="_".join([link["peer"], link["peer_interface"]]),
                )

                if "subinterfaces" in link:
                    for subinterface in link["subinterfaces"]:
                        # We need to add basic BGP VRF config in case the device is not covered by network_services. (Like a spine)
                        if subinterface["vrf"] not in self.structured_config.router_bgp.vrfs:
                            self.structured_config.router_bgp.vrfs.append_new(name=subinterface["vrf"], router_id=self.shared_utils.router_id)

                        self.structured_config.router_bgp.vrfs[subinterface["vrf"]].neighbor_interfaces.append_new(
                            name=subinterface["interface"],
                            peer_group=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
                            remote_as=link["peer_bgp_as"],
                            # TODO: - implement some centralized way to generate these descriptions
                            description=f"{'_'.join([link['peer'], subinterface['peer_interface']])}_vrf_{subinterface['vrf']}",
                        )

        # Neighbors and VRF Neighbors
        else:
            for link in self._underlay_links:
                if link["type"] != "underlay_p2p":
                    continue

                neighbor = EosCliConfigGen.RouterBgp.NeighborsItem(
                    ip_address=link["peer_ip_address"],
                    peer_group=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
                    remote_as=get(link, "peer_bgp_as"),
                    peer=link["peer"],
                    description="_".join([link["peer"], link["peer_interface"]]),
                    bfd=get(link, "bfd"),
                )

                if self.inputs.shutdown_bgp_towards_undeployed_peers and link["peer_is_deployed"] is False:
                    neighbor.shutdown = True

                if self.inputs.underlay_filter_peer_as:
                    neighbor.route_map_out = f"RM-BGP-AS{link['peer_bgp_as']}-OUT"

                self.structured_config.router_bgp.neighbors.append(neighbor)

                if "subinterfaces" in link:
                    for subinterface in link["subinterfaces"]:
                        subinterface_vrf = subinterface["vrf"]
                        # We need to add basic BGP VRF config in case the device is not covered by network_services. (Like a spine)
                        if subinterface_vrf not in self.structured_config.router_bgp.vrfs:
                            self.structured_config.router_bgp.vrfs.append_new(name=subinterface_vrf, router_id=self.shared_utils.router_id)

                        self.structured_config.router_bgp.vrfs[subinterface_vrf].neighbors.append_new(
                            ip_address=subinterface["peer_ip_address"],
                            peer_group=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
                            remote_as=get(link, "peer_bgp_as"),
                            description=f"{'_'.join([link['peer'], subinterface['peer_interface']])}_vrf_{subinterface_vrf}",
                            bfd=get(link, "bfd"),
                        )
