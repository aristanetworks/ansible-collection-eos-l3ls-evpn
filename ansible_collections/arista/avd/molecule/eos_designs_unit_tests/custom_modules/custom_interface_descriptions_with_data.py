# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from functools import cached_property

from pyavd.api.interface_descriptions import AvdInterfaceDescriptions, InterfaceDescriptionData


class CustomAvdInterfaceDescriptions(AvdInterfaceDescriptions):
    @cached_property
    def _custom_description_prefix(self) -> str:
        return str(self._hostvars.get("description_prefix") or "")

    def underlay_ethernet_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Implementation using new data.

        Available data:
            - link_type
            - peer
            - peer_interface
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
            - vrf
        """
        link_peer = str(data.peer).upper()
        if data.link_type == "underlay_p2p":
            vrf_desc = f" VRF {data.vrf}" if data.vrf else ""
            return f"{self._custom_description_prefix}_P2P_LINK_TO_{link_peer}_{data.peer_interface}{vrf_desc}"

        if data.link_type == "underlay_l2":
            return f"{self._custom_description_prefix}_{link_peer}_{data.peer_interface}"

        return ""

    def underlay_port_channel_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Implementation using new data.

        Available data:
            - peer
            - peer_channel_group_id
            - port_channel_description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        if data.port_channel_description is not None:
            link_channel_description = str(data.port_channel_description).upper()
            return f"{self._custom_description_prefix}_{link_channel_description}_Po{data.peer_channel_group_id}"

        link_peer = str(data.peer).upper()
        return f"{self._custom_description_prefix}_{link_peer}_Po{data.peer_channel_group_id}"

    def mlag_ethernet_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Implementation using new data.

        Available data:
            - peer_interface
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        return f"{self._custom_description_prefix}_MLAG_PEER_{data.mlag_peer}_{data.interface}"

    def mlag_port_channel_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Implementation using new data.

        Available data:
            - mlag_peer
            - peer_channel_group_id
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        return f"{self._custom_description_prefix}_MLAG_PEER_{data.mlag_peer}_Po{data.mlag_port_channel_id}"

    def mlag_peer_svi(self, data: InterfaceDescriptionData) -> str:  # noqa: ARG002
        return "MLAG_PEER"

    def mlag_peer_l3_svi(self, data: InterfaceDescriptionData) -> str:  # noqa: ARG002
        return "MLAG_PEER_L3_PEERING"

    def mlag_peer_l3_vrf_svi(self, data: InterfaceDescriptionData) -> str:
        return f"MLAG_PEER_L3_iBGP: vrf {data.vrf}"

    def connected_endpoints_ethernet_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Implementation using new data.

        Available data:
            - peer
            - peer_interface
            - description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        elements = [data.peer, data.peer_interface]
        return "_".join([str(element) for element in elements if element is not None])

    def connected_endpoints_port_channel_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Implementation using new data.

        Available data:
            - peer
            - description
            - port_channel_description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        elements = [self._custom_description_prefix, data.peer, data.port_channel_description]
        return "_".join([str(element) for element in elements if element is not None])

    def router_id_loopback_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Called per device.

        Available data:
        - description
        - mpls_overlay_role
        - mpls_lsr
        - overlay_routing_protocol
        - type
        """
        switch_type = str(data.type).upper()
        return f"{self._custom_description_prefix}_EVPN_Overlay_Peering_{switch_type}"

    def vtep_loopback_interface(self, data: InterfaceDescriptionData) -> str:  # noqa: ARG002
        """Implementation of custom code similar to jinja."""
        switch_type = str(self.shared_utils.type).upper()
        return f"{self._custom_description_prefix}_VTEP_VXLAN_Tunnel_Source_{switch_type}"
