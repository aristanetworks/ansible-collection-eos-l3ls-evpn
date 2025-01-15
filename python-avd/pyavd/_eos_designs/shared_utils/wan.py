# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from re import findall
from typing import TYPE_CHECKING, Literal

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils import default, get, get_ip_from_ip_prefix, strip_empties_from_dict
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from . import SharedUtils


class WanMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def wan_role(self: SharedUtils) -> str | None:
        if self.underlay_router is False:
            return None

        default_wan_role = self.node_type_key_data.default_wan_role
        return self.node_config.wan_role or default_wan_role

    @cached_property
    def is_wan_router(self: SharedUtils) -> bool:
        return bool(self.wan_role)

    @cached_property
    def is_wan_server(self: SharedUtils) -> bool:
        return self.wan_role == "server"

    @cached_property
    def is_wan_client(self: SharedUtils) -> bool:
        return self.wan_role == "client"

    @cached_property
    def wan_listen_ranges(self: SharedUtils) -> EosDesigns.BgpPeerGroups.WanOverlayPeers.ListenRangePrefixes:
        if not self.inputs.bgp_peer_groups.wan_overlay_peers.listen_range_prefixes:
            msg = "bgp_peer_groups.wan_overlay_peers.listen_range_prefixes"
            raise AristaAvdMissingVariableError(msg)
        return self.inputs.bgp_peer_groups.wan_overlay_peers.listen_range_prefixes

    @cached_property
    def cv_pathfinder_transit_mode(self: SharedUtils) -> Literal["region", "zone"] | None:
        """When wan_mode is CV Pathfinder, return the transit mode "region", "zone" or None."""
        if not self.is_cv_pathfinder_client:
            return None

        return self.node_config.cv_pathfinder_transit_mode

    @cached_property
    def wan_interfaces(self: SharedUtils) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3Interfaces:
        """
        As a first approach, only interfaces under node config l3_interfaces can be considered as WAN interfaces.

        This may need to be made wider.
        This also may require a different format for the dictionaries inside the list.
        """
        if not self.is_wan_router:
            return EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3Interfaces()

        wan_interfaces = EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3Interfaces(
            [interface for interface in self.l3_interfaces if interface.wan_carrier]
        )
        if not wan_interfaces:
            msg = "At least one WAN interface must be configured on a WAN router. Add WAN interfaces under `l3_interfaces` node setting with `wan_carrier` set."
            raise AristaAvdError(msg)
        return wan_interfaces

    @cached_property
    def wan_local_carriers(self: SharedUtils) -> list:
        """
        List of carriers present on this router based on the wan_interfaces with the associated WAN interfaces.

            interfaces:
              - name: ...
                ip: ... (for route-servers the IP may come from wan_route_servers).
        """
        if not self.is_wan_router:
            return []

        local_carriers_dict = {}
        for interface in self.wan_interfaces:
            interface_carrier: str = interface.wan_carrier
            if interface_carrier not in local_carriers_dict:
                if interface_carrier not in self.inputs.wan_carriers:
                    msg = f"WAN carrier {interface_carrier} is not in the available carriers defined in `wan_carriers`"
                    raise AristaAvdInvalidInputsError(msg)
                local_carriers_dict[interface_carrier] = self.inputs.wan_carriers[interface_carrier]._as_dict(include_default_values=True)
                local_carriers_dict[interface_carrier]["interfaces"] = []

            local_carriers_dict[interface_carrier]["interfaces"].append(
                strip_empties_from_dict(
                    {
                        "name": interface.name,
                        "public_ip": self.get_public_ip_for_wan_interface(interface),
                        "connected_to_pathfinder": interface.connected_to_pathfinder,
                        "wan_circuit_id": interface.wan_circuit_id,
                    },
                ),
            )

        return list(local_carriers_dict.values())

    @cached_property
    def wan_local_path_groups(self: SharedUtils) -> EosDesigns.WanPathGroups:
        """
        List of path-groups present on this router based on the local carriers.

        Also add for each path-groups the local interfaces in a data structure
            interfaces:
              - name: ...
                public_ip: ...
        """
        local_path_groups = EosDesigns.WanPathGroups()

        if not self.is_wan_router:
            return local_path_groups

        for carrier in self.wan_local_carriers:
            path_group_name: str = get(carrier, "path_group", required=True)
            if path_group_name not in local_path_groups:
                if path_group_name not in self.inputs.wan_path_groups:
                    msg = f"WAN path_group {path_group_name} defined for a WAN carrier is not in the available path_groups defined in `wan_path_groups`"
                    raise AristaAvdInvalidInputsError(msg)

                local_path_groups[path_group_name] = self.inputs.wan_path_groups[path_group_name]._deepcopy()
                local_path_groups[path_group_name]._interfaces = []

            local_path_groups[path_group_name]._interfaces.extend(carrier["interfaces"])

        return local_path_groups

    @cached_property
    def wan_local_path_group_names(self: SharedUtils) -> list:
        """Return a list of wan_local_path_group names."""
        return list(self.wan_local_path_groups.keys())

    @cached_property
    def wan_ha_peer_path_groups(self: SharedUtils) -> list:
        """List of WAN HA peer path-groups coming from facts."""
        if not self.is_wan_router or not self.wan_ha:
            return []
        peer_facts = self.get_peer_facts(self.wan_ha_peer, required=True)
        return get(peer_facts, "wan_path_groups", required=True)

    @cached_property
    def wan_ha_peer_path_group_names(self: SharedUtils) -> list:
        """Return a list of wan_ha_peer_path_group names."""
        return [path_group["name"] for path_group in self.wan_ha_peer_path_groups]

    def get_public_ip_for_wan_interface(self: SharedUtils, interface: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem) -> str:
        """
        Takes a dict which looks like `l3_interface` from node config.

        If not a WAN route-server this returns public IP and if not found then the interface IP without a mask.

        For WAN route-servers we try to find the IP under wan_route_servers.path_groups.interfaces.
        If not found we look for the public_ip and then the ip_address under the interface.
        If there is no public_ip and if ip_address is "dhcp" we raise an error.
        """
        if not self.is_wan_server:
            return default(interface.public_ip, get_ip_from_ip_prefix(interface.ip_address))

        if self.hostname in self.inputs.wan_route_servers:
            for path_group in self.inputs.wan_route_servers[self.hostname].path_groups:
                if interface.name not in path_group.interfaces:
                    continue

                if public_ip := path_group.interfaces[interface.name].public_ip:
                    return public_ip

        if interface.public_ip:
            return interface.public_ip

        if interface.ip_address == "dhcp":
            msg = (
                f"The IP address for WAN interface '{interface.name}' on Route Server '{self.hostname}' is set to 'dhcp'. "
                "Clients need to peer with a static IP which must be set under the 'wan_route_servers.path_groups.interfaces' key."
            )
            raise AristaAvdError(msg)

        return get_ip_from_ip_prefix(interface.ip_address)

    @cached_property
    def wan_site(self: SharedUtils) -> EosDesigns.CvPathfinderRegionsItem.SitesItem | EosDesigns.CvPathfinderGlobalSitesItem | None:
        """
        WAN site for CV Pathfinder.

        The site is required for edges, but optional for pathfinders
        """
        node_defined_site = self.node_config.cv_pathfinder_site
        if not node_defined_site and self.is_cv_pathfinder_client:
            msg = "A node variable 'cv_pathfinder_site' must be defined when 'wan_role' is 'client' and 'wan_mode' is 'cv-pathfinder'."
            raise AristaAvdInvalidInputsError(msg)

        if not node_defined_site:
            return None

        # Special case for cv_pathfinders without a region, we find the site details under `cv_pathfinder_global_sites` instead.
        if self.is_cv_pathfinder_server and self.wan_region is None:
            if node_defined_site not in self.inputs.cv_pathfinder_global_sites:
                msg = f"The 'cv_pathfinder_site '{node_defined_site}' defined at the node level could not be found under the 'cv_pathfinder_global_sites' list"
                raise AristaAvdInvalidInputsError(msg)
            return self.inputs.cv_pathfinder_global_sites[node_defined_site]

        if self.wan_region is None or node_defined_site not in self.wan_region.sites:
            msg = (
                f"The 'cv_pathfinder_site '{node_defined_site}' defined at the node level could not be found under the 'sites' list for the region"
                f" '{self.wan_region.name if self.wan_region is not None else '.'}'."
            )
            raise AristaAvdInvalidInputsError(msg)

        return self.wan_region.sites[node_defined_site]

    @cached_property
    def wan_region(self: SharedUtils) -> EosDesigns.CvPathfinderRegionsItem | None:
        """
        WAN region for CV Pathfinder.

        The region is required for edges, but optional for pathfinders
        """
        node_defined_region = self.node_config.cv_pathfinder_region
        if not node_defined_region and self.is_cv_pathfinder_client:
            msg = "A node variable 'cv_pathfinder_region' must be defined when 'wan_role' is 'client' and 'wan_mode' is 'cv-pathfinder'."
            raise AristaAvdInvalidInputsError(msg)

        if node_defined_region is None:
            return None

        if node_defined_region not in self.inputs.cv_pathfinder_regions:
            msg = "The 'cv_pathfinder_region' defined at the node level could not be found under the 'cv_pathfinder_regions' key."
            raise AristaAvdInvalidInputsError(msg)

        return self.inputs.cv_pathfinder_regions[node_defined_region]

    @property
    def wan_zone(self: SharedUtils) -> dict:
        """
        WAN zone for Pathfinder.

        Currently, only one default zone with ID 1 is supported.
        """
        # Injecting default zone with id 1.
        if self.wan_region is None:
            # Should never happen but just in case.
            msg = "Could not find 'cv_pathfinder_region' so it is not possible to auto-generate the zone."
            raise AristaAvdInvalidInputsError(msg)

        return {"name": f"{self.wan_region.name}-ZONE", "id": 1}

    @cached_property
    def filtered_wan_route_servers(self: SharedUtils) -> EosDesigns.WanRouteServers:
        """
        Return a dict keyed by Wan RR based on the the wan_mode type with only the path_groups the router should connect to.

        If the RR is part of the inventory, the peer_facts are read..
        If any key is specified in the variables, it overwrites whatever is in the peer_facts.

        If no peer_fact is found the variables are required in the inventory.
        """
        filtered_wan_route_servers = EosDesigns.WanRouteServers()

        for org_wan_rs in self.inputs.wan_route_servers._natural_sorted():
            if org_wan_rs.hostname == self.hostname:
                # Don't add yourself
                continue

            wan_rs = org_wan_rs._deepcopy()

            # These remote gw can be outside of the inventory
            if (peer_facts := self.get_peer_facts(wan_rs.hostname, required=False)) is not None:
                # Found a matching server in inventory
                bgp_as = peer_facts.get("bgp_as")

                # Only ibgp is supported for WAN so raise if peer from peer_facts BGP AS is different from ours.
                if bgp_as != self.bgp_as:
                    msg = f"Only iBGP is supported for WAN, the BGP AS {bgp_as} on {wan_rs} is different from our own: {self.bgp_as}."
                    raise AristaAvdError(msg)

                # Prefer values coming from the input variables over peer facts
                if not wan_rs.vtep_ip:
                    if not (peer_vtep_ip := peer_facts.get("vtep_ip")):
                        msg = (
                            f"'vtep_ip' is missing for peering with {wan_rs}, either set it in under 'wan_route_servers' or something is wrong with the peer"
                            " facts."
                        )
                        raise AristaAvdInvalidInputsError(msg)
                    wan_rs.vtep_ip = peer_vtep_ip

                if not wan_rs.path_groups:
                    if not (peer_path_groups := peer_facts.get("wan_path_groups")):
                        msg = (
                            f"'wan_path_groups' is missing for peering with {wan_rs}, either set it in under 'wan_route_servers'"
                            " or something is wrong with the peer facts."
                        )
                        raise AristaAvdInvalidInputsError(msg)

                    # We cannot coerce or load with _from_list() since the data models are not compatible.
                    wan_rs.path_groups = EosDesigns.WanRouteServersItem.PathGroups(
                        [
                            EosDesigns.WanRouteServersItem.PathGroupsItem(
                                name=peer_path_group["name"],
                                interfaces=EosDesigns.WanRouteServersItem.PathGroupsItem.Interfaces(
                                    [
                                        EosDesigns.WanRouteServersItem.PathGroupsItem.InterfacesItem(
                                            name=interface["name"], public_ip=interface.get("public_ip")
                                        )
                                        for interface in peer_path_group.get("_interfaces", [])
                                    ]
                                ),
                            )
                            for peer_path_group in peer_path_groups
                        ]
                    )

            else:
                # Retrieve the values from the dictionary, making them required if the peer_facts were not found
                if not wan_rs.vtep_ip:
                    msg = (
                        f"'vtep_ip' is missing for peering with {wan_rs} which was not found in the inventory. Either set it in under 'wan_route_servers'"
                        " or check your inventory."
                    )
                    raise AristaAvdInvalidInputsError(msg)

                if not wan_rs.path_groups:
                    msg = (
                        f"'path_groups' is missing for peering with {wan_rs} which was not found in the inventory, Either set it in under 'wan_route_servers'"
                        " or check your inventory."
                    )
                    raise AristaAvdInvalidInputsError(msg)

            # Filtering wan_path_groups to only take the ones this device uses to connect to pathfinders.
            wan_rs.path_groups = EosDesigns.WanRouteServersItem.PathGroups(
                [path_group for path_group in wan_rs.path_groups if self.should_connect_to_wan_rs([path_group.name])]
            )

            # If no common path-group then skip
            # TODO: - this may need to change when `import` path-groups is available
            if wan_rs.path_groups:
                filtered_wan_route_servers.append(wan_rs)

        return filtered_wan_route_servers

    def should_connect_to_wan_rs(self: SharedUtils, path_group_names: list[str]) -> bool:
        """
        This helper implements whether or not a connection to the wan_router_server should be made or not based on a list of path-groups.

        To do this the logic is the following:
        * Look at the wan_interfaces on the router and check if there is any path-group in common with the RR where
          `connected_to_pathfinder` is not False.
        """
        return any(
            local_path_group.name in path_group_names and any(wan_interface["connected_to_pathfinder"] for wan_interface in local_path_group._interfaces)
            for local_path_group in self.wan_local_path_groups
        )

    @cached_property
    def is_cv_pathfinder_router(self: SharedUtils) -> bool:
        """Return True is the current wan_mode is cv-pathfinder and the device is a wan router."""
        return self.inputs.wan_mode == "cv-pathfinder" and self.is_wan_router

    @cached_property
    def is_cv_pathfinder_client(self: SharedUtils) -> bool:
        """Return True is the current wan_mode is cv-pathfinder and the device is either an edge or a transit device."""
        return self.is_cv_pathfinder_router and self.is_wan_client

    @cached_property
    def is_cv_pathfinder_server(self: SharedUtils) -> bool:
        """Return True is the current wan_mode is cv-pathfinder and the device is a pathfinder device."""
        return self.is_cv_pathfinder_router and self.is_wan_server

    @cached_property
    def cv_pathfinder_role(self: SharedUtils) -> str | None:
        if not self.is_cv_pathfinder_router:
            return None

        if self.is_cv_pathfinder_server:
            return "pathfinder"

        # Transit
        if (transit_mode := self.cv_pathfinder_transit_mode) is not None:
            return f"transit {transit_mode}"

        # Edge
        return "edge"

    @cached_property
    def wan_ha(self: SharedUtils) -> bool:
        """Only trigger HA if 2 cv_pathfinder clients are in the same group and wan_ha.enabled is true."""
        if not self.is_cv_pathfinder_client or self.node_group_is_primary_and_peer_hostname is None:
            return False

        if self.node_config.wan_ha.enabled is None:
            msg = (
                "Placing two WAN routers in a common node group will trigger WAN HA in a future AVD release. "
                "Currently WAN HA is in preview, so it will not be automatically enabled. "
                "To avoid unplanned configuration changes once the feature is released, "
                "it is currently required to set 'wan_ha.enabled' to 'true' or 'false'."
            )
            raise AristaAvdError(msg)
        return self.node_config.wan_ha.enabled

    @cached_property
    def wan_ha_ipsec(self: SharedUtils) -> bool:
        return self.wan_ha and self.node_config.wan_ha.ipsec

    @cached_property
    def is_first_ha_peer(self: SharedUtils) -> bool:
        """
        Returns True if the device is the first device in the node_group, false otherwise.

        This should be called only from functions which have checked that HA is enabled.
        """
        return self.node_group_is_primary_and_peer_hostname is not None and self.node_group_is_primary_and_peer_hostname[0]

    @cached_property
    def wan_ha_peer(self: SharedUtils) -> str | None:
        """Return the name of the WAN HA peer."""
        if not self.wan_ha:
            return None

        if self.node_group_is_primary_and_peer_hostname is not None:
            return self.node_group_is_primary_and_peer_hostname[1]

        msg = "Unable to find WAN HA peer within same node group"
        raise AristaAvdError(msg)

    @cached_property
    def vrf_default_uplinks(self: SharedUtils) -> list:
        """Return the uplinkss in VRF default."""
        return [uplink for uplink in self.get_switch_fact("uplinks") if get(uplink, "vrf") is None]

    @cached_property
    def vrf_default_uplink_interfaces(self: SharedUtils) -> list:
        """Return the uplink interfaces in VRF default."""
        return [uplink["interface"] for uplink in self.vrf_default_uplinks]

    @cached_property
    def use_uplinks_for_wan_ha(self: SharedUtils) -> bool:
        """
        Indicates whether the device is using its uplinks for WAN HA or direct HA.

        Returns:
            bool: True if uplinks are used for HA, False otherwise

        Raises:
            AristaAvdError: when the list of configured interfaces is a mix of uplinks and none uplinks.
        """
        interfaces = set(self.node_config.wan_ha.ha_interfaces)
        uplink_interfaces = set(self.vrf_default_uplink_interfaces)

        if interfaces.issubset(uplink_interfaces):
            return True
        if not interfaces.intersection(uplink_interfaces):
            return False
        msg = "Either all `wan_ha.ha_interfaces` must be uplink interfaces or all of them must not be uplinks."
        raise AristaAvdError(msg)

    @cached_property
    def wan_ha_interfaces(self: SharedUtils) -> list:
        """
        Return the list of interfaces for WAN HA.

        If using uplinks for WAN HA, returns the filtered uplinks if self.node_config.wan_ha.ha_interfaces is not empty
        else returns all of them.
        """
        if self.use_uplinks_for_wan_ha:
            return natural_sort(set(self.node_config.wan_ha.ha_interfaces)) or self.vrf_default_uplink_interfaces
        # Using node values
        return natural_sort(set(self.node_config.wan_ha.ha_interfaces))

    @cached_property
    def wan_ha_port_channel_id(self: SharedUtils) -> int:
        """
        Port-channel ID to use for direct WAN HA port-channel.

        If not provided, computed from the list of configured members.
        """
        return default(self.node_config.wan_ha.port_channel_id, int("".join(findall(r"\d", self.wan_ha_interfaces[0]))))

    @cached_property
    def use_port_channel_for_direct_ha(self: SharedUtils) -> bool:
        """
        Indicate if port-channel should be used for direct HA.

        Returns:
            bool: False is use_uplinks_for_wan_ha is True
                  True if strictly there is more than one configured wan_ha.interfaces
                  otherwise the value of `wan_ha.use_port_channel_for_direct_ha` which defaults to True.
        """
        if self.use_uplinks_for_wan_ha:
            return False

        interfaces = set(self.node_config.wan_ha.ha_interfaces)

        return len(interfaces) > 1 or self.node_config.wan_ha.use_port_channel_for_direct_ha

    @cached_property
    def wan_ha_peer_ip_addresses(self: SharedUtils) -> list:
        """
        Read the IP addresses/prefix length from HA peer uplinks.

        Used also to generate the prefix list of the PEER HA prefixes.
        """
        ip_addresses = []
        if self.use_uplinks_for_wan_ha:
            peer_facts = self.get_peer_facts(self.wan_ha_peer, required=True)
            vrf_default_peer_uplinks = [uplink for uplink in get(peer_facts, "uplinks", required=True) if get(uplink, "vrf") is None]
            interfaces = set(self.node_config.wan_ha.ha_interfaces)
            for uplink in vrf_default_peer_uplinks:
                if not interfaces or uplink["interface"] in interfaces:
                    ip_address = get(
                        uplink,
                        "ip_address",
                        required=True,
                        custom_error_msg=(
                            f"The uplink interface {uplink['interface']} used as WAN LAN HA on the remote peer {self.wan_ha_peer} does not have an IP address."
                        ),
                    )
                    prefix_length = uplink["prefix_length"]
                    ip_addresses.append(f"{ip_address}/{prefix_length}")
        else:
            # Only one supported HA interface today when not using uplinks
            ip_addresses.append(self.ip_addressing.wan_ha_peer_ip())
        return ip_addresses

    @cached_property
    def wan_ha_ip_addresses(self: SharedUtils) -> list:
        """
        Read the IP addresses/prefix length from this device uplinks used for HA.

        Used to generate the prefix list.
        """
        ip_addresses = []

        if self.use_uplinks_for_wan_ha:
            interfaces = set(self.node_config.wan_ha.ha_interfaces)
            for uplink in self.vrf_default_uplinks:
                if not interfaces or uplink["interface"] in interfaces:
                    ip_address = get(
                        uplink,
                        "ip_address",
                        required=True,
                        custom_error_msg=f"The uplink interface {uplink['interface']} used as WAN LAN HA does not have an IP address.",
                    )
                    # We can use [] notation here because if there is an ip_address, there should be a prefix_length
                    prefix_length = uplink["prefix_length"]
                    ip_addresses.append(f"{ip_address}/{prefix_length}")
        else:
            # Only one supported HA interface today when not using uplinks
            ip_addresses.append(self.ip_addressing.wan_ha_ip())
        return ip_addresses

    @cached_property
    def wan_ha_ipv4_pool(self: SharedUtils) -> str:
        """Return the configured wan_ha.ha_ipv4_pool."""
        if not self.node_config.wan_ha.ha_ipv4_pool:
            msg = "Missing `wan_ha.ha_ipv4_pool` node settings to allocate an IP address to defined HA interface."
            raise AristaAvdInvalidInputsError(msg)
        return self.node_config.wan_ha.ha_ipv4_pool

    def generate_lb_policy_name(self: SharedUtils, name: str) -> str:
        """Returns LB-{name}."""
        return f"LB-{name}"

    @cached_property
    def wan_stun_dtls_profile_name(self: SharedUtils) -> str | None:
        """Return the DTLS profile name to use for STUN for WAN."""
        if not self.is_wan_router or self.inputs.wan_stun_dtls_disable:
            return None

        return self.inputs.wan_stun_dtls_profile_name

    def vrf_has_wan_vni(self: SharedUtils, vrf_name: str) -> bool:
        """Returns True if the VRF `vrf_name` is present under wan_virtual_topologies and wan_vni is set."""
        return vrf_name in self.inputs.wan_virtual_topologies.vrfs and self.inputs.wan_virtual_topologies.vrfs[vrf_name].wan_vni
