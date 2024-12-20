# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
from asyncio import gather, run
from dataclasses import asdict
from pathlib import Path
from string import Template
from typing import Any

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display
from yaml import load

from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleHandler, YamlLoader

PLUGIN_NAME = "arista.avd.cv_workflow"

try:
    from pyavd._cv.workflows.deploy_to_cv import deploy_to_cv
    from pyavd._cv.workflows.models import (
        CloudVision,
        CVChangeControl,
        CVDevice,
        CVDeviceTag,
        CVEosConfig,
        CVInterfaceTag,
        CVPathfinderMetadata,
        CVTimeOuts,
        CVWorkspace,
    )
    from pyavd._utils import get, strip_empties_from_dict

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


LOGGER = logging.getLogger("ansible_collections.arista.avd")
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]

ARGUMENT_SPEC = {
    "configuration_dir": {"type": "str", "required": True},
    "structured_config_dir": {"type": "str", "required": False},
    "structured_config_suffix": {"type": "str", "default": "yml"},
    "device_list": {"type": "list", "elements": "str", "required": True},
    "strict_tags": {"type": "bool", "required": False, "default": False},
    "skip_missing_devices": {"type": "bool", "required": False, "default": False},
    "configlet_name_template": {"type": "str", "default": "AVD-${hostname}"},
    "cv_servers": {"type": "list", "elements": "str", "required": True},
    "cv_token": {"type": "str", "secret": True, "required": True},
    "cv_verify_certs": {"type": "bool", "default": True},
    "workspace": {
        "type": "dict",
        "options": {
            "name": {"type": "str", "required": False},
            "description": {"type": "str", "required": False},
            "id": {"type": "str", "required": False},
            "requested_state": {"type": "str", "default": "built", "choices": ["pending", "built", "submitted", "abandoned", "deleted"]},
            "force": {"type": "bool", "default": False},
        },
    },
    "change_control": {
        "type": "dict",
        "options": {
            "name": {"type": "str", "required": False},
            "description": {"type": "str", "required": False},
            "requested_state": {"type": "str", "default": "pending approval", "choices": ["pending approval", "approved", "running", "completed"]},
        },
    },
    "timeouts": {
        "type": "dict",
        "options": {
            "workspace_build_timeout": {"type": "float", "default": CVTimeOuts.workspace_build_timeout if HAS_PYAVD else 300.0},
            "change_control_creation_timeout": {"type": "float", "default": CVTimeOuts.change_control_creation_timeout if HAS_PYAVD else 300.0},
        },
    },
    "return_details": {"type": "bool", "required": False, "default": False},
}


