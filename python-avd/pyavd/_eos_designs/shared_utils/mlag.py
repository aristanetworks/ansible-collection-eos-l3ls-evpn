# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from re import findall
from typing import TYPE_CHECKING, Any

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils import default, get, get_ip_from_ip_prefix
from pyavd.j2filters import range_expand

if TYPE_CHECKING:
    from typing import Literal

    from pyavd._eos_designs.eos_designs_facts import EosDesignsFacts

    from . import SharedUtils


class MlagMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def mlag(self: SharedUtils) -> bool:
        return self.node_type_key_data.mlag_support and self.node_config.mlag and self.node_group_is_primary_and_peer_hostname is not None

    @cached_property
    def group(self: SharedUtils) -> str | None:
        """Group set to "node_group" name or None."""
        if self.node_group_config is not None:
            return self.node_group_config.group
        return None

    @cached_property
    def mlag_interfaces(self: SharedUtils) -> list:
        return range_expand(self.node_config.mlag_interfaces or get(self.cv_topology_config, "mlag_interfaces") or self.default_interfaces.mlag_interfaces)

    @cached_property
    def mlag_peer_ipv4_pool(self: SharedUtils) -> str:
        if not self.node_config.mlag_peer_ipv4_pool:
            msg = "mlag_peer_ipv4_pool"
            raise AristaAvdMissingVariableError(msg)
        return self.node_config.mlag_peer_ipv4_pool

    @cached_property
    def mlag_peer_ipv6_pool(self: SharedUtils) -> str:
        if not self.node_config.mlag_peer_ipv6_pool:
            msg = "mlag_peer_ipv6_pool"
            raise AristaAvdMissingVariableError(msg)
        return self.node_config.mlag_peer_ipv6_pool

    @cached_property
    def mlag_peer_l3_ipv4_pool(self: SharedUtils) -> str:
        if not self.node_config.mlag_peer_l3_ipv4_pool:
            msg = "mlag_peer_l3_ipv4_pool"
            raise AristaAvdMissingVariableError(msg)
        return self.node_config.mlag_peer_l3_ipv4_pool

    @cached_property
    def mlag_role(self: SharedUtils) -> Literal["primary", "secondary"] | None:
        if self.mlag and self.node_group_is_primary_and_peer_hostname is not None:
            return "primary" if self.node_group_is_primary_and_peer_hostname[0] else "secondary"

        return None

    @cached_property
    def mlag_peer(self: SharedUtils) -> str:
        if self.node_group_is_primary_and_peer_hostname is not None:
            return self.node_group_is_primary_and_peer_hostname[1]
        msg = "Unable to find MLAG peer within same node group"
        raise AristaAvdError(msg)

    @cached_property
    def mlag_l3(self: SharedUtils) -> bool:
        return self.mlag is True and self.underlay_router is True

    @cached_property
    def mlag_peer_l3_vlan(self: SharedUtils) -> int | None:
        if self.mlag_l3:
            mlag_peer_vlan = self.node_config.mlag_peer_vlan
            mlag_peer_l3_vlan = self.node_config.mlag_peer_l3_vlan
            if mlag_peer_l3_vlan not in [None, False, mlag_peer_vlan]:
                return mlag_peer_l3_vlan
        return None

    @cached_property
    def mlag_peer_ip(self: SharedUtils) -> str:
        return self.get_mlag_peer_fact("mlag_ip")

    @cached_property
    def mlag_peer_l3_ip(self: SharedUtils) -> str | None:
        if self.mlag_peer_l3_vlan is not None:
            return self.get_mlag_peer_fact("mlag_l3_ip")
        return None

    @cached_property
    def mlag_peer_id(self: SharedUtils) -> int:
        return self.get_mlag_peer_fact("id")

    def get_mlag_peer_fact(self: SharedUtils, key: str, required: bool = True) -> Any:
        return get(self.mlag_peer_facts, key, required=required, org_key=f"avd_switch_facts.({self.mlag_peer}).switch.{key}")

    @cached_property
    def mlag_peer_facts(self: SharedUtils) -> EosDesignsFacts | dict:
        return self.get_peer_facts(self.mlag_peer, required=True)

    @cached_property
    def mlag_peer_mgmt_ip(self: SharedUtils) -> str | None:
        if (mlag_peer_mgmt_ip := self.get_mlag_peer_fact("mgmt_ip", required=False)) is None:
            return None

        return get_ip_from_ip_prefix(mlag_peer_mgmt_ip)

    @cached_property
    def mlag_ip(self: SharedUtils) -> str | None:
        """Render ipv4 address for mlag_ip using dynamically loaded python module."""
        if self.mlag_role == "primary":
            return self.ip_addressing.mlag_ip_primary()
        if self.mlag_role == "secondary":
            return self.ip_addressing.mlag_ip_secondary()
        return None

    @cached_property
    def mlag_l3_ip(self: SharedUtils) -> str | None:
        """Render ipv4 address for mlag_l3_ip using dynamically loaded python module."""
        if self.mlag_peer_l3_vlan is None:
            return None
        if self.mlag_role == "primary":
            return self.ip_addressing.mlag_l3_ip_primary()
        if self.mlag_role == "secondary":
            return self.ip_addressing.mlag_l3_ip_secondary()
        return None

    @cached_property
    def mlag_switch_ids(self: SharedUtils) -> dict | None:
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
    def mlag_port_channel_id(self: SharedUtils) -> int:
        if not self.mlag_interfaces:
            msg = f"'mlag_interfaces' not set on '{self.hostname}."
            raise AristaAvdInvalidInputsError(msg)
        default_mlag_port_channel_id = int("".join(findall(r"\d", self.mlag_interfaces[0])))
        return default(self.node_config.mlag_port_channel_id, default_mlag_port_channel_id)

    @cached_property
    def mlag_peer_port_channel_id(self: SharedUtils) -> int:
        return get(self.mlag_peer_facts, "mlag_port_channel_id", default=self.mlag_port_channel_id)

    @cached_property
    def mlag_peer_interfaces(self: SharedUtils) -> list:
        return get(self.mlag_peer_facts, "mlag_interfaces", default=self.mlag_interfaces)

    @cached_property
    def mlag_ibgp_ip(self: SharedUtils) -> str:
        if self.mlag_l3_ip is not None:
            return self.mlag_l3_ip

        return self.mlag_ip

    @cached_property
    def mlag_peer_ibgp_ip(self: SharedUtils) -> str:
        if self.mlag_peer_l3_ip is not None:
            return self.mlag_peer_l3_ip

        return self.mlag_peer_ip
