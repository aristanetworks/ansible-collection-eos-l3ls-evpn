# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from functools import cached_property
from typing import TYPE_CHECKING, Any

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import default, get
from pyavd.j2filters import natural_sort, range_expand

if TYPE_CHECKING:
    from pyavd._eos_designs.eos_designs_facts import EosDesignsFacts

    from . import SharedUtils


class MiscMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def all_fabric_devices(self: SharedUtils) -> list[str]:
        avd_switch_facts: dict = get(self.hostvars, "avd_switch_facts", required=True)
        return list(avd_switch_facts.keys())

    @cached_property
    def hostname(self: SharedUtils) -> str:
        """Hostname set based on inventory_hostname variable."""
        return get(self.hostvars, "inventory_hostname", required=True)

    @cached_property
    def is_deployed(self: SharedUtils) -> bool:
        return get(self.hostvars, "is_deployed", default=True)

    @cached_property
    def id(self: SharedUtils) -> int | None:
        return get(self.switch_data_combined, "id")

    @cached_property
    def trunk_groups(self: SharedUtils) -> dict:
        return {
            "mlag": {"name": get(self.hostvars, "trunk_groups.mlag.name", default="MLAG")},
            "mlag_l3": {"name": get(self.hostvars, "trunk_groups.mlag_l3.name", default="MLAG")},
            "uplink": {"name": get(self.hostvars, "trunk_groups.uplink.name", default="UPLINK")},
        }

    @cached_property
    def enable_trunk_groups(self: SharedUtils) -> bool:
        return get(self.hostvars, "enable_trunk_groups", default=False)

    @cached_property
    def filter_only_vlans_in_use(self: SharedUtils) -> bool:
        return get(self.switch_data_combined, "filter.only_vlans_in_use", default=False)

    @cached_property
    def filter_tags(self: SharedUtils) -> list:
        """Return filter.tags + group if defined."""
        filter_tags = get(self.switch_data_combined, "filter.tags", default=["all"])
        if self.group is not None:
            filter_tags.append(self.group)
        return filter_tags

    @cached_property
    def filter_allow_vrfs(self: SharedUtils) -> list:
        return get(self.switch_data_combined, "filter.allow_vrfs", default=["all"])

    @cached_property
    def filter_deny_vrfs(self: SharedUtils) -> list:
        return get(self.switch_data_combined, "filter.deny_vrfs", default=[])

    @cached_property
    def filter_tenants(self: SharedUtils) -> list:
        return get(self.switch_data_combined, "filter.tenants", default=["all"])

    @cached_property
    def always_include_vrfs_in_tenants(self: SharedUtils) -> list:
        return get(self.switch_data_combined, "filter.always_include_vrfs_in_tenants", default=[])

    @cached_property
    def igmp_snooping_enabled(self: SharedUtils) -> bool:
        default_igmp_snooping_enabled = get(self.hostvars, "default_igmp_snooping_enabled", default=True)
        return get(self.switch_data_combined, "igmp_snooping_enabled", default=default_igmp_snooping_enabled) is True

    @cached_property
    def only_local_vlan_trunk_groups(self: SharedUtils) -> bool:
        return self.enable_trunk_groups and get(self.hostvars, "only_local_vlan_trunk_groups", default=False)

    @cached_property
    def system_mac_address(self: SharedUtils) -> str | None:
        """
        system_mac_address.

        system_mac_address is inherited from
        Fabric Topology data model system_mac_address ->
            Host variable var system_mac_address ->.
        """
        return default(get(self.switch_data_combined, "system_mac_address"), get(self.hostvars, "system_mac_address"))

    @cached_property
    def uplink_switches(self: SharedUtils) -> list:
        return default(
            get(self.switch_data_combined, "uplink_switches"),
            get(self.cv_topology_config, "uplink_switches"),
            [],
        )

    @cached_property
    def uplink_interfaces(self: SharedUtils) -> list:
        return range_expand(
            default(
                get(self.switch_data_combined, "uplink_interfaces"),
                get(self.cv_topology_config, "uplink_interfaces"),
                get(self.default_interfaces, "uplink_interfaces"),
                [],
            ),
        )

    @cached_property
    def uplink_switch_interfaces(self: SharedUtils) -> list:
        uplink_switch_interfaces = default(
            get(self.switch_data_combined, "uplink_switch_interfaces"),
            get(self.cv_topology_config, "uplink_switch_interfaces"),
        )
        if uplink_switch_interfaces is not None:
            return range_expand(uplink_switch_interfaces)

        if not self.uplink_switches:
            return []

        if self.id is None:
            msg = f"'id' is not set on '{self.hostname}'"
            raise AristaAvdInvalidInputsError(msg)

        uplink_switch_interfaces = []
        uplink_switch_counter = {}
        for uplink_switch in self.uplink_switches:
            uplink_switch_facts: EosDesignsFacts = self.get_peer_facts(uplink_switch, required=True)

            # Count the number of instances the current switch was processed
            uplink_switch_counter[uplink_switch] = uplink_switch_counter.get(uplink_switch, 0) + 1
            index_of_parallel_uplinks = uplink_switch_counter[uplink_switch] - 1

            # Add uplink_switch_interface based on this switch's ID (-1 for 0-based) * max_parallel_uplinks + index_of_parallel_uplinks.
            # For max_parallel_uplinks: 2 this would assign downlink interfaces like this:
            # spine1 downlink-interface mapping: [ leaf-id1, leaf-id1, leaf-id2, leaf-id2, leaf-id3, leaf-id3, ... ]
            downlink_index = (self.id - 1) * self.max_parallel_uplinks + index_of_parallel_uplinks
            if len(uplink_switch_facts._default_downlink_interfaces) > downlink_index:
                uplink_switch_interfaces.append(uplink_switch_facts._default_downlink_interfaces[downlink_index])
            else:
                msg = (
                    f"'uplink_switch_interfaces' is not set on '{self.hostname}' and 'uplink_switch' '{uplink_switch}' "
                    f"does not have 'downlink_interfaces[{downlink_index}]' set under 'default_interfaces'"
                )
                raise AristaAvdError(
                    msg,
                )

        return uplink_switch_interfaces

    @cached_property
    def virtual_router_mac_address(self: SharedUtils) -> str | None:
        return get(self.switch_data_combined, "virtual_router_mac_address")

    @cached_property
    def serial_number(self: SharedUtils) -> str | None:
        """
        serial_number.

        serial_number is inherited from
        Fabric Topology data model serial_number ->
            Host variable var serial_number.
        """
        return default(get(self.switch_data_combined, "serial_number"), get(self.hostvars, "serial_number"))

    @cached_property
    def max_parallel_uplinks(self: SharedUtils) -> int:
        """Exposed in avd_switch_facts."""
        return get(self.switch_data_combined, "max_parallel_uplinks", default=1)

    @cached_property
    def max_uplink_switches(self: SharedUtils) -> int:
        """max_uplink_switches will default to the length of uplink_switches."""
        return get(self.switch_data_combined, "max_uplink_switches", default=len(self.uplink_switches))

    @cached_property
    def p2p_uplinks_mtu(self: SharedUtils) -> int | None:
        if not self.platform_settings_feature_support_per_interface_mtu:
            return None
        p2p_uplinks_mtu = default(self.platform_settings_p2p_uplinks_mtu, get(self.hostvars, "p2p_uplinks_mtu", default=9214))
        return get(self.switch_data_combined, "uplink_mtu", default=p2p_uplinks_mtu)

    @cached_property
    def evpn_short_esi_prefix(self: SharedUtils) -> str:
        return get(self.hostvars, "evpn_short_esi_prefix", default="0000:0000:")

    @cached_property
    def shutdown_interfaces_towards_undeployed_peers(self: SharedUtils) -> bool:
        return get(self.hostvars, "shutdown_interfaces_towards_undeployed_peers", default=True) is True

    @cached_property
    def shutdown_bgp_towards_undeployed_peers(self: SharedUtils) -> bool:
        return get(self.hostvars, "shutdown_bgp_towards_undeployed_peers", default=True) is True

    @cached_property
    def bfd_multihop(self: SharedUtils) -> dict:
        default_bfd_multihop = {
            "interval": 300,
            "min_rx": 300,
            "multiplier": 3,
        }
        return get(self.hostvars, "bfd_multihop", default=default_bfd_multihop)

    @cached_property
    def evpn_ebgp_multihop(self: SharedUtils) -> int:
        return get(self.hostvars, "evpn_ebgp_multihop", default=3)

    @cached_property
    def evpn_ebgp_gateway_multihop(self: SharedUtils) -> int:
        return get(self.hostvars, "evpn_ebgp_gateway_multihop", default=15)

    @cached_property
    def evpn_overlay_bgp_rtc(self: SharedUtils) -> bool:
        return get(self.hostvars, "evpn_overlay_bgp_rtc") is True

    @cached_property
    def evpn_prevent_readvertise_to_server(self: SharedUtils) -> bool:
        return get(self.hostvars, "evpn_prevent_readvertise_to_server") is True

    @cached_property
    def dc_name(self: SharedUtils) -> str | None:
        return get(self.hostvars, "dc_name")

    @cached_property
    def fabric_name(self: SharedUtils) -> str:
        return get(self.hostvars, "fabric_name", required=True)

    @cached_property
    def rack(self: SharedUtils) -> str | None:
        return get(self.switch_data_combined, "rack")

    @cached_property
    def network_services_keys(self: SharedUtils) -> list[dict]:
        """
        Return sorted network_services_keys filtered for invalid entries and unused keys.

        NOTE: This method is called _before_ any schema validation, since we need to resolve network_services_keys dynamically
        """
        # Reading default value from schema
        default_network_services_keys = self.schema.get_default_value(["network_services_keys"])
        network_services_keys = get(self.hostvars, "network_services_keys", default=default_network_services_keys)
        network_services_keys = [entry for entry in network_services_keys if entry.get("name") is not None and self.hostvars.get(entry["name"]) is not None]
        return natural_sort(network_services_keys, "name")

    @cached_property
    def port_profiles(self: SharedUtils) -> list:
        return get(self.hostvars, "port_profiles", default=[])

    @cached_property
    def uplink_interface_speed(self: SharedUtils) -> str | None:
        return get(self.switch_data_combined, "uplink_interface_speed")

    @cached_property
    def uplink_switch_interface_speed(self: SharedUtils) -> str | None:
        return get(self.switch_data_combined, "uplink_switch_interface_speed")

    @cached_property
    def uplink_bfd(self: SharedUtils) -> bool:
        return get(self.switch_data_combined, "uplink_bfd") is True

    @cached_property
    def uplink_ptp(self: SharedUtils) -> dict | None:
        return get(self.switch_data_combined, "uplink_ptp")

    @cached_property
    def uplink_macsec(self: SharedUtils) -> dict | None:
        return get(self.switch_data_combined, "uplink_macsec")

    @cached_property
    def uplink_structured_config(self: SharedUtils) -> dict | None:
        return get(self.switch_data_combined, "uplink_structured_config")

    @cached_property
    def p2p_uplinks_qos_profile(self: SharedUtils) -> str | None:
        return get(self.hostvars, "p2p_uplinks_qos_profile")

    @cached_property
    def isis_default_metric(self: SharedUtils) -> int:
        return get(self.hostvars, "isis_default_metric", default=50)

    @cached_property
    def isis_default_circuit_type(self: SharedUtils) -> str | None:
        return get(self.hostvars, "isis_default_circuit_type", default="level-2")

    @cached_property
    def pod_name(self: SharedUtils) -> str | None:
        return get(self.hostvars, "pod_name")

    @cached_property
    def fabric_ip_addressing_mlag_algorithm(self: SharedUtils) -> str:
        """
        This method fetches the MLAG algorithm value from host variables.

        It defaults to 'first_id' if the variable is not defined.
        """
        return get(self.hostvars, "fabric_ip_addressing.mlag.algorithm", default="first_id")

    @cached_property
    def fabric_ip_addressing_mlag_ipv4_prefix_length(self: SharedUtils) -> int:
        return get(self.hostvars, "fabric_ip_addressing.mlag.ipv4_prefix_length", default=31)

    @cached_property
    def fabric_ip_addressing_mlag_ipv6_prefix_length(self: SharedUtils) -> int:
        return get(self.hostvars, "fabric_ip_addressing.mlag.ipv6_prefix_length", default=64)

    @cached_property
    def fabric_ip_addressing_p2p_uplinks_ipv4_prefix_length(self: SharedUtils) -> int:
        return get(self.hostvars, "fabric_ip_addressing.p2p_uplinks.ipv4_prefix_length", default=31)

    @cached_property
    def fabric_ip_addressing_wan_ha_ipv4_prefix_length(self: SharedUtils) -> int:
        return get(self.hostvars, "fabric_ip_addressing.wan_ha.ipv4_prefix_length", default=31)

    @cached_property
    def fabric_sflow_uplinks(self: SharedUtils) -> bool | None:
        return get(self.hostvars, "fabric_sflow.uplinks")

    @cached_property
    def fabric_sflow_downlinks(self: SharedUtils) -> bool | None:
        return get(self.hostvars, "fabric_sflow.downlinks")

    @cached_property
    def fabric_sflow_endpoints(self: SharedUtils) -> bool | None:
        return get(self.hostvars, "fabric_sflow.endpoints")

    @cached_property
    def fabric_sflow_mlag_interfaces(self: SharedUtils) -> bool | None:
        return get(self.hostvars, "fabric_sflow.mlag_interfaces")

    @cached_property
    def fabric_sflow_l3_interfaces(self: SharedUtils) -> bool | None:
        return get(self.hostvars, "fabric_sflow.l3_interfaces")

    @cached_property
    def default_interface_mtu(self: SharedUtils) -> int | None:
        default_default_interface_mtu = get(self.hostvars, "default_interface_mtu")
        return get(self.platform_settings, "default_interface_mtu", default=default_default_interface_mtu)

    def get_switch_fact(self: SharedUtils, key: str, required: bool = True) -> Any:
        """
        Return facts from EosDesignsFacts.

        We need to go via avd_switch_facts since PyAVD does not expose "switch.*" in get_avdfacts.
        """
        return get(self.hostvars, f"avd_switch_facts..{self.hostname}..switch..{key}", required=required, org_key=f"switch.{key}", separator="..")

    @cached_property
    def evpn_multicast(self: SharedUtils) -> bool:
        return self.get_switch_fact("evpn_multicast", required=False) is True

    @cached_property
    def ipv4_acls(self: SharedUtils) -> dict:
        return {acl["name"]: acl for acl in get(self.hostvars, "ipv4_acls", default=[])}

    def get_ipv4_acl(self: SharedUtils, name: str, interface_name: str, *, interface_ip: str | None = None, peer_ip: str | None = None) -> dict:
        """
        Get one IPv4 ACL from "ipv4_acls" where fields have been substituted.

        If any substitution is done, the ACL name will get "_<interface_name>" appended.
        """
        org_ipv4_acl = get(self.ipv4_acls, name, required=True, org_key=f"ipv4_acls[name={name}]")
        # deepcopy to avoid inplace updates below from modifying the original.
        ipv4_acl = deepcopy(org_ipv4_acl)
        ip_replacements = {
            "interface_ip": interface_ip,
            "peer_ip": peer_ip,
        }
        for index, entry in enumerate(get(ipv4_acl, "entries", default=[])):
            if entry.get("remark") is not None:
                continue

            err_context = f"ipv4_acls[name={name}].entries[{index}]"
            source_field = get(entry, "source", required=True, org_key=f"{err_context}.source")
            destination_field = get(entry, "destination", required=True, org_key=f"{err_context}.destination")
            entry["source"] = self._get_ipv4_acl_field_with_substitution(source_field, ip_replacements, f"{err_context}.source", interface_name)
            entry["destination"] = self._get_ipv4_acl_field_with_substitution(destination_field, ip_replacements, f"{err_context}.destination", interface_name)

        if ipv4_acl != org_ipv4_acl:
            ipv4_acl["name"] += f"_{self.sanitize_interface_name(interface_name)}"
        return ipv4_acl

    @staticmethod
    def _get_ipv4_acl_field_with_substitution(field_value: str, replacements: dict[str, str], field_context: str, interface_name: str) -> str:
        """
        Checks one field if the value can be substituted.

        The given "replacements" dict will be parsed as:
          key: substitution field to look for
          value: replacement value to set.

        If a replacement is done, but the value is None, an error will be raised.
        """
        for key, value in replacements.items():
            if field_value != key:
                continue

            if value is None:
                msg = (
                    f"Unable to perform substitution of the value '{key}' defined under '{field_context}', "
                    f"since no substitution value was found for interface '{interface_name}'. "
                    "Make sure to set the appropriate fields on the interface."
                )
                raise AristaAvdError(
                    msg,
                )

            return value

        return field_value

    @cached_property
    def ipv4_prefix_list_catalog(self: SharedUtils) -> list:
        return get(self.hostvars, "ipv4_prefix_list_catalog", default=[])

    @cached_property
    def use_router_general_for_router_id(self: SharedUtils) -> bool:
        return bool(get(self.hostvars, "use_router_general_for_router_id"))
