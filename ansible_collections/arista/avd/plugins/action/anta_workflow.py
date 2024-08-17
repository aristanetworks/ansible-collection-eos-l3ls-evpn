# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
from asyncio import run
from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING, Any

import yaml
from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleHandler

if TYPE_CHECKING:
    from collections.abc import Mapping

PLUGIN_NAME = "arista.avd.anta_workflow"

try:
    from pyavd._anta.lib import AntaCatalog, AntaInventory, AsyncEOSDevice, ResultManager, anta_runner, setup_logging
    from pyavd._utils import default, get, strip_empties_from_dict
    from pyavd.get_device_anta_catalog import get_device_anta_catalog
    from pyavd.get_fabric_data import get_fabric_data

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False

LOGGER = logging.getLogger("ansible_collections.arista.avd")
# ANTA uses RichHandler at the root logger. Disabling propagation to avoid duplicate logs
LOGGER.propagate = False
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]

ANSIBLE_HTTPAPI_CONNECTION_DOC = "https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/httpapi_connection.html"

ARGUMENT_SPEC = {
    "structured_config_dir": {"type": "str", "required": True},
    "structured_config_suffix": {"type": "str", "default": "yml", "choices": ["yml", "yaml", "json"]},
    "device_list": {"type": "list", "elements": "str", "required": True},
    "custom_anta_catalogs": {
        "type": "dict",
        "options": {
            "directory": {"type": "str", "required": True},
            "overwrite_default": {"type": "bool", "default": False},
        },
    },
    "skip_tests": {
        "type": "dict",
        "options": {
            "all_devices": {
                "type": "list",
                "elements": "str",
            },
            "per_device": {
                "type": "list",
                "elements": "dict",
                "options": {
                    "device": {"type": "str", "required": True},
                    "tests": {"type": "list", "elements": "str", "required": True},
                },
            },
        },
    },
    "anta_logging": {
        "type": "dict",
        "options": {
            "log_level": {"type": "str", "default": "WARNING", "choices": LOGGING_LEVELS},
            "log_file": {"type": "str"},
        },
    },
    "anta_global_settings": {
        "type": "dict",
        "options": {
            "timeout": {"type": "float", "default": 30.0},
            "disable_cache": {"type": "bool", "default": False},
        },
    },
}


