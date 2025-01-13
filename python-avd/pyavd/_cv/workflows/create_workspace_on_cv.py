# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.workspace.v1 import WorkspaceState
from pyavd._cv.client.exceptions import CVResourceInvalidState, CVResourceNotFound

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

    from .models import CVWorkspace

LOGGER = getLogger(__name__)


async def create_workspace_on_cv(workspace: CVWorkspace, cv_client: CVClient) -> None:
    """
    Create or update a Workspace from the given workspace object.

    In-place update the workspace state.
    """
    LOGGER.info("create_workspace_on_cv: %s", workspace)
    try:
        existing_workspace = await cv_client.get_workspace(workspace_id=workspace.id)
        if existing_workspace.state == WorkspaceState.PENDING:
            workspace.state = "pending"
        else:
            msg = "The requested workspace is not in state 'pending'"
            raise CVResourceInvalidState(msg)
    except CVResourceNotFound:
        await cv_client.create_workspace(workspace_id=workspace.id, display_name=workspace.name, description=workspace.description)
        workspace.state = "pending"
