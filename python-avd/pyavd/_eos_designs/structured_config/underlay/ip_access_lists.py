# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._utils import append_if_not_duplicate
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigUnderlayProtocol


class IpAccesslistsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def ip_access_lists(self: AvdStructuredConfigUnderlayProtocol) -> list | None:
        """
        Return structured config for ip_access_lists.

        Covers ipv4_acl_in/out defined under node l3_port_channels.
        """
        if not self._l3_port_channel_acls:
            return None

        ip_access_lists = []
        context_str = "IPv4 Access lists for node l3_port_channels"
        for interface_acls in self._l3_port_channel_acls.values():
            for acl in interface_acls.values():
                append_if_not_duplicate(ip_access_lists, "name", acl, context=context_str, context_keys=["name"])

        return natural_sort(ip_access_lists, "name")

    def _set_ipv4_acl(self: AvdStructuredConfigUnderlayProtocol, ipv4_acl: EosDesigns.Ipv4AclsItem) -> None:
        """
        Set structured config for ip_access_lists.

        Called from l3_interfaces when applying ipv4_acls
        """
        self.structured_config.ip_access_lists.append(ipv4_acl._cast_as(EosCliConfigGen.IpAccessListsItem))
