# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from itertools import filterfalse
from typing import TYPE_CHECKING, Generic, TypeVar, cast

from yaml import CSafeDumper, CSafeLoader, dump, load

from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from pathlib import Path

    from typing_extensions import Self

    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol

T_ValueType = TypeVar("T_ValueType", int, str)
T_PoolKeyType = TypeVar("T_PoolKeyType", bound="PoolKey")
T_AssignmentKeyType = TypeVar("T_AssignmentKeyType", bound="AssignmentKey")

FILE_HEADER = """\
# This file is auto-generated by AVD eos_designs.
# When there is a merge conflict for this file, rebase the branch, accept all current changes for this file, and re-run AVD.
"""


@dataclass(frozen=True)
class PoolKey:
    """Base class for Pool Key classes. Kept separate from AssignmentKey base class to provide stronger type checking with the TypeVar T_PoolKeyType."""

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        return cls(**data)


@dataclass(frozen=True)
class AssignmentKey:
    """Base class for Assignment Key classes. Kept separate from PoolKey base class to provide stronger type checking with the TypeVar T_AssignmentKeyType."""

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        return cls(**data)


@dataclass
class PoolAssignment(Generic[T_AssignmentKeyType, T_ValueType]):
    key: T_AssignmentKeyType
    value: T_ValueType
    accessed: bool = False

    def as_dict(self) -> dict:
        return {"key": asdict(self.key), "value": self.value}


