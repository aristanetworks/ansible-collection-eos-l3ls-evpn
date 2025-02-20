# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Literal

from yaml import CSafeDumper

from .node_id_pools import NodeIdPoolCollection

if TYPE_CHECKING:
    from pathlib import Path

    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol

    from .base_classes import Pool, PoolCollection

PoolType = Literal["node_id_pools"]


class PoolManager:
    """
    Class used to handle pooled resources.

    This class is imported and initialized once in eos_designs_facts
    and given to shared_utils for each device.
    """

    _pool_collection_types: ClassVar = {"node_id_pools": NodeIdPoolCollection}
    _output_dir: Path
    _pool_collections: dict[PoolType, dict[Path, PoolCollection]]
    """PoolCollection collections keys by file path."""

    def __init__(self, output_dir: Path) -> None:
        self._output_dir = output_dir
        self._pool_collections = {}
        self._changed_pool_files = {}

    def save_updated_pools(self, dumper_cls: type = CSafeDumper) -> bool:
        """
        Save data if anything changed. Returns a boolean telling if anything was changed.

        Note that this will also prune any unused/stale allocations (not requested for since initialization) and remove empty pools.
        """
        any_changes = False
        for pools_files_map in self._pool_collections.values():
            changes_for_this_pool_type = [pool_collection.save_updates(dumper_cls) for pool_collection in pools_files_map.values()]
            any_changes = any_changes or any(changes_for_this_pool_type)
        return any_changes

    def get_pool(self, pool_type: PoolType, shared_utils: SharedUtilsProtocol) -> Pool:
        """Returns the pool of the given type for this device. Pool will be autocreated if missing."""
        if pool_type not in self._pool_collection_types:
            msg = f"Invalid pool type '{pool_type}'. Expected one of {', '.join(self._pool_collection_types.keys())}"
            raise ValueError(msg)

        pools_files_map = self._pool_collections.setdefault(pool_type, {})
        pools_cls = self._pool_collection_types[pool_type]
        pools_file = pools_cls._pools_file_from_shared_utils(self._output_dir, shared_utils)

        if pools_file not in pools_files_map:
            # Not using setdefault since initializing the pool will read from file.
            pools_files_map[pools_file] = pools_cls(pools_file=pools_file)
        pool_collection = pools_files_map[pools_file]

        pool_key = pools_cls._pool_key_from_shared_utils(shared_utils)
        return pool_collection.get_pool(pool_key)

    def get_assignment(self, pool_type: PoolType, shared_utils: SharedUtilsProtocol, requested_value: int | str | None = None) -> int:
        """
        Returns the assignment value for this device for the given pool type. Assignment and pool will be autocreated if missing.

        Args:
            pool_type: Currently only supports "node_id_pools".
            shared_utils: Instance of SharedUtils for the device.
            requested_value: A requested value to assign to the device if available. Existing assignment will be changed if possible.
                There are no guarantees that this value will be assigned, so the caller should check and handle accordingly.
        """
        pool = self.get_pool(pool_type, shared_utils)
        key = self._pool_collection_types[pool_type]._assignment_key_from_shared_utils(shared_utils)
        return pool.get_assignment(key, requested_value).value
