# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import AvdStringFormatter, append_if_not_duplicate, get, get_item

from .utils import UtilsMixin

if TYPE_CHECKING:
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
            for vrf in tenant["vrfs"]:
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
                for loopback in vrf["loopbacks"]:
                    loopback_interface = {
                        "name": f"Loopback{loopback['loopback']}",
                        "ip_address": loopback.get("ip_address"),
                        "shutdown": not loopback.get("enabled", True),
                        "description": loopback.get("description"),
                        "eos_cli": loopback.get("raw_eos_cli"),
                    }

                    if vrf["name"] != "default":
                        loopback_interface["vrf"] = vrf["name"]

                    if get(loopback, "ospf.enabled") is True and get(vrf, "ospf.enabled") is True:
                        loopback_interface["ospf_area"] = loopback["ospf"].get("area", "0.0.0.0")  # noqa: S104

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

    def _get_vtep_diagnostic_loopback_for_vrf(self: AvdStructuredConfigNetworkServices, vrf: dict) -> dict | None:
        if (loopback := get(vrf, "vtep_diagnostic.loopback")) is None:
            return None

        if (loopback_ipv4_pool := get(vrf, "vtep_diagnostic.loopback_ip_range")) is None:
            if (pod_name := self.shared_utils.pod_name) is None:
                # Skip this vrf since we have no loopback_ip_range and pod_name
                return None

            if (loopback_ip_pools := get(vrf, "vtep_diagnostic.loopback_ip_pools")) is None:
                # Skip this vrf since we have no pools either
                return None

            if (loopback_ipv4_pool := get_item(loopback_ip_pools, "pod", pod_name, default={}).get("ipv4_pool")) is None:
                # Skip this vrf since we cannot find our pod_name in the pools or the pool is missing the ipv4_pool
                return None

        # If we ended up here, it means we have a loopback_ipv4_pool set
        interface_name = f"Loopback{loopback}"
        description_template = get(vrf, "vtep_diagnostic.loopback_description", default=self.shared_utils.default_vrf_diag_loopback_description)
        return {
            "name": interface_name,
            "description": AvdStringFormatter().format(description_template, interface=interface_name, vrf=vrf["name"], tenant=vrf["tenant"]),
            "shutdown": False,
            "vrf": vrf["name"],
            "ip_address": f"{self.shared_utils.ip_addressing.vrf_loopback_ip(loopback_ipv4_pool)}/32",
        }
