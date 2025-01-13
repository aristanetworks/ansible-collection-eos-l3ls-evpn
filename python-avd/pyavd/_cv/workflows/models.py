# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Literal
from uuid import uuid4


@dataclass
class CloudVision:
    servers: str | list[str]
    token: str
    verify_certs: bool = True


@dataclass
class CVChangeControl:
    name: str | None = None
    description: str | None = None
    id: str | None = None
    """ `id` should not be set on the request. It will be updated with the ID of the created Change Control. """
    change_control_template: CVChangeControlTemplate | None = None
    requested_state: Literal["pending approval", "approved", "running", "completed", "deleted"] = "pending approval"
    """
    The requested state for the Change Control.

    - `"pending approval"` (default): Leave the Change Control in "pending approval" state.
    - `"approved"`: Approve the Change Control but do not start.
    - `"running"`: Approve and start the Change Control. Do not wait for the Change Control to be completed or failed.
    - `"completed"`: Approve and start the Change Control. Wait for the Change Control to be completed.
    - `"deleted"`: Create and delete the Change Control. Used for dry-run where no changes will be committed to the network.
    """
    state: Literal["pending approval", "approved", "running", "completed", "deleted", "failed"] | None = None


@dataclass
class CVChangeControlTemplate:
    name: str
    id: str | None = None


@dataclass
class CVDeviceTag:
    label: str
    value: str
    device: CVDevice | None = None


@dataclass
class CVInterfaceTag:
    label: str
    value: str
    device: CVDevice | None = None
    interface: str | None = None
    """Must be set if device is set"""


@dataclass
class CVStudioInputs:
    studio_id: str
    inputs: Any
    """Data to set at the given path."""
    input_path: list[str] = field(default_factory=list)
    """Data path elements for setting specific inputs. If not given, inputs are set at the root, replacing all existing inputs."""


@dataclass
class CVPathfinderMetadata:
    metadata: dict
    device: CVDevice | None = None


@dataclass
class CVWorkspace:
    name: str = field(default_factory=lambda: f"AVD {datetime.now()}")
    description: str | None = None
    id: str = field(default_factory=lambda: f"ws-{uuid4()}")
    requested_state: Literal["pending", "built", "submitted", "abandoned", "deleted"] = "submitted"
    """
    The requested state for the Workspace.

    - `"pending"`: Leave the Workspace in pending state.
    - `"built"`: Build the Workspace but do not submit.
    - `"submitted"` (default): Build and submit the Workspace.
    - `"abandoned"`: Build and then abandon the Workspace. \
        Used for dry-run where no changes will be committed to CloudVision.
    - `"deleted"`: Build, abort and then delete the Workspace. \
        Used for dry-run where no changes will be committed to CloudVision and the temporary Workspace will be removed to avoid "clutter".
    """
    force: bool = False
    """ Force submit the workspace even if some devices are not actively streaming to CloudVision."""
    state: Literal["pending", "built", "submitted", "build failed", "submit failed", "abandoned", "deleted"] | None = None
    """The final state of the Workspace. Do not set this manually."""
    change_control_id: str | None = None
    """Do not set this manually."""


@dataclass
class DeployChangeControlResult:
    failed: bool = False
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    change_control: CVChangeControl | None = None
    deployed_devices: list[CVDevice] = field(default_factory=list)
    skipped_devices: list[CVDevice] = field(default_factory=list)


@dataclass
class DeployToCvResult:
    failed: bool = False
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    workspace: CVWorkspace | None = field(default_factory=CVWorkspace)
    change_control: CVChangeControl | None = None
    deployed_configs: list[CVEosConfig] = field(default_factory=list)
    deployed_device_tags: list[CVDeviceTag] = field(default_factory=list)
    deployed_interface_tags: list[CVInterfaceTag] = field(default_factory=list)
    deployed_studio_inputs: list[CVStudioInputs] = field(default_factory=list)
    deployed_cv_pathfinder_metadata: list[CVPathfinderMetadata] = field(default_factory=list)
    skipped_configs: list[CVEosConfig] = field(default_factory=list)
    skipped_device_tags: list[CVDeviceTag] = field(default_factory=list)
    skipped_interface_tags: list[CVInterfaceTag] = field(default_factory=list)
    skipped_cv_pathfinder_metadata: list[CVPathfinderMetadata] = field(default_factory=list)
    removed_configs: list[str] = field(default_factory=list)
    removed_device_tags: list[CVDeviceTag] = field(default_factory=list)
    removed_interface_tags: list[CVInterfaceTag] = field(default_factory=list)


@dataclass
class CVDevice:
    hostname: str
    """
    Device hostname or intended hostname.
    `serial_number` or `system_mac_address` must be set if the hostname is not already configured on the device or
    if the hostname is not unique.
    """
    serial_number: str | None = None
    system_mac_address: str | None = None
    _exists_on_cv: bool | None = None
    """ Do not set this manually. """


@dataclass
class CVEosConfig:
    file: str
    """Path to file containing EOS Config"""
    device: CVDevice
    configlet_name: str | None = None
    """By default "AVD_<hostname>"""


@dataclass
class CVTimeOuts:
    """Timeouts in seconds."""

    workspace_build_timeout: float = 300.0
    change_control_creation_timeout: float = 300.0
