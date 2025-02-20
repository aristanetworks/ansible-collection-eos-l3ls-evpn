# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlayProtocol


class IpExtCommunityListsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def ip_extcommunity_lists(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set the structured config for ip_extcommunity_lists."""
        if self.shared_utils.overlay_routing_protocol != "ibgp" and not self.shared_utils.is_wan_router:
            return

        if self.shared_utils.evpn_role == "server" and not self.shared_utils.is_wan_router:
            return

        if self.shared_utils.overlay_vtep or self.shared_utils.is_wan_router:
            ip_extcommunity_list = EosCliConfigGen.IpExtcommunityListsItem(name="ECL-EVPN-SOO")
            ip_extcommunity_list.entries.append_new(type="permit", extcommunities=f"soo {self.shared_utils.evpn_soo}")
            self.structured_config.ip_extcommunity_lists.append(ip_extcommunity_list)
