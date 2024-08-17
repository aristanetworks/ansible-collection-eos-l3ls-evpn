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
    """Input factory class for the VerifyLLDPNeighbors test."""

    @classmethod
    def create(cls, test: type[VerifyLLDPNeighbors], manager: ConfigManager, logger: TestLoggerAdapter) -> VerifyLLDPNeighbors.Input | None:
        """Create Input for the VerifyLLDPNeighbors test."""
        ethernet_interfaces = get(manager.structured_config, "ethernet_interfaces", [])

        neighbors = []
        required_keys = ["peer", "peer_interface"]
        required_key_values = {"shutdown": False}

        for interface in ethernet_interfaces:
            if manager.is_subinterface(interface):
                logger.info(LogMessage.SUBINTERFACE, entity=interface["name"])
                continue

            manager.update_interface_shutdown(interface)

            is_valid, issues = validate_dict(interface, required_keys, required_key_values)
            if not is_valid:
                logger.info(LogMessage.INVALID_DATA, entity=interface["name"], issues=issues)
                continue

            if not manager.is_peer_available(peer := interface["peer"]):
                logger.info(LogMessage.UNAVAILABLE_PEER, entity=interface["name"], peer=peer)
                continue

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
    """Input factory class for the VerifyReachability test."""

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
                logger.info(LogMessage.UNAVAILABLE_PEER, entity=f"Destination {dst_ip}", peer=dst_node)
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
        required_key_values = {"type": "routed", "shutdown": False}

        for interface in ethernet_interfaces:
            manager.update_interface_shutdown(interface)

            is_valid, issues = validate_dict(interface, required_keys, required_key_values)
            if not is_valid:
                logger.info(LogMessage.INVALID_DATA, entity=interface["name"], issues=issues)
                continue

            if not manager.is_peer_available(peer := interface["peer"]):
                logger.info(LogMessage.UNAVAILABLE_PEER, entity=interface["name"], peer=peer)
                continue

            if (
                peer_interface_ip := manager.get_interface_ip(interface_model="ethernet_interfaces", interface_name=interface["peer_interface"], device=peer)
            ) is None:
                logger.info(LogMessage.UNAVAILABLE_PEER_IP, entity=interface["name"], peer=peer, peer_interface=interface["peer_interface"])
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
            logger.info(LogMessage.NO_SOURCES, entity="P2P")

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
                logger.info(LogMessage.INVALID_DATA, entity=svi["name"], issues=issues)
                continue

            vrf = get(svi, "vrf", default="default")

            svis.append({"source": ip_interface(svi["ip_address"]).ip, "vrf": vrf})

        if not svis:
            logger.info(LogMessage.NO_SOURCES, entity="inband management SVI")

        return svis

    @staticmethod
    def _get_vtep_loopback0s(manager: ConfigManager, logger: TestLoggerAdapter) -> list[dict]:
        """Generate the source IPs and VRFs from loopback0 interfaces of VTEPs for the VerifyReachability test."""
        vtep_loopback0s = []

        # TODO: Improve the VTEP logic
        if not manager.is_vtep():
            logger.info(LogMessage.NOT_VTEP)
        elif manager.is_wan_vtep():
            logger.info(LogMessage.WAN_VTEP)
        elif (loopback0_ip := manager.get_interface_ip(interface_model="loopback_interfaces", interface_name="Loopback0")) is None:
            logger.info(LogMessage.UNAVAILABLE_IP, entity="Loopback0")
        else:
            vtep_loopback0s.append({"source": ip_interface(loopback0_ip).ip, "vrf": "default"})

        if not vtep_loopback0s:
            logger.info(LogMessage.NO_SOURCES, entity="Loopback0")

        return vtep_loopback0s
