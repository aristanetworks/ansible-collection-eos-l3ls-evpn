# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import append_if_not_duplicate, get
from pyavd.api.interface_descriptions import InterfaceDescriptionData

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigCoreInterfacesAndL3Edge


class EthernetInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def ethernet_interfaces(self: AvdStructuredConfigCoreInterfacesAndL3Edge) -> list | None:
        """Return structured config for ethernet_interfaces."""
        ethernet_interfaces = []

        for p2p_link in self._filtered_p2p_links:
            if p2p_link["data"]["port_channel_id"] is None:
                # Ethernet interface
                ethernet_interface = self._get_common_interface_cfg(p2p_link)
                ethernet_interface["description"] = self._p2p_link_ethernet_description(p2p_link)
                ethernet_interface.update(self._get_ethernet_cfg(p2p_link))

                # Remove None values
                ethernet_interface = {key: value for key, value in ethernet_interface.items() if value is not None}

                append_if_not_duplicate(
                    list_of_dicts=ethernet_interfaces,
                    primary_key="name",
                    new_dict=ethernet_interface,
                    context=f"Ethernet Interfaces defined under {self.data_model} p2p_link",
                    context_keys=["name", "peer", "peer_interface"],
                )

            # Port-Channel members
            for member in p2p_link["data"]["port_channel_members"]:
                ethernet_interface = self._get_port_channel_member_cfg(p2p_link, member)
                ethernet_interface["description"] = self._port_channel_member_description(p2p_link, member)
                ethernet_interface.update(self._get_ethernet_cfg(p2p_link))

                # Remove None values
                ethernet_interface = {key: value for key, value in ethernet_interface.items() if value is not None}

                append_if_not_duplicate(
                    list_of_dicts=ethernet_interfaces,
                    primary_key="name",
                    new_dict=ethernet_interface,
                    context=f"Ethernet Interfaces defined under {self.data_model} p2p_link port-Channel members",
                    context_keys=["name", "peer", "peer_interface"],
                )

        if ethernet_interfaces:
            return ethernet_interfaces

        return None

    def _p2p_link_ethernet_description(self: AvdStructuredConfigCoreInterfacesAndL3Edge, p2p_link: dict) -> str:
        return self.shared_utils.interface_descriptions.underlay_ethernet_interface(
            InterfaceDescriptionData(
                shared_utils=self.shared_utils,
                description=get(p2p_link, "data.description"),
                interface=p2p_link["data"]["interface"],
                link_type=self.data_model,
                peer=p2p_link["data"]["peer"],
                peer_interface=p2p_link["data"]["peer_interface"],
            ),
        )

    def _port_channel_member_description(self: AvdStructuredConfigCoreInterfacesAndL3Edge, p2p_link: dict, member: dict) -> str:
        return self.shared_utils.interface_descriptions.underlay_ethernet_interface(
            InterfaceDescriptionData(
                shared_utils=self.shared_utils,
                description=get(p2p_link, "data.description"),
                interface=member["interface"],
                link_type=self.data_model,
                peer=p2p_link["data"]["peer"],
                peer_interface=member["peer_interface"],
            ),
        )
