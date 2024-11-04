# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import ip_interface
from typing import TYPE_CHECKING

from pyavd._anta.utils import LogMessage
from pyavd._utils import get, validate_dict

if TYPE_CHECKING:
    from anta.tests.connectivity import VerifyLLDPNeighbors, VerifyReachability

    from pyavd._anta.utils import TestLoggerAdapter
    from pyavd._anta.utils.config_manager import ConfigManager


class VerifyLLDPNeighborsInputFactory:
    """Input factory class for the VerifyLLDPNeighbors test.

    This factory creates test inputs for LLDP neighbor verification.

    It collects expected LLDP neighbors for:
      - All non-shutdown Ethernet interfaces (excluding subinterfaces)
      - Only interfaces with `peer` & `peer_interface` configuration

    The factory ensures:
      - Only available peers (`is_deployed: true`) are included
      - DNS domain is appended to peer name when available (`dns_domain`)
      - Neighbor collection is skipped if no valid neighbors are found
    """

    @classmethod
    def create(cls, test: type[VerifyLLDPNeighbors], manager: ConfigManager, logger: TestLoggerAdapter) -> VerifyLLDPNeighbors.Input | None:
        """Create Input for the VerifyLLDPNeighbors test."""
        ethernet_interfaces = get(manager.structured_config, "ethernet_interfaces", [])

        neighbors = []
        required_keys = ["peer", "peer_interface"]
        required_key_values = {"shutdown": False}

        for interface in ethernet_interfaces:
            # Skip subinterfaces
            if manager.is_subinterface(interface):
                logger.debug(LogMessage.SUBINTERFACE, entity=interface["name"])
                continue

            manager.update_interface_shutdown(interface)

            is_valid, issues = validate_dict(interface, required_keys, required_key_values)
            if not is_valid:
                logger.debug(LogMessage.INELIGIBLE_DATA, entity=interface["name"], issues=issues)
                continue

            if not manager.is_peer_available(peer := interface["peer"]):
                logger.debug(LogMessage.UNAVAILABLE_PEER, entity=interface["name"], peer=peer)
                continue

            # Append the DNS domain if available
            if (dns_domain := get(manager.fabric_data.structured_configs[peer], "dns_domain")) is not None:
                peer = f"{peer}.{dns_domain}"

            neighbors.append(
                test.Input.Neighbor(
                    port=interface["name"],
                    neighbor_device=peer,
                    neighbor_port=interface["peer_interface"],
                ),
            )

        return test.Input(neighbors=neighbors) if neighbors else None


