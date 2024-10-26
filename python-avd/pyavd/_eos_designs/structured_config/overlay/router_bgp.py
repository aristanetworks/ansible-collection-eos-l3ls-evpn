# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError
from pyavd._utils import AvdStringFormatter, default, get, strip_empties_from_dict
from pyavd.j2filters import natural_sort

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlay


class RouterBgpMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_bgp(self: AvdStructuredConfigOverlay) -> dict | None:
        """Return the structured config for router_bgp."""
        if self.shared_utils.overlay_cvx:
            return None

        router_bgp = {
            "bgp_cluster_id": self._bgp_cluster_id(),
            "listen_ranges": self._bgp_listen_ranges(),
            "peer_groups": self._peer_groups(),
            "address_family_evpn": self._address_family_evpn(),
            "address_family_ipv4": self._address_family_ipv4(),
            "address_family_ipv4_sr_te": self._address_family_ipv4_sr_te(),
            "address_family_link_state": self._address_family_link_state(),
            "address_family_path_selection": self._address_family_path_selection(),
            "address_family_rtc": self._address_family_rtc(),
            "bgp": self._bgp_overlay_dpath(),
            "address_family_vpn_ipv4": self._address_family_vpn_ipvx(4),
            "address_family_vpn_ipv6": self._address_family_vpn_ipvx(6),
            "neighbors": self._neighbors(),
        }

        # Need to keep potentially empty dict for redistribute_routes
        return strip_empties_from_dict(router_bgp, strip_values_tuple=(None, ""))

    def _bgp_cluster_id(self: AvdStructuredConfigOverlay) -> str | None:
        if self.shared_utils.overlay_routing_protocol == "ibgp" and (
            self.shared_utils.evpn_role == "server" or self.shared_utils.mpls_overlay_role == "server"
        ):
            return get(self.shared_utils.switch_data_combined, "bgp_cluster_id", default=self.shared_utils.router_id)
        return None

    def _bgp_listen_ranges(self: AvdStructuredConfigOverlay) -> list | None:
        """Generate listen-ranges. Currently only supported for WAN RR."""
        if not self.shared_utils.is_wan_server:
            return None

        return [
            {
                "prefix": prefix,
                "peer_group": self._get_peer_group_name("wan_overlay_peers"),
                "remote_as": self.shared_utils.bgp_as,
            }
            for prefix in self.shared_utils.wan_listen_ranges
        ] or None

    def _generate_base_peer_group(
        self: AvdStructuredConfigOverlay,
        pg_type: str,
        pg_name: str,
        maximum_routes: int = 0,
        update_source: str = "Loopback0",
    ) -> dict:
        return {
            "name": self.shared_utils.bgp_peer_groups[pg_name]["name"],
            "type": pg_type,
            "update_source": update_source,
            "bfd": self.shared_utils.bgp_peer_groups[pg_name]["bfd"],
            "password": self.shared_utils.bgp_peer_groups[pg_name]["password"],
            "send_community": "all",
            "maximum_routes": maximum_routes,
            "struct_cfg": self.shared_utils.bgp_peer_groups[pg_name]["structured_config"],
        }

    def _peer_groups(self: AvdStructuredConfigOverlay) -> list | None:
        peer_groups = []

        if self.shared_utils.overlay_routing_protocol == "ebgp":
            # EVPN OVERLAY peer group
            ebgp_peer_group = {
                **self._generate_base_peer_group("evpn", "evpn_overlay_peers"),
                "ebgp_multihop": self.shared_utils.evpn_ebgp_multihop,
            }

            if self.shared_utils.evpn_role == "server":
                ebgp_peer_group["next_hop_unchanged"] = True

            peer_groups.append(ebgp_peer_group)

            if self.shared_utils.evpn_gateway_vxlan_l2 is True or self.shared_utils.evpn_gateway_vxlan_l3 is True:
                peer_groups.append(
                    {
                        **self._generate_base_peer_group("evpn", "evpn_overlay_core"),
                        "ebgp_multihop": self.shared_utils.evpn_ebgp_gateway_multihop,
                    },
                )

        elif self.shared_utils.overlay_routing_protocol == "ibgp":
            if self.shared_utils.overlay_mpls is True:
                # MPLS OVERLAY peer group
                mpls_peer_group = {
                    **self._generate_base_peer_group("mpls", "mpls_overlay_peers"),
                    "remote_as": self.shared_utils.bgp_as,
                }

                if self.shared_utils.mpls_overlay_role == "server" or (self.shared_utils.evpn_role == "server" and self.shared_utils.overlay_evpn_mpls is True):
                    mpls_peer_group["route_reflector_client"] = True

                peer_groups.append(mpls_peer_group)

            if self.shared_utils.overlay_evpn_vxlan is True:
                peer_group_config = {"remote_as": self.shared_utils.bgp_as}
                if self.shared_utils.is_wan_router:
                    # WAN OVERLAY peer group
                    peer_group_config["ttl_maximum_hops"] = self.shared_utils.bgp_peer_groups["wan_overlay_peers"]["ttl_maximum_hops"]
                    if self.shared_utils.is_wan_server:
                        peer_group_config["route_reflector_client"] = True
                    peer_group_config["bfd_timers"] = get(self.shared_utils.bgp_peer_groups["wan_overlay_peers"], "bfd_timers")
                    peer_groups.append(
                        {
                            **self._generate_base_peer_group("wan", "wan_overlay_peers", update_source=self.shared_utils.vtep_loopback),
                            **peer_group_config,
                        },
                    )
                else:
                    # EVPN OVERLAY peer group - also in EBGP..
                    if self.shared_utils.evpn_role == "server":
                        peer_group_config["route_reflector_client"] = True
                    peer_groups.append(
                        {
                            **self._generate_base_peer_group("evpn", "evpn_overlay_peers"),
                            **peer_group_config,
                        },
                    )

            # RR Overlay peer group rendered either for MPLS route servers
            if self._is_mpls_server is True:
                peer_groups.append({**self._generate_base_peer_group("mpls", "rr_overlay_peers"), "remote_as": self.shared_utils.bgp_as})

            if self._is_wan_server_with_peers:
                wan_rr_overlay_peer_group = self._generate_base_peer_group("wan", "wan_rr_overlay_peers", update_source=self.shared_utils.vtep_loopback)
                wan_rr_overlay_peer_group.update(
                    {
                        "remote_as": self.shared_utils.bgp_as,
                        "ttl_maximum_hops": self.shared_utils.bgp_peer_groups["wan_rr_overlay_peers"]["ttl_maximum_hops"],
                        "bfd_timers": get(self.shared_utils.bgp_peer_groups["wan_rr_overlay_peers"], "bfd_timers"),
                        "route_reflector_client": True,
                    },
                )
                peer_groups.append(wan_rr_overlay_peer_group)

        # same for ebgp and ibgp
        if self.shared_utils.overlay_ipvpn_gateway is True:
            peer_groups.append(
                {
                    **self._generate_base_peer_group("mpls", "ipvpn_gateway_peers"),
                    "local_as": self._ipvpn_gateway_local_as,
                    "maximum_routes": get(self.shared_utils.switch_data_combined, "ipvpn_gateway.maximum_routes", default=0),
                },
            )

        return peer_groups

    def _address_family_ipv4(self: AvdStructuredConfigOverlay) -> dict:
        """Deactivate the relevant peer_groups in address_family_ipv4."""
        peer_groups = []

        if self.shared_utils.is_wan_router:
            peer_groups.append({"name": self._get_peer_group_name("wan_overlay_peers"), "activate": False})

        # TODO: no elif
        elif self.shared_utils.overlay_evpn_vxlan is True:
            peer_groups.append({"name": self._get_peer_group_name("evpn_overlay_peers"), "activate": False})

        if self.shared_utils.overlay_routing_protocol == "ebgp" and (
            self.shared_utils.evpn_gateway_vxlan_l2 is True or self.shared_utils.evpn_gateway_vxlan_l3 is True
        ):
            peer_groups.append({"name": self._get_peer_group_name("evpn_overlay_core"), "activate": False})

        if self.shared_utils.overlay_routing_protocol == "ibgp":
            if self.shared_utils.overlay_mpls is True:
                peer_groups.append({"name": self._get_peer_group_name("mpls_overlay_peers"), "activate": False})

            if self._is_mpls_server is True:
                peer_groups.append({"name": self._get_peer_group_name("rr_overlay_peers"), "activate": False})

            if self._is_wan_server_with_peers:
                peer_groups.append({"name": self._get_peer_group_name("wan_rr_overlay_peers"), "activate": False})

        if self.shared_utils.overlay_ipvpn_gateway is True:
            peer_groups.append({"name": self._get_peer_group_name("ipvpn_gateway_peers"), "activate": False})

        return {"peer_groups": peer_groups}

    def _get_peer_group_name(self: AvdStructuredConfigOverlay, key: str) -> str:
        """Helper to retrieve the configured peer_group name for the given key."""
        return self.shared_utils.bgp_peer_groups[key]["name"]

    def _address_family_evpn(self: AvdStructuredConfigOverlay) -> dict | None:
        address_family_evpn = {}

        peer_groups = []

        overlay_peer_group = {}
        if self.shared_utils.overlay_evpn_vxlan is True:
            if self.shared_utils.is_wan_router:
                overlay_peer_group = {
                    "name": self._get_peer_group_name("wan_overlay_peers"),
                    "activate": True,
                    "encapsulation": self.shared_utils.wan_encapsulation,
                }
            else:
                overlay_peer_group = {"name": self._get_peer_group_name("evpn_overlay_peers"), "activate": True}

        if self.shared_utils.overlay_routing_protocol == "ebgp":
            if self.shared_utils.evpn_gateway_vxlan_l2 is True or self.shared_utils.evpn_gateway_vxlan_l3 is True:
                peer_groups.append(
                    {
                        "name": self._get_peer_group_name("evpn_overlay_core"),
                        "domain_remote": True,
                        "activate": True,
                    },
                )

            if self.shared_utils.evpn_gateway_vxlan_l3 is True:
                address_family_evpn["neighbor_default"] = {
                    "next_hop_self_received_evpn_routes": {
                        "enable": True,
                        "inter_domain": self.shared_utils.evpn_gateway_vxlan_l3_inter_domain,
                    },
                }

        if self.shared_utils.overlay_routing_protocol == "ibgp":
            # TODO: - assess this condition - both can't be true at the same time.
            if self.shared_utils.overlay_evpn_mpls is True and self.shared_utils.overlay_evpn_vxlan is not True:
                overlay_peer_group = {"name": self._get_peer_group_name("mpls_overlay_peers"), "activate": True}
                address_family_evpn["neighbor_default"] = {"encapsulation": "mpls"}
                if self.shared_utils.overlay_ler is True:
                    address_family_evpn["neighbor_default"]["next_hop_self_source_interface"] = "Loopback0"

                if self._is_mpls_server is True:
                    peer_groups.append({"name": self._get_peer_group_name("rr_overlay_peers"), "activate": True})

            if self.shared_utils.overlay_vtep is True and self.shared_utils.evpn_role != "server" and overlay_peer_group:
                overlay_peer_group.update(
                    {
                        "route_map_in": "RM-EVPN-SOO-IN",
                        "route_map_out": "RM-EVPN-SOO-OUT",
                    },
                )

            if self._is_wan_server_with_peers:
                peer_groups.append(
                    {
                        "name": self._get_peer_group_name("wan_rr_overlay_peers"),
                        "activate": True,
                        "encapsulation": self.shared_utils.wan_encapsulation,
                    }
                )

        if overlay_peer_group:
            peer_groups.append(overlay_peer_group)

        if peer_groups:
            address_family_evpn["peer_groups"] = peer_groups

        # host flap detection & route pruning
        if self.shared_utils.overlay_vtep is True:
            if (evpn_host_flap := get(self._hostvars, "evpn_hostflap_detection")) is not None:
                address_family_evpn["evpn_hostflap_detection"] = {
                    "window": evpn_host_flap.get("window", 180),
                    "threshold": evpn_host_flap.get("threshold", 5),
                    "enabled": evpn_host_flap.get("enabled", True),
                    "expiry_timeout": evpn_host_flap.get("expiry_timeout"),
                }
            if get(self._hostvars, "evpn_import_pruning") is True:
                address_family_evpn["route"] = {
                    "import_match_failure_action": "discard",
                }

        if self.shared_utils.overlay_dpath is True:
            address_family_evpn["domain_identifier"] = get(self.shared_utils.switch_data_combined, "ipvpn_gateway.evpn_domain_id", default="65535:1")

        if self.shared_utils.is_wan_server:
            address_family_evpn["next_hop"] = {"resolution_disabled": True}

        # Activitating HA iBGP session for WAN HA
        if self.shared_utils.wan_ha:
            address_family_evpn["neighbor_default"] = {
                "next_hop_self_received_evpn_routes": {
                    "enable": True,
                },
            }
            address_family_evpn["neighbors"] = [
                {
                    "ip_address": self._wan_ha_peer_vtep_ip(),
                    "activate": True,
                    "encapsulation": self.shared_utils.wan_encapsulation,
                }
            ]

        return address_family_evpn or None

    def _address_family_ipv4_sr_te(self: AvdStructuredConfigOverlay) -> dict | None:
        """Generate structured config for IPv4 SR-TE address family."""
        if not self.shared_utils.is_cv_pathfinder_router:
            return None

        address_family_ipv4_sr_te = {
            "peer_groups": [
                {
                    "name": self._get_peer_group_name("wan_overlay_peers"),
                    "activate": True,
                },
            ],
        }

        if self._is_wan_server_with_peers:
            address_family_ipv4_sr_te["peer_groups"].append({"name": self._get_peer_group_name("wan_rr_overlay_peers"), "activate": True})

        return address_family_ipv4_sr_te

    def _address_family_link_state(self: AvdStructuredConfigOverlay) -> dict | None:
        """Generate structured config for link-state address family."""
        if not self.shared_utils.is_cv_pathfinder_router:
            return None

        address_family_link_state = {
            "peer_groups": [
                {
                    "name": self._get_peer_group_name("wan_overlay_peers"),
                    "activate": True,
                },
            ],
        }

        if self.shared_utils.is_cv_pathfinder_server:
            address_family_link_state["path_selection"] = {"roles": {"consumer": True, "propagator": True}}
            address_family_link_state["peer_groups"][0].update(
                {
                    "missing_policy": {
                        "direction_out_action": "deny",
                    },
                },
            )
        else:  # other roles are transit / edge
            address_family_link_state["path_selection"] = {"roles": {"producer": True}}

        if self._is_wan_server_with_peers:
            address_family_link_state["peer_groups"].append({"name": self._get_peer_group_name("wan_rr_overlay_peers"), "activate": True})

        return address_family_link_state

    def _address_family_path_selection(self: AvdStructuredConfigOverlay) -> dict | None:
        if not self.shared_utils.is_wan_router:
            return None

        address_family_path_selection = {
            "peer_groups": [
                {
                    "name": self._get_peer_group_name("wan_overlay_peers"),
                    "activate": True,
                },
            ],
            "bgp": {"additional_paths": {"receive": True, "send": "any"}},
        }

        if self._is_wan_server_with_peers:
            address_family_path_selection["peer_groups"].append({"name": self._get_peer_group_name("wan_rr_overlay_peers"), "activate": True})

        return address_family_path_selection

    def _address_family_rtc(self: AvdStructuredConfigOverlay) -> dict | None:
        """
        Activate EVPN OVERLAY peer group and EVPN OVERLAY CORE peer group (if present) in address_family_rtc.

        if the evpn_role is server, enable default_route_target only
        """
        if self.shared_utils.evpn_overlay_bgp_rtc is not True:
            return None

        address_family_rtc = {}

        peer_groups = []
        evpn_overlay_peers = {"name": self._get_peer_group_name("evpn_overlay_peers")}
        if self.shared_utils.overlay_evpn_vxlan is True:
            evpn_overlay_peers["activate"] = True

        if self.shared_utils.overlay_routing_protocol == "ebgp":
            if self.shared_utils.evpn_gateway_vxlan_l2 is True or self.shared_utils.evpn_gateway_vxlan_l3 is True:
                core_peer_group = {"name": self._get_peer_group_name("evpn_overlay_core"), "activate": True}
                # TODO: (@Claus) told me to remove this
                if self.shared_utils.evpn_role == "server":
                    core_peer_group["default_route_target"] = {"only": True}
                peer_groups.append(core_peer_group)

            # Transposing the Jinja2 logic: if the evpn_overlay_core peer group is not
            # configured then the default_route_target is applied in the evpn_overlay_peers peer group.
            elif self.shared_utils.evpn_role == "server":
                evpn_overlay_peers["default_route_target"] = {"only": True}

        if self.shared_utils.overlay_routing_protocol == "ibgp":
            if self.shared_utils.overlay_mpls is True:
                mpls_peer_group = {"name": self._get_peer_group_name("mpls_overlay_peers"), "activate": True}
                if self.shared_utils.evpn_role == "server" or self.shared_utils.mpls_overlay_role == "server":
                    mpls_peer_group["default_route_target"] = {"only": True}
                peer_groups.append(mpls_peer_group)

            if self.shared_utils.overlay_evpn_vxlan is True and (self.shared_utils.evpn_role == "server" or self.shared_utils.mpls_overlay_role == "server"):
                evpn_overlay_peers["default_route_target"] = {"only": True}

        peer_groups.append(evpn_overlay_peers)
        address_family_rtc["peer_groups"] = peer_groups

        return address_family_rtc

    def _address_family_vpn_ipvx(self: AvdStructuredConfigOverlay, version: int) -> dict | None:
        if version not in [4, 6]:
            msg = "_address_family_vpn_ipvx should be called with version 4 or 6 only"
            raise AristaAvdError(msg)

        if (version == 4 and self.shared_utils.overlay_vpn_ipv4 is not True) or (version == 6 and self.shared_utils.overlay_vpn_ipv6 is not True):
            return None

        address_family_vpn_ipvx = {}

        if self.shared_utils.overlay_ler is True or self.shared_utils.overlay_ipvpn_gateway is True:
            address_family_vpn_ipvx["neighbor_default_encapsulation_mpls_next_hop_self"] = {"source_interface": "Loopback0"}

        peer_groups = []

        if self.shared_utils.overlay_ipvpn_gateway is True:
            peer_groups.append({"name": self._get_peer_group_name("ipvpn_gateway_peers"), "activate": True})

        if self.shared_utils.overlay_routing_protocol == "ibgp":
            if self.shared_utils.overlay_mpls is True:
                peer_groups.append({"name": self._get_peer_group_name("mpls_overlay_peers"), "activate": True})

            if self.shared_utils.mpls_overlay_role == "server":
                peer_groups.append({"name": self._get_peer_group_name("rr_overlay_peers"), "activate": True})

        if peer_groups:
            address_family_vpn_ipvx["peer_groups"] = peer_groups

        if self.shared_utils.overlay_dpath is True:
            address_family_vpn_ipvx["domain_identifier"] = get(self.shared_utils.switch_data_combined, "ipvpn_gateway.ipvpn_domain_id", default="65535:2")

        return address_family_vpn_ipvx

    def _create_neighbor(
        self: AvdStructuredConfigOverlay,
        ip_address: str,
        name: str,
        peer_group: str,
        remote_as: str | None = None,
        overlay_peering_interface: str | None = None,
    ) -> dict:
        neighbor = {
            "ip_address": ip_address,
            "peer_group": peer_group,
            "peer": name,
            "description": AvdStringFormatter().format(
                self.shared_utils.overlay_bgp_peer_description, **strip_empties_from_dict({"peer": name, "peer_interface": overlay_peering_interface})
            ),
        }

        if self.shared_utils.overlay_routing_protocol == "ebgp":
            if remote_as is None:
                msg = "Configuring eBGP neighbor without a remote_as"
                raise AristaAvdError(msg)
            neighbor["remote_as"] = remote_as

        if self.shared_utils.shutdown_bgp_towards_undeployed_peers is True and name in self._avd_overlay_peers:
            peer_facts = self.shared_utils.get_peer_facts(name)
            if peer_facts["is_deployed"] is False:
                neighbor["shutdown"] = True

        return neighbor

    def _neighbors(self: AvdStructuredConfigOverlay) -> list | None:
        neighbors = []

        if self.shared_utils.overlay_routing_protocol == "ebgp":
            for route_server, data in natural_sort(self._evpn_route_servers.items()):
                neighbor = self._create_neighbor(
                    data["ip_address"],
                    route_server,
                    self._get_peer_group_name("evpn_overlay_peers"),
                    remote_as=data["bgp_as"],
                    overlay_peering_interface=data.get("overlay_peering_interface"),
                )

                if self.shared_utils.evpn_prevent_readvertise_to_server is True:
                    neighbor["route_map_out"] = f"RM-EVPN-FILTER-AS{data['bgp_as']}"
                neighbors.append(neighbor)

            for route_client, data in natural_sort(self._evpn_route_clients.items()):
                neighbor = self._create_neighbor(
                    data["ip_address"],
                    route_client,
                    self._get_peer_group_name("evpn_overlay_peers"),
                    remote_as=data["bgp_as"],
                    overlay_peering_interface=data.get("overlay_peering_interface"),
                )
                neighbors.append(neighbor)

            for gw_remote_peer, data in natural_sort(self._evpn_gateway_remote_peers.items()):
                neighbor = self._create_neighbor(
                    data["ip_address"],
                    gw_remote_peer,
                    self._get_peer_group_name("evpn_overlay_core"),
                    remote_as=data["bgp_as"],
                    overlay_peering_interface=data.get("overlay_peering_interface"),
                )
                neighbors.append(neighbor)

        if self.shared_utils.overlay_routing_protocol == "ibgp":
            if self.shared_utils.overlay_mpls is True:
                for route_reflector, data in natural_sort(self._mpls_route_reflectors.items()):
                    neighbor = self._create_neighbor(
                        data["ip_address"],
                        route_reflector,
                        self._get_peer_group_name("mpls_overlay_peers"),
                        overlay_peering_interface=data.get("overlay_peering_interface"),
                    )
                    neighbors.append(neighbor)

                for route_client, data in natural_sort(self._mpls_route_clients.items()):
                    neighbor = self._create_neighbor(
                        data["ip_address"],
                        route_client,
                        self._get_peer_group_name("mpls_overlay_peers"),
                        overlay_peering_interface=data.get("overlay_peering_interface"),
                    )
                    neighbors.append(neighbor)

                for mesh_pe, data in natural_sort(self._mpls_mesh_pe.items()):
                    neighbor = self._create_neighbor(
                        data["ip_address"],
                        mesh_pe,
                        self._get_peer_group_name("mpls_overlay_peers"),
                        overlay_peering_interface=data.get("overlay_peering_interface"),
                    )
                    neighbors.append(neighbor)

                if self._is_mpls_server is True:
                    for rr_peer, data in natural_sort(self._mpls_rr_peers.items()):
                        neighbor = self._create_neighbor(
                            data["ip_address"],
                            rr_peer,
                            self._get_peer_group_name("rr_overlay_peers"),
                            overlay_peering_interface=data.get("overlay_peering_interface"),
                        )
                        neighbors.append(neighbor)

            if self.shared_utils.overlay_evpn_vxlan is True:
                for route_server, data in natural_sort(self._evpn_route_servers.items()):
                    neighbor = self._create_neighbor(
                        data["ip_address"],
                        route_server,
                        self._get_peer_group_name("evpn_overlay_peers"),
                        overlay_peering_interface=data.get("overlay_peering_interface"),
                    )
                    neighbors.append(neighbor)

                for route_client, data in natural_sort(self._evpn_route_clients.items()):
                    neighbor = self._create_neighbor(
                        data["ip_address"],
                        route_client,
                        self._get_peer_group_name("evpn_overlay_peers"),
                        overlay_peering_interface=data.get("overlay_peering_interface"),
                    )
                    neighbors.append(neighbor)

            if self.shared_utils.is_wan_client:
                if not self._ip_in_listen_ranges(self.shared_utils.vtep_ip, self.shared_utils.wan_listen_ranges):
                    msg = f"{self.shared_utils.vtep_loopback} IP {self.shared_utils.vtep_ip} is not in the Route Reflector listen range prefixes"
                    raise AristaAvdError(msg)
                for wan_route_server, data in self.shared_utils.filtered_wan_route_servers.items():
                    neighbor = self._create_neighbor(
                        data["vtep_ip"],
                        wan_route_server,
                        self._get_peer_group_name("wan_overlay_peers"),
                        overlay_peering_interface=self.shared_utils.vtep_loopback,
                    )
                    neighbors.append(neighbor)

                if self.shared_utils.wan_ha:
                    neighbor = {
                        "ip_address": self._wan_ha_peer_vtep_ip(),
                        "peer": self.shared_utils.wan_ha_peer,
                        "description": self.shared_utils.wan_ha_peer,
                        "remote_as": self.shared_utils.bgp_as,
                        "update_source": "Dps1",
                        "route_reflector_client": True,
                        "send_community": "all",
                        "route_map_in": "RM-WAN-HA-PEER-IN",
                        "route_map_out": "RM-WAN-HA-PEER-OUT",
                    }
                    neighbors.append(neighbor)

            if self.shared_utils.is_wan_server:
                # No neighbor configured on the `wan_overlay_peers` peer group as it is covered by listen ranges
                for wan_route_server, data in self.shared_utils.filtered_wan_route_servers.items():
                    neighbor = self._create_neighbor(
                        data["vtep_ip"],
                        wan_route_server,
                        self._get_peer_group_name("wan_rr_overlay_peers"),
                        overlay_peering_interface=self.shared_utils.vtep_loopback,
                    )
                    neighbors.append(neighbor)

        for ipvpn_gw_peer, data in natural_sort(self._ipvpn_gateway_remote_peers.items()):
            neighbor = self._create_neighbor(
                data["ip_address"],
                ipvpn_gw_peer,
                self._get_peer_group_name("ipvpn_gateway_peers"),
                remote_as=data["bgp_as"],
                overlay_peering_interface=data.get("overlay_peering_interface"),
            )
            # Add ebgp_multihop if the gw peer is an ebgp peer.
            if data["bgp_as"] != default(self._ipvpn_gateway_local_as, self.shared_utils.bgp_as):
                neighbor["ebgp_multihop"] = self.shared_utils.evpn_ebgp_gateway_multihop

            neighbors.append(neighbor)

        if neighbors:
            return neighbors

        return None

    def _ip_in_listen_ranges(self: AvdStructuredConfigOverlay, source_ip: str, listen_range_prefixes: list) -> bool:
        """Check if our source IP is in any of the listen range prefixes."""
        source_ip = ipaddress.ip_address(source_ip)
        return any(source_ip in ipaddress.ip_network(prefix) for prefix in listen_range_prefixes)

    def _bgp_overlay_dpath(self: AvdStructuredConfigOverlay) -> dict | None:
        if self.shared_utils.overlay_dpath is True:
            return {
                "bestpath": {
                    "d_path": True,
                },
            }
        return None
