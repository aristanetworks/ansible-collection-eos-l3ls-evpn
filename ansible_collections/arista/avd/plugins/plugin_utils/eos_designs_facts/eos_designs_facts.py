from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .mlag import MlagMixin
from .overlay import OverlayMixin
from .short_esi import ShortEsiMixin
from .uplinks import UplinksMixin
from .vlans import VlansMixin


class EosDesignsFacts(AvdFacts, MlagMixin, ShortEsiMixin, OverlayMixin, UplinksMixin, VlansMixin):
    """
    `EosDesignsFacts` is based on `AvdFacts`, so make sure to read the description there first.

    The class is instantiated once per device. Methods may use references to other device instances using `hostvars.avd_switch_facts`,
    which is a dict of `EosDesignsfacts` instances covering all devices.

    hostvars["switch"] is set to self, to allow `shared_utils` to work the same when they are called from `EosDesignsFacts` or from
    `AvdStructuredConfig`.
    """

    def __init__(self, hostvars, templar):
        # Add reference to this instance of EosDesignsFacts object inside hostvars.
        # This is used to allow templates to access the facts object directly with "switch.*"
        hostvars["switch"] = self

        shared_utils = SharedUtils(hostvars=hostvars, templar=templar)
        super().__init__(hostvars=hostvars, shared_utils=shared_utils)

    @cached_property
    def id(self) -> int | None:
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.id

    @cached_property
    def type(self) -> str:
        """
        Exposed in avd_switch_facts

        switch.type fact set based on type variable
        """
        return self.shared_utils.type

    @cached_property
    def platform(self) -> str | None:
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.platform

    @cached_property
    def is_deployed(self) -> bool:
        """
        Exposed in avd_switch_facts
        """
        return get(self._hostvars, "is_deployed", default=True)

    @cached_property
    def serial_number(self) -> str | None:
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.serial_number

    @cached_property
    def mgmt_interface(self) -> str | None:
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.mgmt_interface

    @cached_property
    def mgmt_ip(self) -> str | None:
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.mgmt_ip

    @cached_property
    def mpls_lsr(self) -> bool:
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.mpls_lsr

    @cached_property
    def evpn_multicast(self) -> bool | None:
        """
        Exposed in avd_switch_facts

        This method _must_ be in EosDesignsFacts and not in SharedUtils, since it reads the SharedUtils instance on the peer.
        This is only possible when running from EosDesignsFacts, since this is the only time where we can access the actual
        python instance of EosDesignsFacts and not the simplified dict.
        """
        if "evpn" not in self.shared_utils.overlay_address_families:
            return None
        if get(self._hostvars, "evpn_multicast") is True and self.shared_utils.vtep is True:
            if not (self.shared_utils.underlay_multicast is True and self.shared_utils.igmp_snooping_enabled is not False):
                raise AristaAvdError(
                    "'evpn_multicast: True' is only supported in combination with 'underlay_multicast: True' and 'igmp_snooping_enabled : True'"
                )
            elif self.shared_utils.mlag is True:
                peer_eos_designs_facts: EosDesignsFacts = self.shared_utils.mlag_peer_facts
                if self.shared_utils.overlay_rd_type_admin_subfield == peer_eos_designs_facts.shared_utils.overlay_rd_type_admin_subfield:
                    raise AristaAvdError(
                        "For MLAG devices Route Distinguisher must be unique when 'evpn_multicast: True' since it will create a multi-vtep configuration."
                    )
            return True
        return None

    @cached_property
    def loopback_ipv4_pool(self) -> str | None:
        """
        Exposed in avd_switch_facts
        """
        if self.shared_utils.underlay_router is True:
            return get(self.shared_utils.switch_data_combined, "loopback_ipv4_pool", required=True)
        return None

    @cached_property
    def uplink_ipv4_pool(self) -> str | None:
        """
        Exposed in avd_switch_facts
        """
        if self.shared_utils.underlay_router is True:
            return get(self.shared_utils.switch_data_combined, "uplink_ipv4_pool")
        return None

    @cached_property
    def bgp_as(self) -> str | None:
        """
        Exposed in avd_switch_facts
        """
        if self.shared_utils.underlay_router is True:
            return self.shared_utils.bgp_as

    @cached_property
    def underlay_routing_protocol(self) -> str:
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.underlay_routing_protocol

    @cached_property
    def vtep_loopback_ipv4_pool(self) -> str | None:
        """
        Exposed in avd_switch_facts
        """
        if self.shared_utils.vtep is True:
            return get(self.shared_utils.switch_data_combined, "vtep_loopback_ipv4_pool", required=True)
        return None

    @cached_property
    def inband_management_subnet(self) -> str | None:
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.inband_management_subnet

    @cached_property
    def inband_management_vlan(self) -> int | None:
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.inband_management_vlan
