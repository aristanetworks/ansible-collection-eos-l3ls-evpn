# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdError
from pyavd._schema.models.avd_base import AvdBase
from pyavd._utils import default, get_v2

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigMetadataProtocol

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


class CvTagsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _cv_tags(self: AvdStructuredConfigMetadataProtocol) -> None:
        """Generate the data structure `metadata.cv_tags`."""
        if self.inputs.generate_cv_tags.topology_hints:
            self._get_topology_hints()
        if self.shared_utils.is_cv_pathfinder_router:
            self._get_cv_pathfinder_device_tags()
        if self.inputs.generate_cv_tags.device_tags:
            self._get_device_tags()

        if self.inputs.generate_cv_tags.interface_tags or self.shared_utils.is_cv_pathfinder_router:
            self._get_interface_tags()

    def _get_topology_hints(self: AvdStructuredConfigMetadataProtocol) -> None:
        """Return list of topology_hint tags."""
        default_type_hint = self.shared_utils.node_type_key_data.cv_tags_topology_type
        if self.inputs.dc_name:
            self.structured_config.metadata.cv_tags.device_tags.append(
                EosCliConfigGen.Metadata.CvTags.DeviceTagsItem(name="topology_hint_datacenter", value=self.inputs.dc_name)
            )
        if self.shared_utils.fabric_name:
            self.structured_config.metadata.cv_tags.device_tags.append(
                EosCliConfigGen.Metadata.CvTags.DeviceTagsItem(name="topology_hint_fabric", value=self.shared_utils.fabric_name)
            )
        if self.inputs.pod_name:
            self.structured_config.metadata.cv_tags.device_tags.append(
                EosCliConfigGen.Metadata.CvTags.DeviceTagsItem(name="topology_hint_pod", value=self.inputs.pod_name)
            )
        if default(self.inputs.cv_tags_topology_type, default_type_hint):
            self.structured_config.metadata.cv_tags.device_tags.append(
                EosCliConfigGen.Metadata.CvTags.DeviceTagsItem(name="topology_hint_type", value=default(self.inputs.cv_tags_topology_type, default_type_hint))
            )
        if default(self.shared_utils.node_config.rack, self.shared_utils.group):
            self.structured_config.metadata.cv_tags.device_tags.append(
                EosCliConfigGen.Metadata.CvTags.DeviceTagsItem(
                    name="topology_hint_rack", value=default(self.shared_utils.node_config.rack, self.shared_utils.group)
                )
            )

    def _get_cv_pathfinder_device_tags(self: AvdStructuredConfigMetadataProtocol) -> None:
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
        region_name = self.shared_utils.wan_region.name if self.shared_utils.wan_region is not None else None
        site_name = self.shared_utils.wan_site.name if self.shared_utils.wan_site is not None else None
        if self.shared_utils.cv_pathfinder_role:
            self.structured_config.metadata.cv_tags.device_tags.append(
                EosCliConfigGen.Metadata.CvTags.DeviceTagsItem(name="Role", value=self.shared_utils.cv_pathfinder_role)
            )
        if region_name:
            self.structured_config.metadata.cv_tags.device_tags.append(EosCliConfigGen.Metadata.CvTags.DeviceTagsItem(name="Region", value=region_name))

        if self.shared_utils.is_cv_pathfinder_server:
            self.structured_config.metadata.cv_tags.device_tags.append(
                EosCliConfigGen.Metadata.CvTags.DeviceTagsItem(name="PathfinderSet", value=self.shared_utils.group or "PATHFINDERS")
            )
        else:
            self.structured_config.metadata.cv_tags.device_tags.append(
                EosCliConfigGen.Metadata.CvTags.DeviceTagsItem(name="Zone", value=self.shared_utils.wan_zone["name"])
            )
            self.structured_config.metadata.cv_tags.device_tags.append(EosCliConfigGen.Metadata.CvTags.DeviceTagsItem(name="Site", value=site_name))

    def _get_device_tags(self: AvdStructuredConfigMetadataProtocol) -> None:
        """Return list of device_tags."""
        tags_to_generate = self.inputs.generate_cv_tags.device_tags
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
                self.structured_config.metadata.cv_tags.device_tags.append(EosCliConfigGen.Metadata.CvTags.DeviceTagsItem(name=generate_tag.name, value=value))

    def _get_interface_tags(self: AvdStructuredConfigMetadataProtocol) -> None:
        """Return list of interface_tags."""
        tags_to_generate = self.inputs.generate_cv_tags.interface_tags

        for ethernet_interface in self.structured_config.ethernet_interfaces:
            tags = EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags()
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
                    tags.append(EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.TagsItem(name=generate_tag.name, value=value))

            if self.shared_utils.is_cv_pathfinder_router:
                tags.extend(self._get_cv_pathfinder_interface_tags(ethernet_interface))

            if tags:
                self.structured_config.metadata.cv_tags.interface_tags.append(
                    EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem(interface=ethernet_interface.name, tags=tags)
                )

        # handle tags for L3 port-channel interfaces (cv_pathfinder use case)
        for port_channel_intf in self.structured_config.port_channel_interfaces:
            tags = EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags()
            if self.shared_utils.is_cv_pathfinder_router:
                tags.extend(self._get_cv_pathfinder_interface_tags(port_channel_intf))
            if tags:
                self.structured_config.metadata.cv_tags.interface_tags.append(
                    EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem(interface=port_channel_intf.name, tags=tags)
                )

    def _get_cv_pathfinder_interface_tags(
        self: AvdStructuredConfigMetadataProtocol, generic_interface: EosCliConfigGen.EthernetInterfacesItem | EosCliConfigGen.PortChannelInterfacesItem
    ) -> EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags:
        """
        Return list of interface tags for cv_pathfinder solution.

        generic_interface is either ethernet or port_channel interface.

        Example: [
            {"name": "Type", <"lan" or "wan">},
            {"name": "Carrier", <value copied from wan_carrier if this is a wan interface>},
            {"name": "Circuit", <value copied from wan_circuit_id if this is a wan interface>}
        ].
        """
        if generic_interface.name in self.shared_utils.wan_interfaces:
            wan_interface = self.shared_utils.wan_interfaces[generic_interface.name]
            return self._get_cv_pathfinder_wan_interface_tags(wan_interface)
        if generic_interface.name in self.shared_utils.wan_port_channels:
            wan_port_channel_intf = self.shared_utils.wan_port_channels[generic_interface.name]
            return self._get_cv_pathfinder_wan_interface_tags(wan_port_channel_intf)
        # Check if input eth interface is member of any L3 Port-Channel wan interface
        # if so, skip generation of interface tags for such member interface.
        # TODO: Consider if we should skip this for all port-channel members,
        # since we would now set it on the port-channel instead.
        if generic_interface.name in self.shared_utils._wan_port_channel_member_interfaces:
            return EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags()
        tags = EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags()
        tags.append(EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.TagsItem(name="Type", value="lan"))
        return tags

    # Generate wan interface tags while accounting for wan interface to be either L3 interface or L3 Port-Channel type
    def _get_cv_pathfinder_wan_interface_tags(
        self: AvdStructuredConfigMetadataProtocol,
        wan_interface: (
            EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem
            | EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3PortChannelsItem
        ),
    ) -> EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags:
        """Return list of wan interface tags for cv_pathfinder solution for a given wan interface."""
        tags = EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags()
        tags.append(EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.TagsItem(name="Type", value="wan"))
        if wan_interface.wan_carrier:
            tags.append(EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.TagsItem(name="Carrier", value=wan_interface.wan_carrier))
        if wan_interface.wan_circuit_id:
            tags.append(EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.TagsItem(name="Circuit", value=wan_interface.wan_circuit_id))
        return tags
