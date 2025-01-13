# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import get_ip_from_ip_prefix

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigCoreInterfacesAndL3Edge


class RouterBgpMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_bgp(self: AvdStructuredConfigCoreInterfacesAndL3Edge) -> dict | None:
        """Return structured config for router_bgp."""
        if not self.shared_utils.underlay_bgp:
            return None

        neighbors = []
        neighbor_interfaces = []
        for p2p_link, p2p_link_data in self._filtered_p2p_links:
            if not p2p_link.include_in_underlay_protocol:
                continue

            if p2p_link_data["bgp_as"] is None or p2p_link_data["peer_bgp_as"] is None:
                msg = f"{self.data_model}.p2p_links.[].as or {self.data_model}.p2p_links_profiles.[].as"
                raise AristaAvdInvalidInputsError(msg)

            neighbor = {
                "remote_as": p2p_link_data["peer_bgp_as"],
                "peer": p2p_link_data["peer"],
                "description": p2p_link_data["peer"],
                "peer_group": self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
            }

            # RFC5549
            if self.inputs.underlay_rfc5549 and p2p_link.routing_protocol != "ebgp":
                neighbor_interfaces.append({"name": p2p_link_data["interface"], **neighbor})
                continue

            # Regular BGP Neighbors
            if p2p_link_data["ip"] is None or p2p_link_data["peer_ip"] is None:
                msg = f"{self.data_model}.p2p_links.[].ip, .subnet or .ip_pool"
                raise AristaAvdInvalidInputsError(msg)

            neighbor["bfd"] = p2p_link.bfd
            if p2p_link_data["bgp_as"] != self.shared_utils.bgp_as:
                neighbor["local_as"] = p2p_link_data["bgp_as"]

            # Remove None values
            neighbor = {key: value for key, value in neighbor.items() if value is not None}

            neighbors.append({"ip_address": get_ip_from_ip_prefix(p2p_link_data["peer_ip"]), **neighbor})

        router_bgp = {}
        if neighbors:
            router_bgp["neighbors"] = neighbors

        if neighbor_interfaces:
            router_bgp["neighbor_interfaces"] = neighbor_interfaces

        if router_bgp:
            return router_bgp

        return None
