# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.input_models.routing.bgp import BgpPeer
from anta.tests.routing.bgp import VerifyBGPPeerMPCaps, VerifyBGPPeerSession

from pyavd._anta.logs import LogMessage

from ._base_classes import AntaTestInputFactory
from ._constants import DEFAULT_VRF_ADDRESS_FAMILIES, VRF_ADDRESS_FAMILIES


class VerifyBGPPeerSessionInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyBGPPeerSession test.

    This factory generates test inputs for IPv4 BGP peer session verification.

    It collects BGP IPv4 neighbors that are not directly shutdown or not in shutdown
    peer groups from the default VRF. If `allow_bgp_vrfs` is enabled in the fabric scope,
    it will also include IPv4 BGP neighbors in VRFs.

    When a fabric `peer` is provided in the neighbor structured config, the factory verifies
    that the peer is available (`is_deployed: true`) before including it in the test inputs.
    """

    def create(self) -> VerifyBGPPeerSession.Input | None:
        """Create Input for the VerifyBGPPeerSession test."""
        bgp_peers = [
            BgpPeer(
                peer_address=neighbor.ip_address,
                vrf=neighbor.vrf,
            )
            for neighbor in self.device.bgp_neighbors
        ]
        return VerifyBGPPeerSession.Input(bgp_peers=bgp_peers) if bgp_peers else None


class VerifyBGPPeerMPCapsInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyBGPPeerMPCaps test.

    This factory generates test inputs for IPv4 BGP peer multiprotocol capabilities.

    It collects IPv4 BGP neighbors that are not directly shutdown or not in shutdown
    peer groups from the default VRF. If `allow_bgp_vrfs` is enabled in the fabric scope,
    it will also include IPv4 BGP neighbors in VRFs.

    When a fabric `peer` is provided in the neighbor structured config, the factory verifies
    that the peer is available (`is_deployed: true`) before including it in the test inputs.

    For applicable neighbors, it checks the following address families:

    Default VRF:
      - EVPN
      - Flowspec IPv4
      - Flowspec IPv6
      - IPv4 unicast
      - IPv4 labeled unicast
      - IPv4 multicast
      - IPv4 SR-TE
      - IPv6 unicast
      - IPv6 multicast
      - IPv6 SR-TE
      - Link-State (BGP-LU)
      - Path selection
      - RT membership
      - VPNv4
      - VPNv6

    Non-default VRFs (when `allow_bgp_vrfs` is enabled):
      - Flowspec IPv4
      - Flowspec IPv6
      - IPv4 unicast
      - IPv4 multicast
      - IPv6 unicast
      - IPv6 multicast

    For non-default VRFs, the address families are also checked for activation via
    peer groups at the global level, following EOS behavior.
    """

    def create(self) -> VerifyBGPPeerMPCaps.Input | None:
        """Create Input for the VerifyBGPPeerMPCaps test."""
        bgp_peers = []
        for neighbor in self.device.bgp_neighbors:
            multiprotocol_caps = set()
            not_activated_afs = set()
            neighbor_ip = str(neighbor.ip_address)

            # TODO: Check if we want to consider `router_bgp.bgp.default.ipv4_unicast` and `ipv4_unicast_transport_ipv6`
            if neighbor.vrf == "default":
                for af_name, multiprotocol_cap in DEFAULT_VRF_ADDRESS_FAMILIES.items():
                    global_af = getattr(self.structured_config.router_bgp, af_name)
                    if neighbor.peer_group in global_af.peer_groups and global_af.peer_groups[neighbor.peer_group].activate is True:
                        multiprotocol_caps.add(multiprotocol_cap)
                        continue
                    # RT membership AF doesn't support neighbors
                    if af_name != "address_family_rtc" and neighbor_ip in global_af.neighbors and global_af.neighbors[neighbor_ip].activate is True:
                        multiprotocol_caps.add(multiprotocol_cap)
                        continue
                    not_activated_afs.add(multiprotocol_cap)
            else:
                for af_name, multiprotocol_cap in VRF_ADDRESS_FAMILIES.items():
                    # Check if the address family is activated for the neighbor at the VRF level
                    vrf = self.structured_config.router_bgp.vrfs[neighbor.vrf]
                    vrf_af = getattr(vrf, af_name)
                    if neighbor_ip in vrf_af.neighbors and vrf_af.neighbors[neighbor_ip].activate is True:
                        multiprotocol_caps.add(multiprotocol_cap)
                        continue
                    # Check if the neighbor is part of a peer group that activates the address family at the global level
                    global_af = getattr(self.structured_config.router_bgp, af_name)
                    if (
                        neighbor_ip in vrf.neighbors
                        and vrf.neighbors[neighbor_ip].peer_group in global_af.peer_groups
                        and global_af.peer_groups[vrf.neighbors[neighbor_ip].peer_group].activate is True
                    ):
                        multiprotocol_caps.add(multiprotocol_cap)
                        continue
                    not_activated_afs.add(multiprotocol_cap)

            if not_activated_afs:
                caller = f"Peer {neighbor.peer if neighbor.peer else neighbor_ip} in VRF {neighbor.vrf}"
                self.logger.debug(LogMessage.BGP_AF_NOT_ACTIVATED, caller=caller, capability=", ".join(sorted(not_activated_afs)))

            capabilities = sorted(multiprotocol_caps)
            if capabilities:
                bgp_peers.append(BgpPeer(peer_address=neighbor.ip_address, vrf=neighbor.vrf, capabilities=capabilities, strict=True))

        return VerifyBGPPeerMPCaps.Input(bgp_peers=bgp_peers) if bgp_peers else None
