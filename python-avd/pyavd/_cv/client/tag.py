# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._cv.api.arista.tag.v2 import (
    CreatorType,
    ElementType,
    Tag,
    TagAssignment,
    TagAssignmentConfig,
    TagAssignmentConfigServiceStub,
    TagAssignmentConfigSetSomeRequest,
    TagAssignmentConfigStreamRequest,
    TagAssignmentKey,
    TagAssignmentServiceStub,
    TagAssignmentStreamRequest,
    TagConfig,
    TagConfigServiceStub,
    TagConfigSetSomeRequest,
    TagConfigStreamRequest,
    TagKey,
    TagServiceStub,
    TagStreamRequest,
)
from pyavd._cv.api.arista.time import TimeBounds

from .constants import DEFAULT_API_TIMEOUT
from .exceptions import get_cv_client_exception

if TYPE_CHECKING:
    from datetime import datetime

    from . import CVClientProtocol


ELEMENT_TYPE_MAP = {
    "device": ElementType.DEVICE,
    "interface": ElementType.INTERFACE,
    None: ElementType.UNSPECIFIED,
}

CREATOR_TYPE_MAP = {
    "user": CreatorType.USER,
    "system": CreatorType.SYSTEM,
    "external": CreatorType.EXTERNAL,
    None: CreatorType.UNSPECIFIED,
}


