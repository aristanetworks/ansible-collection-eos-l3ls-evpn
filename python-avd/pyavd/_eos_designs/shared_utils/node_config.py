# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from . import SharedUtils


class NodeConfigMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def node_type_config(
        self: SharedUtils,
    ) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes:
        node_type_key = self.node_type_key_data.key

        if node_type_key in self.inputs._dynamic_keys.custom_node_types:
            return self.inputs._dynamic_keys.custom_node_types[node_type_key].value._cast_as(EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes)

        if node_type_key in self.inputs._dynamic_keys.node_types:
            return self.inputs._dynamic_keys.node_types[node_type_key].value

        msg = f"'type' is set to '{self.type}', for which node configs should use the key '{node_type_key}'. '{node_type_key}' was not found."
        raise AristaAvdInvalidInputsError(msg)

    @cached_property
    def node_group_config(
        self: SharedUtils,
    ) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodeGroupsItem:
        for node_group in self.node_type_config.node_groups:
            if self.hostname in node_group.nodes:
                return node_group

        return EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodeGroupsItem()

    @cached_property
    def node_config(
        self: SharedUtils,
    ) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem:
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
            if self.hostname in self.node_group_config.nodes:
                node_config._deepinherit(
                    self.node_group_config.nodes[self.hostname]._cast_as(
                        EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True
                    )
                )
            node_config._deepinherit(self.node_group_config._cast_as(EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True))

        node_config._deepinherit(
            self.node_type_config.defaults._cast_as(EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True)
        )

        return node_config
