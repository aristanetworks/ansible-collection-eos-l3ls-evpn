# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError
from pyavd._utils import append_if_not_duplicate
from pyavd.j2filters import list_compress, natural_sort, range_expand

if TYPE_CHECKING:
    from . import EosDesignsFacts


class UplinksMixin:
    """
    Mixin Class used to generate some of the EosDesignsFacts.

    Class should only be used as Mixin to the EosDesignsFacts class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def max_parallel_uplinks(self: EosDesignsFacts) -> int:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.node_config.max_parallel_uplinks

    @cached_property
    def max_uplink_switches(self: EosDesignsFacts) -> int:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.max_uplink_switches

    @cached_property
    def _uplink_port_channel_id(self: EosDesignsFacts) -> int:
        """
        For MLAG secondary get the uplink_port_channel_id from the peer's facts.

        We don't need to validate it (1-2000), since it will be validated on the peer.

        For MLAG primary or none MLAG, take the value of 'uplink_port_channel_id' if set,
        or use the numbers from the first interface in 'uplink_interfaces'.

        For MLAG primary validate that the port-channel id falls within 1-2000 since we also use this ID as MLAG ID.
        """
        uplink_port_channel_id = self.shared_utils.node_config.uplink_port_channel_id

        if self.shared_utils.mlag_role == "secondary":
            # MLAG Secondary
            peer_uplink_port_channel_id = self.shared_utils.mlag_peer_facts._uplink_port_channel_id
            # check that port-channel IDs are the same as on primary
            if uplink_port_channel_id is not None and uplink_port_channel_id != peer_uplink_port_channel_id:
                msg = (
                    f"'uplink_port_channel_id' is set to {uplink_port_channel_id} and is not matching {peer_uplink_port_channel_id} set on MLAG peer."
                    " The 'uplink_port_channel_id' must be matching on MLAG peers."
                )
                raise AristaAvdError(msg)
            return peer_uplink_port_channel_id

        # MLAG Primary or not MLAG.
        if uplink_port_channel_id is None:
            # Overwriting uplink_port_channel_id
            uplink_port_channel_id = int("".join(re.findall(r"\d", self.shared_utils.uplink_interfaces[0])))

        # produce an error if the switch is MLAG and port-channel ID is above 2000
        if self.shared_utils.mlag and not 1 <= uplink_port_channel_id <= 2000:
            msg = f"'uplink_port_channel_id' must be between 1 and 2000 for MLAG switches. Got '{uplink_port_channel_id}'."
            raise AristaAvdError(msg)

        return uplink_port_channel_id

    @cached_property
    def _uplink_switch_port_channel_id(self: EosDesignsFacts) -> int:
        """
        For MLAG secondary get the uplink_switch_port_channel_id from the peer's facts.

        We don't need to validate it (1-2000), since it will be validated on the peer.

        For MLAG primary or none MLAG, take the value of 'uplink_switch_port_channel_id' if set,
        or use the numbers from the first interface in 'uplink_switch_interfaces'.

        If the *uplink_switch* is in MLAG,  validate that the port-channel id falls within 1-2000
        since we also use this ID as MLAG ID on the *uplink switch*.
        """
        uplink_switch_port_channel_id = self.shared_utils.node_config.uplink_switch_port_channel_id

        if self.shared_utils.mlag_role == "secondary":
            # MLAG Secondary
            peer_uplink_switch_port_channel_id = self.shared_utils.mlag_peer_facts._uplink_switch_port_channel_id
            # check that port-channel IDs are the same as on primary
            if uplink_switch_port_channel_id is not None and uplink_switch_port_channel_id != peer_uplink_switch_port_channel_id:
                msg = (
                    f"'uplink_switch_port_channel_id' is set to {uplink_switch_port_channel_id} and is not matching {peer_uplink_switch_port_channel_id} "
                    "set on MLAG peer. The 'uplink_switch_port_channel_id' must be matching on MLAG peers."
                )
                raise AristaAvdError(msg)
            return peer_uplink_switch_port_channel_id

        # MLAG Primary or not MLAG.
        if uplink_switch_port_channel_id is None:
            # Overwriting uplink_switch_port_channel_id
            uplink_switch_port_channel_id = int("".join(re.findall(r"\d", self.shared_utils.uplink_switch_interfaces[0])))

        # produce an error if the uplink switch is MLAG and port-channel ID is above 2000
        uplink_switch_facts: EosDesignsFacts = self.shared_utils.get_peer_facts(self.shared_utils.uplink_switches[0], required=True)

        if uplink_switch_facts.shared_utils.mlag and not 1 <= uplink_switch_port_channel_id <= 2000:
            msg = f"'uplink_switch_port_channel_id' must be between 1 and 2000 for MLAG switches. Got '{uplink_switch_port_channel_id}'."
            raise AristaAvdError(msg)

        return uplink_switch_port_channel_id

    @cached_property
    def uplinks(self: EosDesignsFacts) -> list:
        """
        Exposed in avd_switch_facts.

        List of uplinks with all parameters

        These facts are leveraged by templates for this device when rendering uplinks
        and by templates for peer devices when rendering downlinks
        """
        if self.shared_utils.uplink_type == "p2p":
            get_uplink = self._get_p2p_uplink
        elif self.shared_utils.uplink_type == "port-channel":
            get_uplink = self._get_port_channel_uplink
        elif self.shared_utils.uplink_type == "p2p-vrfs":
            if self.shared_utils.network_services_l3 is False or self.shared_utils.underlay_router is False:
                msg = "'underlay_router' and 'network_services.l3' must be 'true' for the node_type_key when using 'p2p-vrfs' as 'uplink_type'."
                raise AristaAvdError(msg)
            get_uplink = self._get_p2p_vrfs_uplink
        elif self.shared_utils.uplink_type == "lan":
            if self.shared_utils.network_services_l3 is False or self.shared_utils.underlay_router is False:
                msg = "'underlay_router' and 'network_services.l3' must be 'true' for the node_type_key when using 'lan' as 'uplink_type'."
                raise AristaAvdError(msg)
            if len(self.shared_utils.uplink_interfaces) > 1:
                msg = f"'uplink_type: lan' only supports a single uplink interface. Got {self.shared_utils.uplink_interfaces}."
                raise AristaAvdError(msg)
                # TODO: Adjust error message when we add lan-port-channel support.
                # uplink_type: lan' only supports a single uplink interface.
                # Got {self._uplink_interfaces}. Consider 'uplink_type: lan-port-channel' if applicable.
            get_uplink = self._get_l2_uplink
        else:
            msg = f"Invalid uplink_type '{self.shared_utils.uplink_type}'."
            raise AristaAvdError(msg)

        uplinks = []
        uplink_switches = self.shared_utils.uplink_switches
        uplink_switch_interfaces = self.shared_utils.uplink_switch_interfaces
        for uplink_index, uplink_interface in enumerate(self.shared_utils.uplink_interfaces):
            if len(uplink_switches) <= uplink_index or len(uplink_switch_interfaces) <= uplink_index:
                # Invalid length of input variables. Skipping
                continue

            uplink_switch = uplink_switches[uplink_index]
            uplink_switch_interface = uplink_switch_interfaces[uplink_index]
            if uplink_switch is None or uplink_switch not in self.shared_utils.all_fabric_devices:
                # Invalid uplink_switch. Skipping.
                continue

            if (uplink := get_uplink(uplink_index, uplink_interface, uplink_switch, uplink_switch_interface)) is not None:
                uplinks.append(uplink)

        return uplinks

    def _get_p2p_uplink(self: EosDesignsFacts, uplink_index: int, uplink_interface: str, uplink_switch: str, uplink_switch_interface: str) -> dict:
        """Return a single uplink dictionary for uplink_type p2p."""
        uplink_switch_facts: EosDesignsFacts = self.shared_utils.get_peer_facts(uplink_switch, required=True)
        uplink = {
            "interface": uplink_interface,
            "peer": uplink_switch,
            "peer_interface": uplink_switch_interface,
            "peer_type": uplink_switch_facts.type,
            "peer_is_deployed": uplink_switch_facts.is_deployed,
            "peer_bgp_as": uplink_switch_facts.bgp_as,
            "type": "underlay_p2p",
        }
        if self.shared_utils.uplink_interface_speed is not None:
            uplink["speed"] = self.shared_utils.uplink_interface_speed

        if self.shared_utils.node_config.uplink_bfd:
            uplink["bfd"] = True

        if self.shared_utils.uplink_switch_interface_speed is not None:
            uplink["peer_speed"] = self.shared_utils.uplink_switch_interface_speed

        if self.shared_utils.node_config.uplink_ptp:
            uplink["ptp"] = {"enable": self.shared_utils.node_config.uplink_ptp.enable}
        elif self.shared_utils.ptp_enabled:
            uplink["ptp"] = {"enable": True}

        if self.shared_utils.node_config.uplink_macsec.profile:
            uplink["mac_security"] = {"profile": self.shared_utils.node_config.uplink_macsec.profile}

        if self.shared_utils.underlay_multicast is True and uplink_switch_facts.shared_utils.underlay_multicast is True:
            uplink["underlay_multicast"] = True

        if self.inputs.underlay_rfc5549:
            uplink["ipv6_enable"] = True
        else:
            uplink["prefix_length"] = self.inputs.fabric_ip_addressing.p2p_uplinks.ipv4_prefix_length
            uplink["ip_address"] = self.shared_utils.ip_addressing.p2p_uplinks_ip(uplink_index)
            uplink["peer_ip_address"] = self.shared_utils.ip_addressing.p2p_uplinks_peer_ip(uplink_index)

        if self.shared_utils.link_tracking_groups is not None:
            uplink["link_tracking_groups"] = [{"name": lt_group["name"], "direction": "upstream"} for lt_group in self.shared_utils.link_tracking_groups]
        if self.shared_utils.node_config.uplink_structured_config is not None:
            uplink["structured_config"] = self.shared_utils.node_config.uplink_structured_config

        return uplink

    def _get_port_channel_uplink(self: EosDesignsFacts, uplink_index: int, uplink_interface: str, uplink_switch: str, uplink_switch_interface: str) -> dict:
        """Return a single uplink dictionary for uplink_type port-channel."""
        uplink_switch_facts: EosDesignsFacts = self.shared_utils.get_peer_facts(uplink_switch, required=True)

        # Reusing get_l2_uplink
        uplink = self._get_l2_uplink(uplink_index, uplink_interface, uplink_switch, uplink_switch_interface)

        if uplink_switch_facts.shared_utils.mlag is True or self._short_esi is not None:
            # Override our description on port-channel to be peer's group name if they are mlag pair or A/A #}
            uplink["peer_node_group"] = uplink_switch_facts.shared_utils.group

        # Used to determine whether or not port-channel should have an mlag id configure on the uplink_switch
        unique_uplink_switches = set(self.shared_utils.uplink_switches)
        if self.shared_utils.mlag is True:
            # Override the peer's description on port-channel to be our group name if we are mlag pair #}
            uplink["node_group"] = self.shared_utils.group

            # Updating unique_uplink_switches with our mlag peer's uplink switches
            unique_uplink_switches.update(self.shared_utils.mlag_peer_facts.shared_utils.uplink_switches)

        # Only enable mlag for this port-channel on the uplink switch if there are multiple unique uplink switches
        uplink["peer_mlag"] = len(unique_uplink_switches) > 1

        uplink["channel_group_id"] = str(self._uplink_port_channel_id)
        uplink["peer_channel_group_id"] = str(self._uplink_switch_port_channel_id)

        return uplink

    def _get_l2_uplink(
        self: EosDesignsFacts,
        uplink_index: int,  # pylint: disable=unused-argument # noqa: ARG002
        uplink_interface: str,
        uplink_switch: str,
        uplink_switch_interface: str,
    ) -> dict:
        """Return a single uplink dictionary for an L2 uplink. Reused for both uplink_type port-channel, lan and TODO: lan-port-channel."""
        uplink_switch_facts: EosDesignsFacts = self.shared_utils.get_peer_facts(uplink_switch, required=True)
        uplink = {
            "interface": uplink_interface,
            "peer": uplink_switch,
            "peer_interface": uplink_switch_interface,
            "peer_type": uplink_switch_facts.type,
            "peer_is_deployed": uplink_switch_facts.is_deployed,
            "type": "underlay_l2",
        }
        if self.shared_utils.uplink_interface_speed is not None:
            uplink["speed"] = self.shared_utils.uplink_interface_speed

        if self.shared_utils.uplink_switch_interface_speed is not None:
            uplink["peer_speed"] = self.shared_utils.uplink_switch_interface_speed

        if self.shared_utils.node_config.uplink_ptp:
            uplink["ptp"] = {"enable": self.shared_utils.node_config.uplink_ptp.enable}
        elif self.shared_utils.ptp_enabled:
            uplink["ptp"] = {"enable": True}

        # Remove vlans if upstream switch does not have them #}
        if self.inputs.enable_trunk_groups:
            uplink["trunk_groups"] = ["UPLINK"]
            if self.shared_utils.mlag is True:
                uplink["peer_trunk_groups"] = [self.shared_utils.group]
            else:
                uplink["peer_trunk_groups"] = [self.shared_utils.hostname]

        uplink_vlans = set(self._vlans)
        uplink_vlans = uplink_vlans.intersection(uplink_switch_facts._vlans)

        if self.shared_utils.configure_inband_mgmt or self.shared_utils.configure_inband_mgmt_ipv6:
            # Always add inband_mgmt_vlan even if the uplink switch does not have this vlan defined
            uplink_vlans.add(self.shared_utils.node_config.inband_mgmt_vlan)

        uplink["vlans"] = list_compress(list(uplink_vlans)) if uplink_vlans else "none"

        if uplink_native_vlan := self.shared_utils.node_config.uplink_native_vlan:
            uplink["native_vlan"] = uplink_native_vlan

        if self._short_esi is not None:
            uplink["peer_short_esi"] = self._short_esi

        if self.shared_utils.link_tracking_groups is not None:
            uplink["link_tracking_groups"] = [{"name": lt_group["name"], "direction": "upstream"} for lt_group in self.shared_utils.link_tracking_groups]

        if not self.shared_utils.network_services_l2:
            # This child device does not support VLANs, so we tell the peer to enable portfast
            uplink["peer_spanning_tree_portfast"] = "edge"

        if self.shared_utils.node_config.uplink_structured_config is not None:
            uplink["structured_config"] = self.shared_utils.node_config.uplink_structured_config

        return uplink

    def _get_p2p_vrfs_uplink(self: EosDesignsFacts, uplink_index: int, uplink_interface: str, uplink_switch: str, uplink_switch_interface: str) -> dict:
        """Return a single uplink dictionary for uplink_type p2p-vrfs."""
        uplink_switch_facts: EosDesignsFacts = self.shared_utils.get_peer_facts(uplink_switch, required=True)

        # Reusing regular p2p logic for main interface.
        uplink = self._get_p2p_uplink(uplink_index, uplink_interface, uplink_switch, uplink_switch_interface)
        uplink["subinterfaces"] = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                # Only keep VRFs present on the uplink switch as well.
                # Also skip VRF default since it is covered on the parent interface.
                # ok to use like this because this is only ever called inside EosDesignsFacts
                uplink_switch_vrfs = uplink_switch_facts.shared_utils.vrfs
                if vrf.name == "default" or vrf.name not in uplink_switch_vrfs:
                    continue

                vrf_id = self.shared_utils.get_vrf_id(vrf)
                subinterface = {
                    "interface": f"{uplink_interface}.{vrf_id}",
                    "peer_interface": f"{uplink_switch_interface}.{vrf_id}",
                    "vrf": vrf.name,
                    "encapsulation_dot1q_vlan": vrf_id,
                }

                if self.inputs.underlay_rfc5549:
                    subinterface["ipv6_enable"] = True
                else:
                    subinterface["prefix_length"] = self.inputs.fabric_ip_addressing.p2p_uplinks.ipv4_prefix_length
                    subinterface["ip_address"] = self.shared_utils.ip_addressing.p2p_vrfs_uplinks_ip(uplink_index, vrf.name)
                    subinterface["peer_ip_address"] = self.shared_utils.ip_addressing.p2p_vrfs_uplinks_peer_ip(uplink_index, vrf.name)

                if self.shared_utils.node_config.uplink_structured_config is not None:
                    subinterface["structured_config"] = self.shared_utils.node_config.uplink_structured_config

                append_if_not_duplicate(
                    uplink["subinterfaces"],
                    "vrf",
                    subinterface,
                    context="Uplink subinterfaces",
                    context_keys=["interface", "vrf"],
                    ignore_same_dict=True,
                )

        return uplink

    @cached_property
    def uplink_peers(self: EosDesignsFacts) -> list:
        """
        Exposed in avd_switch_facts.

        List of all **unique** uplink peers

        These are used to generate the "avd_topology_peers" fact covering downlinks for all devices.
        """
        # Since uplinks logic silently skips extra entries in uplink vars, we only need to parse shortest list.
        min_length = min(len(self.shared_utils.uplink_switch_interfaces), len(self.shared_utils.uplink_interfaces), len(self.shared_utils.uplink_switches))
        # Using set to only get unique uplink switches
        unique_uplink_switches = set(self.shared_utils.uplink_switches[:min_length])
        return natural_sort(unique_uplink_switches)

    @cached_property
    def _default_downlink_interfaces(self: EosDesignsFacts) -> list:
        """
        internal _default_downlink_interfaces set based on default_interfaces.

        Parsed by downstream switches during eos_designs_facts phase.
        """
        return range_expand(self.shared_utils.default_interfaces.downlink_interfaces)

    @cached_property
    def uplink_switch_vrfs(self: EosDesignsFacts) -> list[str] | None:
        """
        Exposed in avd_switch_facts.

        Return the list of VRF names present on uplink switches.
        """
        if self.shared_utils.uplink_type != "p2p-vrfs":
            return None

        vrfs = set()
        for uplink_switch in self.uplink_peers:
            uplink_switch_facts = self.shared_utils.get_peer_facts(uplink_switch)
            vrfs.update(uplink_switch_facts.shared_utils.vrfs)

        return natural_sort(vrfs) or None
