# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import default, get
from pyavd.api.interface_descriptions import InterfaceDescriptionData

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigCoreInterfacesAndL3Edge


class PortChannelInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def port_channel_interfaces(self: AvdStructuredConfigCoreInterfacesAndL3Edge) -> list | None:
        """Return structured config for port_channel_interfaces."""
        port_channel_interfaces = []
        for p2p_link in self._filtered_p2p_links:
            if p2p_link["data"]["port_channel_id"] is None:
                continue

            # Port-Channel interface
            port_channel_interface = self._get_common_interface_cfg(p2p_link)
            port_channel_interface["description"] = self._p2p_link_port_channel_description(p2p_link)

            # Remove None values
            port_channel_interface = {key: value for key, value in port_channel_interface.items() if value is not None}

            port_channel_interfaces.append(port_channel_interface)

        if port_channel_interfaces:
            return port_channel_interfaces

        return None

    def _p2p_link_port_channel_description(self: AvdStructuredConfigCoreInterfacesAndL3Edge, p2p_link: dict) -> str:
        return self.shared_utils.interface_descriptions.underlay_port_channel_interface(
            InterfaceDescriptionData(
                shared_utils=self.shared_utils,
                port_channel_description=default(get(p2p_link, "data.port_channel_description"), get(p2p_link, "data.description")),
                interface=p2p_link["data"]["interface"],
                port_channel_id=p2p_link["data"]["port_channel_id"],
                peer_channel_group_id=p2p_link["data"]["peer_port_channel_id"],
                link_type=self.data_model,
                peer=p2p_link["data"]["peer"],
                peer_interface=p2p_link["data"]["peer_interface"],
            ),
        )
