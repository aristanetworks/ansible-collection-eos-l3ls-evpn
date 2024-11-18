# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.workspace.v1 import ResponseStatus, WorkspaceState
from pyavd._cv.client.exceptions import CVWorkspaceBuildFailed, CVWorkspaceSubmitFailed

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

    from .models import CVDevice, CVWorkspace

from .constants import EOS_CLI_PORTFAST_WARNING
from .models import (
    CVWorkspaceBuildConfigValidationError,
    CVWorkspaceBuildConfigValidationResult,
    CVWorkspaceBuildImageValidationError,
    CVWorkspaceBuildImageValidationResult,
    CVWorkspaceBuildImageValidationWarning,
    CVWorkspaceBuildResult,
    CVWorkspaceBuildStageState,
)

LOGGER = getLogger(__name__)

WORKSPACE_STATE_TO_FINAL_STATE_MAP = {
    WorkspaceState.ABANDONED: "abandoned",
    WorkspaceState.CONFLICTS: "build failed",
    WorkspaceState.PENDING: "pending",
    WorkspaceState.ROLLED_BACK: "pending",
    WorkspaceState.SUBMITTED: "submitted",
    WorkspaceState.UNSPECIFIED: None,
}


async def finalize_workspace_on_cv(workspace: CVWorkspace, cv_client: CVClient, devices: list[CVDevice]) -> None:
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
    workspace.build_id = cv_workspace.last_build_id
    workspace.build_results = await process_workspace_build_details(workspace=workspace, cv_client=cv_client, devices=devices)
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
        if submit_result.status != ResponseStatus.SUCCESS:
            workspace.state = "submit failed"
            LOGGER.info("finalize_workspace_on_cv: %s", workspace)
            msg = f"Failed to submit workspace {workspace.id}: {submit_result}"
            raise CVWorkspaceSubmitFailed(msg)

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


async def process_workspace_build_details(
    workspace: CVWorkspace,
    cv_client: CVClient,
    devices: list[CVDevice],
) -> list[CVWorkspaceBuildResult]:
    """
    Get and parse Workspace Build Details Response.

    Extracts (with ability to suppress warnings based on the pre-defined use-cases or custom pattern strings):
    - Config validation errors.
    - Config validation warnings.
    - Image validation errors.
    - Image validation warnings.

    Parameters:
        workspace: Active Workspace.
        cv_client: CVClient.
        devices: List of CVDevice objects representing existing CV devices.

    Returns:
        List of 'CVWorkspaceBuildResult's describing observed Workspace build validation errors and warnings per targeted device.
    """
    try:
        workspace_build_details_stream_response = await cv_client.get_workspace_build_details(workspace_id=workspace.id, build_id=workspace.build_id)

        if workspace.build_warnings:
            workspace_build_warning_suppress_list = workspace.build_warnings_suppress_patterns[:]
            if workspace.build_warnings_suppress_portfast and EOS_CLI_PORTFAST_WARNING not in workspace_build_warning_suppress_list:
                workspace_build_warning_suppress_list.append(EOS_CLI_PORTFAST_WARNING)

        workspace_build_results = [
            CVWorkspaceBuildResult(
                device=next((device for device in devices if device.serial_number == device_id), None)
                if (device_id := getattr(getattr(getattr(response, "value", None), "key", None), "device_id", None)) is not None
                else None,
                stages_states=[
                    CVWorkspaceBuildStageState(
                        stage=stage,
                        state=getattr(state, "name", None),
                    )
                    for stage, state in getattr(getattr(getattr(response, "value", None), "build_stage_state", None), "values", {}).items()
                ],
                config_validation=CVWorkspaceBuildConfigValidationResult(
                    errors=[
                        CVWorkspaceBuildConfigValidationError(
                            error_code=getattr(getattr(config_validation_error, "error_code", None), "name", None),
                            error_msg=getattr(config_validation_error, "error_msg", None),
                            line_num=getattr(config_validation_error, "line_num", None),
                            configlet_name=getattr(config_validation_error, "configlet_name", None),
                        )
                        for config_validation_error in getattr(
                            getattr(getattr(getattr(response, "value", None), "config_validation_result", None), "errors", None), "values", []
                        )
                    ],
                    warnings=[
                        CVWorkspaceBuildConfigValidationError(
                            error_code=getattr(getattr(config_validation_warning, "error_code", None), "name", None),
                            error_msg=error_msg,
                            line_num=getattr(config_validation_warning, "line_num", None),
                            configlet_name=getattr(config_validation_warning, "configlet_name", None),
                        )
                        for config_validation_warning in getattr(
                            getattr(getattr(getattr(response, "value", None), "config_validation_result", None), "warnings", None), "values", []
                        )
                        if (error_msg := getattr(config_validation_warning, "error_msg", None)) not in workspace_build_warning_suppress_list
                    ]
                    if workspace.build_warnings
                    else [],
                ),
                image_validation=CVWorkspaceBuildImageValidationResult(
                    image_input_error=getattr(getattr(getattr(response, "value", None), "image_validation_result", None), "image_input_error", None),
                    errors=[
                        CVWorkspaceBuildImageValidationError(
                            sku=getattr(image_validation_error, "sku", None),
                            error_code=getattr(getattr(image_validation_error, "error_code", None), "name", None),
                            error_msg=getattr(image_validation_error, "error_msg", None),
                        )
                        for image_validation_error in getattr(
                            getattr(getattr(getattr(response, "value", None), "image_validation_result", None), "errors", None), "values", []
                        )
                    ],
                    warnings=[
                        CVWorkspaceBuildImageValidationWarning(
                            sku=getattr(image_validation_warning, "sku", None),
                            warning_code=warning_code,
                            warning_msg=warning_msg,
                        )
                        for image_validation_warning in getattr(
                            getattr(getattr(getattr(response, "value", None), "image_validation_result", None), "warnings", None), "values", []
                        )
                        if (warning_msg := getattr(image_validation_warning, "warning_msg", None)) not in workspace_build_warning_suppress_list
                    ]
                    if workspace.build_warnings
                    else [],
                ),
            )
            async for response in workspace_build_details_stream_response
            if (
                getattr(getattr(getattr(response, "value", None), "config_validation_result", None), "errors", None)
                or getattr(getattr(getattr(response, "value", None), "image_validation_result", None), "errors", None)
            )
            or (
                workspace.build_warnings
                and (
                    getattr(getattr(getattr(response, "value", None), "config_validation_result", None), "warnings", None)
                    or getattr(getattr(getattr(response, "value", None), "image_validation_result", None), "warnings", None)
                )
                and (
                    not {
                        i.error_msg
                        for i in getattr(getattr(getattr(getattr(response, "value", None), "config_validation_result", None), "warnings", None), "values", [])
                    }.issubset(set(workspace_build_warning_suppress_list))
                    or not {
                        i.warning_msg
                        for i in getattr(getattr(getattr(getattr(response, "value", None), "image_validation_result", None), "warnings", None), "values", [])
                    }.issubset(set(workspace_build_warning_suppress_list))
                )
            )
        ]

    except Exception as e:
        LOGGER.info(
            "process_workspace_build_details: Failed to fetch and process Workspace build results for workspace '%s' and it's build_id '%s'. Error: '%s'",
            workspace.id,
            workspace.build_id,
            e,
        )
        return []

    else:
        return workspace_build_results
