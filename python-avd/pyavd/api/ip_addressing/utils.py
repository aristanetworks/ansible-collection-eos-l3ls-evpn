# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import get
from pyavd.j2filters import range_expand

if TYPE_CHECKING:
    from . import AvdIpAddressing


class UtilsMixin:
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to an AvdIpAddressing class.
    """

    @cached_property
    def _mlag_primary_id(self: AvdIpAddressing) -> int:
        if self.shared_utils.mlag_switch_ids is None or self.shared_utils.mlag_switch_ids.get("primary") is None:
            msg = "'mlag_switch_ids' is required to calculate MLAG IP addresses."
            raise AristaAvdInvalidInputsError(msg)
        return self.shared_utils.mlag_switch_ids["primary"]

    @cached_property
    def _mlag_secondary_id(self: AvdIpAddressing) -> int:
        if self.shared_utils.mlag_switch_ids is None or self.shared_utils.mlag_switch_ids.get("secondary") is None:
            msg = "'mlag_switch_ids' is required to calculate MLAG IP addresses."
            raise AristaAvdInvalidInputsError(msg)
        return self.shared_utils.mlag_switch_ids["secondary"]

    @cached_property
    def _mlag_peer_ipv4_pool(self: AvdIpAddressing) -> str:
        return self.shared_utils.mlag_peer_ipv4_pool

    @cached_property
    def _mlag_peer_ipv6_pool(self: AvdIpAddressing) -> str:
        return self.shared_utils.mlag_peer_ipv6_pool

    @cached_property
    def _mlag_peer_l3_ipv4_pool(self: AvdIpAddressing) -> str:
        return self.shared_utils.mlag_peer_l3_ipv4_pool

    @cached_property
    def _uplink_ipv4_pool(self: AvdIpAddressing) -> str:
        if self.shared_utils.node_config.uplink_ipv4_pool is None:
            msg = "'uplink_ipv4_pool' is required to calculate uplink IP addresses."
            raise AristaAvdInvalidInputsError(msg)
        return self.shared_utils.node_config.uplink_ipv4_pool

    @cached_property
    def _id(self: AvdIpAddressing) -> int:
        if self.shared_utils.id is None:
            msg = "'id' is required to calculate IP addresses."
            raise AristaAvdInvalidInputsError(msg)
        return self.shared_utils.id

    @cached_property
    def _max_uplink_switches(self: AvdIpAddressing) -> int:
        return self.shared_utils.max_uplink_switches

    @cached_property
    def _max_parallel_uplinks(self: AvdIpAddressing) -> int:
        return self.shared_utils.node_config.max_parallel_uplinks

    @cached_property
    def _loopback_ipv4_address(self: AvdIpAddressing) -> str | None:
        return self.shared_utils.node_config.loopback_ipv4_address

    @cached_property
    def _loopback_ipv4_pool(self: AvdIpAddressing) -> str:
        return self.shared_utils.loopback_ipv4_pool

    @cached_property
    def _loopback_ipv4_offset(self: AvdIpAddressing) -> int:
        return self.shared_utils.node_config.loopback_ipv4_offset

    @cached_property
    def _loopback_ipv6_pool(self: AvdIpAddressing) -> str:
        return self.shared_utils.loopback_ipv6_pool

    @cached_property
    def _loopback_ipv6_offset(self: AvdIpAddressing) -> int:
        return self.shared_utils.node_config.loopback_ipv6_offset

    @cached_property
    def _vtep_loopback_ipv4_address(self: AvdIpAddressing) -> str | None:
        return self.shared_utils.node_config.vtep_loopback_ipv4_address

    @cached_property
    def _vtep_loopback_ipv4_pool(self: AvdIpAddressing) -> str:
        return self.shared_utils.vtep_loopback_ipv4_pool

    @cached_property
    def _mlag_odd_id_based_offset(self: AvdIpAddressing) -> int:
        """
        Return the subnet offset for an MLAG pair based on odd id.

        Requires a pair of odd and even IDs
        """
        # Verify a mix of odd and even IDs
        if (self._mlag_primary_id % 2) == (self._mlag_secondary_id % 2):
            msg = "MLAG compact addressing mode requires all MLAG pairs to have a single odd and even ID"
            raise AristaAvdError(msg)

        odd_id = self._mlag_primary_id
        if odd_id % 2 == 0:
            odd_id = self._mlag_secondary_id

        return int((odd_id - 1) / 2)

    def _get_downlink_ipv4_pool_and_offset(self: AvdIpAddressing, uplink_switch_index: int) -> tuple[str, int]:
        """
        Returns the downlink IP pool and offset as a tuple according to the uplink_switch_index.

        Offset is the matching interface's index in the list of downlink_interfaces
        (None, None) is returned if downlink_pools are not used
        """
        uplink_switch_interface = self.shared_utils.uplink_switch_interfaces[uplink_switch_index]
        uplink_switch = self.shared_utils.uplink_switches[uplink_switch_index]
        peer_facts = self.shared_utils.get_peer_facts(uplink_switch, required=True)
        downlink_pools = get(peer_facts, "downlink_pools")

        if not downlink_pools:
            return (None, None)

        for downlink_pool_and_interfaces in downlink_pools:
            downlink_interfaces = range_expand(get(downlink_pool_and_interfaces, "downlink_interfaces"))

            for interface_index, downlink_interface in enumerate(downlink_interfaces):
                if uplink_switch_interface == downlink_interface:
                    return (get(downlink_pool_and_interfaces, "ipv4_pool"), interface_index)

        # If none of the interfaces match up, throw error
        msg = (
            f"'downlink_pools' was defined at uplink_switch, but one of the 'uplink_switch_interfaces' ({uplink_switch_interface}) "
            "in the downlink_switch does not match any of the downlink_pools"
        )
        raise AristaAvdError(msg)

    def _get_p2p_ipv4_pool_and_offset(self: AvdIpAddressing, uplink_switch_index: int) -> tuple[str, int]:
        """
        Returns IP pool and offset as a tuple according to the uplink_switch_index.

        Uplink pool or downlink pool is returned with its corresponding offset
        A downlink pool's offset is the matching interface's index in the list of downlink_interfaces
        A uplink pool's offset is `((id - 1) * 2 * max_uplink_switches * max_parallel_uplinks) + (uplink_switch_index * 2) + 1`

        One and only one of these pools are required to be set, otherwise an error will be thrown
        """
        uplink_pool = self.shared_utils.node_config.uplink_ipv4_pool
        if uplink_pool is not None:
            uplink_offset = ((self._id - 1) * self._max_uplink_switches * self._max_parallel_uplinks) + uplink_switch_index

        downlink_pool, downlink_offset = self._get_downlink_ipv4_pool_and_offset(uplink_switch_index)

        if uplink_pool is not None and downlink_pool is not None:
            msg = (
                f"Unable to assign IPs for uplinks. 'uplink_ipv4_pool' ({uplink_pool}) on this switch cannot be combined "
                f"with 'downlink_pools' ({downlink_pool}) on any uplink switch."
            )
            raise AristaAvdError(msg)

        if uplink_pool is None and downlink_pool is None:
            msg = "Unable to assign IPs for uplinks. Either 'uplink_ipv4_pool' on this switch or 'downlink_pools' on all the uplink switches must be set."
            raise AristaAvdInvalidInputsError(msg)

        if uplink_pool is not None:
            return (uplink_pool, uplink_offset)

        return (downlink_pool, downlink_offset)
