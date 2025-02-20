# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from .avd_model import AvdModel

if TYPE_CHECKING:
    from collections.abc import Mapping

    from typing_extensions import Self


class EosCliConfigGenRootModel(AvdModel):
    @classmethod
    def _from_dict(cls, data: Mapping, keep_extra_keys: bool = True) -> Self:
        """
        Returns a new instance loaded with the data from the given dict.

        Args:
            data: A mapping containing the EosDesigns input data to be loaded.
            keep_extra_keys: Store all unknown keys in the self._custom_data dict and include it again in the output of _to_dict().
                By default _all_ keys will be stored. Setting this to False will only store keys starting with _.

        TODO: AVD6.0.0 remove the keep_extra_keys option so we no longer support custom keys without _ in structured config
        """
        return super()._from_dict(data, keep_extra_keys=keep_extra_keys)
