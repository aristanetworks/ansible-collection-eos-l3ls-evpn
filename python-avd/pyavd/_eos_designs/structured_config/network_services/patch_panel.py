# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import append_if_not_duplicate

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class PatchPanelMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def patch_panel(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """Return structured config for patch_panel."""
        if not self.shared_utils.network_services_l1:
            return None

        patches = []
        for tenant in self.shared_utils.filtered_tenants:
            if not tenant.point_to_point_services:
                continue

            for point_to_point_service in tenant.point_to_point_services._natural_sorted():
                for endpoint in point_to_point_service.endpoints:
                    if self.shared_utils.hostname not in endpoint.nodes:
                        continue

                    node_index = endpoint.nodes.index(self.shared_utils.hostname)
                    interface = endpoint.interfaces[node_index]
                    if endpoint.port_channel.mode in ["active", "on"]:
                        channel_group_id = "".join(re.findall(r"\d", interface))
                        interface = f"Port-Channel{channel_group_id}"

                    # TODO: refactor this by inverting if and else condition and using continue at the end of the if
                    if point_to_point_service.subinterfaces:
                        for subif in point_to_point_service.subinterfaces:
                            patch = {
                                "name": f"{point_to_point_service.name}_{subif.number}",
                                "enabled": True,
                                "connectors": [
                                    {
                                        "id": "1",
                                        "type": "interface",
                                        "endpoint": f"{interface}.{subif.number}",
                                    },
                                ],
                            }
                            if point_to_point_service.type == "vpws-pseudowire":
                                patch["connectors"].append(
                                    {
                                        "id": "2",
                                        "type": "pseudowire",
                                        "endpoint": f"bgp vpws {tenant.name} pseudowire {point_to_point_service.name}_{subif.number}",
                                    },
                                )
                            append_if_not_duplicate(
                                list_of_dicts=patches,
                                primary_key="name",
                                new_dict=patch,
                                context="Patches defined under point_to_point_services",
                                context_keys=["name"],
                            )
                    else:
                        patch = {
                            "name": f"{point_to_point_service.name}",
                            "enabled": True,
                            "connectors": [
                                {
                                    "id": "1",
                                    "type": "interface",
                                    "endpoint": f"{interface}",
                                },
                            ],
                        }
                        if point_to_point_service.type == "vpws-pseudowire":
                            patch["connectors"].append(
                                {
                                    "id": "2",
                                    "type": "pseudowire",
                                    "endpoint": f"bgp vpws {tenant.name} pseudowire {point_to_point_service.name}",
                                },
                            )
                        append_if_not_duplicate(
                            list_of_dicts=patches,
                            primary_key="name",
                            new_dict=patch,
                            context="Patches defined under point_to_point_services",
                            context_keys=["name"],
                        )

        if patches:
            return {"patches": patches}

        return None
