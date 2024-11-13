# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from pyavd._eos_designs.avdfacts import AvdFacts
from pyavd._utils import get

CUSTOM_STRUCTURED_CONFIGURATION_EXEMPT_KEYS = ["custom_structured_configuration_prefix", "custom_structured_configuration_list_merge"]


class AvdStructuredConfigCustomStructuredConfiguration(AvdFacts):
    """
    The AvdStructuredConfig Class is imported by "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.

    The Class uses AvdFacts, as the base class, to inherit _hostvars other attributes.
    """

    @cached_property
    def _router_bgp(self) -> dict | None:
        return get(self._hostvars, "router_bgp")

    def _extract_and_apply_struct_cfg_from_list_of_dicts(self, list_of_dicts: list, primary_key: str) -> list:
        if not list_of_dicts:
            return []

        struct_cfgs = []
        for item in list_of_dicts:
            if "struct_cfg" not in item:
                continue

            struct_cfg = item.pop("struct_cfg")
            struct_cfgs.append({primary_key: item[primary_key], **struct_cfg})

        return struct_cfgs

    def _struct_cfg(self) -> list:
        if struct_cfg := self.shared_utils.node_config.structured_config._as_dict():
            return [struct_cfg]

        return []

    def _struct_cfgs(self) -> list:
        if (struct_cfgs := self._hostvars.pop("struct_cfgs", None)) is not None:
            return struct_cfgs

        return []

    def _ethernet_interfaces(self) -> list:
        if (struct_cfgs := self._extract_and_apply_struct_cfg_from_list_of_dicts(self._hostvars.get("ethernet_interfaces"), "name")) == []:
            return []

        return [{"ethernet_interfaces": struct_cfgs}]

    def _port_channel_interfaces(self) -> list:
        if (struct_cfgs := self._extract_and_apply_struct_cfg_from_list_of_dicts(self._hostvars.get("port_channel_interfaces"), "name")) == []:
            return []

        return [{"port_channel_interfaces": struct_cfgs}]

    def _vlan_interfaces(self) -> list:
        if (struct_cfgs := self._extract_and_apply_struct_cfg_from_list_of_dicts(self._hostvars.get("vlan_interfaces"), "name")) == []:
            return []

        return [{"vlan_interfaces": struct_cfgs}]

    def _router_bgp_peer_groups(self) -> list:
        if self._router_bgp is None:
            return []

        if (struct_cfgs := self._extract_and_apply_struct_cfg_from_list_of_dicts(self._router_bgp.get("peer_groups"), "name")) == []:
            return []

        return [
            {
                "router_bgp": {
                    "peer_groups": struct_cfgs,
                },
            },
        ]

    def _router_bgp_vrfs(self) -> list:
        if self._router_bgp is None:
            return []

        if (struct_cfgs := self._extract_and_apply_struct_cfg_from_list_of_dicts(self._router_bgp.get("vrfs"), "name")) == []:
            return []

        return [
            {
                "router_bgp": {
                    "vrfs": struct_cfgs,
                },
            },
        ]

    def _router_bgp_vlans(self) -> list:
        if self._router_bgp is None:
            return []

        if (struct_cfgs := self._extract_and_apply_struct_cfg_from_list_of_dicts(self._router_bgp.get("vlans"), "id")) == []:
            return []

        return [
            {
                "router_bgp": {
                    "vlans": struct_cfgs,
                },
            },
        ]

    def _custom_structured_configurations(self) -> list[dict]:
        return [custom_structured_configuration.value._as_dict() for custom_structured_configuration in self.inputs._custom_structured_configurations]

    def render(self) -> list[dict]:
        """
        Custom Structured Configuration can contain any key, so we cannot use the regular render method.

        This method returns a list of dicts with structured_configuration.

        get_structured_config will merge this list into a single dict.
        """
        struct_cfgs = self._struct_cfg()
        struct_cfgs.extend(self._struct_cfgs())
        struct_cfgs.extend(self._ethernet_interfaces())
        struct_cfgs.extend(self._port_channel_interfaces())
        struct_cfgs.extend(self._vlan_interfaces())
        struct_cfgs.extend(self._router_bgp_peer_groups())
        struct_cfgs.extend(self._router_bgp_vrfs())
        struct_cfgs.extend(self._router_bgp_vlans())
        struct_cfgs.extend(self._custom_structured_configurations())

        return struct_cfgs
