# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import append_if_not_duplicate, default, get

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class RouterOspfMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_ospf(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """
        return structured config for router_ospf.

        If we have static_routes in default VRF and not EPVN, and underlay is OSPF
        Then add redistribute static to the underlay OSPF process.
        """
        if not self.shared_utils.network_services_l3:
            return None

        ospf_processes = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant["vrfs"]:
                if get(vrf, "ospf.enabled") is not True:
                    continue

                if self.shared_utils.hostname not in get(vrf, "ospf.nodes", default=[self.shared_utils.hostname]):
                    continue

                ospf_interfaces = []
                for l3_interface in vrf["l3_interfaces"]:
                    if get(l3_interface, "ospf.enabled") is True:
                        for node_index, node in enumerate(l3_interface["nodes"]):
                            if node != self.shared_utils.hostname:
                                continue

                            ospf_interfaces.append(l3_interface["interfaces"][node_index])

                for svi in vrf["svis"]:
                    if get(svi, "ospf.enabled") is True:
                        interface_name = f"Vlan{svi['id']}"
                        ospf_interfaces.append(interface_name)

                process_id = default(get(vrf, "ospf.process_id"), vrf.get("vrf_id"))
                if not process_id:
                    msg = f"'ospf.process_id' or 'vrf_id' under vrf '{vrf['name']}"
                    raise AristaAvdInvalidInputsError(msg)

                process = {
                    "id": process_id,
                    "vrf": vrf["name"] if vrf["name"] != "default" else None,
                    "passive_interface_default": True,
                    "no_passive_interfaces": ospf_interfaces,
                    "bfd_enable": get(vrf, "ospf.bfd"),
                    "max_lsa": get(vrf, "ospf.max_lsa"),
                }

                if ospf_router_id := get(vrf, "ospf.router_id"):
                    process["router_id"] = ospf_router_id
                elif not self.shared_utils.use_router_general_for_router_id:
                    process["router_id"] = self.shared_utils.router_id

                process_redistribute = {}

                if get(vrf, "ospf.redistribute_bgp.enabled", default=True) is True:
                    process_redistribute["bgp"] = {"enabled": True}
                    if (route_map := get(vrf, "ospf.redistribute_bgp.route_map")) is not None:
                        process_redistribute["bgp"]["route_map"] = route_map

                if get(vrf, "ospf.redistribute_connected.enabled", default=False) is True:
                    process_redistribute["connected"] = {"enabled": True}
                    if (route_map := get(vrf, "ospf.redistribute_connected.route_map")) is not None:
                        process_redistribute["connected"]["route_map"] = route_map

                process["redistribute"] = process_redistribute or None

                # Strip None values from process before adding to list
                process = {key: value for key, value in process.items() if value is not None}

                append_if_not_duplicate(
                    list_of_dicts=ospf_processes,
                    primary_key="id",
                    new_dict=process,
                    context="OSPF Processes defined under network services",
                    context_keys="id",
                )

        # If we have static_routes in default VRF and not EPVN, and underlay is OSPF
        # Then add redistribute static to the underlay OSPF process.
        if self._vrf_default_ipv4_static_routes["redistribute_in_underlay"] and self.shared_utils.underlay_routing_protocol in ["ospf", "ospf-ldp"]:
            ospf_processes.append({"id": int(self.shared_utils.underlay_ospf_process_id), "redistribute": {"static": {"enabled": True}}})
        if ospf_processes:
            return {"process_ids": ospf_processes}

        return None
