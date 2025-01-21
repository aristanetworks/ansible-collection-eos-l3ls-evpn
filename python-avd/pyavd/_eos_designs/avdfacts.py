# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from .shared_utils import SharedUtils


class AvdFacts:
    _hostvars: dict
    inputs: EosDesigns
    shared_utils: SharedUtils

    def __init__(self, hostvars: dict, inputs: EosDesigns, shared_utils: SharedUtils) -> None:
        self._hostvars = hostvars
        self.inputs = inputs
        self.shared_utils = shared_utils

    @classmethod
    def __keys(cls) -> list[str]:  # pylint: disable=bad-option-value, unused-private-member # CH Sep-22: Some pylint bug.
        """
        Get all class attributes including those of base Classes and Mixins.

        Using MRO, which is the same way Python resolves attributes.
        """
        keys = []
        for c in cls.mro():
            c_keys = [key for key in c.__dict__ if key not in keys]
            keys.extend(c_keys)

        return keys

    @classmethod
    def keys(cls) -> list[str]:
        """
        Return the list of "keys".

        Actually the returned list are the names of attributes not starting with "_" and using cached_property class.
        The "_" check is added to allow support for "internal" cached_properties storing temporary values.
        """
        return [key for key in cls.__keys() if not key.startswith("_") and isinstance(getattr(cls, key), cached_property)]

    @classmethod
    def internal_keys(cls) -> list[str]:
        """Return a list containing the names of attributes starting with "_" and using cached_property class."""
        return [key for key in cls.__keys() if key.startswith("_") and isinstance(getattr(cls, key), cached_property)]

    def get(self, key: str, default_value: Any = None) -> Any:
        """Emulate the builtin dict .get method."""
        if key in self.keys():
            return getattr(self, key)
        return default_value

    def render(self) -> dict:
        """
        Return a dictionary of all @cached_property values.

        If the value is cached, it will automatically get returned from cache
        If the value is not cached, it will be resolved by the attribute function first.
        Empty values are removed from the returned data.
        """
        return {key: getattr(self, key) for key in self.keys() if getattr(self, key) is not None}

    def clear_cache(self) -> None:
        for key in self.keys() + self.internal_keys():
            self.__dict__.pop(key, None)
