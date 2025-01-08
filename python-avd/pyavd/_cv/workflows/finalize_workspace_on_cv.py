# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from re import Pattern
from re import compile as re_compile
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.workspace.v1 import ResponseStatus, WorkspaceBuildDetails, WorkspaceState
from pyavd._cv.client.exceptions import CVWorkspaceBuildFailed, CVWorkspaceSubmitFailed
from pyavd._utils import get_v2

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


def prepare_build_warnings_suppress_patterns(
    workspace: CVWorkspace,
    static_suppression_patterns: list[str],
) -> list[Pattern]:
    """
    Process static and custom inputs for Build Warnings Suppression and return unified list of Regex patterns.

    Parameters:
        workspace: Active Workspace.
        static_suppression_patterns: List of pre-defined Regex string patterns for matching undesired warnings.

    Returns:
        Unified list of compiled Regex patterns describing Workspace Build warnings that we would like to suppress.
    """
    # Deduplicate list of patterns from user
    workspace_build_warning_suppress_list = list(set(workspace.build_warnings_suppress_patterns[:]))
    if workspace.build_warnings_suppress_portfast:
        for static_suppression_pattern in static_suppression_patterns:
            if static_suppression_pattern not in workspace_build_warning_suppress_list:
                workspace_build_warning_suppress_list.append(static_suppression_pattern)

    compiled_workspace_build_warning_suppress_list: list[Pattern] = []
    for proposed_regex_pattern in workspace_build_warning_suppress_list:
        try:
            compiled_workspace_build_warning_suppress_list.append(re_compile(proposed_regex_pattern))
        except Exception as e:  # noqa: PERF203
            LOGGER.warning(
                "prepare_build_warnings_suppress_patterns: Failed to process proposed regex pattern '%s'. "
                "This incorrect pattern will not be used for warnings suppression. Error: '%s'",
                proposed_regex_pattern,
                e,
            )
            # Delete invalid regex pattern string from workspace.build_warnings_suppress_patterns
            workspace.build_warnings_suppress_patterns = [item for item in workspace.build_warnings_suppress_patterns if item != proposed_regex_pattern]

    return compiled_workspace_build_warning_suppress_list


async def produce_cvworkspace_build_result(
    workspace: CVWorkspace,
    workspace_build_details: list[WorkspaceBuildDetails],
    compiled_workspace_build_warning_suppress_list: list[Pattern],
    devices: list[CVDevice],
) -> CVWorkspaceBuildResult:
    """
    Process list of WorkspaceBuildDetails to generate CVWorkspaceBuildResult suppressing undesired warnings.

    Parameters:
        workspace: Active Workspace.
        workspace_build_details: List of WorkspaceBuildDetails objects.
        compiled_workspace_build_warning_suppress_list: List of compiled Regex patterns for matching undesired warnings.
        devices: List of CVDevice objects representing existing CV devices.

    Returns:
        CVWorkspaceBuildResult object defining details of the Workspace build.
    """
    return [
        CVWorkspaceBuildResult(
            device=next((device for device in devices if device.serial_number == device_id), None)
            if (device_id := workspace_build_details_item.key.device_id) is not None
            else None,
            stages_states=[
                CVWorkspaceBuildStageState(
                    stage=stage,
                    state=state.name,
                )
                for stage, state in get_v2(workspace_build_details_item, "build_stage_state.values", {}).items()
            ],
            config_validation=CVWorkspaceBuildConfigValidationResult(
                errors=[
                    CVWorkspaceBuildConfigValidationError(
                        error_code=config_validation_error.error_code.name,
                        error_msg=config_validation_error.error_msg,
                        line_num=config_validation_error.line_num,
                        configlet_name=config_validation_error.configlet_name,
                    )
                    for config_validation_error in get_v2(workspace_build_details_item, "config_validation_result.errors.values", [])
                ],
                warnings=[
                    CVWorkspaceBuildConfigValidationError(
                        error_code=config_validation_warning.error_code.name,
                        error_msg=config_validation_warning.error_msg,
                        line_num=config_validation_warning.line_num,
                        configlet_name=config_validation_warning.configlet_name,
                    )
                    for config_validation_warning in get_v2(workspace_build_details_item, "config_validation_result.warnings.values", [])
                    if not any(pattern.search(config_validation_warning.error_msg) for pattern in compiled_workspace_build_warning_suppress_list)
                ]
                if workspace.build_warnings
                else [],
            ),
            image_validation=CVWorkspaceBuildImageValidationResult(
                image_input_error=workspace_build_details_item.image_validation_result.image_input_error,
                errors=[
                    CVWorkspaceBuildImageValidationError(
                        sku=image_validation_error.sku,
                        error_code=image_validation_error.error_code.name,
                        error_msg=image_validation_error.error_msg,
                    )
                    for image_validation_error in get_v2(workspace_build_details_item, "image_validation_result.errors.values", [])
                ],
                warnings=[
                    CVWorkspaceBuildImageValidationWarning(
                        sku=image_validation_warning.sku,
                        warning_code=image_validation_warning.warning_code,
                        warning_msg=image_validation_warning.warning_msg,
                    )
                    for image_validation_warning in get_v2(workspace_build_details_item, "image_validation_result.warnings.values", [])
                    if not any(pattern.search(image_validation_warning.warning_msg) for pattern in compiled_workspace_build_warning_suppress_list)
                ]
                if workspace.build_warnings
                else [],
            ),
        )
        for workspace_build_details_item in workspace_build_details
        if isinstance(workspace_build_details_item, WorkspaceBuildDetails)
        and (
            (workspace_build_details_item.config_validation_result.errors or workspace_build_details_item.image_validation_result.errors)
            or (
                workspace.build_warnings
                and (workspace_build_details_item.config_validation_result.warnings or workspace_build_details_item.image_validation_result.warnings)
                and (
                    len(compiled_workspace_build_warning_suppress_list) == 0
                    or {False}
                    in [
                        {bool(pattern.search(i.error_msg)) for pattern in compiled_workspace_build_warning_suppress_list}
                        for i in get_v2(workspace_build_details_item, "config_validation_result.warnings.values", [])
                    ]
                    or {False}
                    in [
                        {bool(pattern.search(i.warning_msg)) for pattern in compiled_workspace_build_warning_suppress_list}
                        for i in get_v2(workspace_build_details_item, "image_validation_result.warnings.values", [])
                    ]
                )
            )
        )
    ]


async def process_workspace_build_details(
    workspace: CVWorkspace,
    cv_client: CVClient,
    devices: list[CVDevice],
) -> list[CVWorkspaceBuildResult]:
    """
    Get and parse Workspace Build Details.

    Extracts (with ability to suppress warnings based on the pre-defined use-cases or custom regex pattern(s)):
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
    workspace_build_details = await cv_client.get_workspace_build_details(workspace_id=workspace.id, build_id=workspace.build_id)

    if workspace.build_warnings:
        compiled_workspace_build_warning_suppress_list = prepare_build_warnings_suppress_patterns(
            workspace=workspace, static_suppression_patterns=[EOS_CLI_PORTFAST_WARNING]
        )
    else:
        compiled_workspace_build_warning_suppress_list = []

    return await produce_cvworkspace_build_result(
        workspace=workspace,
        workspace_build_details=workspace_build_details,
        compiled_workspace_build_warning_suppress_list=compiled_workspace_build_warning_suppress_list,
        devices=devices,
    )
