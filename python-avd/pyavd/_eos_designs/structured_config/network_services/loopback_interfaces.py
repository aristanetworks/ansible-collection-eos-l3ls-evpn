# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import AvdStringFormatter, append_if_not_duplicate, default, strip_empties_from_dict

from .utils import UtilsMixin

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServices


class LoopbackInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def loopback_interfaces(self: AvdStructuredConfigNetworkServices) -> list | None:
        """
        Return structured config for loopback_interfaces.

        Used for Tenant vrf loopback interfaces
        This function is also called from virtual_source_nat_vrfs to avoid duplicate logic
        """
        if not self.shared_utils.network_services_l3:
            return None

        loopback_interfaces = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if (loopback_interface := self._get_vtep_diagnostic_loopback_for_vrf(vrf)) is not None:
                    append_if_not_duplicate(
                        list_of_dicts=loopback_interfaces,
                        primary_key="name",
                        new_dict=loopback_interface,
                        context="VTEP Diagnostic Loopback Interfaces",
                        context_keys=["name", "vrf", "tenant"],
                        ignore_keys={"tenant"},
                    )

                # The loopbacks have already been filtered in _filtered_tenants
                # to only contain entries with our hostname
                for loopback in vrf.loopbacks:
                    loopback_interface = {
                        "name": f"Loopback{loopback.loopback}",
                        "ip_address": loopback.ip_address,
                        "shutdown": not loopback.enabled,
                        "description": loopback.description,
                        "eos_cli": loopback.raw_eos_cli,
                    }

                    if vrf.name != "default":
                        loopback_interface["vrf"] = vrf.name

                    if loopback.ospf.enabled and vrf.ospf.enabled:
                        loopback_interface["ospf_area"] = loopback.ospf.area

                    # Strip None values from interface before adding to list
                    loopback_interface = {key: value for key, value in loopback_interface.items() if value is not None}
                    append_if_not_duplicate(
                        list_of_dicts=loopback_interfaces,
                        primary_key="name",
                        new_dict=loopback_interface,
                        context="Loopback Interfaces defined under network_services, vrfs, loopbacks",
                        context_keys=["name", "vrf"],
                    )

        if loopback_interfaces:
            return loopback_interfaces

        return None

    def _get_vtep_diagnostic_loopback_for_vrf(
        self: AvdStructuredConfigNetworkServices, vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem
    ) -> dict | None:
        if (loopback := vrf.vtep_diagnostic.loopback) is None:
            return None

        pod_name = self.inputs.pod_name
        loopback_ip_pools = vrf.vtep_diagnostic.loopback_ip_pools
        if not (loopback_ipv4_pool := vrf.vtep_diagnostic.loopback_ip_range) and pod_name and loopback_ip_pools and pod_name in loopback_ip_pools:
            loopback_ipv4_pool = loopback_ip_pools[pod_name].ipv4_pool

        if not (loopback_ipv6_pool := vrf.vtep_diagnostic.loopback_ipv6_range) and pod_name and loopback_ip_pools and pod_name in loopback_ip_pools:
            loopback_ipv6_pool = loopback_ip_pools[pod_name].ipv6_pool

        if not loopback_ipv4_pool and not loopback_ipv6_pool:
            return None

        interface_name = f"Loopback{loopback}"
        description_template = default(vrf.vtep_diagnostic.loopback_description, self.inputs.default_vrf_diag_loopback_description)
        return strip_empties_from_dict(
            {
                "name": interface_name,
                "description": AvdStringFormatter().format(description_template, interface=interface_name, vrf=vrf.name, tenant=vrf._tenant),
                "shutdown": False,
                "vrf": vrf.name,
                "ip_address": f"{self.shared_utils.ip_addressing.vrf_loopback_ip(loopback_ipv4_pool)}/32" if loopback_ipv4_pool else None,
                "ipv6_address": f"{self.shared_utils.ip_addressing.vrf_loopback_ipv6(loopback_ipv6_pool)}/128" if loopback_ipv6_pool else None,
            }
        )
