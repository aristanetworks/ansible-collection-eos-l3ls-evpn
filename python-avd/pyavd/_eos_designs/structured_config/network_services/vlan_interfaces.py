# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import Undefined, default, get
from pyavd.api.interface_descriptions import InterfaceDescriptionData

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class VlanInterfacesMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def vlan_interfaces(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Return structured config for vlan_interfaces.

        Consist of svis and mlag peering vlans from filtered tenants
        """
        if not (self.shared_utils.network_services_l2 and self.shared_utils.network_services_l3):
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for svi in vrf.svis:
                    self.structured_config.vlan_interfaces.append(self._get_vlan_interface_config_for_svi(svi, vrf), ignore_fields=("tenant",))

                # MLAG IBGP Peering VLANs per VRF
                # Continue to next VRF if mlag vlan_id is not set
                if (vlan_id := self._mlag_ibgp_peering_vlan_vrf(vrf, tenant)) is None:
                    continue

                self.structured_config.vlan_interfaces.append(self._get_vlan_interface_config_for_mlag_peering(vrf, vlan_id), ignore_fields=("tenant",))

    def _check_virtual_router_mac_address(
        self: AvdStructuredConfigNetworkServicesProtocol, vlan_interface_config: EosCliConfigGen.VlanInterfacesItem, variables: tuple[str, ...]
    ) -> None:
        """
        Error if virtual router mac address is required but missing.

        Check if any variable in the list of variables is not None in vlan_interface_config
        and if it is the case, raise an Exception if virtual_router_mac_address is None.

        NOTE: SVI settings are also used for subinterfaces for uplink_type: 'lan'.
        So any changes here may also be needed in underlay.utils.UtilsMixin._get_l2_as_subint().
        """
        if any(vlan_interface_config._get(var) for var in variables) and self.shared_utils.node_config.virtual_router_mac_address is None:
            quoted_vars = [f"'{var}'" for var in variables]
            msg = f"'virtual_router_mac_address' must be set for node '{self.shared_utils.hostname}' when using {' or '.join(quoted_vars)} under 'svi'"
            raise AristaAvdInvalidInputsError(msg)

    def _get_vlan_interface_config_for_svi(
        self: AvdStructuredConfigNetworkServicesProtocol,
        svi: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> EosCliConfigGen.VlanInterfacesItem:
        interface_name = f"Vlan{svi.id}"
        vlan_interface_config = EosCliConfigGen.VlanInterfacesItem(
            name=interface_name,
            tenant=svi._tenant,
            tags=EosCliConfigGen.VlanInterfacesItem.Tags(svi._get("tags", [])),  # Historic behavior is to not output the default ["all"]
            description=default(svi.description, svi.name),
            shutdown=not default(svi.enabled, False),  # noqa: FBT003
            ip_address=svi.ip_address,
            ipv6_address=svi.ipv6_address,
            ipv6_enable=svi.ipv6_enable,
            access_group_in=get(self._svi_acls, f"{interface_name}.ipv4_acl_in.name"),
            access_group_out=get(self._svi_acls, f"{interface_name}.ipv4_acl_out.name"),
            mtu=svi.mtu if self.shared_utils.platform_settings.feature_support.per_interface_mtu else None,
            eos_cli=svi.raw_eos_cli,
        )

        if svi.structured_config:
            self.custom_structured_configs.nested.vlan_interfaces.obtain(interface_name)._deepmerge(
                svi.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )

        # Only set VARP if ip_address is set
        if vlan_interface_config.ip_address:
            vlan_interface_config.ip_virtual_router_addresses.extend(svi.ip_virtual_router_addresses)
            self._check_virtual_router_mac_address(vlan_interface_config, ("ip_virtual_router_addresses",))

        # Only set Anycast GW if VARP is not set
        if not vlan_interface_config.ip_virtual_router_addresses:
            vlan_interface_config.ip_address_virtual = svi.ip_address_virtual
            vlan_interface_config.ip_address_virtual_secondaries.extend(svi.ip_address_virtual_secondaries)
            self._check_virtual_router_mac_address(vlan_interface_config, ("ip_address_virtual", "ip_address_virtual_secondaries"))

        if default(svi.evpn_l3_multicast.enabled, getattr(vrf, "_evpn_l3_multicast_enabled", False)) is True:
            if self.shared_utils.mlag:
                vlan_interface_config.pim.ipv4.sparse_mode = True
            else:
                vlan_interface_config.ip_igmp = True

            if (
                vlan_interface_config._get_defined_attr("ip_address_virtual") is not Undefined
            ):  # Historic behavior of checking for mere presence of the key. TODO: Fix this but it is breaking.
                if (vrf_diagnostic_loopback := vrf.vtep_diagnostic.loopback) is None:
                    msg = (
                        f"No vtep_diagnostic loopback defined on VRF '{vrf.name}' in Tenant '{svi._tenant}'."
                        "This is required when 'l3_multicast' is enabled on the VRF and ip_address_virtual is used on an SVI in that VRF."
                    )
                    raise AristaAvdInvalidInputsError(msg)
                vlan_interface_config.pim.ipv4.local_interface = f"Loopback{vrf_diagnostic_loopback}"

        # Only set VARPv6 if ipv6_address is set or ipv6_enable is set to true
        if vlan_interface_config.ipv6_address or vlan_interface_config.ipv6_enable:
            vlan_interface_config.ipv6_virtual_router_addresses.extend(svi.ipv6_virtual_router_addresses)
            self._check_virtual_router_mac_address(vlan_interface_config, ("ipv6_virtual_router_addresses",))

        # Only set Anycast v6 GW if VARPv6 is not set
        if not vlan_interface_config.ipv6_virtual_router_addresses:
            if svi.ipv6_address_virtuals:
                vlan_interface_config.ipv6_address_virtuals.extend(svi.ipv6_address_virtuals)

            self._check_virtual_router_mac_address(vlan_interface_config, ("ipv6_address_virtuals",))

            if vlan_interface_config.ipv6_address_virtuals:
                # If any anycast IPs are set, we also enable link-local IPv6 per best practice, unless specifically disabled with 'ipv6_enable: false'
                vlan_interface_config.ipv6_enable = default(vlan_interface_config.ipv6_enable, True)  # noqa: FBT003

        if vrf.name != "default":
            vlan_interface_config.vrf = vrf.name

        # Adding IP helpers and OSPF via a common function also used for subinterfaces when uplink_type: lan
        self.shared_utils.get_additional_svi_config(vlan_interface_config, svi, vrf)

        return vlan_interface_config

    def _get_vlan_interface_config_for_mlag_peering(
        self: AvdStructuredConfigNetworkServicesProtocol, vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem, vlan_id: int
    ) -> EosCliConfigGen.VlanInterfacesItem:
        """Build full config for MLAG peering SVI for the given VRF."""
        vlan_interface_config = EosCliConfigGen.VlanInterfacesItem(
            name=f"Vlan{vlan_id}",
            tenant=vrf._tenant,
            type="underlay_peering",
            shutdown=False,
            description=self.shared_utils.interface_descriptions.mlag_peer_l3_vrf_svi(
                InterfaceDescriptionData(shared_utils=self.shared_utils, interface=f"Vlan{vlan_id}", vrf=vrf.name, vlan=vlan_id)
            ),
            vrf=vrf.name,
            mtu=self.shared_utils.p2p_uplinks_mtu,
        )
        vlan_interface_config._update(**self._get_vlan_ip_config_for_mlag_peering(vrf))
        return vlan_interface_config

    def _get_vlan_ip_config_for_mlag_peering(
        self: AvdStructuredConfigNetworkServicesProtocol, vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem
    ) -> dict:
        """
        Build IP config for MLAG peering SVI for the given VRF.

        Called from _get_vlan_interface_config_for_mlag_peering and prefix_lists.

        TODO: Refactor to update the input in-place
        """
        if self.inputs.underlay_rfc5549 and self.inputs.overlay_mlag_rfc5549:
            return {"ipv6_enable": True}

        if vrf.mlag_ibgp_peering_ipv4_pool:
            if self.shared_utils.mlag_role == "primary":
                return {
                    "ip_address": (
                        f"{self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_primary(vrf.mlag_ibgp_peering_ipv4_pool)}/"
                        f"{self.inputs.fabric_ip_addressing.mlag.ipv4_prefix_length}"
                    )
                }

            return {
                "ip_address": (
                    f"{self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_secondary(vrf.mlag_ibgp_peering_ipv4_pool)}/"
                    f"{self.inputs.fabric_ip_addressing.mlag.ipv4_prefix_length}"
                )
            }

        return {"ip_address": f"{self.shared_utils.mlag_ibgp_ip}/{self.inputs.fabric_ip_addressing.mlag.ipv4_prefix_length}"}