class VerifyReachabilityInputFactory:
    """Input factory class for the VerifyReachability test.

    This factory creates test inputs for IP reachability verification.

    It collects source and destination pairs for:
      - Inband management SVIs to all fabric Loopback0s
      - VTEP Loopback0s to all fabric Loopback0s
      - P2P links between directly connected Ethernet interfaces

    TODO: Add WAN VTEPs support - DPS to DPS reachability
    TODO: Should we add support for VTEP diagnostics?
    TODO: Should we add VTEP VXLAN source interface to VTEP source interface reachability? Usually Loopback1

    The factory ensures:
      - Only non-shutdown interfaces (`shutdown: false`) with valid `ip_address` configuration are used as sources
      - Only available peers (`is_deployed: true`) are used as destinations
      - SVIs must be type `inband_mgmt` to be considered as sources
      - P2P interfaces must be routed (`switchport.enabled: false`) and have valid `peer` & `peer_interface` configuration
      - VTEP Loopback0 testing is on VTEP devices (presence of `vxlan_interface`) only, excluding WAN VTEPs (DPS interface)
      - Reachability collection is skipped if no valid pairs are found
    """

    @classmethod
    def create(cls, test: type[VerifyReachability], manager: ConfigManager, logger: TestLoggerAdapter) -> VerifyReachability.Input | None:
        """Create Input for the VerifyReachability test."""
        # Get the eligible source IPs and VRFs
        inband_mgmt_svis = cls._get_inband_mgmt_svis(manager, logger=logger.add_context(context="Inband MGMT"))
        vtep_loopback0s = cls._get_vtep_loopback0s(manager, logger=logger.add_context(context="VTEP Loopback0"))

        # Generate the hosts from the eligible sources and remote loopback0 interfaces from the mapping
        hosts = []
        for dst_node, dst_ip in manager.fabric_data.loopback0_mapping.items():
            if not manager.is_peer_available(dst_node):
                logger.debug(LogMessage.UNAVAILABLE_PEER, entity=f"Destination {dst_ip}", peer=dst_node)
                continue

            hosts.extend([test.Input.Host(**source_vrf, destination=dst_ip, repeat=1) for source_vrf in inband_mgmt_svis + vtep_loopback0s])

        # Add the P2P hosts
        hosts.extend(cls._get_p2p_hosts(test, manager, logger=logger.add_context(context="P2P")))

        return test.Input(hosts=hosts) if hosts else None

    @staticmethod
    def _get_p2p_hosts(test: type[VerifyReachability], manager: ConfigManager, logger: TestLoggerAdapter) -> list[VerifyReachability.Input.Host]:
        """Generate the P2P hosts for the VerifyReachability test."""
        ethernet_interfaces = get(manager.structured_config, "ethernet_interfaces", default=[])

        hosts = []
        required_keys = ["peer", "peer_interface", "ip_address"]
        required_key_values = {"switchport.enabled": False, "shutdown": False}

        for interface in ethernet_interfaces:
            manager.update_interface_shutdown(interface)

            is_valid, issues = validate_dict(interface, required_keys, required_key_values)
            if not is_valid:
                logger.debug(LogMessage.INELIGIBLE_DATA, entity=interface["name"], issues=issues)
                continue

            if not manager.is_peer_available(peer := interface["peer"]):
                logger.debug(LogMessage.UNAVAILABLE_PEER, entity=interface["name"], peer=peer)
                continue

            if (
                peer_interface_ip := manager.get_interface_ip(interface_model="ethernet_interfaces", interface_name=interface["peer_interface"], device=peer)
            ) is None:
                logger.debug(LogMessage.UNAVAILABLE_PEER_IP, entity=interface["name"], peer=peer, peer_interface=interface["peer_interface"])
                continue

            hosts.append(
                test.Input.Host(
                    source=ip_interface(interface["ip_address"]).ip,
                    destination=ip_interface(peer_interface_ip).ip,
                    vrf="default",
                    repeat=1,
                ),
            )

        if not hosts:
            logger.debug(LogMessage.NO_SOURCES, entity="P2P")

        return hosts

    @staticmethod
    def _get_inband_mgmt_svis(manager: ConfigManager, logger: TestLoggerAdapter) -> list[dict]:
        """Generate the source IPs and VRFs from inband management SVIs for the VerifyReachability test."""
        vlan_interfaces = get(manager.structured_config, "vlan_interfaces", default=[])

        svis = []
        required_keys = ["ip_address"]
        required_key_values = {"type": "inband_mgmt", "shutdown": False}

        for svi in vlan_interfaces:
            manager.update_interface_shutdown(svi)

            is_valid, issues = validate_dict(svi, required_keys, required_key_values)
            if not is_valid:
                logger.debug(LogMessage.INELIGIBLE_DATA, entity=svi["name"], issues=issues)
                continue

            vrf = get(svi, "vrf", default="default")

            svis.append({"source": ip_interface(svi["ip_address"]).ip, "vrf": vrf})

        if not svis:
            logger.debug(LogMessage.NO_SOURCES, entity="inband management SVI")

        return svis

    @staticmethod
    def _get_vtep_loopback0s(manager: ConfigManager, logger: TestLoggerAdapter) -> list[dict]:
        """Generate the source IPs and VRFs from loopback0 interfaces of VTEPs for the VerifyReachability test."""
        vtep_loopback0s = []

        if not manager.is_vtep() or manager.is_wan_vtep():
            logger.debug(LogMessage.NOT_VTEP)
            return vtep_loopback0s

        if (loopback0_ip := manager.get_interface_ip(interface_model="loopback_interfaces", interface_name="Loopback0")) is None:
            logger.debug(LogMessage.UNAVAILABLE_IP, entity="Loopback0")
        else:
            vtep_loopback0s.append({"source": ip_interface(loopback0_ip).ip, "vrf": "default"})

        if not vtep_loopback0s:
            logger.debug(LogMessage.NO_SOURCES, entity="Loopback0")

        return vtep_loopback0s
