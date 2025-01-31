# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._utils import strip_empties_from_dict

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class MplsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def mpls(self: AvdStructuredConfigUnderlayProtocol) -> dict | None:
        """Return structured config for mpls."""
        if self.shared_utils.underlay_mpls is not True:
            return None

        if self.shared_utils.underlay_ldp is True:
            return strip_empties_from_dict(
                {
                    "ip": True,
                    "ldp": {
                        "interface_disabled_default": True,
                        "router_id": self.shared_utils.router_id if not self.inputs.use_router_general_for_router_id else None,
                        "shutdown": False,
                        "transport_address_interface": "Loopback0",
                    },
                }
            )

        return {"ip": True}
