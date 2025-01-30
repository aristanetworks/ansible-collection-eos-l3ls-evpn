# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from re import findall
from typing import TYPE_CHECKING, Any, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils import default, get, get_ip_from_ip_prefix
from pyavd._utils.format_string import AvdStringFormatter
from pyavd.j2filters import range_expand

if TYPE_CHECKING:
    from typing import Literal

    from pyavd._eos_designs.eos_designs_facts import EosDesignsFacts
    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.structured_config.structured_config_generator import StructCfgs

    from . import SharedUtilsProtocol


class MlagMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def mlag(self: SharedUtilsProtocol) -> bool:
        return self.node_type_key_data.mlag_support and self.node_config.mlag and self.node_group_is_primary_and_peer_hostname is not None

    @cached_property
    def group(self: SharedUtilsProtocol) -> str | None:
        """Group set to "node_group" name or None."""
        if self.node_group_config is not None:
            return self.node_group_config.group
        return None

    @cached_property
    def mlag_interfaces(self: SharedUtilsProtocol) -> list:
        return range_expand(self.node_config.mlag_interfaces or get(self.cv_topology_config, "mlag_interfaces") or self.default_interfaces.mlag_interfaces)

    @cached_property
    def mlag_peer_ipv4_pool(self: SharedUtilsProtocol) -> str:
        if not self.node_config.mlag_peer_ipv4_pool:
            msg = "mlag_peer_ipv4_pool"
            raise AristaAvdMissingVariableError(msg)
        return self.node_config.mlag_peer_ipv4_pool

    @cached_property
    def mlag_peer_ipv6_pool(self: SharedUtilsProtocol) -> str:
        if not self.node_config.mlag_peer_ipv6_pool:
            msg = "mlag_peer_ipv6_pool"
            raise AristaAvdMissingVariableError(msg)
        return self.node_config.mlag_peer_ipv6_pool

    @cached_property
    def mlag_peer_l3_ipv4_pool(self: SharedUtilsProtocol) -> str:
        if not self.node_config.mlag_peer_l3_ipv4_pool:
            msg = "mlag_peer_l3_ipv4_pool"
            raise AristaAvdMissingVariableError(msg)
        return self.node_config.mlag_peer_l3_ipv4_pool

    @cached_property
    def mlag_role(self: SharedUtilsProtocol) -> Literal["primary", "secondary"] | None:
        if self.mlag and self.node_group_is_primary_and_peer_hostname is not None:
            return "primary" if self.node_group_is_primary_and_peer_hostname[0] else "secondary"

        return None

    @cached_property
    def mlag_peer(self: SharedUtilsProtocol) -> str:
        if self.node_group_is_primary_and_peer_hostname is not None:
            return self.node_group_is_primary_and_peer_hostname[1]
        msg = "Unable to find MLAG peer within same node group"
        raise AristaAvdError(msg)

    @cached_property
    def mlag_l3(self: SharedUtilsProtocol) -> bool:
        return self.mlag is True and self.underlay_router is True

    @cached_property
    def mlag_peer_l3_vlan(self: SharedUtilsProtocol) -> int | None:
        if self.mlag_l3:
            mlag_peer_vlan = self.node_config.mlag_peer_vlan
            mlag_peer_l3_vlan = self.node_config.mlag_peer_l3_vlan
            if mlag_peer_l3_vlan not in [None, False, mlag_peer_vlan]:
                return mlag_peer_l3_vlan
        return None

    @cached_property
    def mlag_peer_ip(self: SharedUtilsProtocol) -> str:
        return self.get_mlag_peer_fact("mlag_ip")

    @cached_property
    def mlag_peer_l3_ip(self: SharedUtilsProtocol) -> str | None:
        if self.mlag_peer_l3_vlan is not None:
            return self.get_mlag_peer_fact("mlag_l3_ip")
        return None

    @cached_property
    def mlag_peer_id(self: SharedUtilsProtocol) -> int:
        return self.get_mlag_peer_fact("id")

    def get_mlag_peer_fact(self: SharedUtilsProtocol, key: str, required: bool = True) -> Any:
        return get(self.mlag_peer_facts, key, required=required, org_key=f"avd_switch_facts.({self.mlag_peer}).switch.{key}")

    @cached_property
    def mlag_peer_facts(self: SharedUtilsProtocol) -> EosDesignsFacts | dict:
        return self.get_peer_facts(self.mlag_peer, required=True)

    @cached_property
    def mlag_peer_mgmt_ip(self: SharedUtilsProtocol) -> str | None:
        if (mlag_peer_mgmt_ip := self.get_mlag_peer_fact("mgmt_ip", required=False)) is None:
            return None

        return get_ip_from_ip_prefix(mlag_peer_mgmt_ip)

    @cached_property
    def mlag_ip(self: SharedUtilsProtocol) -> str | None:
        """Render ipv4 address for mlag_ip using dynamically loaded python module."""
        if self.mlag_role == "primary":
            return self.ip_addressing.mlag_ip_primary()
        if self.mlag_role == "secondary":
            return self.ip_addressing.mlag_ip_secondary()
        return None

    @cached_property
    def mlag_l3_ip(self: SharedUtilsProtocol) -> str | None:
        """Render ipv4 address for mlag_l3_ip using dynamically loaded python module."""
        if self.mlag_peer_l3_vlan is None:
            return None
        if self.mlag_role == "primary":
            return self.ip_addressing.mlag_l3_ip_primary()
        if self.mlag_role == "secondary":
            return self.ip_addressing.mlag_l3_ip_secondary()
        return None

    @cached_property
    def mlag_switch_ids(self: SharedUtilsProtocol) -> dict | None:
        """
        Returns the switch id's of both primary and secondary switches for a given node group.

        {"primary": int, "secondary": int}.
        """
        if self.mlag_role == "primary":
            if self.id is None:
                msg = f"'id' is not set on '{self.hostname}' and is required to compute MLAG ids"
                raise AristaAvdInvalidInputsError(msg)
            return {"primary": self.id, "secondary": self.mlag_peer_id}
        if self.mlag_role == "secondary":
            if self.id is None:
                msg = f"'id' is not set on '{self.hostname}' and is required to compute MLAG ids"
                raise AristaAvdInvalidInputsError(msg)
            return {"primary": self.mlag_peer_id, "secondary": self.id}
        return None

    @cached_property
    def mlag_port_channel_id(self: SharedUtilsProtocol) -> int:
        if not self.mlag_interfaces:
            msg = f"'mlag_interfaces' not set on '{self.hostname}."
            raise AristaAvdInvalidInputsError(msg)
        default_mlag_port_channel_id = int("".join(findall(r"\d", self.mlag_interfaces[0])))
        return default(self.node_config.mlag_port_channel_id, default_mlag_port_channel_id)

    @cached_property
    def mlag_peer_port_channel_id(self: SharedUtilsProtocol) -> int:
        return get(self.mlag_peer_facts, "mlag_port_channel_id", default=self.mlag_port_channel_id)

    @cached_property
    def mlag_peer_interfaces(self: SharedUtilsProtocol) -> list:
        return get(self.mlag_peer_facts, "mlag_interfaces", default=self.mlag_interfaces)

    @cached_property
    def mlag_ibgp_ip(self: SharedUtilsProtocol) -> str:
        if self.mlag_l3_ip is not None:
            return self.mlag_l3_ip

        return self.mlag_ip

    @cached_property
    def mlag_peer_ibgp_ip(self: SharedUtilsProtocol) -> str:
        if self.mlag_peer_l3_ip is not None:
            return self.mlag_peer_l3_ip

        return self.mlag_peer_ip

    @cached_property
    def use_separate_peer_group_for_mlag_vrfs(self: SharedUtilsProtocol) -> bool:
        return bool(
            self.inputs.bgp_peer_groups.mlag_ipv4_vrfs_peer
            and self.inputs.bgp_peer_groups.mlag_ipv4_vrfs_peer.name != self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer.name
        )

    @cached_property
    def mlag_vrfs_peer_group_name(self: SharedUtilsProtocol) -> str:
        if self.use_separate_peer_group_for_mlag_vrfs:
            return self.inputs.bgp_peer_groups.mlag_ipv4_vrfs_peer.name
        return self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer.name

    def get_router_bgp_with_mlag_peer_group(self: SharedUtilsProtocol, custom_structured_configs: StructCfgs) -> EosCliConfigGen.RouterBgp:
        """
        Return a partial router_bgp structured_config covering the MLAG peer_group(s) and associated address_family activations.

        Inserts custom structured configuration into the given custom_structured_configs instance.

        This is called from MLAG in the case of BGP underlay routing protocol.
        In the case of another underlay routing protocol, it may be called from network_services instead in case there are VRFs with iBGP peerings.
        """
        router_bgp = EosCliConfigGen.RouterBgp()

        # Only create the underlay peer group if the underlay is BGP or if we reuse the same peer-group from network services.
        if self.underlay_bgp or not self.use_separate_peer_group_for_mlag_vrfs:
            bgp_peer_group = self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer
            router_bgp.peer_groups.append(self.get_mlag_peer_group(bgp_peer_group, custom_structured_configs))
            router_bgp.address_family_ipv4.peer_groups.append(self.get_mlag_peer_group_address_familiy_ipv4(bgp_peer_group, self.inputs.underlay_rfc5549))
            if self.underlay_ipv6:
                router_bgp.address_family_ipv6.peer_groups.append_new(name=bgp_peer_group.name, activate=True)

        if self.use_separate_peer_group_for_mlag_vrfs:
            bgp_peer_group = self.inputs.bgp_peer_groups.mlag_ipv4_vrfs_peer
            router_bgp.peer_groups.append(self.get_mlag_peer_group(bgp_peer_group, custom_structured_configs))
            router_bgp.address_family_ipv4.peer_groups.append(self.get_mlag_peer_group_address_familiy_ipv4(bgp_peer_group, self.inputs.overlay_mlag_rfc5549))

        return router_bgp

    def get_mlag_peer_group(
        self: SharedUtilsProtocol,
        bgp_peer_group: EosDesigns.BgpPeerGroups.MlagIpv4UnderlayPeer | EosDesigns.BgpPeerGroups.MlagIpv4VrfsPeer,
        custom_structured_configs: StructCfgs,
    ) -> EosCliConfigGen.RouterBgp.PeerGroupsItem:
        """Return structured_config for one MLAG peer_group."""
        peer_group_name = bgp_peer_group.name
        peer_group = EosCliConfigGen.RouterBgp.PeerGroupsItem(
            name=peer_group_name,
            type="ipv4",
            remote_as=self.bgp_as,
            next_hop_self=True,
            description=AvdStringFormatter().format(self.inputs.mlag_bgp_peer_group_description, mlag_peer=self.mlag_peer),
            password=bgp_peer_group.password,
            bfd=bgp_peer_group.bfd or None,
            maximum_routes=12000,
            send_community="all",
        )

        if bgp_peer_group.structured_config:
            custom_structured_configs.nested.router_bgp.peer_groups.obtain(peer_group_name)._deepmerge(
                bgp_peer_group.structured_config, list_merge=custom_structured_configs.list_merge_strategy
            )

        if self.node_config.mlag_ibgp_origin_incomplete:
            peer_group.route_map_in = "RM-MLAG-PEER-IN"

        return peer_group

    def get_mlag_peer_group_address_familiy_ipv4(
        self: SharedUtilsProtocol,
        bgp_peer_group: EosDesigns.BgpPeerGroups.MlagIpv4UnderlayPeer | EosDesigns.BgpPeerGroups.MlagIpv4VrfsPeer,
        rfc5549: bool,
    ) -> EosCliConfigGen.RouterBgp.AddressFamilyIpv4.PeerGroupsItem:
        """Return structured_config for activation of one MLAG peer_group under address-family IPv4."""
        address_family_peer_group = EosCliConfigGen.RouterBgp.AddressFamilyIpv4.PeerGroupsItem(name=bgp_peer_group.name, activate=True)
        if rfc5549:
            address_family_peer_group.next_hop.address_family_ipv6._update(enabled=True, originate=True)
        return address_family_peer_group
