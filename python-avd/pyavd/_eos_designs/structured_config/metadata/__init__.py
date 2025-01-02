# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from pyavd._eos_designs.structured_config.structured_config_generator import StructuredConfigGenerator
from pyavd._utils import strip_empties_from_dict

from .cv_pathfinder import CvPathfinderMixin
from .cv_tags import CvTagsMixin


class AvdStructuredConfigMetadata(StructuredConfigGenerator, CvTagsMixin, CvPathfinderMixin):
    """
    This returns the metadata data structure as per the below example.

    {
        "metadata": {
            "platform": "7050X3",
            "cv_tags": {
                "device_tags": [
                    {"name": "topology_hint_type", "value": <topology_hint_type taken from node_type_keys.[].cvp_tags.topology_hint_type> },
                    {"name: "topology_hint_dc", "value": <taken from the dc_name> },
                    {"name": "topology_hint_fabric", "value": <value copied from fabric_name>},
                    {"name": "topology_hint_pod", "value": <value copied from pod_name>},
                    {"name": "topolgoy_hint_rack", "value": <value copied from rack field if it is defined for the node>},
                    {"name": "<custom_tag_name>", "value": "custom tag value"},
                    {"name": "<custom_tag_name>", "value": "<value extracted from structured_config>"},
                    {"name": "Region", "value": <value copied from cv_pathfinder_region>},
                    {"name": "Zone", "value": <"<region-name>-ZONE" for pathfinder clients>},
                    {"name": "Site", "value": <value copied from cv_pathfinder_site for pathfinder clients>},
                    {"name": "PathfinderSet", "value": <value copied from node group or default "PATHFINDERS" for pathfinder servers>},
                    {"name": "Role", "value": <'pathfinder', 'edge', 'transit region' or 'transit zone'>}
                },
                "interface_tags": [
                    {
                        "interface": "Ethernet1",
                        "tags":[
                            {"name": "peer", "value": "leaf1a"}
                            {"name": "Type", <"lan" or "wan">},
                            {"name": "Carrier", <value copied from wan_carrier if this is a wan interface>},
                            {"name": "Circuit", <value copied from wan_circuit_id if this is a wan interface>}
                        ]
                    }
                ]
            },
            "cv_pathfinder": {<see schema for model>}
        }
    }.
    """

    @cached_property
    def metadata(self) -> dict | None:
        metadata = {
            "platform": self.shared_utils.platform,
            "system_mac_address": self.shared_utils.system_mac_address,
            "cv_tags": self._cv_tags(),
            "cv_pathfinder": self._cv_pathfinder(),
        }
        return strip_empties_from_dict(metadata) or None