@dataclass
class Pool(Generic[T_PoolKeyType, T_AssignmentKeyType, T_ValueType]):
    """One Pool of resources indexed by T_PoolKeyType. Currently only supporting a pool of Integers."""

    collection: PoolCollection[T_PoolKeyType, T_AssignmentKeyType, T_ValueType]
    pool_key: T_PoolKeyType
    assignments: dict[T_AssignmentKeyType, PoolAssignment[T_AssignmentKeyType, T_ValueType]]

    def _is_value_available(self, value: T_ValueType) -> bool:
        if self.collection.value_type is int and isinstance(value, int):
            existing_ids = {assignment.value for assignment in self.assignments.values()}
            return not (
                value in existing_ids or value < self.collection.min_value or (self.collection.max_value is not None and value > self.collection.max_value)
            )

        # currently we only support int pools
        return False

    def _next_available(self) -> T_ValueType:
        if self.collection.value_type is int:
            collection = cast(PoolCollection[T_PoolKeyType, T_AssignmentKeyType, int], self.collection)
            assignments = cast(dict[T_AssignmentKeyType, PoolAssignment[T_AssignmentKeyType, int]], self.assignments)
            existing_ids = {assignment.value for assignment in assignments.values()}
            # Create a filterfalse generator from a range starting from the min_value, excluding the values that are already assigned.
            # Nothing will be iterated at this point, but the next(iter()) below will ask the generator for the first item.
            available_ids = filterfalse(existing_ids.__contains__, range(collection.min_value))
            next_available = next(iter(available_ids))
            if collection.max_value is not None and next_available > collection.max_value:
                msg = (
                    f"No available values found within '{self.collection.pools_key}' with key '{self.pool_key}' "
                    f"and range {collection.min_value}-{collection.max_value}."
                )
                raise ValueError(msg)
            return cast(T_ValueType, next_available)

        msg = f"Currently we only support pools of Integers. Got {self.collection.value_type}."
        raise NotImplementedError(msg)

    def get_assignment(self, key: T_AssignmentKeyType, requested_value: T_ValueType | None = None) -> PoolAssignment[T_AssignmentKeyType, T_ValueType]:
        """
        Returns the assignment for the key if found in the pool.

        Otherwise a new entry is inserted into the pool and returned.

        If 'requested_value' is given and available in the pool, any existing assignment will be updated and returned.
        For new assignments this value will be used.
        """
        if key not in self.assignments:
            # No existing assignment. Use the requested value if given and available. Otherwise use next available.
            new_assignment_value = requested_value if requested_value is not None and self._is_value_available(requested_value) else self._next_available()
            self.assignments[key] = self.collection.assignment_cls(key=key, value=new_assignment_value, accessed=True)
            self.collection.changed = True
        elif requested_value is not None and requested_value != self.assignments[key].value and self._is_value_available(requested_value):
            # Existing assignment but not with the requested value. Change the existing assignment to the requested_value.
            self.assignments[key] = self.collection.assignment_cls(key=key, value=requested_value, accessed=True)
            self.collection.changed = True
        else:
            # Existing item
            self.assignments[key].accessed = True

        return self.assignments[key]

    def _remove_stale_assignments(self) -> None:
        """
        Remove stale assignments. An assignment is deemed stale if "accessed" is not True. Sets parent .changed if it removed anything.

        Note: This method is called from the parent collection and should _not_ be called manually.
        """
        len_before = len(self.assignments)
        self.assignments = {key: assignment for key, assignment in self.assignments.items() if assignment.accessed}
        self.collection.changed = self.collection.changed or len_before != len(self.assignments)

    def as_dict(self) -> dict:
        """Returns a dict representing the object."""
        return {
            "pool_key": asdict(
                self.pool_key,
            ),
            "assignments": natural_sort([assignment.as_dict() for assignment in self.assignments.values()], sort_key="value"),
        }

    @classmethod
    def from_dict(
        cls, data: dict, collection: PoolCollection[T_PoolKeyType, T_AssignmentKeyType, T_ValueType]
    ) -> Pool[T_PoolKeyType, T_AssignmentKeyType, T_ValueType]:
        """Returns pool from file data."""
        if not isinstance(data, dict):
            msg = f"Invalid type for 'pool' '{type(data)}'. Expected a dict."
            raise TypeError(msg)

        if not isinstance(pool_key_dict := data["pool_key"], dict):
            msg = f"Invalid type for 'pool_key' '{type(pool_key_dict)}'. Expected a dict."
            raise TypeError(msg)

        pool_key = collection.pool_key_cls.from_dict(pool_key_dict)

        if not isinstance(pool_assignments := data["assignments"], list):
            msg = f"Invalid type for 'assignments' '{type(pool_assignments)}'. Expected a list."
            raise TypeError(msg)

        assignments = {}
        for assignment_dict in pool_assignments:
            if not isinstance(assignment_dict, dict):
                msg = f"Invalid assignment type '{type(assignment_dict)}'. Expected a dict."
                raise TypeError(msg)

            if not isinstance(assignment_key_dict := assignment_dict["key"], dict):
                msg = f"Invalid type for assignment 'key' '{type(assignment_key_dict)}'. Expected a dict."
                raise TypeError(msg)

            if not isinstance(assignment_value := assignment_dict["value"], collection.value_type):
                msg = f"Invalid type for assignment 'value' '{type(assignment_value)}'. Expected a {collection.value_type.__name__}."
                raise TypeError(msg)

            assignment = collection.assignment_cls(collection.assignment_key_cls.from_dict(assignment_key_dict), value=assignment_value)
            assignments[assignment.key] = assignment

        return cls(
            collection=collection,
            pool_key=pool_key,
            assignments=assignments,
        )