class ActionModule(ActionBase):
    def run(self, tmp: Any = None, task_vars: dict | None = None) -> dict:
        self._supports_check_mode = False

        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        if not HAS_PYAVD:
            msg = f"The {PLUGIN_NAME} plugin requires the 'pyavd' Python library. Got import error"
            raise AnsibleActionFail(msg)

        # Setup module logging
        setup_module_logging(result)

        # Setup variables
        hostvars = task_vars["hostvars"]

        # Get task arguments and validate them
        validated_args = strip_empties_from_dict(self._task.args)
        validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to json and back to remove any AnsibeUnsafe types
        validated_args = json.loads(json.dumps(validated_args))

        # Launch the run_anta coroutine to run everything
        return run(self.run_anta(validated_args, hostvars, result))

    async def run_anta(self, validated_args: dict, hostvars: Mapping, result: dict) -> dict:
        """Main coroutine to run the ANTA workflow.

        Parameters
        ----------
            validated_args: The validated plugin arguments.
            hostvars: The Ansible hostvars object containing all variables of each device.
            result: The dictionary used for the Ansible module results.

        Returns:
        -------
            dict: The updated Ansible module result dictionary.
        """
        # Setup logging for ANTA
        log_file = get(validated_args, "anta_logging.log_file")
        if log_file:
            log_file = Path(log_file)
        log_level = get(validated_args, "anta_logging.log_level")
        setup_logging(level=log_level, file=log_file)

        # Build the connection settings for each device using Ansible hostvars
        device_list = get(validated_args, "device_list")
        global_settings = get(validated_args, "anta_global_settings")
        connection_settings = self.build_connection_settings(device_list, hostvars, global_settings)

        # Build the required ANTA objects
        result_manager, inventory, catalog = self.build_objects(
            device_list=device_list,
            connection_settings=connection_settings,
            structured_config_dir=get(validated_args, "structured_config_dir"),
            structured_config_suffix=get(validated_args, "structured_config_suffix"),
            custom_anta_catalogs=get(validated_args, "custom_anta_catalogs"),
            skip_tests=get(validated_args, "skip_tests"),
        )

        await anta_runner(result_manager, inventory, catalog)

        # TODO: Do something useful with the results (reporting, etc.)
        LOGGER.info("ANTA run completed; total tests: %s", len(result_manager.results))
        LOGGER.info("ANTA run results: %s", result_manager.json)

        return result

    def build_objects(
        self,
        device_list: list[str],
        connection_settings: dict,
        structured_config_dir: str,
        structured_config_suffix: str,
        custom_anta_catalogs: dict | None,
        skip_tests: dict | None,
    ) -> tuple[ResultManager, AntaInventory, AntaCatalog]:
        """Build the objects required to run the ANTA.

        Parameters
        ----------
            device_list: The list of device names.
            connection_settings: The connection settings for each device to create the `AsyncEOSDevice` objects.
            structured_config_dir: The directory where the structured configurations are stored.
            structured_config_suffix: The suffix of the structured configuration files (yml, yaml, json).
            custom_anta_catalogs: Optional custom ANTA catalogs input dictionary containing the directory and overwrite flag.
            skip_tests: Optional skip_tests input dictionary containing tests to skip for all devices and per device.

        Returns:
        -------
            tuple: A tuple containing the ResultManager, AntaInventory, and AntaCatalog ANTA objects.

        # NOTE: Tests from custom catalogs tagged by the device name will be honored, i.e. they will run only on the device with the same name
        # TODO: Other tags will be ignored since we don't have a way (yet) to add these tags to the devices in the Ansible inventory
        """
        # Initialize the ANTA objects
        final_inventory = AntaInventory()
        final_catalog = AntaCatalog()
        result_manager = ResultManager()

        # Determine if we're overwriting the default catalog
        overwrite_default_catalog = custom_anta_catalogs and custom_anta_catalogs["overwrite_default"]

        # Load custom ANTA catalogs if provided
        if custom_anta_catalogs:
            final_catalog = final_catalog.merge(self.load_custom_anta_catalogs(custom_anta_catalogs["directory"]))

        # Only process default catalog data if not overwriting the default catalog
        if not overwrite_default_catalog:
            parsed_skip_tests = self.parse_skip_tests(device_list, skip_tests) if skip_tests else {}
            structured_configs = self.load_structured_configs(device_list, structured_config_dir, structured_config_suffix)
        else:
            LOGGER.info("Overwriting the default catalog with custom catalogs")
            parsed_skip_tests = {}
            structured_configs = {}

        # Create the fabric data from the structured configs. Will be empty and not used if overwriting the default catalog
        fabric_data = get_fabric_data(structured_configs, logger=LOGGER)

        # Update the ANTA inventory and catalog for each device
        for device, settings in connection_settings.items():
            anta_device = AsyncEOSDevice(name=device, **settings)
            final_inventory.add_device(anta_device)

            # Skip adding the device catalog if the default catalog should be overwritten
            if not overwrite_default_catalog:
                device_skip_tests = get(parsed_skip_tests, device)
                device_catalog = get_device_anta_catalog(device, fabric_data, skip_tests=device_skip_tests, logger=LOGGER)
                final_catalog = final_catalog.merge(device_catalog)

        return result_manager, final_inventory, final_catalog

    def build_connection_settings(self, device_list: list[str], hostvars: Mapping, global_settings: dict) -> dict:
        """Build the connection settings for each device using the Ansible hostvars.

        Parameters
        ----------
            device_list: The list of device names.
            hostvars: The Ansible hostvars object containing all variables of each device.
            global_settings: The global settings dictionary from the plugin arguments.

        Returns:
        -------
            dict: A dictionary with device names as keys and connection settings as values to create the `AsyncEOSDevice` objects.
        """
        connection_settings = {}

        # Required settings to create the ANTA device object
        required_settings = ["host", "username", "password"]

        for device in device_list:
            if device not in hostvars:
                LOGGER.warning("Device %s not found in Ansible inventory. Skipping device", device)
                continue

            device_vars = hostvars[device]
            device_connection_settings = {
                "host": get(device_vars, "ansible_host", default=get(device_vars, "inventory_hostname")),
                "username": get(device_vars, "ansible_user"),
                "password": default(
                    get(device_vars, "ansible_password"), get(device_vars, "ansible_httpapi_pass"), get(device_vars, "ansible_httpapi_password")
                ),
                "enable": get(device_vars, "ansible_become", default=False),
                "enable_password": get(device_vars, "ansible_become_password"),
                "port": get(device_vars, "ansible_httpapi_port", default=(80 if get(device_vars, "ansible_httpapi_use_ssl", default=False) is False else 443)),
                "timeout": get(global_settings, "timeout"),
                "disable_cache": get(global_settings, "disable_cache"),
            }

            # Make sure we found all required connection settings. Other settings have defaults in the ANTA device object
            if any(value is None for key, value in device_connection_settings.items() if key in required_settings):
                msg = (
                    f"Device {device} is missing required connection settings. Skipping device. "
                    f"Please make sure all required connection variables are defined in the Ansible inventory, "
                    f"following the Ansible HTTPAPI connection plugin settings: {ANSIBLE_HTTPAPI_CONNECTION_DOC}"
                )
                LOGGER.warning(msg)
                continue

            connection_settings[device] = device_connection_settings

        return connection_settings

    def parse_skip_tests(self, device_list: list[str], skip_tests: dict) -> dict:
        """Parse the skip_tests input dictionary.

        Parameters
        ----------
            device_list: The list of device names.
            skip_tests: The skip_tests input dictionary from the plugin arguments.

        Returns:
        -------
            dict: A dictionary with device names as keys and the tests to skip as values.
        """
        parsed_skip_tests = defaultdict(set)

        # Handle tests to skip for all devices
        skip_for_all = set(get(skip_tests, "all_devices", default=[]))
        for device in device_list:
            parsed_skip_tests[device].update(skip_for_all)

        # Handle device-specific tests to skip
        for item in get(skip_tests, "per_device", default=[]):
            device = item["device"]
            if device in device_list:
                parsed_skip_tests[device].update(item["tests"])

        return dict(parsed_skip_tests)

    def load_custom_anta_catalogs(self, custom_anta_catalogs_dir: str) -> AntaCatalog:
        """Load custom ANTA catalogs from the provided directory.

        Supports YAML files only.

        Parameters
        ----------
            custom_anta_catalogs_dir: The directory where the custom ANTA catalogs are stored.

        Returns:
        -------
            AntaCatalog: Instance of the merged custom ANTA catalogs.
        """
        custom_catalog = AntaCatalog()
        for path_obj in Path(custom_anta_catalogs_dir).iterdir():
            if path_obj.is_file() and path_obj.suffix.lower() in {".yml", ".yaml"}:
                # Error handling is done in ANTA
                LOGGER.info("Loading custom ANTA catalog from %s", path_obj)
                catalog = AntaCatalog.parse(path_obj)
                custom_catalog = custom_catalog.merge(catalog)

        return custom_catalog

    def load_structured_configs(self, device_list: list[str], structured_config_dir: str, structured_config_suffix: str) -> dict:
        """Load the structured configurations for the devices in the provided list from the given directory.

        Parameters
        ----------
            device_list: The list of device names.
            structured_config_dir: The directory where the structured configurations are stored.
            structured_config_suffix: The suffix of the structured configuration files (yml, yaml, json).

        Returns:
        -------
            dict: A dictionary with the device names as keys and the structured configurations as values.
        """
        structured_configs = {}
        for device in device_list:
            try:
                structured_config = self.load_device_structured_config(device, structured_config_dir, structured_config_suffix)
            except FileNotFoundError:
                LOGGER.warning("Structured configuration file for device %s not found. Skipping device", device)
                continue
            except (OSError, yaml.YAMLError, json.JSONDecodeError) as exc:
                LOGGER.warning("Error loading structured configuration for device %s: %s. Skipping device", device, str(exc))
                continue

            # Skip devices that are not deployed
            if structured_config.get("is_deployed", True) is False:
                LOGGER.info("Device %s `is_deployed` key is set to False. Skipping device", device)
                continue

            structured_configs[device] = structured_config

        return structured_configs

    def load_device_structured_config(self, device: str, structured_config_dir: str, structured_config_suffix: str) -> dict:
        """Load the structured configuration for a device from the provided directory.

        Parameters
        ----------
            device: The name of the device.
            structured_config_dir: The directory where the structured configurations are stored.
            structured_config_suffix: The suffix of the structured configuration files (yml, yaml, json).

        Returns:
        -------
            dict: The structured configuration for the device.
        """
        config_path = Path(structured_config_dir, f"{device}.{structured_config_suffix}")
        with config_path.open(mode="r", encoding="UTF-8") as stream:
            if structured_config_suffix in {"yml", "yaml"}:
                return yaml.load(stream, Loader=yaml.CSafeLoader)
            return json.load(stream)


def setup_module_logging(result: dict) -> None:
    """Add a Handler to copy the logs from the plugin into Ansible output based on their level.

    Parameters
    ----------
        result: The dictionary used for the Ansible module results.
    """
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)
    LOGGER.addHandler(python_to_ansible_handler)

    # Set the logging level based on the Ansible verbosity level
    if display.verbosity >= 3:
        LOGGER.setLevel(logging.DEBUG)
    elif display.verbosity >= 1:
        LOGGER.setLevel(logging.INFO)
