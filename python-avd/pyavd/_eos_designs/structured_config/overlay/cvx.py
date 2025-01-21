# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import get, get_ip_from_ip_prefix

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlay


class CvxMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def cvx(self: AvdStructuredConfigOverlay) -> dict | None:
        """Detect if this is a CVX server for overlay and configure service & peer hosts accordingly."""
        if not self.shared_utils.overlay_cvx:
            return None

        if self.shared_utils.hostname not in self.inputs.overlay_cvx_servers:
            return None

        peer_hosts = []
        for overlay_cvx_server in self.inputs.overlay_cvx_servers:
            if overlay_cvx_server == self.shared_utils.hostname:
                continue

            peer_switch_facts = self.shared_utils.get_peer_facts(overlay_cvx_server, required=True)
            cvx_server_ip = get(peer_switch_facts, "mgmt_ip", required=True, custom_error_msg=f"'mgmt_ip' for CVX Server {overlay_cvx_server} is required.")
            peer_hosts.append(get_ip_from_ip_prefix(cvx_server_ip))

        return {
            "shutdown": False,
            "peer_hosts": peer_hosts,
            "services": {
                "vxlan": {
                    "shutdown": False,
                },
            },
        }
