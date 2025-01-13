# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from hashlib import sha256
from typing import TYPE_CHECKING

from pyavd._utils import default

if TYPE_CHECKING:
    from . import EosDesignsFacts


class ShortEsiMixin:
    """
    Mixin Class used to generate some of the EosDesignsFacts.

    Class should only be used as Mixin to the EosDesignsFacts class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def _short_esi(self: EosDesignsFacts) -> str | None:
        """
        If short_esi is set to "auto" we will use sha256 to create a unique short_esi value based on various uplink information.

        Note: Secondary MLAG switch should have the same short-esi value
        as primary MLAG switch.
        """
        # On the MLAG Secondary use short-esi from MLAG primary
        if self.shared_utils.mlag_role == "secondary" and (peer_short_esi := self.shared_utils.mlag_peer_facts._short_esi) is not None:
            return peer_short_esi
        short_esi = self.shared_utils.node_config.short_esi
        if short_esi == "auto":
            esi_seed_1 = "".join(self.shared_utils.uplink_switches[:2])
            esi_seed_2 = "".join(self.shared_utils.uplink_switch_interfaces[:2])
            esi_seed_3 = "".join(self.shared_utils.uplink_interfaces[:2])
            esi_seed_4 = default(self.shared_utils.group, "")
            esi_hash = sha256(f"{esi_seed_1}{esi_seed_2}{esi_seed_3}{esi_seed_4}".encode()).hexdigest()
            short_esi = re.sub(r"([0-9a-f]{4})", r"\1:", esi_hash)[:14]
        return short_esi
