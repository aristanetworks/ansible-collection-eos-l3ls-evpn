# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
from asyncio import run
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
    "device_list": {"type": "list", "elements": "str", "required": True},
    "anta_catalogs": {
        "type": "dict",
        "required": True,
        "options": {
            "avd_catalog_dir": {"type": "str"},
            "avd_catalog_filters": {
                "type": "list",
                "elements": "dict",
                "options": {
                    "device_list": {"type": "list", "elements": "str"},
                    "run_tests": {"type": "list", "elements": "str"},
                    "skip_tests": {"type": "list", "elements": "str"},
                },
            },
            "structured_config_dir": {"type": "str"},
            "structured_config_suffix": {"type": "str", "default": "yml", "choices": ["yml", "yaml", "json"]},
            "user_catalog_dir": {"type": "str"},
        },
    },
    "anta_logging": {
        "type": "dict",
        "options": {
            "log_level": {"type": "str", "default": "WARNING", "choices": LOGGING_LEVELS},
            "log_file": {"type": "str"},
        },
    },
    "anta_runner_settings": {
        "type": "dict",
        "options": {
            "timeout": {"type": "float", "default": 30.0},
            "disable_cache": {"type": "bool", "default": False},
            "tags": {"type": "list", "elements": "str"},
        },
    },
    "report": {
        "type": "dict",
        "options": {
            "test_results_dir": {"type": "str"},
            "csv_output": {"type": "str"},
            "md_output": {"type": "str"},
            "filters": {
                "type": "dict",
                "options": {
                    "hide_statuses": {
                        "type": "list",
                        "elements": "str",
                        "choices": ["success", "failure", "error", "skipped"],
                    },
                },
            },
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
            msg = f"The {PLUGIN_NAME} plugin requires the 'pyavd' Python library. Got import error."
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

        # Build the required ANTA objects
        result_manager, inventory, catalog = self.build_objects(
            hostvars=hostvars,
            device_list=get(validated_args, "device_list"),
            anta_catalogs=get(validated_args, "anta_catalogs"),
            anta_runner_settings=get(validated_args, "anta_runner_settings"),
        )

        tags = set(get(validated_args, "anta_runner_settings.tags", default=[])) or None

        await anta_runner(result_manager, inventory, catalog, tags=tags)

        # TODO: Do something useful with the results (reporting, etc.)
        LOGGER.info("ANTA run completed; total tests: %s", len(result_manager.results))
        LOGGER.info("ANTA run results: %s", result_manager.json)

        return result

    def build_objects(
        self,
        hostvars: Mapping,
        device_list: list[str],
        anta_catalogs: dict,
        anta_runner_settings: dict,
    ) -> tuple[ResultManager, AntaInventory, AntaCatalog]:
        """Build the objects required to run the ANTA.

        Parameters
        ----------
            hostvars: The Ansible hostvars object containing all variables of each device.
            device_list: The list of device names to run the ANTA tests on.
            anta_catalogs: The ANTA catalogs settings for the run.
            anta_runner_settings: The ANTA runner settings.

        Returns:
        -------
            tuple: A tuple containing the ResultManager, AntaInventory, and AntaCatalog ANTA objects.

        # NOTE: Tests from user-defined catalogs tagged by the device name will be honored, i.e. they will run only on the device with the same name
        # NOTE: Other tags will also be honored and will be used in conjunction with the `metadata.anta_tags` variable of each device
        # NOTE: `skip_tests` and `run_tests` are used to filter tests from the AVD catalog only
        """
        # Initialize the ANTA objects
        final_inventory = AntaInventory()
        final_catalog = AntaCatalog()
        result_manager = ResultManager()

        # Load the user-defined ANTA catalogs if a directory path is provided
        user_catalog_dir = get(anta_catalogs, "avd_catalog_dir")
        if user_catalog_dir is not None:
            user_catalog = self.load_anta_catalogs(user_catalog_dir)
            final_catalog = AntaCatalog.merge_catalogs([final_catalog, user_catalog])

        # Load the structured configs if a directory path is provided and build the fabric data
        structured_config_dir = get(anta_catalogs, "structured_config_dir")
        if structured_config_dir is not None:
            structured_configs = self.load_structured_configs(device_list, structured_config_dir, anta_catalogs["structured_config_suffix"])
            fabric_data = get_fabric_data(structured_configs, logger=LOGGER)

        for device in device_list:
            # Build the ANTA device object and add it to the ANTA inventory
            anta_device = self.build_anta_device(device, hostvars, anta_runner_settings)
            if anta_device:
                final_inventory.add_device(anta_device)

            # Load the AVD catalog for that device if structured configs are provided
            if structured_config_dir is not None:
                run_tests, skip_tests = self.get_test_filters_for_device(device, anta_catalogs)
                device_catalog = get_device_anta_catalog(device, fabric_data, run_tests=run_tests, skip_tests=skip_tests, logger=LOGGER)

                # Dump the device catalog to the provided directory if provided
                catalog_dir = get(anta_catalogs, "user_catalog_dir")
                if catalog_dir is not None:
                    self.dump_anta_catalog(device, device_catalog, catalog_dir)

                final_catalog = AntaCatalog.merge_catalogs([final_catalog, device_catalog])

        return result_manager, final_inventory, final_catalog

    def get_test_filters_for_device(self, device: str, anta_catalogs: dict) -> tuple[set[str], set[str]]:
        """Get the test filters for a device from the ANTA catalogs settings.

        Parameters
        ----------
            device: The name of the device.
            anta_catalogs: The ANTA catalogs settings for the run.

        Returns:
        -------
            tuple: A tuple containing the `run_tests` and `skip_tests` filters for the device.
        """
        run_tests = set()
        skip_tests = set()

        catalog_filters = get(anta_catalogs, "avd_catalog_filters", default=[])

        for filter_config in catalog_filters:
            device_list = get(filter_config, "device_list", default=[])
            if device in device_list:
                run_tests.update(get(filter_config, "run_tests", default=[]))
                skip_tests.update(get(filter_config, "skip_tests", default=[]))

        return run_tests or None, skip_tests or None

    def build_anta_device(self, device: str, hostvars: Mapping, anta_runner_settings: dict) -> AsyncEOSDevice | None:
        """Build the ANTA device object for a device using the provided Ansible hostvars.

        Parameters
        ----------
            device: The name of the device.
            hostvars: The Ansible hostvars object containing all variables of each device.
            anta_runner_settings: The ANTA runner settings.

        Returns:
        -------
            The ANTA device object for the device or None if the device is not found in the hostvars or missing required connection settings.
        """
        # Required settings to create the AsyncEOSDevice object
        required_settings = ["host", "username", "password"]

        if device not in hostvars:
            LOGGER.warning("Device '%s' not found in Ansible inventory. Skipping device.", device)
            return None

        device_vars = hostvars[device]
        device_settings = {
            "name": device,
            "host": get(device_vars, "ansible_host", default=get(device_vars, "inventory_hostname")),
            "username": get(device_vars, "ansible_user"),
            "password": default(get(device_vars, "ansible_password"), get(device_vars, "ansible_httpapi_pass"), get(device_vars, "ansible_httpapi_password")),
            "enable": get(device_vars, "ansible_become", default=False),
            "enable_password": get(device_vars, "ansible_become_password"),
            "port": get(device_vars, "ansible_httpapi_port", default=(80 if get(device_vars, "ansible_httpapi_use_ssl", default=False) is False else 443)),
            "timeout": get(anta_runner_settings, "timeout"),
            "disable_cache": get(anta_runner_settings, "disable_cache"),
            "tags": set(get(device_vars, "anta_tags", default=[])),
        }

        # Make sure we found all required connection settings. Other settings have defaults in the ANTA device object
        if any(value is None for key, value in device_settings.items() if key in required_settings):
            msg = (
                f"Device '{device}' is missing required connection settings. Skipping device. "
                f"Please make sure all required connection variables are defined in the Ansible inventory, "
                f"following the Ansible HTTPAPI connection plugin settings: {ANSIBLE_HTTPAPI_CONNECTION_DOC}"
            )
            LOGGER.warning(msg)
            return None

        return AsyncEOSDevice(**device_settings)

    def dump_anta_catalog(self, device: str, catalog: AntaCatalog, catalog_dir: str) -> None:
        """Dump the ANTA catalog for a device to the provided directory.

        Parameters
        ----------
            device: The name of the device.
            catalog: The ANTA catalog of the device.
            catalog_dir: The directory where the ANTA catalogs should be saved.
        """
        catalog_path = Path(catalog_dir) / f"{device}.yml"
        catalog_dump = catalog.dump()

        with catalog_path.open(mode="w", encoding="UTF-8") as stream:
            stream.write(catalog_dump.yaml())

    def load_anta_catalogs(self, catalog_dir: str) -> AntaCatalog:
        """Load ANTA catalogs from the provided directory.

        Supported file formats are YAML and JSON.

        Parameters
        ----------
            catalog_dir: The directory where the ANTA catalogs are stored.

        Returns:
        -------
            AntaCatalog: Instance of the merged ANTA catalogs.
        """
        supported_formats = {".yml": "yaml", ".yaml": "yaml", ".json": "json"}
        catalogs = []

        for path_obj in Path(catalog_dir).iterdir():
            # Skip directories and non-files
            if not path_obj.is_file():
                continue

            file_format = supported_formats.get(path_obj.suffix.lower())
            if not file_format:
                LOGGER.warning("Unsupported file format for ANTA catalog: %s. Skipping file.", path_obj)
                continue

            LOGGER.info("Loading ANTA catalog from %s", path_obj)
            catalog = AntaCatalog.parse(path_obj, file_format)
            catalogs.append(catalog)

        if not catalogs:
            LOGGER.warning("No valid ANTA catalog files found in directory: %s", catalog_dir)
            return AntaCatalog()

        return AntaCatalog.merge_catalogs(catalogs)

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
                LOGGER.warning("Structured configuration file for device '%s' not found. Skipping device.", device)
                continue
            except (OSError, yaml.YAMLError, json.JSONDecodeError) as exc:
                LOGGER.warning("Error loading structured configuration for device '%s': %s. Skipping device", device, exc)
                continue

            structured_configs[device] = structured_config

        return structured_configs

    def load_device_structured_config(self, device: str, structured_config_dir: str, structured_config_suffix: str) -> dict[str, Any]:
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
        config_path = Path(structured_config_dir) / f"{device}.{structured_config_suffix}"

        with config_path.open(mode="r", encoding="UTF-8") as stream:
            if structured_config_suffix in ("yml", "yaml"):
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
