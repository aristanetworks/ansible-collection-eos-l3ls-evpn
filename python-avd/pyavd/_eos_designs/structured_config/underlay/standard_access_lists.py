# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class StandardAccessListsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def standard_access_lists(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """
        Return structured config for standard_access_lists.

        Used for to configure ACLs used by multicast RPs for the underlay
        """
        if not self.shared_utils.underlay_multicast or not self.inputs.underlay_multicast_rps:
            return

        for rp_entry in self.inputs.underlay_multicast_rps:
            if not rp_entry.groups or not rp_entry.access_list_name:
                continue
            standard_access_list = EosCliConfigGen.StandardAccessListsItem(name=rp_entry.access_list_name)
            for index, group in enumerate(rp_entry.groups):
                standard_access_list.sequence_numbers.append_new(sequence=(index + 1) * 10, action=f"permit {group}")
            self.structured_config.standard_access_lists.append(standard_access_list)
