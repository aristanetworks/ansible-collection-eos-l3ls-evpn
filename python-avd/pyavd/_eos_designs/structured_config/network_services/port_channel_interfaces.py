# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import append_if_not_duplicate, short_esi_to_route_target
from pyavd.j2filters import natural_sort

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

        Only used with L1 network services or L3 network services
        """
        if not self.shared_utils.network_services_l1 and not self.shared_utils.network_services_l3:
            return

        # Keeping separate list of auto-generated parent interfaces
        # This is used to check for conflicts between auto-generated parents
        # At the end of _set_point_to_point_port_channel_interfaces, parent interfaces are
        # added to structured_config if they were not explicitly configured.
        potential_parent_interfaces = EosCliConfigGen.PortChannelInterfaces()

        # Set to collect all the physical port-channels explicitly configured by _set_point_to_point_port_channel_interfaces.
        configured_physical_po: set[str] = set()

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                # The l3_port_channel has already been filtered in filtered_tenants
                # to only contain entries with our hostname
                subif_parent_port_channel_names = set()
                regular_l3_port_channel_names = set()
                for l3_port_channel in vrf.l3_port_channels:
                    interface_name = l3_port_channel.name
                    is_subinterface = "." in interface_name

                    nodes_length = len(l3_port_channel.nodes)
                    if (l3_port_channel.ip_addresses and len(l3_port_channel.ip_addresses) != nodes_length) or (
                        l3_port_channel.descriptions and len(l3_port_channel.descriptions) != nodes_length
                    ):
                        msg = f"Length of lists, 'nodes', 'ip_addresses' and 'descriptions' must match for l3_port_channels for {vrf.name} in {tenant.name}"
                        raise AristaAvdError(msg)

                    if not is_subinterface:
                        # This is a regular Port-Channel (not sub-interface)
                        regular_l3_port_channel_names.add(interface_name)
                        continue
                    # This is a subinterface for a port-channel interface.
                    # We need to ensure that parent port-channel interface is also included explicitly
                    # within list of Port-Channel interfaces.
                    parent_port_channel_name = interface_name.split(".", maxsplit=1)[0]
                    subif_parent_port_channel_names.add(parent_port_channel_name)
                    if l3_port_channel.member_interfaces:
                        msg = f"L3 Port-Channel sub-interface '{interface_name}' has 'member_interfaces' set. This is not a valid setting."
                        raise AristaAvdInvalidInputsError(msg)
                    if l3_port_channel._get("mode"):
                        # implies 'mode' is set when not applicable for a sub-interface
                        msg = f"L3 Port-Channel sub-interface '{interface_name}' has 'mode' set. This is not a valid setting."
                        raise AristaAvdInvalidInputsError(msg)
                    if l3_port_channel._get("mtu"):
                        # implies 'mtu' is set when not applicable for a sub-interface
                        msg = f"L3 Port-Channel sub-interface '{interface_name}' has 'mtu' set. This is not a valid setting."
                        raise AristaAvdInvalidInputsError(msg)

                # Sanity check if there are any sub-interfaces for which parent Port-channel is not explicitly specified
                if missing_parent_port_channels := subif_parent_port_channel_names.difference(regular_l3_port_channel_names):
                    msg = (
                        f"One or more L3 Port-Channels '{', '.join(natural_sort(missing_parent_port_channels))}' "
                        "need to be specified as they have sub-interfaces referencing them."
                    )
                    raise AristaAvdInvalidInputsError(msg)

                # Now that validation is complete, we can make another pass at all l3_port_channels
                # (subinterfaces or otherwise) and generate their structured config.
                for l3_port_channel in vrf.l3_port_channels:
                    for node_index, node_name in enumerate(l3_port_channel.nodes):
                        if node_name != self.shared_utils.hostname:
                            continue

                        port_channel_interface = self._get_l3_port_channel_cfg(l3_port_channel, node_index, vrf.name, vrf.ospf.enabled)
                        append_if_not_duplicate(
                            list_of_dicts=port_channel_interfaces,
                            primary_key="name",
                            new_dict=port_channel_interface,
                            context="L3 Port-Channel interfaces defined under network services l3_port_channels",
                            context_keys=["name", "peer", "peer_port_channel"],
                        )

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
