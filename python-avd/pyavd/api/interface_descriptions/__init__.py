# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""AVD eos_designs base module to generate interface descriptions."""

from __future__ import annotations

from collections import ChainMap
from typing import TYPE_CHECKING, Any

from pyavd._eos_designs.avdfacts import AvdFacts
from pyavd._utils import AvdStringFormatter, default, strip_null_from_data

if TYPE_CHECKING:
    from pyavd._eos_designs.shared_utils import SharedUtils


class AvdInterfaceDescriptions(AvdFacts):
    """
    Class used to render Interface Descriptions either from custom Jinja2 templates or using default Python Logic.

    Since some templates might contain certain legacy variables (switch_*),
    those are mapped from the switch.* model

    This class is imported adhoc based on the variable `templates.interface_descriptions.python_module` so it can
    be overridden by a custom python class.

    Attributes starting with _ are internal and may change at any time.

    Other attributes are "stable" and changes follow semver practices:
    - Existing attributes will not be changed in terms of type and value, but the underlying code for cached_properties may change.
    - New attributes may be added in minor releases.
    - The __init__ method may change between minor versions as the data may need to be consumed from other sources.
    - Breaking changes may happen between major releases or in rare cases for bug fixes.
    """

    def _template(self, template_path: str, **kwargs: Any) -> str:
        template_vars = ChainMap(kwargs, self._hostvars)
        return self.shared_utils.template_var(template_path, template_vars)

    def underlay_ethernet_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Build an underlay Ethernet interface description.

        If a jinja template is configured, use it.

        Available data:
            - link_type
            - description
            - peer
            - peer_interface
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
            - vrf
            - wan_carrier
            - wan_circuit_id.
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("underlay_ethernet_interfaces"):
            return self._template(
                template_path,
                link={
                    "type": data.link_type,
                    "peer": data.peer,
                    "peer_interface": data.peer_interface,
                },
            )

        if data.description is not None:
            description = data.description
        elif data.link_type in ("underlay_p2p", "l3_edge", "core_interfaces"):
            description = self.shared_utils.default_underlay_p2p_ethernet_description
        elif data.link_type == "underlay_l2":
            description = self.shared_utils.underlay_l2_ethernet_description
        else:
            elems = [data.wan_carrier, data.wan_circuit_id, data.peer, data.peer_interface]
            description = "_".join([elem for elem in elems if elem])
            return f"{description}_vrf_{data.vrf}" if data.vrf is not None else description

        return AvdStringFormatter().format(
            description,
            **strip_null_from_data(
                {
                    "peer": data.peer,
                    "peer_interface": data.peer_interface,
                    "vrf": data.vrf,
                }
            ),
        )

    def underlay_port_channel_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Build an underlay Port-Channel interface description.

        If a jinja template is configured, use it.

        Available data:
            - peer
            - peer_interface
            - peer_channel_group_id
            - peer_node_group
            - port_channel_id
            - port_channel_description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("underlay_port_channel_interfaces"):
            return self._template(
                template_path,
                link={
                    "peer": data.peer,
                    "channel_group_id": data.port_channel_id,
                    "peer_channel_group_id": data.peer_channel_group_id,
                    "channel_description": data.port_channel_description,
                    "peer_node_group": data.peer_node_group,
                },
            )

        if data.port_channel_description is not None:
            description = data.port_channel_description
        elif data.link_type in ("l3_edge", "core_interfaces"):
            description = self.shared_utils.default_underlay_p2p_port_channel_description
        else:
            # This is for L2 port-channels
            description = self.shared_utils.underlay_l2_port_channel_description

        return AvdStringFormatter().format(
            description,
            **strip_null_from_data(
                {
                    "peer": data.peer,
                    "interface": data.interface,
                    "peer_interface": data.peer_interface,
                    "port_channel_id": data.port_channel_id,
                    "peer_port_channel_id": data.peer_channel_group_id,
                    "peer_node_group": data.peer_node_group,
                    "peer_node_group_or_peer": data.peer_node_group or data.peer,
                    "peer_node_group_or_uppercase_peer": data.peer_node_group or str(data.peer or "").upper() or None,
                }
            ),
        )

    def mlag_ethernet_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Build an MLAG Ethernet interface description.

        If a jinja template is configured, use it.
        If not, use the default template as a format string template.

        Available data:
            - interface
            - peer_interface
            - mlag_peer
            - mlag_port_channel_id
            - mlag_peer_port_channel_id
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("mlag_ethernet_interfaces"):
            return self._template(
                template_path,
                mlag_interface=data.interface,
                mlag_peer=data.mlag_peer,
            )

        return AvdStringFormatter().format(
            self.shared_utils.mlag_member_description,
            **strip_null_from_data(
                {
                    "mlag_peer": data.mlag_peer,
                    "interface": data.interface,
                    "peer_interface": data.peer_interface,
                    "mlag_port_channel_id": data.mlag_port_channel_id,
                    "mlag_peer_port_channel_id": data.mlag_peer_port_channel_id,
                }
            ),
        )

    def mlag_port_channel_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Build an MLAG Port-Channel interface description.

        If a jinja template is configured, use it.
        If not, use the default template as a format string template.

        Available data:
            - interface
            - peer_interface
            - mlag_peer
            - mlag_port_channel_id
            - mlag_peer_port_channel_id
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("mlag_port_channel_interfaces"):
            return self._template(
                template_path,
                mlag_interfaces=data.mlag_interfaces,
                mlag_peer=data.mlag_peer,
                mlag_port_channel_id=data.mlag_port_channel_id,
            )

        return AvdStringFormatter().format(
            self.shared_utils.mlag_port_channel_description,
            **strip_null_from_data(
                {
                    "mlag_peer": data.mlag_peer,
                    "interface": data.interface,
                    "peer_interface": data.peer_interface,
                    "mlag_port_channel_id": data.mlag_port_channel_id,
                    "mlag_peer_port_channel_id": data.mlag_peer_port_channel_id,
                }
            ),
        )

    def mlag_peer_svi(self, data: InterfaceDescriptionData) -> str:
        """
        Build an MLAG Peering SVI description.

        Available data:
            - interface
            - mlag_peer
            - mlag_peer_vlan
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        return AvdStringFormatter().format(
            self.shared_utils.mlag_peer_svi_description,
            **strip_null_from_data(
                {
                    "mlag_peer": data.mlag_peer,
                    "interface": data.interface,
                    "mlag_peer_vlan": data.mlag_peer_vlan,
                }
            ),
        )

    def mlag_peer_l3_svi(self, data: InterfaceDescriptionData) -> str:
        """
        Build an MLAG Peering SVI description.

        Available data:
            - interface
            - mlag_peer
            - mlag_peer_l3_vlan
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        return AvdStringFormatter().format(
            self.shared_utils.mlag_peer_l3_svi_description,
            **strip_null_from_data(
                {
                    "mlag_peer": data.mlag_peer,
                    "interface": data.interface,
                    "mlag_peer_l3_vlan": data.mlag_peer_l3_vlan,
                }
            ),
        )

    def mlag_peer_l3_vrf_svi(self, data: InterfaceDescriptionData) -> str:
        """
        Build an MLAG Peering SVI description.

        Available data:
            - interface
            - vlan
            - vrf
            - mlag_peer
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        return AvdStringFormatter().format(
            self.shared_utils.mlag_peer_l3_vrf_svi_description,
            **strip_null_from_data(
                {
                    "mlag_peer": data.mlag_peer,
                    "interface": data.interface,
                    "vlan": data.vlan,
                    "vrf": data.vrf,
                }
            ),
        )

    def connected_endpoints_ethernet_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Build a connected endpoint Ethernet interface description.

        If a jinja template is configured, use it.
        If not, use the adapter.description as a format string template if set.
        Finally fall back to default templates depending on this being a network_port or not.

        Available data:
            - peer
            - peer_type
            - peer_interface
            - description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("connected_endpoints_ethernet_interfaces"):
            return self._template(
                template_path,
                peer=data.peer,
                peer_interface=data.peer_interface,
                adapter_description=data.description,
                peer_type=data.peer_type,
            )

        if data.description:
            description = data.description
        elif data.peer_type == "network_port":
            description = self.shared_utils.default_network_ports_description
        else:
            description = self.shared_utils.default_connected_endpoints_description

        return AvdStringFormatter().format(
            description,
            **strip_null_from_data(
                {
                    "endpoint": data.peer,
                    "endpoint_port": data.peer_interface,
                    "endpoint_type": data.peer_type,
                }
            ),
        )

    def connected_endpoints_port_channel_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Build a connected endpoint Port-channel description.

        If a jinja template is configured, use it.
        If not, use the port_channel.description as a format string template if set.
        Finally fall back to default templates depending on this being a network_port or not.

        Available data:
            - peer
            - peer_interface
            - peer_type
            - description
            - port_channel_id
            - port_channel_description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("connected_endpoints_port_channel_interfaces"):
            return self._template(
                template_path,
                peer=data.peer,
                adapter_port_channel_id=data.port_channel_id,
                adapter_port_channel_description=data.port_channel_description,
                adapter_description=data.description,
            )

        if data.port_channel_description:
            port_channel_description = data.port_channel_description
        elif data.peer_type == "network_port":
            port_channel_description = self.shared_utils.default_network_ports_port_channel_description
        else:
            port_channel_description = self.shared_utils.default_connected_endpoints_port_channel_description

        # Template the adapter description in case it is being referenced in the port_channel_description
        adapter_description = (
            AvdStringFormatter().format(
                data.description,
                **strip_null_from_data(
                    {
                        "endpoint": data.peer,
                        "endpoint_port": data.peer_interface,
                        "endpoint_type": data.peer_type,
                    }
                ),
            )
            if data.description and "adapter_description" in port_channel_description
            else data.description
        )

        return AvdStringFormatter().format(
            port_channel_description,
            **strip_null_from_data(
                {
                    "endpoint": data.peer,
                    "endpoint_port_channel": data.peer_interface,
                    "endpoint_type": data.peer_type,
                    "port_channel_id": data.port_channel_id,
                    "adapter_description": adapter_description,
                    "adapter_description_or_endpoint": adapter_description or data.peer,
                }
            ),
        )

    def router_id_loopback_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Build Router ID loopback interface description.

        Available data:
            - description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        if template_path := default(
            self.shared_utils.interface_descriptions_templates.get("router_id_loopback_interface"),
            self.shared_utils.interface_descriptions_templates.get("overlay_loopback_interface"),
        ):
            return self._template(template_path, overlay_loopback_description=data.description, router_id_loopback_description=data.description)

        return data.description

    def vtep_loopback_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Build VTEP loopback interface description.

        Available data:
            - description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("vtep_loopback_interface"):
            return self._template(template_path, vtep_loopback_description=data.description)

        return data.description

    def wan_ha_ethernet_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Build WAN HA ethernet interface description.

        Available data:
            - interface
            - peer
            - peer_interface
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        return f"WAN_HA_{data.peer}_{data.peer_interface}"

    def wan_ha_port_channel_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Build WAN HA port-channel interface description.

        Available data:
            - interface
            - peer
            - peer_interface
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        return f"WAN_HA_{data.peer}_{data.peer_interface}"


class InterfaceDescriptionData:
    """
    This class is used as transport of data between AVD code and instances of AvdInterfaceDescriptions class or subclasses hereof.

    Attributes starting with _ are internal and may change at any time.

    Other attributes are "stable" and changes follow semver practices:
    - Existing attributes will not be changed in terms of type and value, but the underlying code for cached_properties may change.
    - New attributes may be added in minor releases.
    - The __init__ method may change between minor versions as the data may need to be consumed from other sources.
    - Breaking changes may happen between major releases.
    """

    _shared_utils: SharedUtils
    description: str | None
    """Set description for interface"""
    interface: str | None
    """Local interface"""
    link_type: str | None
    """Type of connection. Like 'underlay_p2p' or 'underlay_l2'"""
    peer: str | None
    """Hostname of peer"""
    peer_interface: str | None
    """Interface of peer"""
    peer_channel_group_id: int | None
    """Port channel ID of peer"""
    peer_node_group: str | None
    """Node group of peer"""
    peer_type: str | None
    """Type of peer"""
    port_channel_id: int | None
    """Port channel ID"""
    port_channel_description: str | None
    """Set description for port-channel"""
    vlan: int | None
    """VLAN ID"""
    vrf: str | None
    """Interface VRF"""
    wan_carrier: str | None
    """The WAN Carrier this interface is connected to"""
    wan_circuit_id: str | None
    """The WAN Circuit ID for this interface."""

    def __init__(
        self,
        shared_utils: SharedUtils,
        description: str | None = None,
        interface: str | None = None,
        link_type: str | None = None,
        peer: str | None = None,
        peer_interface: str | None = None,
        peer_channel_group_id: int | None = None,
        peer_node_group: str | None = None,
        peer_type: str | None = None,
        port_channel_id: int | None = None,
        port_channel_description: str | None = None,
        vlan: int | None = None,
        vrf: str | None = None,
        wan_carrier: str | None = None,
        wan_circuit_id: str | None = None,
    ) -> None:
        self._shared_utils = shared_utils
        self.description = description
        self.interface = interface
        self.link_type = link_type
        self.peer = peer
        self.peer_interface = peer_interface
        self.peer_channel_group_id = peer_channel_group_id
        self.peer_node_group = peer_node_group
        self.peer_type = peer_type
        self.port_channel_id = port_channel_id
        self.port_channel_description = port_channel_description
        self.vlan = vlan
        self.vrf = vrf
        self.wan_carrier = wan_carrier
        self.wan_circuit_id = wan_circuit_id

    @property
    def mpls_overlay_role(self) -> str | None:
        return self._shared_utils.mpls_overlay_role

    @property
    def overlay_routing_protocol(self) -> str:
        return self._shared_utils.overlay_routing_protocol

    @property
    def mlag_interfaces(self) -> list:
        return self._shared_utils.mlag_interfaces

    @property
    def mlag_peer(self) -> str:
        return self._shared_utils.mlag_peer

    @property
    def mlag_port_channel_id(self) -> int:
        return self._shared_utils.mlag_port_channel_id

    @property
    def mlag_peer_port_channel_id(self) -> int:
        return self._shared_utils.mlag_peer_port_channel_id

    @property
    def mlag_peer_vlan(self) -> int:
        return self._shared_utils.mlag_peer_vlan

    @property
    def mlag_peer_l3_vlan(self) -> int | None:
        return self._shared_utils.mlag_peer_l3_vlan

    @property
    def mpls_lsr(self) -> bool:
        return self._shared_utils.mpls_lsr

    @property
    def type(self) -> str:
        return self._shared_utils.type
