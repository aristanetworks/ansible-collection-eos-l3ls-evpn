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

    Requirements:
      - IPv4 neighbors only
      - Peer not shutdown
      - Peer exists and is deployed if specified
      - Peer within boundary if `allow_bgp_external` is disabled in fabric scope

    Notes:
      - Skips neighbors in shutdown peer groups
      - Skips VRF peers if `allow_bgp_vrfs` is disabled in fabric scope
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

    Requirements:
      - IPv4 neighbors only
      - Peer not shutdown
      - Peer exists and is deployed if specified
      - Peer within boundary if `allow_bgp_external` is disabled in fabric scope

    Supported address families for the default VRF:
      - EVPN
      - Path selection
      - Link state
      - IPv4 unicast
      - IPv6 unicast
      - IPv4 SR-TE
      - IPv6 SR-TE

    Supported address families for non-default VRFs:
      - IPv4 unicast
      - IPv6 unicast

    Notes:
      - Skips neighbors in shutdown peer groups
      - Skips VRF peers if `allow_bgp_vrfs` is disabled in fabric scope
    """

    def create(self) -> VerifyBGPPeerMPCaps.Input | None:
        """Create Input for the VerifyBGPPeerMPCaps test."""
        bgp_peers = []
        for neighbor in self.device.bgp_neighbors:
            multiprotocol_caps = set()
            not_activated_afs = set()
            neighbor_ip = str(neighbor.ip_address)
            identifier = f"{neighbor.peer if neighbor.peer else neighbor_ip} in VRF {neighbor.vrf}"

            # TODO: Check if we want to consider `router_bgp.bgp.default.ipv4_unicast` and `ipv4_unicast_transport_ipv6`
            if neighbor.vrf == "default":
                for af_name, multiprotocol_cap in DEFAULT_VRF_ADDRESS_FAMILIES.items():
                    global_af = getattr(self.structured_config.router_bgp, af_name)
                    if (neighbor_ip in global_af.neighbors and global_af.neighbors[neighbor_ip].activate is True) or (
                        neighbor.peer_group in global_af.peer_groups and global_af.peer_groups[neighbor.peer_group].activate is True
                    ):
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
                with self.logger.context(identifier):
                    self.logger.debug(LogMessage.BGP_AF_NOT_ACTIVATED, capability=", ".join(sorted(not_activated_afs)))

            capabilities = sorted(multiprotocol_caps)
            bgp_peers.append(BgpPeer(peer_address=neighbor.ip_address, vrf=neighbor.vrf, capabilities=capabilities, strict=True))

        return VerifyBGPPeerMPCaps.Input(bgp_peers=bgp_peers) if bgp_peers else None
