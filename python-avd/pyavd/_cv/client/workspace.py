# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING, Literal, Protocol
from uuid import uuid4

from pyavd._cv.api.arista.workspace.v1 import (
    Request,
    RequestParams,
    Response,
    Workspace,
    WorkspaceConfig,
    WorkspaceConfigDeleteRequest,
    WorkspaceConfigServiceStub,
    WorkspaceConfigSetRequest,
    WorkspaceKey,
    WorkspaceRequest,
    WorkspaceServiceStub,
    WorkspaceStreamRequest,
)

from .constants import DEFAULT_API_TIMEOUT
from .exceptions import get_cv_client_exception

if TYPE_CHECKING:
    from datetime import datetime

    from . import CVClientProtocol


LOGGER = getLogger(__name__)

REQUEST_MAP = {
    "abandon": Request.ABANDON,
    "cancel_build": Request.CANCEL_BUILD,
    "rollback": Request.ROLLBACK,
    "start_build": Request.START_BUILD,
    "submit": Request.SUBMIT,
    None: None,
}


class WorkspaceMixin(Protocol):
    """Only to be used as mixin on CVClient class."""

    workspace_api_version: Literal["v1"] = "v1"

    async def get_workspace(
        self: CVClientProtocol,
        workspace_id: str,
        time: datetime | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> Workspace:
        """
        Get Workspace using arista.workspace.v1.WorkspaceService.GetOne API.

        Parameters:
            workspace_id: Unique identifier the workspace.
            time: Timestamp from which the information is fetched. `now()` if not set.
            timeout: Timeout in seconds.

        Returns:
            Workspace object matching the workspace_id
        """
        request = WorkspaceRequest(
            key=WorkspaceKey(
                workspace_id=workspace_id,
            ),
            time=time,
        )
        client = WorkspaceServiceStub(self._channel)

        try:
            response = await client.get_one(request, metadata=self._metadata, timeout=timeout)
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}'") or e

        return response.value

    async def create_workspace(
        self: CVClientProtocol,
        workspace_id: str,
        display_name: str | None = None,
        description: str | None = None,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> WorkspaceConfig:
        """
        Create Workspace using arista.workspace.v1.WorkspaceConfigService.Set API.

        Parameters:
            workspace_id: Unique identifier the workspace.
            display_name: Workspace Name.
            description: Workspace description.
            timeout: Timeout in seconds.

        Returns:
            WorkspaceConfig object after being set including any server-generated values.
        """
        request = WorkspaceConfigSetRequest(
            WorkspaceConfig(
                key=WorkspaceKey(workspace_id=workspace_id),
                display_name=display_name,
                description=description,
            ),
        )
        client = WorkspaceConfigServiceStub(self._channel)
        response = await client.set(request, metadata=self._metadata, timeout=timeout)
        return response.value

    async def abandon_workspace(
        self: CVClientProtocol,
        workspace_id: str,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> WorkspaceConfig:
        """
        Abandon Workspace using arista.workspace.v1.WorkspaceConfigService.Set API.

        Parameters:
            workspace_id: Unique identifier the workspace.
            timeout: Timeout in seconds.

        Returns:
            WorkspaceConfig object after being set including any server-generated values.
        """
        request = WorkspaceConfigSetRequest(
            WorkspaceConfig(
                key=WorkspaceKey(workspace_id=workspace_id),
                request=Request.ABANDON,
                request_params=RequestParams(
                    request_id=f"req-{uuid4()}",
                ),
            ),
        )
        client = WorkspaceConfigServiceStub(self._channel)
        response = await client.set(request, metadata=self._metadata, timeout=timeout)
        return response.value

    async def build_workspace(
        self: CVClientProtocol,
        workspace_id: str,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> WorkspaceConfig:
        """
        Request a build of the Workspace using arista.workspace.v1.WorkspaceConfigService.Set API.

        Parameters:
            workspace_id: Unique identifier the workspace.
            timeout: Timeout in seconds.

        Returns:
            WorkspaceConfig object after being set including any server-generated values.
        """
        request = WorkspaceConfigSetRequest(
            WorkspaceConfig(
                key=WorkspaceKey(workspace_id=workspace_id),
                request=Request.START_BUILD,
                request_params=RequestParams(
                    request_id=f"req-{uuid4()}",
                ),
            ),
        )
        client = WorkspaceConfigServiceStub(self._channel)
        response = await client.set(request, metadata=self._metadata, timeout=timeout)
        return response.value

    async def delete_workspace(
        self: CVClientProtocol,
        workspace_id: str,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> WorkspaceKey:
        """
        Delete Workspace using arista.workspace.v1.WorkspaceConfigService.Delete API.

        Parameters:
            workspace_id: Unique identifier the workspace.
            timeout: Timeout in seconds.

        Returns:
            WorkspaceConfig object after being set including any server-generated values.
        """
        request = WorkspaceConfigDeleteRequest(key=WorkspaceKey(workspace_id=workspace_id))
        client = WorkspaceConfigServiceStub(self._channel)
        response = await client.delete(request, metadata=self._metadata, timeout=timeout)
        return response.key

    async def submit_workspace(
        self: CVClientProtocol,
        workspace_id: str,
        force: bool = False,
        timeout: float = DEFAULT_API_TIMEOUT,
    ) -> WorkspaceConfig:
        """
        Request submission of the Workspace using arista.workspace.v1.WorkspaceConfigService.Set API.

        Parameters:
            workspace_id: Unique identifier the Workspace.
            force: Force submit the Workspace.
            timeout: Timeout in seconds.

        Returns:
            WorkspaceConfig object after being set including any server-generated values.
        """
        request = WorkspaceConfigSetRequest(
            WorkspaceConfig(
                key=WorkspaceKey(workspace_id=workspace_id),
                request=Request.SUBMIT_FORCE if force else Request.SUBMIT,
                request_params=RequestParams(request_id=f"req-{uuid4()}"),
            ),
        )
        client = WorkspaceConfigServiceStub(self._channel)
        response = await client.set(request, metadata=self._metadata, timeout=timeout)
        LOGGER.debug("submit_workspace: Got response to submission: %s", response.value)
        return response.value

    async def wait_for_workspace_response(
        self: CVClientProtocol,
        workspace_id: str,
        request_id: str,
        timeout: float = 3600.0,
    ) -> tuple[Response, Workspace]:
        """
        Monitor a Workspace using arista.workspace.v1.WorkspaceService.Subscribe API for a response to the given request_id.

        Blocks until a response is returned or timed out.

        Parameters:
            workspace_id: Unique identifier the Workspace.
            request_id: Unique identifier for the Request.
            timeout: Timeout in seconds for the Workspace to build.

        Returns:
            Tuple of (<Response object for the request_id>, <Full Workspace object>)
        """
        request = WorkspaceStreamRequest(
            partial_eq_filter=[
                Workspace(
                    key=WorkspaceKey(workspace_id=workspace_id),
                ),
            ],
        )
        client = WorkspaceServiceStub(self._channel)
        try:
            responses = client.subscribe(request, metadata=self._metadata, timeout=timeout)
            async for response in responses:
                if request_id in response.value.responses.values:
                    LOGGER.info("wait_for_workspace_response: Got response for request '%s': %s", request_id, response.value.responses.values[request_id])
                    return response.value.responses.values[request_id], response.value
                LOGGER.debug(
                    "wait_for_workspace_response: Got workspace update but not for request_id '%s'. Workspace State: %s",
                    request_id,
                    response.value.state,
                )
        except Exception as e:
            raise get_cv_client_exception(e, f"Workspace ID '{workspace_id}', Request ID '{request_id}") or e
