# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigUnderlayProtocol


class IpAccesslistsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _set_ipv4_acl(self: AvdStructuredConfigUnderlayProtocol, ipv4_acl: EosDesigns.Ipv4AclsItem) -> None:
        """
        Set structured config for ip_access_lists.

        Called for each interface in l3_interfaces and l3_port_channels when applying ipv4_acls
        """
        self.structured_config.ip_access_lists.append(ipv4_acl._cast_as(EosCliConfigGen.IpAccessListsItem))