@dataclass
class PoolCollection(ABC, Generic[T_PoolKeyType, T_AssignmentKeyType, T_ValueType]):
    """
    Collection of similar Pool instances indexed by a T_PoolKeyType.

    We will maintain a collection of pools per file.
    """

    pools_file: Path
    # Using field(init=False) on fields that are expected to have a default value set on the subclass.
    pools_key: str = field(init=False)
    _pools: dict[T_PoolKeyType, Pool[T_PoolKeyType, T_AssignmentKeyType, T_ValueType]] = field(init=False)
    pool_cls: type[Pool[T_PoolKeyType, T_AssignmentKeyType, T_ValueType]] = field(init=False)
    pool_key_cls: type[T_PoolKeyType] = field(init=False)
    assignment_cls: type[PoolAssignment[T_AssignmentKeyType, T_ValueType]] = field(init=False)
    assignment_key_cls: type[T_AssignmentKeyType] = field(init=False)
    value_type: type[T_ValueType] = field(init=False)
    min_value: T_ValueType = field(init=False)
    max_value: T_ValueType | None = None
    changed: bool = False

    def __post_init__(self) -> None:
        """Try to load data from the pools_file into _pools. If the file is missing, we just set a blank pools."""
        if not self.pools_file.exists():
            self._pools = {}
            return

        file_data = load(self.pools_file.read_text(encoding="UTF-8"), Loader=CSafeLoader)
        if not isinstance(file_data, dict) or self.pools_key not in file_data:
            self._pools = {}
            return

        try:
            self._pools = self._pools_from_list(file_data[self.pools_key])
        except (TypeError, KeyError, ValueError) as e:
            msg = f"An error occurred during parsing of '{self.pools_file}': {e.__class__.__name__}: {e}"
            raise TypeError(msg) from e

    def _pools_from_list(self, data: list) -> dict[T_PoolKeyType, Pool[T_PoolKeyType, T_AssignmentKeyType, T_ValueType]]:
        """Returns pools from file data."""
        if not isinstance(data, list):
            msg = f"Invalid type '{type(data)}'. Expected a list."
            raise TypeError(msg)
        return {pool.pool_key: pool for item in data if (pool := self.pool_cls.from_dict(item, collection=self))}

    def get_pool(self, pool_key: T_PoolKeyType) -> Pool[T_PoolKeyType, T_AssignmentKeyType, T_ValueType]:
        """
        Returns the pool for the given key if found in the collection.

        Otherwise a new pool is inserted into the collection and returned.
        """
        if pool_key not in self._pools:
            self._pools[pool_key] = self.pool_cls(collection=self, pool_key=pool_key, assignments={})
            self.changed = True

        return self._pools[pool_key]

    def _remove_stale_assignments(self) -> None:
        """
        Remove stale assignments from all pools in the collection and remove empty pools afterwards.

        Note: This method is called from the parent pool manager and should _not_ be called manually.
        """
        len_before = len(self._pools)
        [pool._remove_stale_assignments() for pool in self._pools.values()]
        self._pools = {pool_key: pool for pool_key, pool in self._pools.items() if pool.assignments}
        self.changed = self.changed or len_before != len(self._pools)

    def as_list(self) -> list[dict]:
        """Returns a list of dicts representing the object."""
        return natural_sort([pool.as_dict() for pool in self._pools.values()], sort_key="pool_key")

    def save_updates(self, dumper_cls: type = CSafeDumper) -> bool:
        """
        Save data if anything changed. Returns a boolean telling if anything was changed.

        Calls self._remove_stale_assignments first to ensure we save the cleaned data.

        Data is sorted to ensure a consistent layout.
        """
        self._remove_stale_assignments()
        if not self.changed:
            return False

        if not self.pools_file.exists():
            # Try to create the dir and file.
            self.pools_file.parent.mkdir(mode=0o775, parents=True, exist_ok=True)
            self.pools_file.touch(mode=0o664)

        try:
            self.pools_file.write_text(FILE_HEADER + dump({self.pools_key: self.as_list()}, Dumper=dumper_cls))
        except (PermissionError, OSError) as e:
            msg = f"An error occurred during writing of the AVD Pool Manager file '{self.pools_file}': {e}"
            raise type(e)(msg) from e

        self.changed = False
        return True

    @staticmethod
    @abstractmethod
    def _pool_key_from_shared_utils(shared_utils: SharedUtilsProtocol) -> T_PoolKeyType:
        """Returns the pool key to use for tthis device."""

    @staticmethod
    @abstractmethod
    def _pools_file_from_shared_utils(output_dir: Path, shared_utils: SharedUtilsProtocol) -> Path:
        """Returns the file to use for this device."""

    @staticmethod
    @abstractmethod
    def _assignment_key_from_shared_utils(shared_utils: SharedUtilsProtocol) -> T_AssignmentKeyType:
        """Returns the assignment key to use for this device."""
