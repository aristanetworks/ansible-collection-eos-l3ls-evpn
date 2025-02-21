# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import ip_interface

from anta.input_models.connectivity import Host, LLDPNeighbor
from anta.tests.connectivity import VerifyLLDPNeighbors, VerifyReachability

from pyavd._anta.logs import LogMessage
from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory


class VerifyLLDPNeighborsInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyLLDPNeighbors test.

    This factory collects LLDP neighbors for Ethernet interfaces that have
    `peer` and `peer_interface` fields defined in their configuration.

    Peers must be available (`is_deployed: true`).

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

            if not self.is_peer_available(intf.peer, caller=intf.name):
                continue

            # LLDP neighbor is the FQDN when dns domain is set in EOS
            fqdn = f"{intf.peer}.{dns_domain}" if (dns_domain := self.structured_configs[intf.peer].dns_domain) is not None else intf.peer

            neighbors.append(
                LLDPNeighbor(
                    port=intf.name,
                    neighbor_device=fqdn,
                    neighbor_port=intf.peer_interface,
                )
            )

        return VerifyLLDPNeighbors.Input(neighbors=natural_sort(neighbors, sort_key="port")) if neighbors else None


class VerifyReachabilityInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyReachability test.

    This factory generates test inputs for verifying various reachability checks.

    These types of reachability are checked:

    - Verifies point-to-point links between Ethernet interfaces where `peer`, `peer_interface`,
    `ip_address` (non-dhcp) are configured. Links are checked when interfaces are not `shutdown`,
    fabric peers exist and are deployed (`is_deployed: true`) and peer interfaces have IP addresses.
    """

    def create(self) -> VerifyReachability.Input | None:
        """Create Input for the VerifyReachability test."""
        hosts = []

        # Add the P2P reachability
        with self.logger.context("Point-to-Point Links"):
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

                if (peer_interface_ip := self.get_interface_ip(intf.peer, intf.peer_interface, caller=intf.name)) is None:
                    continue

                hosts.append(
                    Host(
                        destination=ip_interface(peer_interface_ip).ip,
                        source=ip_interface(intf.ip_address).ip,
                        vrf="default",
                        repeat=1,
                    )
                )

        return VerifyReachability.Input(hosts=natural_sort(hosts, sort_key="destination")) if hosts else None
