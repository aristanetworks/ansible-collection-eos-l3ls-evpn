# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pyavd._errors import AristaAvdError
from pyavd._schema.models.avd_base import AvdBase
from pyavd._utils import default, get_v2, strip_empties_from_dict, strip_empties_from_list

if TYPE_CHECKING:
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

    from . import AvdStructuredConfigMetadata

INVALID_CUSTOM_DEVICE_TAGS = [
    "topology_hint_type",
    "topology_type",
    "topology_hint_datacenter",
    "topology_datacenter",
    "topology_hint_rack",
    "topology_rack",
    "topology_pod",
    "topology_hint_pod",
    "eos",
    "eostrain",
    "ztp",
    "bgp",
    "container",
    "mpls",
    "topology_network_type",
    "model",
    "systype",
    "serialnumber",
    "tapagg",
    "hostname",
    "terminattr",
]
"""These tag names overlap with CV system tags or topology_hints"""


class CvTagsMixin:
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _cv_tags(self: AvdStructuredConfigMetadata) -> dict | None:
        """Generate the data structure `metadata.cv_tags`."""
        if not self.inputs.generate_cv_tags and not self.shared_utils.is_cv_pathfinder_router:
            return None

        device_tags = self._get_topology_hints()
        device_tags.extend(self._get_cv_pathfinder_device_tags())
        device_tags.extend(self._get_device_tags())

        cv_tags = {"device_tags": device_tags, "interface_tags": self._get_interface_tags()}

        return strip_empties_from_dict(cv_tags) or None

    @staticmethod
    def _tag_dict(name: str, value: Any) -> dict | None:
        if value is None:
            return None
        return {"name": name, "value": str(value)}

    def _get_topology_hints(self: AvdStructuredConfigMetadata) -> list:
        """Return list of topology_hint tags."""
        if not self.inputs.generate_cv_tags.topology_hints:
            return []

        default_type_hint = self.shared_utils.node_type_key_data.cv_tags_topology_type
        return strip_empties_from_list(
            [
                self._tag_dict("topology_hint_datacenter", self.inputs.dc_name),
                self._tag_dict("topology_hint_fabric", self.shared_utils.fabric_name),
                self._tag_dict("topology_hint_pod", self.inputs.pod_name),
                self._tag_dict("topology_hint_type", default(self.inputs.cv_tags_topology_type, default_type_hint)),
                self._tag_dict("topology_hint_rack", default(self.shared_utils.node_config.rack, self.shared_utils.group)),
            ],
        )

    def _get_cv_pathfinder_device_tags(self: AvdStructuredConfigMetadata) -> list:
        """
        Return list of device_tags for cv_pathfinder solution.

        Example: [
            {"name": "Region", "value": <value copied from cv_pathfinder_region>},
            {"name": "Zone", "value": <"<region-name>-ZONE" for pathfinder clients>},
            {"name": "Site", "value": <value copied from cv_pathfinder_site for pathfinder clients>},
            {"name": "PathfinderSet", "value": <value copied from node group or default "PATHFINDERS" for pathfinder servers>},
            {"name": "Role", "value": <'pathfinder', 'edge', 'transit region' or 'transit zone'>}
        ].
        """
        if not self.shared_utils.is_cv_pathfinder_router:
            return []

        region_name = self.shared_utils.wan_region.name if self.shared_utils.wan_region is not None else None
        site_name = self.shared_utils.wan_site.name if self.shared_utils.wan_site is not None else None

        device_tags = [
            self._tag_dict("Role", self.shared_utils.cv_pathfinder_role),
            self._tag_dict("Region", region_name),
        ]
        if self.shared_utils.is_cv_pathfinder_server:
            device_tags.append(self._tag_dict("PathfinderSet", self.shared_utils.group or "PATHFINDERS"))
        else:
            device_tags.extend(
                [
                    self._tag_dict("Zone", self.shared_utils.wan_zone["name"]),
                    self._tag_dict("Site", site_name),
                ],
            )

        return strip_empties_from_list(device_tags)

    def _get_device_tags(self: AvdStructuredConfigMetadata) -> list:
        """Return list of device_tags."""
        if not (tags_to_generate := self.inputs.generate_cv_tags.device_tags):
            return []

        device_tags = []
        for generate_tag in tags_to_generate:
            if generate_tag.name in INVALID_CUSTOM_DEVICE_TAGS:
                msg = (
                    f"The CloudVision tag name 'generate_cv_tags.device_tags[name={generate_tag.name}] is invalid. "
                    "System Tags cannot be overridden. Try using a different name for this tag."
                )
                raise AristaAvdError(msg)

            # Get value from either 'value' key, structured config based on the 'data_path' key or raise.
            if generate_tag.value is not None:
                value = generate_tag.value
            elif generate_tag.data_path is not None:
                value = get_v2(self.structured_config, generate_tag.data_path)
                if isinstance(type(value), AvdBase):
                    msg = (
                        f"'generate_cv_tags.device_tags[name={generate_tag.name}].data_path' ({generate_tag.data_path}) "
                        f"points to a list or dict. This is not supported for cloudvision tag data_paths."
                    )
                    raise AristaAvdError(msg)
            else:
                msg = f"'generate_cv_tags.device_tags[name={generate_tag.name}]' is missing either a static 'value' or a dynamic 'data_path'"
                raise AristaAvdError(msg)

            # Silently ignoring empty values since structured config may vary between devices.
            if value:
                device_tags.append(self._tag_dict(generate_tag.name, value))

        return device_tags

    def _get_interface_tags(self: AvdStructuredConfigMetadata) -> list:
        """Return list of interface_tags."""
        if not (tags_to_generate := self.inputs.generate_cv_tags.interface_tags) and not self.shared_utils.is_cv_pathfinder_router:
            return []

        interface_tags = []
        for ethernet_interface in self.structured_config.ethernet_interfaces:
            tags = []
            for generate_tag in tags_to_generate:
                # Get value from either 'value' key, structured config based on the 'data_path' key or raise.
                if generate_tag.value is not None:
                    value = generate_tag.value
                elif generate_tag.data_path is not None:
                    value = get_v2(ethernet_interface, generate_tag.data_path)
                    if type(value) in [list, dict]:
                        msg = (
                            f"'generate_cv_tags.interface_tags[name={generate_tag.name}].data_path' ({generate_tag.data_path}) "
                            f"points to a variable of type {type(value).__name__}. This is not supported for cloudvision tag data_paths."
                        )
                        raise AristaAvdError(msg)
                else:
                    msg = f"'generate_cv_tags.interface_tags[name={generate_tag.name}]' is missing either a static 'value' or a dynamic 'data_path'"
                    raise AristaAvdError(msg)

                # Silently ignoring empty values since structured config may vary between devices.
                if value:
                    tags.append(self._tag_dict(generate_tag.name, value))

            if self.shared_utils.is_cv_pathfinder_router:
                tags.extend(self._get_cv_pathfinder_interface_tags(ethernet_interface))

            if tags:
                interface_tags.append({"interface": ethernet_interface.name, "tags": tags})

        return interface_tags

    def _get_cv_pathfinder_interface_tags(self: AvdStructuredConfigMetadata, ethernet_interface: EosCliConfigGen.EthernetInterfacesItem) -> list:
        """
        Return list of device_tags for cv_pathfinder solution.

        Example: [
            {"name": "Type", <"lan" or "wan">},
            {"name": "Carrier", <value copied from wan_carrier if this is a wan interface>},
            {"name": "Circuit", <value copied from wan_circuit_id if this is a wan interface>}
        ].
        """
        if ethernet_interface.name in self.shared_utils.wan_interfaces:
            wan_interface = self.shared_utils.wan_interfaces[ethernet_interface.name]
            return strip_empties_from_list(
                [
                    self._tag_dict("Type", "wan"),
                    self._tag_dict("Carrier", wan_interface.wan_carrier),
                    self._tag_dict("Circuit", wan_interface.wan_circuit_id),
                ],
            )

        return [self._tag_dict("Type", "lan")]
