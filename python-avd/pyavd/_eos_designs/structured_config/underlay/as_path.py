# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class AsPathMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def as_path(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set the structured config for as_path."""
        if self.shared_utils.underlay_routing_protocol != "ebgp":
            return

        if self.shared_utils.wan_ha and self.shared_utils.use_uplinks_for_wan_ha:
            entries = EosCliConfigGen.AsPath.AccessListsItem.Entries()
            entries.append_new(type="permit", match=self.shared_utils.bgp_as)
            self.structured_config.as_path.access_lists.append_new(name="ASPATH-WAN", entries=entries)
