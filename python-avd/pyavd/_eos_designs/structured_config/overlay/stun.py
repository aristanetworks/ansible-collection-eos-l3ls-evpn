# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import itertools
from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import strip_empties_from_dict

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlay


class StunMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def stun(self: AvdStructuredConfigOverlay) -> dict | None:
        """Return structured config for stun."""
        if not self.shared_utils.is_wan_router:
            return None

        stun = {}
        if self.shared_utils.is_wan_server:
            local_interfaces = [wan_interface.name for wan_interface in self.shared_utils.wan_interfaces]
            stun["server"] = {
                "local_interfaces": local_interfaces,
                "ssl_profile": self.shared_utils.wan_stun_dtls_profile_name,
            }

        if self.shared_utils.is_wan_client and (server_profiles := list(itertools.chain.from_iterable(self._stun_server_profiles.values()))):
            stun["client"] = {"server_profiles": server_profiles}
        return strip_empties_from_dict(stun) or None
