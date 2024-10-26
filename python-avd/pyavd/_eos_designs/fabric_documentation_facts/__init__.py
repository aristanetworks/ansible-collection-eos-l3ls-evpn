# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from functools import cached_property
from ipaddress import IPv4Network, IPv6Network, ip_network
from math import ceil

from pyavd._eos_designs.avdfacts import AvdFacts
from pyavd._utils import default, get, get_item
from pyavd.j2filters import natural_sort

from .topology import Topology


class FabricDocumentationFacts(AvdFacts):
    """
    Class calculating/holding facts used for generating Fabric Documentation and CSVs.

    For use in Jinja call the .render() method to return a dict of the cached_properties.
    For use in Python the instance can be used directly to avoid calculating facts unless needed.
    """

    avd_switch_facts: dict[str, dict]
    structured_configs: dict[str, dict]
    _fabric_name: str
    _include_connected_endpoints: bool
    """Avoid building data for connected endpoints unless we need it."""

    # Overriding class vars from AvdFacts, since fabric documentation covers all devices.
    _hostvars = NotImplemented
    shared_utils = NotImplemented

    def __init__(self, avd_facts: dict[str, dict], structured_configs: dict[str, dict], fabric_name: str, include_connected_endpoints: bool) -> None:  # pylint: disable=super-init-not-called
        self.avd_switch_facts = {hostname: facts["switch"] for hostname, facts in get(avd_facts, "avd_switch_facts", required=True).items()}
        self._fabric_name = fabric_name
        self.structured_configs = structured_configs
        self._include_connected_endpoints = include_connected_endpoints

    @cached_property
    def fabric_name(self) -> str:
        """Fabric Name used for heading of Markdown doc."""
        return self._fabric_name

    @cached_property
    def fabric_switches(self) -> list[dict]:
        """List of fabric switches."""
        return natural_sort(
            [
                {
                    "node": hostname,
                    "type": self.avd_switch_facts[hostname]["type"],
                    "pod": self.avd_switch_facts[hostname].get("pod"),
                    "mgmt_ip": self.avd_switch_facts[hostname].get("mgmt_ip") or "-",
                    "platform": self.avd_switch_facts[hostname].get("platform") or "-",
                    "provisioned": "Provisioned" if self.avd_switch_facts[hostname].get("is_deployed") else "Not Available",
                    "serial_number": self.avd_switch_facts[hostname].get("serial_number") or "-",
                    "inband_mgmt_ip": self.avd_switch_facts[hostname].get("inband_mgmt_ip"),
                    "inband_mgmt_interface": self.avd_switch_facts[hostname].get("inband_mgmt_interface"),
                    "loopback0_ip_address": get(
                        get_item(get(structured_config, "loopback_interfaces", default=[]), "name", "Loopback0", default={}), "ip_address"
                    ),
                    # TODO: Improve VTEP loopback detection
                    "vtep_loopback_ip_address": get(
                        get_item(get(structured_config, "loopback_interfaces", default=[]), "name", "Loopback1", default={}), "ip_address"
                    ),
                    "router_isis_net": get(structured_config, "router_isis.net"),
                }
                for hostname, structured_config in self.structured_configs.items()
            ],
            sort_key="node",
        )

    @cached_property
    def has_isis(self) -> bool:
        """At least one device has ISIS configured, so we should include the section in the docs."""
        return any(fabric_switch.get("router_isis_net") for fabric_switch in self.fabric_switches)

    @cached_property
    def _node_types(self) -> set[str]:
        """Set of node types that are part of the fabric."""
        return {switch["type"] for switch in self.fabric_switches}

    @cached_property
    def _topology(self) -> Topology:
        """
        Internal Topology mode.

        The topology model is an undirected graph containing links between devices that are of any type covered by the fabric.
        The model is populated by traversing all ethernet_interfaces and adding the links using information about the device itself as well as the peer.
        The links (edges) of the graph contain FrozenSets to enable automatic deduplication. The same link will only be once in the Graph even if added
        from both ends.

        The topology model is only used for listing deduplicated edges in various ways, but it can be used for other purposes like diagrams later.
        """
        topology = Topology()
        for hostname, structured_config in self.structured_configs.items():
            for ethernet_interface in get(structured_config, "ethernet_interfaces", default=[]):
                if (peer_type := get(ethernet_interface, "peer_type")) not in self._node_types and peer_type != "mlag_peer":
                    continue

                peer = get(ethernet_interface, "peer", required=True)
                if peer_type == "mlag_peer":
                    peer_type = self.avd_switch_facts[peer]["type"]
                    mlag_peer = True
                else:
                    mlag_peer = False
                if peer_interface := get(ethernet_interface, "peer_interface"):
                    peer_ethernet_interface = get_item(
                        get(self.structured_configs, f"{peer}..ethernet_interfaces", separator="..", default=[]), "name", peer_interface, default={}
                    )
                    peer_ip_address = get(peer_ethernet_interface, "ip_address")
                else:
                    peer_ip_address = None

                routed = get(ethernet_interface, "switchport.enabled") is False

                data = (
                    self.avd_switch_facts[hostname]["type"],  # type
                    get(ethernet_interface, "name"),  # interface
                    get(ethernet_interface, "ip_address"),  # ip_address
                    mlag_peer,  # is_mlag_peer
                    routed,  # boolean to tell if the interface is routed or switched
                )
                peer_data = (
                    peer_type,  # type
                    peer_interface,  # interface
                    peer_ip_address,  # ip_address
                    mlag_peer,  # is_mlag_peer
                    routed,  # boolean to tell if the interface is routed or switched
                )
                topology.add_edge(hostname, peer, data, peer_data)

        return topology

    @cached_property
    def topology_links(self) -> list[dict]:
        """List of topology links extracted from _topology."""
        return natural_sort(
            [
                {
                    "node": hostname,
                    "type": data[0],
                    "node_interface": data[1],
                    "node_ip_address": data[2],
                    "routed": data[4],
                    "peer": peer_name,
                    "peer_type": "mlag_peer" if peer_data[3] else peer_data[0],
                    "peer_interface": peer_data[1],
                    "peer_ip_address": peer_data[2],
                }
                for hostname, edges in self._topology.get_edges_by_node_unidirectional_sorted().items()
                if edges
                for edge in edges
                for node_name, data in edge.node_data
                if node_name == hostname
                # Below is just a way to set the peer variables for easy reuse.
                for peer_name, peer_data in edge.node_data
                if peer_name != hostname
            ]
        )

    @cached_property
    def uplink_ipv4_pools(self) -> list[dict]:
        """List of unique uplink_ipv4_pools containing information about size and usage."""
        # Build set of loopback_ipv4_pool for all devices
        pools_set = {f"{pool}" for switch in self.avd_switch_facts.values() if (pool := get(switch, "uplink_ipv4_pool"))}
        pools = [ip_network(pool, strict=False) for pool in pools_set]

        # Build list of ip addresses found in topology
        ip_addresses = [ip_network(data[2], strict=False) for edge in self._topology.get_edges() for _, data in edge.node_data if data[2] is not None]

        return self.render_pools_as_list(pools, ip_addresses)

    @cached_property
    def loopback_ipv4_pools(self) -> list[dict]:
        """List of unique loopback_ipv4_pools containing information about size and usage."""
        # Build set of loopback_ipv4_pool for all devices
        pools_set = {f"{pool}" for switch in self.avd_switch_facts.values() if (pool := get(switch, "loopback_ipv4_pool"))}
        pools = [ip_network(pool, strict=False) for pool in pools_set]

        # Build list of ip addresses found in fabric switches
        ip_addresses = [
            ip_network(fabric_switch["loopback0_ip_address"], strict=False)
            for fabric_switch in self.fabric_switches
            if fabric_switch["loopback0_ip_address"] is not None
        ]
        return self.render_pools_as_list(pools, ip_addresses)

    @cached_property
    def vtep_loopback_ipv4_pools(self) -> list[dict]:
        """List of unique vtep_loopback_ipv4_pools containing information about size and usage."""
        # Build set of vtep_loopback_ipv4_pool from all devices
        pools_set = {f"{pool}" for switch in self.avd_switch_facts.values() if (pool := get(switch, "vtep_loopback_ipv4_pool"))}
        pools = [ip_network(pool, strict=False) for pool in pools_set]

        # Build list of ip addresses found in fabric switches
        ip_addresses = [
            ip_network(fabric_switch["vtep_loopback_ip_address"], strict=False)
            for fabric_switch in self.fabric_switches
            if fabric_switch["vtep_loopback_ip_address"] is not None
        ]
        return self.render_pools_as_list(pools, ip_addresses)

    def render_pools_as_list(self, pools: list[ip_network], addresses: list[ip_network]) -> list:
        """Helper function to build IP pool data for a list of pools."""
        return natural_sort([self.get_pool_data(pool, addresses) for pool in pools], sort_key="pool")

    def get_pool_data(self, pool: IPv4Network | IPv6Network, addresses: list[IPv4Network | IPv6Network]) -> dict:
        """Helper function to build IP pool data for one IP pool."""
        size = self.get_pool_size(pool)
        used = self.count_addresses_in_pool(pool, addresses)
        # rounding up on 100 * percent and then divide by 100 to give 11.22% rounded up on last decimal.
        return {"pool": pool, "size": size, "used": used, "used_percent": (ceil((100 * used / size) * 100) / 100)}

    def get_pool_size(self, pool: IPv4Network | IPv6Network) -> int:
        """
        Helper function returning the size of one IP pool.

        Ignores hosts, broadcast etc since this is a pool of subnets, not one subnet.
        """
        max_prefixlen = 128 if pool.version == 6 else 32
        return 2 ** (max_prefixlen - pool.prefixlen)

    def count_addresses_in_pool(self, pool: IPv4Network | IPv6Network, addresses: list[IPv4Network | IPv6Network]) -> int:
        """Helper function to count the number of addresses that fall within the given IP pool."""
        return len([True for address in addresses if address.subnet_of(pool)])

    @cached_property
    def all_connected_endpoints(self) -> dict[str, list]:
        """
        Returning list of connected_endpoints from all devices.

        First generate a dict of lists keyed with connected endpoint key.
        Then return a natural sorted dict where the inner lists are natural sorted on peer.
        """
        if not self._include_connected_endpoints:
            return {}

        all_connected_endpoints = {}
        for hostname, structured_config in self.structured_configs.items():
            connected_endpoints_keys = get(self.avd_switch_facts[hostname], "connected_endpoints_keys", default=[])
            connected_endpoints_by_type = {item["type"]: item for item in connected_endpoints_keys}
            port_channel_interfaces = get(structured_config, "port_channel_interfaces", default=[])
            for ethernet_interface in get(structured_config, "ethernet_interfaces", default=[]):
                if (peer_type := get(ethernet_interface, "peer_type")) not in connected_endpoints_by_type:
                    continue

                if (channel_group := get(ethernet_interface, "channel_group.id")) is not None:
                    # Port channel member
                    port_channel_interface = get_item(port_channel_interfaces, "name", f"Port-Channel{channel_group}")
                else:
                    port_channel_interface = {}

                all_connected_endpoints.setdefault(connected_endpoints_by_type[peer_type]["key"], []).append(
                    {
                        "peer": get(ethernet_interface, "peer", default="-"),
                        "peer_type": peer_type,
                        "peer_interface": get(ethernet_interface, "peer_interface", default="-"),
                        "fabric_switch": hostname,
                        "fabric_port": ethernet_interface["name"],
                        "description": get(ethernet_interface, "description", default="-"),
                        "shutdown": default(get(ethernet_interface, "shutdown"), get(port_channel_interface, "shutdown"), "-"),
                        "mode": default(get(ethernet_interface, "switchport.mode"), get(port_channel_interface, "switchport.mode"), "-"),
                        "access_vlan": default(get(ethernet_interface, "switchport.access_vlan"), get(port_channel_interface, "switchport.access_vlan"), "-"),
                        "trunk_allowed_vlan": default(
                            get(ethernet_interface, "switchport.trunk.allowed_vlan"), get(port_channel_interface, "switchport.trunk.allowed_vlan"), "-"
                        ),
                        "profile": default(get(ethernet_interface, "port_profile"), "-"),
                    }
                )

        return {key: natural_sort(all_connected_endpoints[key], sort_key="peer") for key in natural_sort(all_connected_endpoints)}

    @cached_property
    def all_connected_endpoints_keys(self) -> list[dict]:
        """
        Returning list of unique connected_endpoints_keys from all devices.

        First generating a set of tuples and then returning as a natural sorted list of dicts.
        """
        if not self._include_connected_endpoints:
            return []

        set_of_tuples = {
            (item["key"], item["type"], item.get("description"))
            for switch in self.avd_switch_facts.values()
            for item in get(switch, "connected_endpoints_keys", default=[])
        }
        return natural_sort(
            [
                {
                    "key": key,
                    "type": item_type,
                    "description": description,
                }
                for key, item_type, description in set_of_tuples
            ],
            sort_key="key",
        )

    @cached_property
    def all_port_profiles(self) -> list[dict]:
        """
        Returning list of unique port-profiles from all devices.

        First generating a set of tuples and then returning as a natural sorted list of dicts.
        """
        if not self._include_connected_endpoints:
            return []

        set_of_tuples = {
            (item["profile"], item.get("parent_profile")) for switch in self.avd_switch_facts.values() for item in get(switch, "port_profile_names", default=[])
        }
        return natural_sort(
            [
                {
                    "profile": profile,
                    "parent_profile": parent_profile,
                }
                for profile, parent_profile in set_of_tuples
            ],
            sort_key="profile",
        )

    def get_physical_links(self) -> list[tuple]:
        """
        Returning list of physical links from all devices used for topology CSV.

        Return a list naturally sorted on hostname and sub-sorted on interface name.
        """
        return [
            (
                self.avd_switch_facts[hostname]["type"],
                hostname,
                ethernet_interface["name"],
                get(ethernet_interface, "peer_type", default=""),
                get(ethernet_interface, "peer", default=""),
                get(ethernet_interface, "peer_interface", default=""),
                not get(ethernet_interface, "shutdown", default=False),
            )
            for hostname in natural_sort(self.structured_configs)
            for ethernet_interface in natural_sort(get(self.structured_configs[hostname], "ethernet_interfaces"), sort_key="name")
        ]
