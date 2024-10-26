# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import append_if_not_duplicate, default, get, strip_empties_from_dict
from pyavd.api.interface_descriptions import InterfaceDescriptionData

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class VlanInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def vlan_interfaces(self: AvdStructuredConfigNetworkServices) -> list | None:
        """
        Return structured config for vlan_interfaces.

        Consist of svis and mlag peering vlans from filtered tenants
        """
        if not (self.shared_utils.network_services_l2 and self.shared_utils.network_services_l3):
            return None

        vlan_interfaces = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant["vrfs"]:
                for svi in vrf["svis"]:
                    vlan_interface = self._get_vlan_interface_config_for_svi(svi, vrf)
                    append_if_not_duplicate(
                        list_of_dicts=vlan_interfaces,
                        primary_key="name",
                        new_dict=vlan_interface,
                        context="VLAN Interfaces",
                        context_keys=["name", "tenant"],
                        ignore_keys={"tenant"},
                    )

                # MLAG IBGP Peering VLANs per VRF
                # Continue to next VRF if mlag vlan_id is not set
                if (vlan_id := self._mlag_ibgp_peering_vlan_vrf(vrf, tenant)) is None:
                    continue

                vlan_interface = {"name": f"Vlan{vlan_id}", **self._get_vlan_interface_config_for_mlag_peering(vrf, vlan_id)}
                append_if_not_duplicate(
                    list_of_dicts=vlan_interfaces,
                    primary_key="name",
                    new_dict=vlan_interface,
                    context="MLAG iBGP Peering VLAN Interfaces",
                    context_keys=["name", "tenant"],
                    ignore_keys={"tenant"},
                )

        if vlan_interfaces:
            return vlan_interfaces

        return None

    def _get_vlan_interface_config_for_svi(self: AvdStructuredConfigNetworkServices, svi: dict, vrf: dict) -> dict:
        def _check_virtual_router_mac_address(vlan_interface_config: dict, variables: list) -> None:
            """
            Error if virtual router mac address is required but missing.

            Check if any variable in the list of variables is not None in vlan_interface_config
            and if it is the case, raise an Exception if virtual_router_mac_address is None.

            NOTE: SVI settings are also used for subinterfaces for uplink_type: 'lan'.
            So any changes here may also be needed in underlay.utils.UtilsMixin._get_l2_as_subint().
            """
            if any(vlan_interface_config.get(var) for var in variables) and self.shared_utils.virtual_router_mac_address is None:
                quoted_vars = [f"'{var}'" for var in variables]
                msg = f"'virtual_router_mac_address' must be set for node '{self.shared_utils.hostname}' when using {' or '.join(quoted_vars)} under 'svi'"
                raise AristaAvdInvalidInputsError(msg)

        interface_name = f"Vlan{svi['id']}"
        vlan_interface_config = {
            "name": interface_name,
            "tenant": svi["tenant"],
            "tags": svi.get("tags"),
            "description": default(svi.get("description"), svi["name"]),
            "shutdown": not (svi.get("enabled", False)),
            "ip_address": svi.get("ip_address"),
            "ipv6_address": svi.get("ipv6_address"),
            "ipv6_enable": svi.get("ipv6_enable"),
            "access_group_in": get(self._svi_acls, f"{interface_name}.ipv4_acl_in.name"),
            "access_group_out": get(self._svi_acls, f"{interface_name}.ipv4_acl_out.name"),
            "mtu": svi.get("mtu") if self.shared_utils.platform_settings_feature_support_per_interface_mtu else None,
            "eos_cli": svi.get("raw_eos_cli"),
            "struct_cfg": svi.get("structured_config"),
        }
        # Only set VARP if ip_address is set
        if vlan_interface_config["ip_address"] is not None:
            vlan_interface_config["ip_virtual_router_addresses"] = svi.get("ip_virtual_router_addresses")
            _check_virtual_router_mac_address(vlan_interface_config, ["ip_virtual_router_addresses"])

        # Only set Anycast GW if VARP is not set
        if vlan_interface_config.get("ip_virtual_router_addresses") is None:
            vlan_interface_config["ip_address_virtual"] = svi.get("ip_address_virtual")
            vlan_interface_config["ip_address_virtual_secondaries"] = svi.get("ip_address_virtual_secondaries")
            _check_virtual_router_mac_address(vlan_interface_config, ["ip_address_virtual", "ip_address_virtual_secondaries"])

        pim_config_ipv4 = {}
        if default(get(svi, "evpn_l3_multicast.enabled"), get(vrf, "_evpn_l3_multicast_enabled")) is True:
            if self.shared_utils.mlag:
                pim_config_ipv4["sparse_mode"] = True
            else:
                vlan_interface_config["ip_igmp"] = True

            if "ip_address_virtual" in vlan_interface_config:
                if (vrf_diagnostic_loopback := get(vrf, "vtep_diagnostic.loopback")) is None:
                    msg = (
                        f"No vtep_diagnostic loopback defined on VRF '{vrf['name']}' in Tenant '{svi['tenant']}'."
                        "This is required when 'l3_multicast' is enabled on the VRF and ip_address_virtual is used on an SVI in that VRF."
                    )
                    raise AristaAvdInvalidInputsError(msg)
                pim_config_ipv4["local_interface"] = f"Loopback{vrf_diagnostic_loopback}"

            if pim_config_ipv4:
                vlan_interface_config["pim"] = {"ipv4": pim_config_ipv4}

        # Only set VARPv6 if ipv6_address is set or ipv6_enable is set to true
        if vlan_interface_config["ipv6_address"] is not None or vlan_interface_config["ipv6_enable"]:
            vlan_interface_config["ipv6_virtual_router_addresses"] = svi.get("ipv6_virtual_router_addresses")
            _check_virtual_router_mac_address(vlan_interface_config, ["ipv6_virtual_router_addresses"])

        # Only set Anycast v6 GW if VARPv6 is not set
        if vlan_interface_config.get("ipv6_virtual_router_addresses") is None:
            if (ipv6_address_virtuals := svi.get("ipv6_address_virtuals")) is not None:
                vlan_interface_config["ipv6_address_virtuals"] = ipv6_address_virtuals

            _check_virtual_router_mac_address(vlan_interface_config, ["ipv6_address_virtuals"])

            if vlan_interface_config.get("ipv6_address_virtuals"):
                # If any anycast IPs are set, we also enable link-local IPv6 per best practice, unless specifically disabled with 'ipv6_enable: false'
                vlan_interface_config["ipv6_enable"] = get(vlan_interface_config, "ipv6_enable", default=True)

        if vrf["name"] != "default":
            vlan_interface_config["vrf"] = vrf["name"]

        # Adding IP helpers and OSPF via a common function also used for subinterfaces when uplink_type: lan
        self.shared_utils.get_additional_svi_config(vlan_interface_config, svi, vrf)

        return strip_empties_from_dict(vlan_interface_config)

    def _get_vlan_interface_config_for_mlag_peering(self: AvdStructuredConfigNetworkServices, vrf: dict, vlan_id: int) -> dict:
        """Build full config for MLAG peering SVI for the given VRF."""
        vlan_interface_config = {
            "tenant": vrf["tenant"],
            "type": "underlay_peering",
            "shutdown": False,
            "description": self.shared_utils.interface_descriptions.mlag_peer_l3_vrf_svi(
                InterfaceDescriptionData(shared_utils=self.shared_utils, interface=f"Vlan{vlan_id}", vrf=vrf["name"], vlan=vlan_id)
            ),
            "vrf": vrf["name"],
            "mtu": self.shared_utils.p2p_uplinks_mtu,
        }
        vlan_interface_config.update(self._get_vlan_ip_config_for_mlag_peering(vrf))
        return vlan_interface_config

    def _get_vlan_ip_config_for_mlag_peering(self: AvdStructuredConfigNetworkServices, vrf: dict) -> dict:
        """
        Build IP config for MLAG peering SVI for the given VRF.

        Called from _get_vlan_interface_config_for_mlag_peering and prefix_lists.
        """
        if self.shared_utils.underlay_rfc5549 and self.shared_utils.overlay_mlag_rfc5549:
            return {"ipv6_enable": True}

        if (mlag_ibgp_peering_ipv4_pool := vrf.get("mlag_ibgp_peering_ipv4_pool")) is not None:
            if self.shared_utils.mlag_role == "primary":
                return {
                    "ip_address": (
                        f"{self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_primary(mlag_ibgp_peering_ipv4_pool)}/"
                        f"{self.shared_utils.fabric_ip_addressing_mlag_ipv4_prefix_length}"
                    )
                }

            return {
                "ip_address": (
                    f"{self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_secondary(mlag_ibgp_peering_ipv4_pool)}/"
                    f"{self.shared_utils.fabric_ip_addressing_mlag_ipv4_prefix_length}"
                )
            }

        return {"ip_address": f"{self.shared_utils.mlag_ibgp_ip}/{self.shared_utils.fabric_ip_addressing_mlag_ipv4_prefix_length}"}
