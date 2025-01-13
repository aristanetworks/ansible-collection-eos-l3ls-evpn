# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from functools import cached_property

from pyavd.api.ip_addressing import AvdIpAddressing


class CustomAvdIpAddressing(AvdIpAddressing):
    @cached_property
    def _custom_ip_offset_10(self) -> int:
        return int(self._hostvars.get("ip_offset_10", 0))

    @cached_property
    def _custom_ip_offset_10_subnets(self) -> int:
        """
        The jinja code did a blind addition of 10 to the resulting IP even for subnets.

        Here we divide the offset with two, since we are calculating /31 subnets more intelligently.
        """
        return int(self._custom_ip_offset_10 / 2)

    @cached_property
    def _custom_ip_offset_20(self) -> int:
        return int(self._hostvars.get("ip_offset_20", 0))

    @cached_property
    def _custom_ip_offset_20_subnets(self) -> int:
        """
        The jinja code did a blind addition of 20 to the resulting IP even for subnets.

        Here we divide the offset with two, since we are calculating /31 subnets more intelligently.
        """
        return int(self._custom_ip_offset_20 / 2)

    def mlag_ibgp_peering_ip_primary(self, mlag_ibgp_peering_ipv4_pool: str) -> str:
        """
        Implementation of custom code similar to jinja.

        {{ vrf.mlag_ibgp_peering_ipv4_pool | ansible.utils.ipaddr('subnet') |
           ansible.utils.ipmath((switch.mlag_switch_ids.primary - 1) * 2 + ip_offset_10) }}.
        """
        offset = self._mlag_primary_id - 1 + self._custom_ip_offset_10_subnets
        return self._ip(mlag_ibgp_peering_ipv4_pool, 31, offset, 0)

    def mlag_ibgp_peering_ip_secondary(self, mlag_ibgp_peering_ipv4_pool: str) -> str:
        """
        Implementation of custom code similar to jinja.

        {{ vrf.mlag_ibgp_peering_ipv4_pool | ansible.utils.ipaddr('subnet') |
           ansible.utils.ipmath(((switch.mlag_switch_ids.primary - 1) * 2) + 1 + ip_offset_10) }}.
        """
        offset = self._mlag_primary_id - 1 + self._custom_ip_offset_10_subnets
        return self._ip(mlag_ibgp_peering_ipv4_pool, 31, offset, 1)

    def mlag_ip_primary(self) -> str:
        """
        Implementation of custom code similar to jinja.

        {{ switch_data.combined.mlag_peer_ipv4_pool | ansible.utils.ipaddr('network') |
           ansible.utils.ipmath((mlag_primary_id - 1) * 2 + ip_offset_10) }}
        """
        offset = self._mlag_primary_id - 1 + self._custom_ip_offset_10_subnets
        return self._ip(self._mlag_peer_ipv4_pool, 31, offset, 0)

    def mlag_ip_secondary(self) -> str:
        """
        Implementation of custom code similar to jinja.

        {{ switch_data.combined.mlag_peer_ipv4_pool | ansible.utils.ipaddr('network') |
           ansible.utils.ipmath(((mlag_primary_id - 1) * 2) + 1 + ip_offset_10) }}
        """
        offset = self._mlag_primary_id - 1 + self._custom_ip_offset_10_subnets
        return self._ip(self._mlag_peer_ipv4_pool, 31, offset, 1)

    def mlag_l3_ip_primary(self) -> str:
        """
        Implementation of custom code similar to jinja.

        {{ switch_data.combined.mlag_peer_l3_ipv4_pool | ansible.utils.ipaddr('network') |
           ansible.utils.ipmath((mlag_primary_id - 1) * 2 + ip_offset_10) }}
        """
        offset = self._mlag_primary_id - 1 + self._custom_ip_offset_10_subnets
        return self._ip(self._mlag_peer_l3_ipv4_pool, 31, offset, 0)

    def mlag_l3_ip_secondary(self) -> str:
        """
        Implementation of custom code similar to jinja.

        {{ switch_data.combined.mlag_peer_l3_ipv4_pool | ansible.utils.ipaddr('network') |
           ansible.utils.ipmath(((mlag_primary_id - 1) * 2) + 1 + ip_offset_10) }}
        """
        offset = self._mlag_primary_id - 1 + self._custom_ip_offset_10_subnets
        return self._ip(self._mlag_peer_l3_ipv4_pool, 31, offset, 1)

    def p2p_uplinks_ip(self, uplink_switch_index: int) -> str:
        """
        Implementation of custom code similar to jinja.

        {{ switch.uplink_ipv4_pool | ansible.utils.ipaddr('network') | ansible.utils.ipmath(((switch.id -1)
           * 2 * switch.max_uplink_switches * switch.max_parallel_uplinks) + (uplink_switch_index) * 2 + 1 + ip_offset_20) }}
        """
        offset = ((self._id - 1) * self._max_uplink_switches * self._max_parallel_uplinks) + uplink_switch_index + self._custom_ip_offset_20_subnets
        return self._ip(self._uplink_ipv4_pool, 31, offset, 1)

    def p2p_uplinks_peer_ip(self, uplink_switch_index: int) -> str:
        """
        Implementation of custom code similar to jinja.

        {{ switch.uplink_ipv4_pool | ansible.utils.ipaddr('network') | ansible.utils.ipmath(((switch.id -1)
           * 2 * switch.max_uplink_switches * switch.max_parallel_uplinks) + (uplink_switch_index) * 2 + ip_offset_20) }}
        """
        offset = ((self._id - 1) * self._max_uplink_switches * self._max_parallel_uplinks) + uplink_switch_index + self._custom_ip_offset_20_subnets
        return self._ip(self._uplink_ipv4_pool, 31, offset, 0)

    def p2p_vrfs_uplinks_ip(self, uplink_switch_index: int, vrf: str) -> str:
        """
        Implementation of custom code to override IP addressing on VRF uplinks.

        We read the uplink pool from a custom dict `custom_ip_pools_for_vrfs.<vrf>` - Note no error handling in this example.
        """
        offset = ((self._id - 1) * self._max_uplink_switches * self._max_parallel_uplinks) + uplink_switch_index + self._custom_ip_offset_20_subnets

        vrf_pool = self._hostvars["custom_ip_pools_for_vrfs"][vrf]
        return self._ip(vrf_pool, 31, offset, 1)

    def p2p_vrfs_uplinks_peer_ip(self, uplink_switch_index: int, vrf: str) -> str:
        """
        Implementation of custom code to override IP addressing on VRF downlinks.

        We read the uplink pool from a custom dict `custom_ip_pools_for_vrfs.<vrf>` - Note no error handling in this example.
        """
        offset = ((self._id - 1) * self._max_uplink_switches * self._max_parallel_uplinks) + uplink_switch_index + self._custom_ip_offset_20_subnets
        vrf_pool = self._hostvars["custom_ip_pools_for_vrfs"][vrf]
        return self._ip(vrf_pool, 31, offset, 0)

    def router_id(self) -> str:
        """
        Implementation of custom code similar to jinja.

        {{ loopback_ipv4_pool | ansible.utils.ipaddr("network") |
           ansible.utils.ipmath(switch_id + loopback_ipv4_offset + ip_offset_20) }}
        """
        offset = self._id + self._loopback_ipv4_offset + self._custom_ip_offset_20
        return self._ip(self._loopback_ipv4_pool, 32, offset, 0)

    def ipv6_router_id(self) -> str:
        """
        Implementation of custom code similar to jinja.

        {{ loopback_ipv6_pool | ansible.utils.ipaddr("network") |
           ansible.utils.ipmath(switch_id + loopback_ipv6_offset + ip_offset_20) }}
        """
        offset = self._id + self._loopback_ipv6_offset + self._custom_ip_offset_20
        return self._ip(self._loopback_ipv6_pool, 128, offset, 0)

    def vtep_ip_mlag(self) -> str:
        """
        Implementation of custom code similar to jinja.

        {{ switch_vtep_loopback_ipv4_pool | ansible.utils.ipaddr('network') |
           ansible.utils.ipmath(mlag_primary_id + loopback_ipv4_offset + ip_offset_20) }}
        """
        offset = self._mlag_primary_id + self._loopback_ipv4_offset + self._custom_ip_offset_20
        return self._ip(self._vtep_loopback_ipv4_pool, 32, offset, 0)

    def vtep_ip(self) -> str:
        """
        Implementation of custom code similar to jinja.

        {{ switch_vtep_loopback_ipv4_pool | ansible.utils.ipaddr('network') |
           ansible.utils.ipmath(switch_id + loopback_ipv4_offset + ip_offset_20) }}
        """
        offset = self._id + self._loopback_ipv4_offset + self._custom_ip_offset_20
        return self._ip(self._vtep_loopback_ipv4_pool, 32, offset, 0)
