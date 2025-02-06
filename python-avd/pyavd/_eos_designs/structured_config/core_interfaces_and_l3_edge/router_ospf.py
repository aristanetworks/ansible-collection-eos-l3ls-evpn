# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigCoreInterfacesAndL3EdgeProtocol


class RouterOspfMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_ospf(self: AvdStructuredConfigCoreInterfacesAndL3EdgeProtocol) -> None:
        """Set the structured config for router_ospf."""
        if not self.shared_utils.underlay_ospf:
            return

        no_passive_interfaces = EosCliConfigGen.RouterOspf.ProcessIdsItem.NoPassiveInterfaces()
        for p2p_link, p2p_link_data in self._filtered_p2p_links:
            if p2p_link.include_in_underlay_protocol:
                no_passive_interfaces.append(p2p_link_data["interface"])

        if no_passive_interfaces:
            self.structured_config.router_ospf.process_ids.append_new(
                id=self.inputs.underlay_ospf_process_id,
                no_passive_interfaces=EosCliConfigGen.RouterOspf.ProcessIdsItem.NoPassiveInterfaces(no_passive_interfaces),
            )
