# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdMissingVariableError
from pyavd._utils import get, get_ip_from_ip_prefix

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlay


class ManagementCvxMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def management_cvx(self: AvdStructuredConfigOverlay) -> dict | None:
        if not (self.shared_utils.overlay_cvx and self.shared_utils.overlay_vtep):
            return None

        if not self.inputs.overlay_cvx_servers:
            msg = "overlay_cvx_servers"
            raise AristaAvdMissingVariableError(msg)

        server_hosts = []
        for overlay_cvx_server in self.inputs.overlay_cvx_servers:
            peer_switch_facts = self.shared_utils.get_peer_facts(overlay_cvx_server, required=True)
            cvx_server_ip = get(peer_switch_facts, "mgmt_ip", required=True, custom_error_msg=f"'mgmt_ip' for CVX Server {overlay_cvx_server} is required.")
            server_hosts.append(get_ip_from_ip_prefix(cvx_server_ip))

        return {
            "shutdown": False,
            "source_interface": "Loopback0",
            "server_hosts": server_hosts,
        }
