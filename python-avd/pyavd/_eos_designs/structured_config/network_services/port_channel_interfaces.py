# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._utils import short_esi_to_route_target

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class PortChannelInterfacesMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def port_channel_interfaces(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set structured config for port_channel_interfaces.

        Only used with L1 network services
        """
        if not self.shared_utils.network_services_l1:
            return

        # Keeping separate list of auto-generated parent interfaces
        # This is used to check for conflicts between auto-generated parents
        # At the end of _set_point_to_point_port_channel_interfaces, parent interfaces are
        # added to structured_config if they were not explicitly configured.
        potential_parent_interfaces = EosCliConfigGen.PortChannelInterfaces()

        # Set to collect all the physical port-channels explicitly configured by _set_point_to_point_port_channel_interfaces.
        configured_physical_po: set[str] = set()

        for tenant in self.shared_utils.filtered_tenants:
            if not tenant.point_to_point_services:
                continue

            self._set_point_to_point_port_channel_interfaces(tenant, potential_parent_interfaces, configured_physical_po)

            for potential_parent_interface in potential_parent_interfaces:
                if potential_parent_interface.name not in configured_physical_po:
                    self.structured_config.port_channel_interfaces.append(potential_parent_interface)

    def _set_point_to_point_port_channel_interfaces(
        self: AvdStructuredConfigNetworkServicesProtocol,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        potential_parent_interfaces: EosCliConfigGen.PortChannelInterfaces,
        configured_physical_po_names: set[str],
    ) -> None:
        """Set the structured_config port_channel_interfaces with the point-to-point interfaces defined under network_services."""
        for point_to_point_service in tenant.point_to_point_services._natural_sorted():
            for endpoint in point_to_point_service.endpoints:
                if self.shared_utils.hostname not in endpoint.nodes:
                    continue

                node_index = endpoint.nodes.index(self.shared_utils.hostname)
                interface_name = endpoint.interfaces[node_index]
                if (port_channel_mode := endpoint.port_channel.mode) not in ["active", "on"]:
                    continue

                channel_group_id = "".join(re.findall(r"\d", interface_name))
                interface_name = f"Port-Channel{channel_group_id}"
                if point_to_point_service.subinterfaces:
                    # This is a subinterface so we need to ensure that the parent is created
                    parent_interface = EosCliConfigGen.PortChannelInterfacesItem(
                        name=interface_name,
                        peer_type="system",
                        shutdown=False,
                    )
                    parent_interface.switchport.enabled = False

                    if (short_esi := endpoint.port_channel.short_esi) is not None and len(short_esi.split(":")) == 3:
                        parent_interface.evpn_ethernet_segment._update(
                            identifier=f"{self.inputs.evpn_short_esi_prefix}{short_esi}", route_target=short_esi_to_route_target(short_esi)
                        )
                        if port_channel_mode == "active":
                            parent_interface.lacp_id = short_esi.replace(":", ".")

                    # Adding the auto-generated parent to the list of potential parents
                    potential_parent_interfaces.append(parent_interface)

                    for subif in point_to_point_service.subinterfaces:
                        subif_name = f"{interface_name}.{subif.number}"

                        self.structured_config.port_channel_interfaces.append_new(
                            name=subif_name,
                            peer_type="point_to_point_service",
                            shutdown=False,
                            encapsulation_vlan=EosCliConfigGen.PortChannelInterfacesItem.EncapsulationVlan(
                                client=EosCliConfigGen.PortChannelInterfacesItem.EncapsulationVlan.Client(encapsulation="dot1q", vlan=subif.number),
                                network=EosCliConfigGen.PortChannelInterfacesItem.EncapsulationVlan.Network(encapsulation="client"),
                            ),
                        )

                else:
                    port_channel_interface = EosCliConfigGen.PortChannelInterfacesItem(
                        name=interface_name,
                        peer_type="point_to_point_service",
                        shutdown=False,
                    )
                    port_channel_interface.switchport.enabled = False

                    if (short_esi := endpoint.port_channel.short_esi) is not None and len(short_esi.split(":")) == 3:
                        port_channel_interface.evpn_ethernet_segment._update(
                            identifier=f"{self.inputs.evpn_short_esi_prefix}{short_esi}",
                            route_target=short_esi_to_route_target(short_esi),
                        )
                        if port_channel_mode == "active":
                            port_channel_interface.lacp_id = short_esi.replace(":", ".")

                    self.structured_config.port_channel_interfaces.append(port_channel_interface)
                    # Tracking the physical interfaces to determine which auto-generated should be injected.
                    configured_physical_po_names.add(interface_name)
