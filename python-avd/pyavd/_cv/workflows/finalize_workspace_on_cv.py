# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.workspace.v1 import ResponseCode, ResponseStatus, WorkspaceState
from pyavd._cv.client.exceptions import CVInactiveDevices, CVWorkspaceBuildFailed, CVWorkspaceSubmitFailed, CVWorkspaceSubmitFailedInactiveDevices

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

    from .models import CVDevice, CVWorkspace

LOGGER = getLogger(__name__)

WORKSPACE_STATE_TO_FINAL_STATE_MAP = {
    WorkspaceState.ABANDONED: "abandoned",
    WorkspaceState.CONFLICTS: "build failed",
    WorkspaceState.PENDING: "pending",
    WorkspaceState.ROLLED_BACK: "pending",
    WorkspaceState.SUBMITTED: "submitted",
    WorkspaceState.UNSPECIFIED: None,
}


async def finalize_workspace_on_cv(workspace: CVWorkspace, cv_client: CVClient, devices: list[CVDevice], warnings: list) -> None:
    """
    Finalize a Workspace from the given result.CVWorkspace object.

    Depending on the requested state the Workspace will be left in pending, built, submitted, abandoned or deleted.
    In-place update the workspace state and creates/updates a ChangeControl object on the result object if applicable.
    """
    LOGGER.info("finalize_workspace_on_cv: %s", workspace)

    if workspace.requested_state in (workspace.state, "pending"):
        return

    workspace_config = await cv_client.build_workspace(workspace_id=workspace.id)
    build_result, cv_workspace = await cv_client.wait_for_workspace_response(workspace_id=workspace.id, request_id=workspace_config.request_params.request_id)
    if build_result.status != ResponseStatus.SUCCESS:
        workspace.state = "build failed"
        LOGGER.info("finalize_workspace_on_cv: %s", workspace)
        msg = (
            f"Failed to build workspace {workspace.id}: {build_result}. "
            f"See details: https://{cv_client._servers[0]}/cv/provisioning/workspaces?ws={workspace.id}"
        )
        raise CVWorkspaceBuildFailed(msg)

    workspace.state = "built"
    LOGGER.info("finalize_workspace_on_cv: %s", workspace)
    if workspace.requested_state == "built":
        return

    # We can only submit if the build was successful
    if workspace.requested_state == "submitted" and workspace.state == "built":
        workspace_config = await cv_client.submit_workspace(workspace_id=workspace.id, force=workspace.force)
        submit_result, cv_workspace = await cv_client.wait_for_workspace_response(
            workspace_id=workspace.id,
            request_id=workspace_config.request_params.request_id,
        )
        # Form a list of known inactive existing devices
        inactive_devices = [device for device in devices if not device._streaming]
        if submit_result.status != ResponseStatus.SUCCESS:
            workspace.state = "submit failed"
            # Unforced Workspace submission failed due to inactive devices.
            if submit_result.code == ResponseCode.INACTIVE_DEVICES_EXIST and not workspace.force:
                # Usecase where some of the devices that we targeted were known to be inactive prior to Workspace submission
                if inactive_devices:
                    msg = (
                        f"Failed to submit CloudVision Workspace due to the presence of inactive devices. "
                        f"Use force to override. Inactive devices: {inactive_devices}."
                    )
                    LOGGER.warning(msg)
                    raise CVWorkspaceSubmitFailedInactiveDevices(msg)
                # Usecase where all devices were actively streaming prior to Workspace submission
                msg = (
                    "Failed to submit CloudVision Workspace due to the presence of inactive devices. "
                    "Use force to override. Exact list of inactive devices is unknown."
                )
                LOGGER.warning(msg)
                raise CVWorkspaceSubmitFailedInactiveDevices(msg)

            # If Workspace submission failed for any other reason and known inactive devices were present - append information to warnings.
            if inactive_devices:
                msg = f"Inactive devices present: {inactive_devices}"
                LOGGER.warning(msg)
                warnings.append(CVInactiveDevices(msg))

            # If Workspace submission failed for any other reason - raise general exception.
            LOGGER.info("finalize_workspace_on_cv: %s", workspace)
            msg = f"Failed to submit workspace {workspace.id}: {submit_result}"
            raise CVWorkspaceSubmitFailed(msg)
        # If successful Workspace submission with inactive devices was forced - append information to warnings.
        if inactive_devices and workspace.force:
            msg = f"Inactive devices present: {inactive_devices}"
            LOGGER.info(msg)
            warnings.append(CVInactiveDevices(msg))

        workspace.state = "submitted"
        if cv_workspace.cc_ids.values:
            workspace.change_control_id = cv_workspace.cc_ids.values[0]
        LOGGER.info("finalize_workspace_on_cv: %s", workspace)
        return

    # We can abort or delete even if we got some unexpected build state.
    if workspace.requested_state == "abandoned":
        await cv_client.abandon_workspace(workspace_id=workspace.id)
        workspace.state = "abandoned"
        LOGGER.info("finalize_workspace_on_cv: %s", workspace)
        return

    if workspace.requested_state == "deleted":
        await cv_client.delete_workspace(workspace_id=workspace.id)
        workspace.state = "deleted"
        LOGGER.info("finalize_workspace_on_cv: %s", workspace)
        return

    return
