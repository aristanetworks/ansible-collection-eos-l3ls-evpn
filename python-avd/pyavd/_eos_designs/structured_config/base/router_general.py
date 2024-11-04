# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from hashlib import sha1
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import get, replace_or_append_item, strip_null_from_data
from pyavd.j2filters import natural_sort, snmp_hash

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigBase


class RouterGeneralMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """
    @cached_property
    def router_general(self: AvdStructuredConfigBase) -> dict | None:
        if self.shared_utils.use_router_general_for_router_id is True:
            router_general = {
                "router_id" : {
                    "ipv4": self.shared_utils.router_id,
                    "ipv6": self.shared_utils.ipv6_router_id
                }
            }
        
            return router_general
        return None
