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

from .utils import UtilsMixin

if TYPE_CHECKING:
    from typing import Literal

    from pyavd._eos_designs.eos_designs_facts import EosDesignsFacts


class MlagMixin(UtilsMixin):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def mlag(self) -> bool:
        return (
            self.shared_utils.node_type_key_data.mlag_support
            and self.shared_utils.node_config.mlag
            and self.shared_utils.node_group_is_primary_and_peer_hostname is not None
        )

    @cached_property
    def group(self) -> str | None:
        """Group set to "node_group" name or None."""
        if self.shared_utils.node_group_config is not None:
            return self.shared_utils.node_group_config.group
        return None

    @cached_property
    def mlag_interfaces(self) -> list:
        return range_expand(
            self.shared_utils.node_config.mlag_interfaces
            or get(self.shared_utils.cv_topology_config, "mlag_interfaces")
            or self.shared_utils.default_interfaces.mlag_interfaces
        )

    @cached_property
    def mlag_peer_ipv4_pool(self) -> str:
        if not self.shared_utils.node_config.mlag_peer_ipv4_pool:
            msg = "mlag_peer_ipv4_pool"
            raise AristaAvdMissingVariableError(msg)
        return self.shared_utils.node_config.mlag_peer_ipv4_pool

    @cached_property
    def mlag_peer_ipv6_pool(self) -> str:
        if not self.shared_utils.node_config.mlag_peer_ipv6_pool:
            msg = "mlag_peer_ipv6_pool"
            raise AristaAvdMissingVariableError(msg)
        return self.shared_utils.node_config.mlag_peer_ipv6_pool

    @cached_property
    def mlag_peer_l3_ipv4_pool(self) -> str:
        if not self.shared_utils.node_config.mlag_peer_l3_ipv4_pool:
            msg = "mlag_peer_l3_ipv4_pool"
            raise AristaAvdMissingVariableError(msg)
        return self.shared_utils.node_config.mlag_peer_l3_ipv4_pool

    @cached_property
    def mlag_role(self) -> Literal["primary", "secondary"] | None:
        if self.mlag and self.shared_utils.node_group_is_primary_and_peer_hostname is not None:
            return "primary" if self.shared_utils.node_group_is_primary_and_peer_hostname[0] else "secondary"

        return None

    @cached_property
    def mlag_peer(self) -> str:
        if self.shared_utils.node_group_is_primary_and_peer_hostname is not None:
            return self.shared_utils.node_group_is_primary_and_peer_hostname[1]
        msg = "Unable to find MLAG peer within same node group"
        raise AristaAvdError(msg)

    @cached_property
    def mlag_l3(self) -> bool:
        return self.mlag is True and self.shared_utils.underlay_router is True

    @cached_property
    def mlag_peer_l3_vlan(self) -> int | None:
        if self.mlag_l3:
            mlag_peer_vlan = self.shared_utils.node_config.mlag_peer_vlan
            mlag_peer_l3_vlan = self.shared_utils.node_config.mlag_peer_l3_vlan
            if mlag_peer_l3_vlan not in [None, False, mlag_peer_vlan]:
                return mlag_peer_l3_vlan
        return None

    @cached_property
    def mlag_peer_ip(self) -> str:
        return self.get_mlag_peer_fact("mlag_ip")

    @cached_property
    def mlag_peer_l3_ip(self) -> str | None:
        if self.mlag_peer_l3_vlan is not None:
            return self.get_mlag_peer_fact("mlag_l3_ip")
        return None

    @cached_property
    def mlag_peer_id(self) -> int:
        return self.get_mlag_peer_fact("id")

    def get_mlag_peer_fact(self, key: str, required: bool = True) -> Any:
        return get(self.mlag_peer_facts, key, required=required, org_key=f"avd_switch_facts.({self.mlag_peer}).switch.{key}")

    @cached_property
    def mlag_peer_facts(self) -> EosDesignsFacts | dict:
        return self.get_peer_facts(self.mlag_peer)

    @cached_property
    def mlag_peer_mgmt_ip(self) -> str | None:
        if (mlag_peer_mgmt_ip := self.get_mlag_peer_fact("mgmt_ip", required=False)) is None:
            return None

        return get_ip_from_ip_prefix(mlag_peer_mgmt_ip)

    @cached_property
    def mlag_ip(self) -> str | None:
        """Render ipv4 address for mlag_ip using dynamically loaded python module."""
        if self.mlag_role == "primary":
            return self.shared_utils.ip_addressing.mlag_ip_primary()
        if self.mlag_role == "secondary":
            return self.shared_utils.ip_addressing.mlag_ip_secondary()
        return None

    @cached_property
    def mlag_l3_ip(self) -> str | None:
        """Render ipv4 address for mlag_l3_ip using dynamically loaded python module."""
        if self.mlag_peer_l3_vlan is None:
            return None
        if self.mlag_role == "primary":
            return self.shared_utils.ip_addressing.mlag_l3_ip_primary()
        if self.mlag_role == "secondary":
            return self.shared_utils.ip_addressing.mlag_l3_ip_secondary()
        return None

    @cached_property
    def mlag_switch_ids(self) -> dict | None:
        """
        Returns the switch id's of both primary and secondary switches for a given node group.

        {"primary": int, "secondary": int}.
        """
        if self.mlag_role == "primary":
            if self.shared_utils.id is None:
                msg = f"'id' is not set on '{self.shared_utils.hostname}' and is required to compute MLAG ids"
                raise AristaAvdInvalidInputsError(msg)
            return {"primary": self.shared_utils.id, "secondary": self.mlag_peer_id}
        if self.mlag_role == "secondary":
            if self.shared_utils.id is None:
                msg = f"'id' is not set on '{self.shared_utils.hostname}' and is required to compute MLAG ids"
                raise AristaAvdInvalidInputsError(msg)
            return {"primary": self.mlag_peer_id, "secondary": self.shared_utils.id}
        return None

    @cached_property
    def mlag_port_channel_id(self) -> int:
        if not self.mlag_interfaces:
            msg = f"'mlag_interfaces' not set on '{self.shared_utils.hostname}."
            raise AristaAvdInvalidInputsError(msg)
        default_mlag_port_channel_id = int("".join(findall(r"\d", self.mlag_interfaces[0])))
        return default(self.shared_utils.node_config.mlag_port_channel_id, default_mlag_port_channel_id)

    @cached_property
    def mlag_peer_port_channel_id(self) -> int:
        return get(self.mlag_peer_facts, "mlag_port_channel_id", default=self.mlag_port_channel_id)

    @cached_property
    def mlag_peer_interfaces(self) -> list:
        return get(self.mlag_peer_facts, "mlag_interfaces", default=self.mlag_interfaces)

    @cached_property
    def mlag_ibgp_ip(self) -> str:
        if self.mlag_l3_ip is not None:
            return self.mlag_l3_ip

        return self.mlag_ip

    @cached_property
    def mlag_peer_ibgp_ip(self) -> str:
        if self.mlag_peer_l3_ip is not None:
            return self.mlag_peer_l3_ip

        return self.mlag_peer_ip
