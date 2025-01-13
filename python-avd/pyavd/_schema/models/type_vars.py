# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from .avd_base import AvdBase
    from .avd_indexed_list import AvdIndexedList
    from .avd_list import AvdList
    from .avd_model import AvdModel

T = TypeVar("T")
T_AvdBase = TypeVar("T_AvdBase", bound="AvdBase")
T_AvdModel = TypeVar("T_AvdModel", bound="AvdModel")
T_AvdIndexedList = TypeVar("T_AvdIndexedList", bound="AvdIndexedList")
T_AvdList = TypeVar("T_AvdList", bound="AvdList")
T_PrimaryKey = TypeVar("T_PrimaryKey", int, str)
T_ItemType = TypeVar("T_ItemType")
