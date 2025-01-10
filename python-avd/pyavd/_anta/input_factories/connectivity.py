# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import ip_interface

from anta.input_models.connectivity import Host, LLDPNeighbor
from anta.tests.connectivity import VerifyLLDPNeighbors, VerifyReachability

from pyavd._anta.logs import LogMessage

from ._base_classes import AntaTestInputFactory


class VerifyLLDPNeighborsInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyLLDPNeighbors test.

    This factory collects LLDP neighbors for Ethernet interfaces that have
    `peer` and `peer_interface` fields defined in their configuration.

    Peers must be available (`is_deployed: true`) and within the boundary scope
    if configured.

    The factory respects `validate_state` and `validate_lldp` settings, excludes
    subinterfaces and shutdown interfaces (considering `interface_defaults.ethernet.shutdown`
    when not set), and uses peer FQDN when `dns_domain` is configured to match EOS
    LLDP format.
    """

    def create(self) -> VerifyLLDPNeighbors.Input | None:
        """Create Input for the VerifyLLDPNeighbors test."""
        neighbors = []
        for intf in self.structured_config.ethernet_interfaces:
            if intf.validate_state is False or intf.validate_lldp is False:
                self.logger.debug(LogMessage.INTERFACE_VALIDATION_DISABLED, caller=intf.name)
                continue
            if "." in intf.name:
                self.logger.debug(LogMessage.INTERFACE_IS_SUBINTERFACE, caller=intf.name)
                continue
            if intf.shutdown or (intf.shutdown is None and self.structured_config.interface_defaults.ethernet.shutdown):
                self.logger.debug(LogMessage.INTERFACE_SHUTDOWN, caller=intf.name)
                continue

            if not intf.peer or not intf.peer_interface:
                self.logger.debug(LogMessage.INPUT_MISSING_FIELDS, caller=intf.name, fields="peer, peer_interface")
                continue

            if not self.is_peer_available(intf.peer, caller=intf.name) or not self.is_peer_in_boundary(intf.peer, caller=intf.name):
                continue

            # LLDP neighbor is the FQDN when dns domain is set in EOS
            fqdn = f"{intf.peer}.{dns_domain}" if (dns_domain := self.fabric_data.devices[intf.peer].dns_domain) is not None else intf.peer

            neighbors.append(
                LLDPNeighbor(
                    port=intf.name,
                    neighbor_device=fqdn,
                    neighbor_port=intf.peer_interface,
                )
            )

        return VerifyLLDPNeighbors.Input(neighbors=neighbors) if neighbors else None


class VerifyReachabilityInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyReachability test.

    This factory generates test inputs for verifying reachability between devices.

    Four types of reachability are checked:

    - Verifies point-to-point links between Ethernet interfaces where `peer`, `peer_interface`,
    `ip_address` (non-dhcp) are configured. Links are checked when interfaces are not `shutdown`,
    fabric peers exist and are deployed (`is_deployed: true`), peers are within boundary scope,
    and peer interfaces have IP addresses.

    - For inband management, it verifies connectivity from inband VLAN interfaces (`type: inband_mgmt`)
    to fabric peer Loopback0 IP addresses. Interfaces must not be `shutdown`, and peers must exist,
    be deployed, be within boundary scope, and have Loopback0 IPs.

    - For VTEP underlay, it verifies connectivity between VTEP (excluding WAN routers) Loopback0 IP
    addresses and fabric peer Loopback0 IPs. Peers must exist, be deployed, be within boundary scope,
    and have Loopback0 IPs.

    - For WAN DPS connectivity, it verifies reachability between WAN router VTEP IPs (Dps1). The
    device must be a WAN router with VTEP IP, and fabric peers must be deployed WAN routers within
    boundary scope that have VTEP IPs.
    """

    def create(self) -> VerifyReachability.Input | None:
        """Create Input for the VerifyReachability test."""
        hosts = []

        # Add the P2P reachability
        with self.logger.context("Point-to-Point Links"):
            hosts.extend(self.get_point_to_point_hosts())

        # Add inband MGMT SVI to Loopback0 reachability
        with self.logger.context("Inband Management to Loopback0"):
            hosts.extend(self.get_inband_management_hosts())

        # Add VTEP underlay reachability (Loopback0 to Loopback0), excluding WAN routers
        with self.logger.context("VTEP Underlay Connectivity"):
            hosts.extend(self.get_vtep_underlay_hosts())

        # Add WAN router to WAN router reachability (DPS to DPS)
        with self.logger.context("WAN Router DPS Connectivity"):
            hosts.extend(self.get_wan_dps_hosts())

        return VerifyReachability.Input(hosts=hosts) if hosts else None

    def get_point_to_point_hosts(self) -> list[Host]:
        """Get reachability hosts for point-to-point interface connections."""
        hosts = []
        for intf in self.structured_config.ethernet_interfaces:
            if intf.shutdown or (intf.shutdown is None and self.structured_config.interface_defaults.ethernet.shutdown):
                self.logger.debug(LogMessage.INTERFACE_SHUTDOWN, caller=intf.name)
                continue

            if not intf.ip_address or not intf.peer or not intf.peer_interface:
                self.logger.debug(LogMessage.INPUT_MISSING_FIELDS, caller=intf.name, fields="ip_address, peer, peer_interface")
                continue

            if intf.ip_address == "dhcp":
                self.logger.debug(LogMessage.INTERFACE_USING_DHCP, caller=intf.name)
                continue

            if not self.is_peer_available(intf.peer, caller=intf.name) or not self.is_peer_in_boundary(intf.peer, caller=intf.name):
                continue

            if (peer_interface_ip := self.fabric_data.devices[intf.peer].routed_interface_ips.get(intf.peer_interface)) is None:
                self.logger.debug(LogMessage.PEER_INTERFACE_NO_IP, caller=intf.name, peer=intf.peer, peer_interface=intf.peer_interface)
                continue

            hosts.append(
                Host(
                    destination=peer_interface_ip,
                    source=ip_interface(intf.ip_address).ip,
                    vrf="default",
                    repeat=1,
                )
            )

        return hosts

    def get_inband_management_hosts(self) -> list[Host]:
        """Get reachability hosts from inband management SVI to all Loopback0 addresses."""
        # Find first eligible inband MGMT SVI
        inband_mgmt_ip = None
        inband_mgmt_vrf = None

        for vlan_intf in self.structured_config.vlan_interfaces:
            if vlan_intf.shutdown:
                self.logger.debug(LogMessage.INTERFACE_SHUTDOWN, caller=vlan_intf.name)
                continue

            if vlan_intf.type != "inband_mgmt":
                self.logger.debug(LogMessage.INTERFACE_NOT_INBAND_MGMT, caller=vlan_intf.name)
                continue

            if not vlan_intf.ip_address:
                self.logger.debug(LogMessage.INTERFACE_NO_IP, caller=vlan_intf.name)
                break

            # Found valid interface
            inband_mgmt_ip = vlan_intf.ip_address
            inband_mgmt_vrf = vlan_intf._get("vrf", default="default")
            break

        if inband_mgmt_ip is None:
            self.logger.debug(LogMessage.DEVICE_NO_INBAND_MGMT)
            return []

        # Build hosts list for inband MGMT SVI to all fabric Loopback0s
        return [
            Host(
                destination=dst_ip,
                source=ip_interface(inband_mgmt_ip).ip,
                vrf=inband_mgmt_vrf,
                repeat=1,
            )
            for dst_peer, dst_ip in self.fabric_data.get_ip_index("loopback0_ips").items()
            if dst_peer != self.device.hostname
            and self.is_peer_available(dst_peer, caller=f"Loopback0 destination {dst_ip}")
            and self.is_peer_in_boundary(dst_peer, caller=f"Loopback0 destination {dst_ip}")
        ]

    def get_vtep_underlay_hosts(self) -> list[Host]:
        """Get reachability hosts between VTEP Loopback0 addresses for underlay connectivity."""
        if not self.device.is_vtep or self.device.is_wan_router:
            self.logger.debug(LogMessage.DEVICE_NOT_VTEP)
            return []
        if not self.device.loopback0_ip:
            self.logger.debug(LogMessage.LOOPBACK0_NO_IP)
            return []

        # Build hosts list for VTEP Loopback0 to all fabric Loopback0s
        return [
            Host(
                destination=dst_ip,
                source=self.device.loopback0_ip,
                vrf="default",
                repeat=1,
            )
            for dst_peer, dst_ip in self.fabric_data.get_ip_index("loopback0_ips").items()
            if dst_peer != self.device.hostname
            and self.is_peer_available(dst_peer, caller=f"Loopback0 destination {dst_ip}")
            and self.is_peer_in_boundary(dst_peer, caller=f"Loopback0 destination {dst_ip}")
        ]

    def get_wan_dps_hosts(self) -> list[Host]:
        """Get reachability hosts between WAN router DPS addresses."""
        if not self.device.is_wan_router:
            self.logger.debug(LogMessage.DEVICE_NOT_WAN_ROUTER)
            return []
        if not self.device.vtep_ip:
            self.logger.debug(LogMessage.VTEP_NO_IP)
            return []

        # Build hosts list for WAN router DPS to all WAN router DPS
        return [
            Host(
                destination=dst_ip,
                source=self.device.vtep_ip,
                vrf="default",
                repeat=1,
            )
            # TODO: Consider pre-computing the WAN VTEP IPs in FabricData
            for dst_peer, dst_ip in self.fabric_data.get_ip_index("vtep_ips", is_wan_router=True).items()
            if dst_peer != self.device.hostname
            and self.is_peer_available(dst_peer, caller=f"DPS destination {dst_ip}")
            and self.is_peer_in_boundary(dst_peer, caller=f"DPS destination {dst_ip}")
        ]