class TagMixin(Protocol):
    """Only to be used as mixin on CVClient class."""

    tags_api_version: Literal["v2"] = "v2"
    # TODO: Ensure the to document that we only support v2 of this api - hence only the CV versions supporting that.

    async def get_tags(
        self: CVClientProtocol,
        workspace_id: str,
        element_type: Literal["device", "interface"] | None = None,
        creator_type: Literal["user", "system", "external"] | None = None,
        time: datetime | None = None,
        timeout: float = 30.0,
    ) -> list[Tag]:
        """
        Get Tags using arista.tag.v2.TagServiceStub.GetAll arista.tag.v2.TagConfigServiceStub.GetAll APIs.

        The Tags GetAll API for the workspace does not return anything from mainline and does not return deletions in the workspace.
        So to produce the workspace tags we need to fetch mainline and then "play back" each config change from the workspace.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched. Use "" for mainline.
            element_type: Optionally filter tags on type.
            creator_type: Optionally filter tags on creator type.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        TODO: Consider if we should add sub_type.

        Returns:
            List of Tag objects.
        """
        request = TagStreamRequest(
            partial_eq_filter=Tag(
                # Notice the "" for workspace, since we are fetching mainline.
                key=TagKey(workspace_id="", element_type=ELEMENT_TYPE_MAP[element_type]),
                creator_type=CREATOR_TYPE_MAP[creator_type],
            ),
            time=TimeBounds(start=None, end=time),
        )
        client = TagServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            tags = [response.value async for response in responses]
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '' (main), Element Type '{element_type}', Creator Type '{creator_type}'") or e

        # Now tags contain all mainline tags.
        if workspace_id == "" or creator_type in ["system", "external"]:
            return tags

        # Next up fetch the tags config from the workspace if workspace is not "".
        request = TagConfigStreamRequest(
            partial_eq_filter=TagConfig(
                # This time fetch for the actual workspace we are interested in.
                key=TagKey(workspace_id=workspace_id, element_type=ELEMENT_TYPE_MAP[element_type]),
            ),
            time=TimeBounds(start=None, end=time),
        )
        client = TagConfigServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                tag_config = response.value

                # Recreating a full tag object. Since this was in the workspace, it *must* be a user created tag.
                tag = Tag(key=tag_config.key, creator_type=CreatorType.USER)
                if tag_config.remove:
                    self._remove_item_from_list(tag, tags, self._match_tags)
                else:
                    self._upsert_item_in_list(tag, tags, self._match_tags)
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Element Type '{element_type}', Creator Type '{creator_type}'") or e

        return tags

    async def set_tags(
        self: CVClientProtocol,
        workspace_id: str,
        tags: list[tuple[str, str]],
        element_type: Literal["device", "interface"],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[TagKey]:
        """
        Set Tags using arista.tag.v2.TagConfigServiceStub.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            tags: List of tuples where each tuple is in the format (<tag_label>, <tag_value>).
            element_type: Type of Tag(s) to create.
            timeout: Base timeout in seconds. 0.1 second will be added per Tag.

        TODO: Consider if we should add sub_type.

        Returns:
            List of Tag objects after being set including any server-generated values.
        """
        request = TagConfigSetSomeRequest(values=[])
        for label, value in tags:
            request.values.append(
                TagConfig(
                    key=TagKey(
                        workspace_id=workspace_id,
                        element_type=ELEMENT_TYPE_MAP[element_type],
                        label=label,
                        value=value,
                    ),
                ),
            )

        client = TagConfigServiceStub(self._channel)
        try:
            responses = client.set_some(request, metadata=self._metadata, timeout=timeout + len(request.values) * 0.1)
            # Recreating a full tag object. Since we just created it, it *must* be a user created tag.
            tag_keys = [response.key async for response in responses]
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Element Type '{element_type}'") or e

        return tag_keys

    async def get_tag_assignments(
        self: CVClientProtocol,
        workspace_id: str,
        element_type: Literal["device", "interface"] | None = None,
        creator_type: Literal["user", "system", "external"] | None = None,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[TagAssignment]:
        """
        Get Tags using arista.tag.v2.TagAssignmentServiceStub.GetAll arista.tag.v2.TagAssignmentConfigServiceStub.GetAll APIs.

        The TagAssignment GetAll API for the workspace does not return anything from mainline and does not return deletions in the workspace.
        So to produce the workspace tag assignments we need to fetch mainline and then "play back" each config change from the workspace.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is fetched.
            element_type: Optionally filter tag assignments on tag type.
            creator_type: Optionally filter tag assignments on tag creator type.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        TODO: Consider if we should add sub_type.

        Returns:
            Workspace object matching the workspace_id
        """
        request = TagAssignmentStreamRequest(
            partial_eq_filter=TagAssignment(
                # Notice the "" for workspace, since we are fetching mainline.
                key=TagAssignmentKey(workspace_id="", element_type=ELEMENT_TYPE_MAP[element_type]),
                tag_creator_type=CREATOR_TYPE_MAP[creator_type],
            ),
            time=TimeBounds(start=None, end=time),
        )
        client = TagAssignmentServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            tag_assignments = [response.value async for response in responses]
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '' (main), Element Type '{element_type}', Creator Type '{creator_type}'") or e

        # Now tags contain all mainline tags.
        if workspace_id == "" or creator_type in ["system", "external"]:
            return tag_assignments

        # Next up fetch the tags config from the workspace if workspace is not "".
        request = TagAssignmentConfigStreamRequest(
            partial_eq_filter=TagAssignmentConfig(
                # This time fetch for the actual workspace we are interested in.
                key=TagKey(workspace_id=workspace_id, element_type=ELEMENT_TYPE_MAP[element_type]),
            ),
            time=TimeBounds(start=None, end=time),
        )
        client = TagAssignmentConfigServiceStub(self._channel)
        try:
            responses = client.get_all(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                tag_assignment_config = response.value

                # Recreating a full tag object. Since this was in the workspace, it *must* be a user created tag assignment.
                tag_assignment = TagAssignment(key=tag_assignment_config.key, tag_creator_type=CreatorType.USER)
                if tag_assignment_config.remove:
                    self._remove_item_from_list(tag_assignment, tag_assignments, self._match_tag_assignments)
                else:
                    self._upsert_item_in_list(tag_assignment, tag_assignments, self._match_tag_assignments)
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Element Type '{element_type}', Creator Type '{creator_type}'") or e

        return tag_assignments

    async def set_tag_assignments(
        self: CVClientProtocol,
        workspace_id: str,
        tag_assignments: list[tuple[str, str, str, str | None]],
        element_type: Literal["device", "interface"],
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> list[TagAssignment]:
        """
        Set Tags using arista.tag.v2.TagConfigServiceStub.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            tag_assignments: List of tuples where each tuple is in the format (<tag_label>, <tag_value>, <device_id/serial_number>, <interface_name | None>).
            element_type: Type of Tag(s) to assign.
            timeout: Base timeout in seconds. 0.1 second will be added per Tag assignment.

        TODO: Consider if we should add sub_type.

        Returns:
            List of TagAssignment objects after being set including any server-generated values.
        """
        request = TagAssignmentConfigSetSomeRequest(values=[])
        for label, value, device_id, interface_id in tag_assignments:
            request.values.append(
                TagAssignmentConfig(
                    key=TagAssignmentKey(
                        workspace_id=workspace_id,
                        element_type=ELEMENT_TYPE_MAP[element_type],
                        label=label,
                        value=value,
                        device_id=device_id,
                        interface_id=interface_id,
                    ),
                ),
            )

        client = TagAssignmentConfigServiceStub(self._channel)
        try:
            responses = client.set_some(request, metadata=self._metadata, timeout=timeout + len(request.values) * 0.1)
            tag_assignment_keys = [response.key async for response in responses]
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Element Type '{element_type}'") or e

        return tag_assignment_keys

    async def delete_tag_assignments(
        self: CVClientProtocol,
        workspace_id: str,
        tag_assignments: list[tuple[str, str, str, str | None]],
        element_type: Literal["device", "interface"],
        timeout: float = 30.0,
    ) -> list[TagAssignmentKey]:
        """
        Set Tags using arista.tag.v2.TagConfigServiceStub.SetSome API.

        Parameters:
            workspace_id: Unique identifier of the Workspace for which the information is set.
            tag_assignments: List of tuples where each tuple is in the format (<tag_label>, <tag_value>, <device_id/serial_number>, <interface_name | None>).
            element_type: Type of Tag assignment(s) to delete.
            timeout: Base timeout in seconds. 0.1 second will be added per Tag assignment.

        TODO: Consider if we should add sub_type.

        Returns:
            List of TagAssignmentKey objects after being set including any server-generated values.
        """
        request = TagAssignmentConfigSetSomeRequest(values=[])
        for label, value, device_id, interface_id in tag_assignments:
            request.values.append(
                TagAssignmentConfig(
                    key=TagAssignmentKey(
                        workspace_id=workspace_id,
                        element_type=ELEMENT_TYPE_MAP[element_type],
                        label=label,
                        value=value,
                        device_id=device_id,
                        interface_id=interface_id,
                    ),
                    remove=True,
                ),
            )

        client = TagAssignmentConfigServiceStub(self._channel)
        try:
            responses = client.set_some(request, metadata=self._metadata, timeout=timeout + len(request.values) * 0.1)
            tag_assignment_keys = [response.key async for response in responses]
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Element Type '{element_type}'") or e

        return tag_assignment_keys

    @staticmethod
    def _match_tags(a: Tag, b: Tag) -> bool:
        """Match up the properties of two tags without looking at the Workspace and Creator Type fields."""
        return all([a.key.element_type == b.key.element_type, a.key.label == b.key.label, a.key.value == b.key.value])

    @staticmethod
    def _match_tag_assignments(a: TagAssignment, b: TagAssignment) -> bool:
        """Match up the properties of two tag assignments without looking at the Workspace and Creator Type fields."""
        return all(
            [
                a.key.element_type == b.key.element_type,
                a.key.label == b.key.label,
                a.key.value == b.key.value,
                a.key.device_id == b.key.device_id,
                a.key.interface_id == b.key.interface_id,
            ],
        )
