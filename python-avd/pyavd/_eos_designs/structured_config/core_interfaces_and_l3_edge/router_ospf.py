# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigCoreInterfacesAndL3Edge


class RouterOspfMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_ospf(self: AvdStructuredConfigCoreInterfacesAndL3Edge) -> dict | None:
        """Return structured config for router_ospf."""
        if not self.shared_utils.underlay_ospf:
            return None

        no_passive_interfaces = [p2p_link_data["interface"] for p2p_link, p2p_link_data in self._filtered_p2p_links if p2p_link.include_in_underlay_protocol]
        if no_passive_interfaces:
            return {
                "process_ids": [
                    {
                        "id": self.inputs.underlay_ospf_process_id,
                        "no_passive_interfaces": no_passive_interfaces,
                    },
                ],
            }

        return None