class ActionModule(ActionBase):
    def run(self, tmp: Any = None, task_vars: dict | None = None) -> dict:
        self._supports_check_mode = False

        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        if not HAS_PYAVD:
            msg = "The arista.avd.cv_workflow' plugin requires the 'pyavd' Python library. Got import error"
            raise AnsibleActionFail(msg)

        # Setup module logging
        setup_module_logging(result)

        # Get task arguments and validate them
        validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to json and back to remove any AnsibeUnsafe types
        validated_args = json.loads(json.dumps(validated_args))

        # Running asyncio coroutine to deploy everything.
        return run(self.deploy(validated_args, result))

    async def deploy(self, validated_args: dict, result: dict) -> dict:
        """Prepare data, perform deployment and convert result data."""
        LOGGER.info("deploy: %s", {**validated_args, "cv_token": "<removed>"})
        try:
            # Create CloudVision object
            cloudvision = CloudVision(
                servers=validated_args["cv_servers"],
                token=validated_args["cv_token"],
                verify_certs=validated_args["cv_verify_certs"],
            )
            # Build lists of CVEosConfig, CVDeviceTag, CVInterfaceTag and CVPathfinderMetadata objects.
            eos_config_objects, device_tag_objects, interface_tag_objects, cv_pathfinder_metadata_objects = await self.build_objects(
                device_list=get(validated_args, "device_list"),
                structured_config_dir=get(validated_args, "structured_config_dir"),
                structured_config_suffix=get(validated_args, "structured_config_suffix"),
                configuration_dir=get(validated_args, "configuration_dir"),
                configlet_name_template=get(validated_args, "configlet_name_template"),
            )
            # Add return data if relevant.
            if validated_args["return_details"]:
                # Objects are converted to JSON compatible dicts.
                result.update(
                    cloudvision=dict(asdict(cloudvision), token="<removed>"),  # noqa: S106
                    configs=[asdict(config) for config in eos_config_objects],
                    device_tags=[asdict(device_tag) for device_tag in device_tag_objects],
                    interface_tags=[asdict(interface_tag) for interface_tag in interface_tag_objects],
                    cv_pathfinder_metadata=[asdict(metadata) for metadata in cv_pathfinder_metadata_objects],
                )
            # Perform deployment of all objects, getting a DeployToCVResult object back.
            result_object = await deploy_to_cv(
                change_control=CVChangeControl(**get(validated_args, "change_control", default={})),
                cloudvision=cloudvision,
                configs=eos_config_objects,
                device_tags=device_tag_objects,
                interface_tags=interface_tag_objects,
                cv_pathfinder_metadata=cv_pathfinder_metadata_objects,
                skip_missing_devices=get(validated_args, "skip_missing_devices"),
                strict_tags=get(validated_args, "strict_tags"),
                timeouts=CVTimeOuts(**get(validated_args, "timeouts", default={})),
                workspace=CVWorkspace(**get(validated_args, "workspace", default={})),
            )
            # Errors and warnings are converted to JSON compatible strings.
            result_object.errors = [str(error) for error in result_object.errors]
            result_object.warnings = [str(warning) for warning in result_object.warnings]

            # Add warnings caught by the logger
            result_object.warnings.extend(result.get("warnings", []))

            # Add either all return data or only warnings, errors, failed.
            if validated_args["return_details"]:
                # Result object is converted to JSON compatible dict.
                result.update(asdict(result_object))
            else:
                result.update(
                    {
                        "warnings": result_object.warnings,
                        "errors": result_object.errors,
                        "failed": result_object.failed,
                    },
                )

            # Set changed if we did anything. TODO: Improve this logic to only set changed if something actually changed.
            if any([result_object.deployed_configs, result_object.deployed_device_tags, result_object.deployed_interface_tags]):
                result["changed"] = True

        except Exception as error:
            # Recast errors as AnsibleActionFail
            msg = f"Error during plugin execution: {error}"
            raise AnsibleActionFail(msg) from error

        return result

    async def build_objects(
        self,
        device_list: list[str],
        structured_config_dir: str | None,
        structured_config_suffix: str,
        configuration_dir: str,
        configlet_name_template: str,
    ) -> tuple[list[CVEosConfig], list[CVDeviceTag], list[CVInterfaceTag], list[CVPathfinderMetadata]]:
        """
        Build objects.

        Parameters:
            device_list: List of device hostnames.
            structured_config_dir: Path to structured config files.
            structured_config_suffix: Suffix for structured config files.
            configuration_dir: Path to EOS config files.
            configlet_name_template: Python string template used for naming configlets. Ex. "AVD-${hostname}"
        Return:
            Tuple containing (<EOS Configs to deploy>, <Device Tags to deploy>, <Interface Tags to deploy>, <CV Pathfinder Metadata to deploy>).

        Workflow:
            Per device:
              - Read and load structured config
              - If is_deployed is false, skip the device.
              - Read serial_number & system_mac from structured config.
              - Create CVDevice object and add to list of device_objects.
        """
        coroutines = [
            self.build_object_for_device(hostname, structured_config_dir, structured_config_suffix, configuration_dir, configlet_name_template)
            for hostname in device_list
        ]
        tuples = await gather(*coroutines)

        eos_config_objects = []
        device_tag_objects = []
        interface_tag_objects = []
        cv_pathfinder_metadata_objects = []
        for device_eos_config_objects, device_device_tag_objects, device_interface_tag_objects, device_cv_pathfinder_metadata_objects in tuples:
            eos_config_objects.extend(device_eos_config_objects)
            device_tag_objects.extend(device_device_tag_objects)
            interface_tag_objects.extend(device_interface_tag_objects)
            cv_pathfinder_metadata_objects.extend(device_cv_pathfinder_metadata_objects)
        return eos_config_objects, device_tag_objects, interface_tag_objects, cv_pathfinder_metadata_objects

    async def build_object_for_device(
        self,
        hostname: str,
        structured_config_dir: str | None,
        structured_config_suffix: str,
        configuration_dir: str,
        configlet_name_template: str,
    ) -> tuple[list[CVEosConfig], list[CVDeviceTag], list[CVInterfaceTag], list[CVPathfinderMetadata]]:
        """
        Build objects for one device.

        Parameters:
            device_list: List of device hostnames.
            structured_config_dir: Path to structured config files.
            structured_config_suffix: Suffix for structured config files.
            configuration_dir: Path to EOS config files.
            configlet_name_template: Python string template used for naming configlets. Ex. "AVD-${hostname}"
        Return:
            Tuple containing (<EOS Configs to deploy>, <Device Tags to deploy>, <Interface Tags to deploy>, <CV Pathfinder Metadata to deploy>).

        Workflow:
            Per device:
              - Read and load structured config
              - If is_deployed is false, skip the device.
              - Read serial_number & system_mac from structured config.
              - Create CVDevice object and add to list of device_objects.

        TODO: Refactor into smaller functions.
        """
        LOGGER.info("build_object_for_device: %s", hostname)
        if structured_config_dir and (file_path := Path(structured_config_dir, f"{hostname}.{structured_config_suffix}")).exists():
            with file_path.open(  # noqa: ASYNC230
                mode="r", encoding="UTF-8"
            ) as structured_config_stream:
                if structured_config_suffix in ["yml", "yaml"]:
                    interesting_keys = ("is_deployed", "serial_number", "metadata")
                    in_interesting_context = False
                    structured_config_lines = []
                    for line in structured_config_stream:
                        if line.startswith(interesting_keys) or (in_interesting_context and line.startswith(" ")):
                            structured_config_lines.append(line)
                            in_interesting_context = True
                        else:
                            in_interesting_context = False

                    structured_config = load("".join(structured_config_lines), Loader=YamlLoader)  # noqa: S506 TODO: Consider safeload
                else:
                    # Load as JSON
                    structured_config = json.load(structured_config_stream)
        else:
            # No structured config file.
            structured_config = {}

        if not get(structured_config, "is_deployed", default=True):
            del structured_config
            return ([], [], [], [])

        # Build device object to be used in other objects.
        serial_number = get(structured_config, "serial_number")
        system_mac_address = get(structured_config, "metadata.system_mac_address")
        device_object = CVDevice(hostname=hostname, serial_number=serial_number, system_mac_address=system_mac_address)

        # Build device config objects
        configlet_name = Template(configlet_name_template).substitute(hostname=hostname)
        config_file_path = str(Path(configuration_dir, f"{hostname}.cfg"))
        eos_config_objects = [CVEosConfig(file=config_file_path, device=device_object, configlet_name=configlet_name)]

        # Build device tag objects for this device.
        # ! metadata:
        # !   cv_tags:
        # !     device_tags:
        # !     - name: topology_hint_datacenter
        # !       value: DC1
        device_tags = get(structured_config, "metadata.cv_tags.device_tags", default=[])
        device_tag_objects = [
            CVDeviceTag(label=device_tag["name"], value=device_tag["value"], device=device_object)
            for device_tag in device_tags
            if "name" in device_tag and "value" in device_tag
        ]

        # Build interface tag objects for this device.
        # ! metadata:
        # !  cv_tags:
        # !    interface_tags:
        # !    - interface: Ethernet3
        # !      tags:
        # !      - name: peer_device_interface
        # !        value: Ethernet3
        all_interface_tags = get(structured_config, "metadata.cv_tags.interface_tags", default=[])
        interface_tag_objects = [
            CVInterfaceTag(
                label=interface_tag["name"],
                value=interface_tag["value"],
                device=device_object,
                interface=one_interface_tags["interface"],
            )
            for one_interface_tags in all_interface_tags
            if "interface" in one_interface_tags and "tags" in one_interface_tags
            for interface_tag in one_interface_tags["tags"]
            if "name" in interface_tag and "value" in interface_tag
        ]

        # Build WAN metadata object for this device.
        cv_pathfinder_metadata_objects = []
        if (cv_pathfinder_metadata := get(structured_config, "metadata.cv_pathfinder")) is not None:
            cv_pathfinder_metadata_objects.append(CVPathfinderMetadata(metadata=cv_pathfinder_metadata, device=device_object))

        del structured_config
        return eos_config_objects, device_tag_objects, interface_tag_objects, cv_pathfinder_metadata_objects


def setup_module_logging(result: dict) -> None:
    """
    Add a Handler to copy the logs from the plugin into Ansible output based on their level.

    Parameters:
        result: The dictionary used for the ansible module results
    """
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)

    # Modifying the root logger to also cover pyavd.
    root_logger = logging.getLogger()
    root_logger.addHandler(python_to_ansible_handler)
    if display.verbosity >= 3:
        root_logger.setLevel(logging.DEBUG)
    elif display.verbosity >= 1:
        root_logger.setLevel(logging.INFO)
