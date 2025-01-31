# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlayProtocol


class RouterBfdMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_bfd(self: AvdStructuredConfigOverlayProtocol) -> dict | None:
        """Return structured config for router_bfd."""
        if self.shared_utils.overlay_cvx:
            return None

        return {"multihop": self.inputs.bfd_multihop._as_dict()}
