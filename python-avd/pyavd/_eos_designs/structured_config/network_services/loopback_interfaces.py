# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from pyavd._utils import append_if_not_duplicate

from .utils import UtilsMixin


class LoopbackInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def loopback_interfaces(self) -> list | None:
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
