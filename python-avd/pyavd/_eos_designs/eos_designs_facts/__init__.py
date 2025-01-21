# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from pyavd._eos_designs.avdfacts import AvdFacts
from pyavd._errors import AristaAvdError

from .mlag import MlagMixin
from .overlay import OverlayMixin
from .short_esi import ShortEsiMixin
from .uplinks import UplinksMixin
from .vlans import VlansMixin
from .wan import WanMixin


class EosDesignsFacts(AvdFacts, MlagMixin, ShortEsiMixin, OverlayMixin, WanMixin, UplinksMixin, VlansMixin):
    """
    `EosDesignsFacts` is based on `AvdFacts`, so make sure to read the description there first.

    The class is instantiated once per device. Methods may use references to other device instances using `hostvars.avd_switch_facts`,
    which is a dict of `EosDesignsfacts` instances covering all devices.
    """

    @cached_property
    def id(self) -> int | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.id

    @cached_property
    def type(self) -> str:
        """
        Exposed in avd_switch_facts.

        switch.type fact set based on type variable
        """
        return self.shared_utils.type

    @cached_property
    def platform(self) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.platform

    @cached_property
    def is_deployed(self) -> bool:
        """Exposed in avd_switch_facts."""
        return self.inputs.is_deployed

    @cached_property
    def serial_number(self) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.serial_number

    @cached_property
    def mgmt_interface(self) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.mgmt_interface

    @cached_property
    def mgmt_ip(self) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.node_config.mgmt_ip

    @cached_property
    def mpls_lsr(self) -> bool:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.mpls_lsr

    @cached_property
    def evpn_multicast(self) -> bool | None:
        """
        Exposed in avd_switch_facts.

        This method _must_ be in EosDesignsFacts and not in SharedUtils, since it reads the SharedUtils instance on the peer.
        This is only possible when running from EosDesignsFacts, since this is the only time where we can access the actual
        python instance of EosDesignsFacts and not the simplified dict.
        """
        if "evpn" not in self.shared_utils.overlay_address_families:
            return None
        if self.inputs.evpn_multicast and self.shared_utils.vtep:
            if not (self.shared_utils.underlay_multicast and self.shared_utils.igmp_snooping_enabled):
                msg = "'evpn_multicast: True' is only supported in combination with 'underlay_multicast: True' and 'igmp_snooping_enabled : True'"
                raise AristaAvdError(msg)

            if self.shared_utils.mlag is True:
                peer_eos_designs_facts: EosDesignsFacts = self.shared_utils.mlag_peer_facts
                if self.shared_utils.overlay_rd_type_admin_subfield == peer_eos_designs_facts.shared_utils.overlay_rd_type_admin_subfield:
                    msg = "For MLAG devices Route Distinguisher must be unique when 'evpn_multicast: True' since it will create a multi-vtep configuration."
                    raise AristaAvdError(msg)
            return True
        return None

    @cached_property
    def loopback_ipv4_pool(self) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.underlay_router:
            return self.shared_utils.loopback_ipv4_pool
        return None

    @cached_property
    def uplink_ipv4_pool(self) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.underlay_router:
            return self.shared_utils.node_config.uplink_ipv4_pool
        return None

    @cached_property
    def downlink_pools(self) -> list | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.underlay_router:
            return [downlink_pool._as_dict() for downlink_pool in self.shared_utils.node_config.downlink_pools]
        return None

    @cached_property
    def bgp_as(self) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.underlay_router is True:
            return self.shared_utils.bgp_as
        return None

    @cached_property
    def underlay_routing_protocol(self) -> str:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.underlay_routing_protocol

    @cached_property
    def vtep_loopback_ipv4_pool(self) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.vtep is True:
            return self.shared_utils.vtep_loopback_ipv4_pool
        return None

    @cached_property
    def inband_mgmt_subnet(self) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.configure_parent_for_inband_mgmt:
            return self.shared_utils.node_config.inband_mgmt_subnet
        return None

    @cached_property
    def inband_mgmt_ipv6_subnet(self) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.configure_parent_for_inband_mgmt_ipv6:
            return self.shared_utils.node_config.inband_mgmt_ipv6_subnet
        return None

    @cached_property
    def inband_mgmt_vlan(self) -> int | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.configure_parent_for_inband_mgmt or self.shared_utils.configure_parent_for_inband_mgmt_ipv6:
            return self.shared_utils.node_config.inband_mgmt_vlan
        return None

    @cached_property
    def inband_ztp(self) -> bool | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.node_config.inband_ztp

    @cached_property
    def inband_ztp_vlan(self) -> int | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.node_config.inband_ztp:
            return self.shared_utils.node_config.inband_mgmt_vlan
        return None

    @cached_property
    def inband_ztp_lacp_fallback_delay(self) -> int | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.node_config.inband_ztp:
            return self.shared_utils.node_config.inband_ztp_lacp_fallback_delay
        return None

    @cached_property
    def dc_name(self) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.inputs.dc_name

    @cached_property
    def group(self) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.group

    @cached_property
    def router_id(self) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.router_id

    @cached_property
    def inband_mgmt_ip(self) -> str | None:
        """
        Exposed in avd_switch_facts.

        Used for fabric docs
        """
        return self.shared_utils.inband_mgmt_ip

    @cached_property
    def inband_mgmt_interface(self) -> str | None:
        """
        Exposed in avd_switch_facts.

        Used for fabric docs
        """
        return self.shared_utils.inband_mgmt_interface

    @cached_property
    def pod(self) -> str:
        """
        Exposed in avd_switch_facts.

        Used for fabric docs
        """
        return self.inputs.pod_name or self.inputs.dc_name or self.shared_utils.fabric_name

    @cached_property
    def connected_endpoints_keys(self) -> list[dict]:
        """
        List of connected_endpoints_keys in use on this device.

        Exposed in avd_switch_facts.

        Used for fabric docs
        """
        return [entry._as_dict() for entry in self.inputs.connected_endpoints_keys if entry.key in self.inputs._dynamic_keys.connected_endpoints]

    @cached_property
    def port_profile_names(self) -> list:
        """
        Exposed in avd_switch_facts.

        Used for fabric docs
        """
        return [{"profile": profile.profile, "parent_profile": profile.parent_profile} for profile in self.inputs.port_profiles]
