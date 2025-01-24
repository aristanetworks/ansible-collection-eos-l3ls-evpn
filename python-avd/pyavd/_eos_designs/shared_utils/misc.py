# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils import default, get
from pyavd.j2filters import range_expand

from .utils import UtilsMixin

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns


class MiscMixin(UtilsMixin):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def all_fabric_devices(self) -> list[str]:
        avd_switch_facts: dict = get(self.shared_utils._hostvars, "avd_switch_facts", required=True)
        return list(avd_switch_facts.keys())

    @cached_property
    def hostname(self) -> str:
        """Hostname set based on inventory_hostname variable. TODO: Get a proper attribute on the class instead of gleaning from the regular inputs."""
        return get(self.shared_utils._hostvars, "inventory_hostname", required=True)

    @cached_property
    def id(self) -> int | None:
        return self.shared_utils.node_config.id

    @cached_property
    def filter_tags(self) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.Filter.Tags:
        """Return filter.tags + group if defined."""
        filter_tags = self.shared_utils.node_config.filter.tags
        if self.shared_utils.group is not None:
            filter_tags.append(self.shared_utils.group)
        return filter_tags

    @cached_property
    def igmp_snooping_enabled(self) -> bool:
        return default(self.shared_utils.node_config.igmp_snooping_enabled, self.inputs.default_igmp_snooping_enabled)

    @cached_property
    def only_local_vlan_trunk_groups(self) -> bool:
        return self.inputs.enable_trunk_groups and self.inputs.only_local_vlan_trunk_groups

    @cached_property
    def system_mac_address(self) -> str | None:
        """
        system_mac_address.

        system_mac_address is inherited from
        Fabric Topology data model system_mac_address ->
            Host variable var system_mac_address ->.
        """
        return default(self.shared_utils.node_config.system_mac_address, self.inputs.system_mac_address)

    @cached_property
    def uplink_switches(self) -> list[str]:
        return self.shared_utils.node_config.uplink_switches._as_list() or get(self.shared_utils.cv_topology_config, "uplink_switches") or []

    @cached_property
    def uplink_interfaces(self) -> list[str]:
        return range_expand(
            self.shared_utils.node_config.uplink_interfaces
            or get(self.shared_utils.cv_topology_config, "uplink_interfaces")
            or self.shared_utils.default_interfaces.uplink_interfaces,
        )

    @cached_property
    def uplink_switch_interfaces(self) -> list[str]:
        uplink_switch_interfaces = (
            self.shared_utils.node_config.uplink_switch_interfaces or get(self.shared_utils.cv_topology_config, "uplink_switch_interfaces") or []
        )
        if uplink_switch_interfaces:
            return range_expand(uplink_switch_interfaces)

        if not self.uplink_switches:
            return []

        if self.id is None:
            msg = f"'id' is not set on '{self.hostname}'"
            raise AristaAvdInvalidInputsError(msg)

        uplink_switch_interfaces = []
        uplink_switch_counter = {}
        for uplink_switch in self.uplink_switches:
            uplink_switch_facts = self.get_peer_facts_cls(uplink_switch)

            # Count the number of instances the current switch was processed
            uplink_switch_counter[uplink_switch] = uplink_switch_counter.get(uplink_switch, 0) + 1
            index_of_parallel_uplinks = uplink_switch_counter[uplink_switch] - 1

            # Add uplink_switch_interface based on this switch's ID (-1 for 0-based) * max_parallel_uplinks + index_of_parallel_uplinks.
            # For max_parallel_uplinks: 2 this would assign downlink interfaces like this:
            # spine1 downlink-interface mapping: [ leaf-id1, leaf-id1, leaf-id2, leaf-id2, leaf-id3, leaf-id3, ... ]
            downlink_index = (self.id - 1) * self.shared_utils.node_config.max_parallel_uplinks + index_of_parallel_uplinks
            if len(uplink_switch_facts._default_downlink_interfaces) > downlink_index:
                uplink_switch_interfaces.append(uplink_switch_facts._default_downlink_interfaces[downlink_index])
            else:
                msg = (
                    f"'uplink_switch_interfaces' is not set on '{self.hostname}' and 'uplink_switch' '{uplink_switch}' "
                    f"does not have 'downlink_interfaces[{downlink_index}]' set under 'default_interfaces'"
                )
                raise AristaAvdError(msg)

        return uplink_switch_interfaces

    @cached_property
    def serial_number(self) -> str | None:
        """
        serial_number.

        serial_number is inherited from
        Fabric Topology data model serial_number ->
            Host variable var serial_number.
        """
        return default(self.shared_utils.node_config.serial_number, self.inputs.serial_number)

    @cached_property
    def max_uplink_switches(self) -> int:
        """max_uplink_switches will default to the length of uplink_switches."""
        return default(self.shared_utils.node_config.max_uplink_switches, len(self.uplink_switches))

    @cached_property
    def p2p_uplinks_mtu(self) -> int | None:
        if not self.shared_utils.platform_settings.feature_support.per_interface_mtu:
            return None
        p2p_uplinks_mtu = default(self.shared_utils.platform_settings.p2p_uplinks_mtu, self.inputs.p2p_uplinks_mtu)
        return default(self.shared_utils.node_config.uplink_mtu, p2p_uplinks_mtu)

    @cached_property
    def fabric_name(self) -> str:
        if not self.inputs.fabric_name:
            msg = "fabric_name"
            raise AristaAvdMissingVariableError(msg)

        return self.inputs.fabric_name

    @cached_property
    def uplink_interface_speed(self) -> str | None:
        return default(self.shared_utils.node_config.uplink_interface_speed, self.shared_utils.default_interfaces.uplink_interface_speed)

    @cached_property
    def uplink_switch_interface_speed(self) -> str | None:
        # Keeping since we will need it when adding speed support under default interfaces.
        return self.shared_utils.node_config.uplink_switch_interface_speed

    @cached_property
    def default_interface_mtu(self) -> int | None:
        return default(self.shared_utils.platform_settings.default_interface_mtu, self.inputs.default_interface_mtu)

    @cached_property
    def evpn_multicast(self) -> bool:
        return self.get_switch_fact("evpn_multicast", required=False) is True

    def get_ipv4_acl(self, name: str, interface_name: str, *, interface_ip: str | None = None, peer_ip: str | None = None) -> EosDesigns.Ipv4AclsItem:
        """
        Get one IPv4 ACL from "ipv4_acls" where fields have been substituted.

        If any substitution is done, the ACL name will get "_<interface_name>" appended.
        """
        if name not in self.inputs.ipv4_acls:
            msg = f"ipv4_acls[name={name}]"
            raise AristaAvdMissingVariableError(msg)
        org_ipv4_acl = self.inputs.ipv4_acls[name]
        # deepcopy to avoid inplace updates below from modifying the original.
        ipv4_acl = org_ipv4_acl._deepcopy()
        ip_replacements = {
            "interface_ip": interface_ip,
            "peer_ip": peer_ip,
        }
        changed = False
        for index, entry in enumerate(ipv4_acl.entries):
            if entry._get("remark"):
                continue

            err_context = f"ipv4_acls[name={name}].entries[{index}]"
            if not entry.source:
                msg = f"{err_context}.source"
                raise AristaAvdMissingVariableError(msg)
            if not entry.destination:
                msg = f"{err_context}.destination"
                raise AristaAvdMissingVariableError(msg)

            entry.source = self._get_ipv4_acl_field_with_substitution(entry.source, ip_replacements, f"{err_context}.source", interface_name)
            entry.destination = self._get_ipv4_acl_field_with_substitution(entry.destination, ip_replacements, f"{err_context}.destination", interface_name)
            if entry.source != org_ipv4_acl.entries[index].source or entry.destination != org_ipv4_acl.entries[index].destination:
                changed = True

        if changed:
            ipv4_acl.name += f"_{self.sanitize_interface_name(interface_name)}"
        return ipv4_acl

    @staticmethod
    def _get_ipv4_acl_field_with_substitution(field_value: str, replacements: dict[str, str | None], field_context: str, interface_name: str) -> str:
        """
        Checks one field if the value can be substituted.

        The given "replacements" dict will be parsed as:
          key: substitution field to look for
          value: replacement value to set.

        If a replacement is done, but the value is None, an error will be raised.
        """
        if field_value not in replacements:
            return field_value

        if (replacement_value := replacements[field_value]) is None:
            msg = (
                f"Unable to perform substitution of the value '{field_value}' defined under '{field_context}', "
                f"since no substitution value was found for interface '{interface_name}'. "
                "Make sure to set the appropriate fields on the interface."
            )
            raise AristaAvdError(msg)

        return replacement_value
