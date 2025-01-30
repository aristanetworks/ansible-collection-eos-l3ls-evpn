# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class StandardAccessListsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def standard_access_lists(self: AvdStructuredConfigUnderlayProtocol) -> list | None:
        """
        Return structured config for standard_access_lists.

        Used for to configure ACLs used by multicast RPs for the underlay
        """
        if not self.shared_utils.underlay_multicast or not self.inputs.underlay_multicast_rps:
            return None

        standard_access_lists = []
        for rp_entry in self.inputs.underlay_multicast_rps:
            if not rp_entry.groups or not rp_entry.access_list_name:
                continue

            standard_access_lists.append(
                {
                    "name": rp_entry.access_list_name,
                    "sequence_numbers": [
                        {
                            "sequence": (index + 1) * 10,
                            "action": f"permit {group}",
                        }
                        for index, group in enumerate(rp_entry.groups)
                    ],
                },
            )

        if standard_access_lists:
            return standard_access_lists

        return None
