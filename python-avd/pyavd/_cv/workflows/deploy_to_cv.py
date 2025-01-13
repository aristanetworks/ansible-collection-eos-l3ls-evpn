# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVClientException

from .create_workspace_on_cv import create_workspace_on_cv
from .deploy_configs_to_cv import deploy_configs_to_cv
from .deploy_cv_pathfinder_metadata_to_cv import deploy_cv_pathfinder_metadata_to_cv
from .deploy_studio_inputs_to_cv import deploy_studio_inputs_to_cv
from .deploy_tags_to_cv import deploy_tags_to_cv
from .finalize_change_control_on_cv import finalize_change_control_on_cv
from .finalize_workspace_on_cv import finalize_workspace_on_cv
from .models import (
    CloudVision,
    CVChangeControl,
    CVDeviceTag,
    CVEosConfig,
    CVInterfaceTag,
    CVPathfinderMetadata,
    CVStudioInputs,
    CVTimeOuts,
    CVWorkspace,
    DeployToCvResult,
)
from .verify_devices_on_cv import verify_devices_on_cv

LOGGER = getLogger(__name__)


async def deploy_to_cv(
    cloudvision: CloudVision,
    workspace: CVWorkspace | None = None,
    change_control: CVChangeControl | None = None,
    configs: list[CVEosConfig] | None = None,
    device_tags: list[CVDeviceTag] | None = None,
    interface_tags: list[CVInterfaceTag] | None = None,
    studio_inputs: list[CVStudioInputs] | None = None,
    cv_pathfinder_metadata: list[CVPathfinderMetadata] | None = None,
    skip_missing_devices: bool = False,
    strict_tags: bool = True,
    timeouts: CVTimeOuts | None = None,  # pylint: disable=unused-argument # noqa: ARG001
) -> DeployToCvResult:
    """
    Deploy various objects to CloudVision.

    For any device referred under `configs`, `device_tags` and `interface_tags` the device:
    - The device must be present in the CloudVision Inventory and onboarded to the "Inventory & Topology Studio".
        - TODO: See if we can onboard ZTP devices and/or preprovision.
    - The hostname will we updated in the I&T Studio.
    - The `serial_number` and `system_mac_address` properties will be inplace updated in the given CVDevice objects.

    TODO: Respect timeouts and add more.

    Parameters:
        cloudvision: CloudVision instance to deploy to.
        workspace: CloudVision Workspace to create or use for the deployment. \
            If the Workspace already exists, it must be in 'pending' state. \
            The `state` property will be inplace updated in the given CVWorkSpace object.
        change_control: CloudVision Change Control to create for the deployment. \
            It is not supported to reuse an existing Change Control, so the `id` field should not be set in the given CVChangeControl object. \
            The `id` and `state` properties will be inplace updated in the given CVChangeControl object.
        configs: Configs to be deployed using the "Static Configlet Studio".
        device_tags: Device Tags to be deployed and assigned.
        interface_tags: Interface Tags to be deployed and assigned.
        studio_inputs: Studio Inputs to be deployed. \
            It is not supported to update overlapping input paths for the same studio in the same deployment.
        cv_pathfinder_metadata: Special metadata for CV Pathfinder solution. Metadata will be combined and deployed to the hidden metadata studio.
        skip_missing_devices: If `True` anything that can be deployed will get deployed. \
            Otherwise the Workspace will be abandoned on any issue.
        strict_tags: If `True` other tags associated with the devices will get removed. \
            Otherwise other tags will be left as-is. \
            Other Tags with the same label are always removed.

    TODO: Consider implementing "strict configs".
          Very hard to implement since configs can now come from various studios and tag queries we have little control over.
            strict_configs: If `True` other configs associated with the devices will get removed. \
                Otherwise other configs will be left as-is.
          We could decide to just remove config assignments under our main container to devices not mentioned in the run.

    Returns:
        Object containing the results of the deployment including all associated objects.

    TODO: Workflow:
        + Create result object.
            + Add workspace object to result if given otherwise create a new workspace object we can return.
            - Add objects to result.deployed_x/skipped_x as we go through each of the following steps.
        + Initialize CVClient
        + Gather all devices from the given lists.
        + On CV Identify all devices based on hostname, serial number or System MAC address.
            + In-place update device objects.
        + On CV Create or update existing Workspace with name and description.
            + In-place update workspace object.
        + On CV in "Inventory & Topology Studio" set/verify hostnames.
        + On CV in "Static Configlet Studio" upload configlets and assign to devices.
            - TODO: Consider if we should create a hierarchy of configuration containers.
                    For now a single folder "AVD Configurations".
        + On CV add and assign device tags.
        + On CV add and assign interface tags.
        + On CV deploy studio inputs
        + On CV deploy cv_pathfinder_metadata
        + On CV build, submit, abandon, delete the Workspace as applicable based on requested state.
            + In-place update workspace and result object.
        + If not submitting the Workspace return the result object. Otherwise continue.
        + Wait for Workspace submission to return a change control id.
            + Update or create a CVChangeControl object and add to result.
        + On CV set description on the created change control
            - TODO: apply the CC template if given.
        + On CV approve, submit the Change Control as applicable based on requested state.
            - TODO: Support Deleting the CC
        + Return result object.
    """
    LOGGER.info("deploy_to_cv:")
    result = DeployToCvResult(workspace=workspace or CVWorkspace(), change_control=change_control)
    if device_tags is None:
        device_tags = []
    if interface_tags is None:
        interface_tags = []
    if configs is None:
        configs = []
    if studio_inputs is None:
        studio_inputs = []
    if cv_pathfinder_metadata is None:
        cv_pathfinder_metadata = []
    try:
        async with CVClient(servers=cloudvision.servers, token=cloudvision.token, verify_certs=cloudvision.verify_certs) as cv_client:
            # Create workspace
            await create_workspace_on_cv(workspace=result.workspace, cv_client=cv_client)

            try:
                # Verify devices exist and update CVDevice objects with _exists_on_cv.
                # Depending on skip_missing_devices we will raise or skip missing devices.
                # Since verify_devices will silently return if _exists_on_cv is already set,
                # we can just send all the items even if we have duplicate device objects.
                await verify_devices_on_cv(
                    devices=(
                        [tag.device for tag in device_tags if tag.device is not None]
                        + [tag.device for tag in interface_tags if tag.device is not None]
                        + [config.device for config in configs if config.device is not None]
                    ),
                    workspace_id=result.workspace.id,
                    skip_missing_devices=skip_missing_devices,
                    warnings=result.warnings,
                    cv_client=cv_client,
                )

                # Deploy device tags
                await deploy_tags_to_cv(
                    tags=device_tags,
                    workspace=result.workspace,
                    strict=strict_tags,
                    skipped_tags=result.skipped_device_tags,
                    deployed_tags=result.deployed_device_tags,
                    removed_tags=result.removed_device_tags,
                    cv_client=cv_client,
                )

                # Deploy interface tags
                await deploy_tags_to_cv(
                    tags=interface_tags,
                    workspace=result.workspace,
                    strict=strict_tags,
                    skipped_tags=result.skipped_interface_tags,
                    deployed_tags=result.deployed_interface_tags,
                    removed_tags=result.removed_interface_tags,
                    cv_client=cv_client,
                )

                # Deploy configs
                await deploy_configs_to_cv(
                    configs=configs,
                    result=result,
                    cv_client=cv_client,
                )

                # Deploy Studio Inputs
                await deploy_studio_inputs_to_cv(
                    studio_inputs=studio_inputs,
                    result=result,
                    cv_client=cv_client,
                )

                # Deploy CV Pathfinder metadata
                await deploy_cv_pathfinder_metadata_to_cv(
                    cv_pathfinder_metadata=cv_pathfinder_metadata,
                    result=result,
                    cv_client=cv_client,
                )

            except CVClientException as e:
                result.errors.append(e)
                result.failed = True

            # Build, submit or abandon Workspace. If failed, we always abandon.
            if result.failed:
                await cv_client.abandon_workspace(workspace_id=result.workspace.id)
                result.workspace.state = "abandoned"
                return result

            await finalize_workspace_on_cv(workspace=result.workspace, cv_client=cv_client)

            # Create/update CVChangeControl object with ID created by workspace.
            if result.workspace.change_control_id is not None:
                if result.change_control is None:
                    result.change_control = CVChangeControl()
                result.change_control.id = result.workspace.change_control_id

            # This is a separate "if" to allow to test stuff on a change control not created by the workspace.
            # You can run this by setting "id" directly in the given change control object.
            # TODO: Remove once we are done with testing (?)
            # Run, Delete or run and wait for Change Control if the workspace created one.
            if result.change_control is not None and result.change_control.id is not None:
                await finalize_change_control_on_cv(change_control=result.change_control, cv_client=cv_client)

    except CVClientException as e:
        result.errors.append(e)
        result.failed = True

    return result
