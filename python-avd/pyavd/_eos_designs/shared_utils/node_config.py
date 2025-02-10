# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from . import SharedUtilsProtocol


class NodeConfigMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def node_type_config(self: SharedUtilsProtocol) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes:
        """
        The object representing the `<node_type_key like l3leaf, spine etc>:` containing the `defaults`, `nodes`, `node_groups` etc.

        The relevant dynamic key is found in self.inputs._dynamic_keys which is populated by the _from_dict() loader on the EosDesigns class.
        """
        node_type_key = self.node_type_key_data.key

        if node_type_key in self.inputs._dynamic_keys.custom_node_types:
            return self.inputs._dynamic_keys.custom_node_types[node_type_key].value._cast_as(EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes)

        if node_type_key in self.inputs._dynamic_keys.node_types:
            return self.inputs._dynamic_keys.node_types[node_type_key].value

        msg = f"'type' is set to '{self.type}', for which node configs should use the key '{node_type_key}'. '{node_type_key}' was not found."
        raise AristaAvdInvalidInputsError(msg)

    @cached_property
    def node_group_config(self: SharedUtilsProtocol) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodeGroupsItem | None:
        """
        The object representing the `<node_type_key like l3leaf, spine etc>.node_groups[]` where this node is found.

        Used by MLAG and WAN HA logic to find out who our MLAG / WAN HA peer is.
        """
        for node_group in self.node_type_config.node_groups:
            if self.hostname in node_group.nodes:
                return node_group

        return None

    @cached_property
    def node_config(self: SharedUtilsProtocol) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem:
        """
        NodesItem object containing the fully inherited node config.

        Vars are inherited like:
        <node_type_key>.defaults ->
            <node_type_key>.node_groups.[<node_group>] ->
                <node_type_key>.node_groups.[<node_group>].nodes.[<node>] ->
                    <node_type_key>.nodes.[<node>]
        """
        node_config = (
            self.node_type_config.nodes[self.hostname]
            if self.hostname in self.node_type_config.nodes
            else EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem()
        )

        if self.node_group_config is not None:
            node_config._deepinherit(
                self.node_group_config.nodes[self.hostname]._cast_as(EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True)
            )
            node_config._deepinherit(self.node_group_config._cast_as(EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True))

        node_config._deepinherit(
            self.node_type_config.defaults._cast_as(EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True)
        )

        return node_config

    @cached_property
    def node_group_is_primary_and_peer_hostname(self: SharedUtilsProtocol) -> tuple[bool, str] | None:
        """
        Node group position and peer used for MLAG and WAN HA.

        Returns None if the device is not in a node_group with exactly two devices.
        Returns True, <peer> if this device is the first one in the node_group.
        Returns False, <peer> if this device is the second one in the node_group.
        """
        if self.node_group_config is None or len(self.node_group_config.nodes) != 2:
            return None

        nodes = list(self.node_group_config.nodes.keys())
        index = nodes.index(self.hostname)
        peer_index = not index  # (0->1 and 1>0)
        return index == 0, nodes[peer_index]
