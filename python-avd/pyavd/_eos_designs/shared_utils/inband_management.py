# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from ipaddress import ip_network
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import get
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from . import SharedUtils


class InbandManagementMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def configure_inband_mgmt(self: SharedUtils) -> bool:
        return bool(self.uplink_type == "port-channel" and self.inband_mgmt_ip)

    @cached_property
    def configure_inband_mgmt_ipv6(self: SharedUtils) -> bool:
        return bool(self.uplink_type == "port-channel" and self.inband_mgmt_ipv6_address)

    @cached_property
    def configure_parent_for_inband_mgmt(self: SharedUtils) -> bool:
        return self.configure_inband_mgmt and not self.node_config.inband_mgmt_ip

    @cached_property
    def configure_parent_for_inband_mgmt_ipv6(self: SharedUtils) -> bool:
        return self.configure_inband_mgmt_ipv6 and not self.node_config.inband_mgmt_ipv6_address

    @cached_property
    def inband_mgmt_mtu(self: SharedUtils) -> int | None:
        if not self.platform_settings.feature_support.per_interface_mtu:
            return None

        return self.node_config.inband_mgmt_mtu

    @cached_property
    def inband_mgmt_vrf(self: SharedUtils) -> str | None:
        if (inband_mgmt_vrf := self.node_config.inband_mgmt_vrf) != "default":
            return inband_mgmt_vrf

        return None

    @cached_property
    def inband_mgmt_gateway(self: SharedUtils) -> str | None:
        """
        Inband management gateway.

        If inband_mgmt_ip is set but not via inband_mgmt_subnet we return the value of inband_mgmt_gateway.

        Otherwise if inband_mgmt_subnet is set we return the gateway derived from inband_mgmt_subnet (first IP)

        Otherwise return None
        """
        if not self.inband_mgmt_ip:
            return None

        if not self.configure_parent_for_inband_mgmt:
            return self.node_config.inband_mgmt_gateway

        if not self.node_config.inband_mgmt_subnet:
            return None

        subnet = ip_network(self.node_config.inband_mgmt_subnet, strict=False)
        return f"{subnet[1]!s}"

    @cached_property
    def inband_mgmt_ipv6_gateway(self: SharedUtils) -> str | None:
        """
        Inband management ipv6 gateway.

        If inband_mgmt_ipv6_address is set but not via inband_mgmt_ipv6_subnet we return the value of inband_mgmt_ipv6_gateway.

        Otherwise if inband_mgmt_ipv6_subnet is set we return the gateway derived from inband_mgmt_ipv6_subnet (first IP)

        Otherwise return None
        """
        if not self.inband_mgmt_ipv6_address:
            return None

        if not self.configure_parent_for_inband_mgmt_ipv6:
            return self.node_config.inband_mgmt_ipv6_gateway

        if not self.node_config.inband_mgmt_ipv6_subnet:
            return None

        subnet = ip_network(self.node_config.inband_mgmt_ipv6_subnet, strict=False)
        return f"{subnet[1]!s}"

    @cached_property
    def inband_mgmt_ip(self: SharedUtils) -> str | None:
        """
        Inband management IP.

        Set to either:
          - Value of inband_mgmt_ip
          - deducted IP from inband_mgmt_subnet & id
          - None.
        """
        if inband_mgmt_ip := self.node_config.inband_mgmt_ip:
            return inband_mgmt_ip

        if not self.node_config.inband_mgmt_subnet:
            return None

        if self.id is None:
            msg = f"'id' is not set on '{self.hostname}' and is required to set inband_mgmt_ip from inband_mgmt_subnet"
            raise AristaAvdInvalidInputsError(msg)

        subnet = ip_network(self.node_config.inband_mgmt_subnet, strict=False)
        inband_mgmt_ip = str(subnet[3 + self.id])
        return f"{inband_mgmt_ip}/{subnet.prefixlen}"

    @cached_property
    def inband_mgmt_ipv6_address(self: SharedUtils) -> str | None:
        """
        Inband management IPv6 Address.

        Set to either:
          - Value of inband_mgmt_ipv6_address
          - deduced IP from inband_mgmt_ipv6_subnet & id
          - None.
        """
        if inband_mgmt_ipv6_address := self.node_config.inband_mgmt_ipv6_address:
            return inband_mgmt_ipv6_address

        if not self.node_config.inband_mgmt_ipv6_subnet:
            return None

        if self.id is None:
            msg = f"'id' is not set on '{self.hostname}' and is required to set inband_mgmt_ipv6_address from inband_mgmt_ipv6_subnet"
            raise AristaAvdInvalidInputsError(msg)

        subnet = ip_network(self.node_config.inband_mgmt_ipv6_subnet, strict=False)
        inband_mgmt_ipv6_address = str(subnet[3 + self.id])
        return f"{inband_mgmt_ipv6_address}/{subnet.prefixlen}"

    @cached_property
    def inband_mgmt_interface(self: SharedUtils) -> str | None:
        """
        Inband management Interface used only to set as source interface on various management protocols.

        For L2 switches defaults to Vlan<inband_mgmt_vlan>
        For all other devices set to value of inband_mgmt_interface or None
        """
        if inband_mgmt_interface := self.node_config.inband_mgmt_interface:
            return inband_mgmt_interface

        if self.configure_inband_mgmt or self.configure_inband_mgmt_ipv6:
            return f"Vlan{self.node_config.inband_mgmt_vlan}"

        return None

    @cached_property
    def inband_management_parent_vlans(self: SharedUtils) -> dict:
        if not self.underlay_router:
            return {}

        svis = {}
        subnets = []
        ipv6_subnets = []
        peers = natural_sort(get(self.hostvars, f"avd_topology_peers..{self.hostname}", separator="..", default=[]))
        for peer in peers:
            peer_facts = self.get_peer_facts(peer, required=True)
            if (vlan := peer_facts.get("inband_mgmt_vlan")) is None:
                continue

            subnet = peer_facts.get("inband_mgmt_subnet")
            ipv6_subnet = peer_facts.get("inband_mgmt_ipv6_subnet")
            if vlan not in svis:
                svis[vlan] = {"ipv4": None, "ipv6": None}

            if subnet not in subnets:
                subnets.append(subnet)
                svis[vlan]["ipv4"] = subnet

            if ipv6_subnet not in ipv6_subnets:
                ipv6_subnets.append(ipv6_subnet)
                svis[vlan]["ipv6"] = ipv6_subnet

        return svis
