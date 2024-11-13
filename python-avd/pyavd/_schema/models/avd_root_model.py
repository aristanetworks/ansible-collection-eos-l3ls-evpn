# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from .avd_model import AvdModel

if TYPE_CHECKING:
    from collections.abc import Mapping

    from typing_extensions import Self


class AvdRootModel(AvdModel):
    @classmethod
    def _from_dict(cls, data: Mapping, keep_extra_keys: bool = True) -> Self:
        """
        Returns a new instance loaded with the data from the given dict.

        TODO: AVD6.0.0 remove the keep_extra_keys option so we no longer support custom keys without _ in structured config
        """
        return super()._from_dict(data, keep_extra_keys=keep_extra_keys)
