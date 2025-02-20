# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

from pyavd._utils import default

from .base_classes import AssignmentKey, Pool, PoolAssignment, PoolCollection, PoolKey

if TYPE_CHECKING:
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol


@dataclass(frozen=True)
class NodeIdAssignmentKey(AssignmentKey):
    hostname: str


@dataclass(frozen=True)
class NodeIdPoolKey(PoolKey):
    fabric_name: str
    dc_name: str | None
    pod_name: str | None
    type: str


@dataclass()
class NodeIdPoolCollection(PoolCollection[NodeIdPoolKey, NodeIdAssignmentKey, int]):
    pools_key: str = "node_id_pools"
    pools: dict[PoolKey, Pool[NodeIdPoolKey, NodeIdAssignmentKey, int]] = field(default_factory=dict)
    pool_cls: type[Pool[NodeIdPoolKey, NodeIdAssignmentKey, int]] = Pool[NodeIdPoolKey, NodeIdAssignmentKey, int]
    pool_key_cls: type[NodeIdPoolKey] = NodeIdPoolKey
    assignment_cls: type[PoolAssignment[NodeIdAssignmentKey, int]] = PoolAssignment[NodeIdAssignmentKey, int]
    assignment_key_cls: type[NodeIdAssignmentKey] = NodeIdAssignmentKey
    value_type: type = int
    min_value: int = 1

    @staticmethod
    def _pool_key_from_shared_utils(shared_utils: SharedUtilsProtocol) -> NodeIdPoolKey:
        """Returns the pool key to use for this device."""
        return NodeIdPoolKey(
            fabric_name=shared_utils.fabric_name, dc_name=shared_utils.inputs.dc_name, pod_name=shared_utils.inputs.pod_name, type=shared_utils.type
        )

    @staticmethod
    def _pools_file_from_shared_utils(output_dir: Path, shared_utils: SharedUtilsProtocol) -> Path:
        """Returns the file to use for this device."""
        fabric_name = shared_utils.fabric_name
        default_id_file = output_dir.joinpath(f"data/{fabric_name}-ids.yml")
        return Path(default(shared_utils.inputs.fabric_numbering.node_id.pools_file, default_id_file))

    @staticmethod
    def _assignment_key_from_shared_utils(shared_utils: SharedUtilsProtocol) -> NodeIdAssignmentKey:
        """Returns the assignment key to use for this device."""
        return NodeIdAssignmentKey(hostname=shared_utils.hostname)
