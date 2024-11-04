# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlay


class MplsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def mpls(self: AvdStructuredConfigUnderlay) -> dict | None:
        """Return structured config for mpls."""
        if self.shared_utils.underlay_mpls is not True:
            return None

        if self.shared_utils.underlay_ldp is True:
            mpls_config = {
                "ip": True,
                "ldp": {
                    "interface_disabled_default": True,
                    "shutdown": False,
                    "transport_address_interface": "Loopback0",
                },
            }
            if self.shared_utils.use_router_general_for_router_id is False:
                mpls_config["ldp"]["router_id"] = self.shared_utils.router_id

            return mpls_config
        return {"ip": True}
