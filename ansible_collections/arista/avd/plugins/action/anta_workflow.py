# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
from asyncio import run
from concurrent.futures import Executor, ProcessPoolExecutor
from functools import partial
from pathlib import Path
from typing import TYPE_CHECKING, Any, NamedTuple

import yaml
from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleHandler

if TYPE_CHECKING:
    from collections.abc import Mapping

    from pyavd.api.fabric_data import FabricData

PLUGIN_NAME = "arista.avd.anta_workflow"

try:
    from pyavd._anta.lib import AntaCatalog, AntaInventory, AsyncEOSDevice, ResultManager, anta_runner, setup_logging
    from pyavd._utils import default, get
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

ANSIBLE_CONNECTION_VARS = [
    "inventory_hostname",
    "ansible_host",
    "ansible_user",
    "ansible_password",
    "ansible_httpapi_pass",
    "ansible_httpapi_password",
    "ansible_become",
    "ansible_become_password",
    "ansible_httpapi_port",
    "ansible_httpapi_use_ssl",
]

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


class AvdCatalog(NamedTuple):
    device: str
    catalog: AntaCatalog


class Batch(NamedTuple):
    devices: list[str]
    catalogs: list[AntaCatalog]


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

        # TODO: Get the max_workers from Ansible forks
        max_workers = 16

        # Get task arguments and validate them
        validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)

        # Converting to json and back to remove any AnsibeUnsafe types
        validated_args = json.loads(json.dumps(validated_args))

        # Extract only the needed vars for each device
        device_list = get(validated_args, "device_list")
        device_vars = extract_hostvars(device_list, task_vars["hostvars"])
        target_devices = list(device_vars.keys())

        # TODO: Check that either avd_catalog_dir or user_catalog_dir is provided

        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            shared_resources = load_shared_resources(validated_args)
            fabric_data = get(shared_resources, "fabric_data")
            user_catalog = get(shared_resources, "user_catalog")

            avd_catalogs = None if fabric_data is None else build_avd_catalogs(target_devices, validated_args, fabric_data, executor)

            # TODO: Need to test at high scale to determine the optimal batch size
            batches = create_batches(target_devices, avd_catalogs, user_catalog, batch_size=2)

            batch_results = run_batches(executor, batches, validated_args, device_vars)

            for manager in batch_results:
                LOGGER.info("ANTA run completed; total tests: %s", len(manager.results))

        return result


def extract_hostvars(device_list: list[str], hostvars: Mapping) -> dict:
    """Extract only the required variables for each device."""
    device_vars = {}

    for device in device_list:
        if device not in hostvars:
            msg = f"Device '{device}' not found in Ansible inventory."
            raise ValueError(msg)

        host_hostvars = hostvars[device]

        if get(host_hostvars, "is_deployed", default=True) is False:
            LOGGER.warning("Device '%s' is marked as not deployed (is_deployed: false). Skipping all tests for this device.", device)
            continue

        device_vars[device] = {key: get(host_hostvars, key) for key in ANSIBLE_CONNECTION_VARS}

    return device_vars


def create_batches(device_list: list[str], avd_catalogs: list[AvdCatalog] | None, user_catalog: AntaCatalog | None, batch_size: int) -> list[Batch]:
    """Create ANTA batches."""
    if avd_catalogs is None and user_catalog is None:
        msg = "No AVD catalogs or user-defined catalogs."
        raise RuntimeError(msg)

    if avd_catalogs:
        catalog_map = {ac.device: ac.catalog for ac in avd_catalogs}

    return [
        Batch(
            devices=device_list[i : i + batch_size],
            catalogs=[
                *(catalog_map[d] for d in device_list[i : i + batch_size] if d in catalog_map),
                user_catalog if user_catalog else [],
            ],
        )
        for i in range(0, len(device_list), batch_size)
    ]


def load_shared_resources(validated_args: dict) -> dict:
    """Load all shared resources needed for ANTA execution."""
    shared_resources = {}

    # Load the user-defined ANTA catalogs if a directory path is provided
    user_catalog_dir = get(validated_args, "anta_catalogs.user_catalog_dir")
    if user_catalog_dir is not None:
        shared_resources["user_catalog"] = load_anta_catalogs(user_catalog_dir)

    # Load the structured configs if a directory path is provided and build the fabric data
    structured_config_dir = get(validated_args, "anta_catalogs.structured_config_dir")
    if structured_config_dir is not None:
        structured_configs = load_structured_configs(
            get(validated_args, "device_list"), structured_config_dir, get(validated_args, "anta_catalogs.structured_config_suffix")
        )
        shared_resources["fabric_data"] = get_fabric_data(structured_configs, logger=LOGGER)

    return shared_resources


def build_avd_catalogs(devices: list[str], validated_args: dict, fabric_data: FabricData, executor: Executor) -> list[AvdCatalog]:
    """Build all device AVD catalogs in parallel."""
    avd_catalog_dir = get(validated_args, "anta_catalogs.avd_catalog_dir")
    catalogs = list(
        executor.map(
            partial(
                build_one_avd_catalog,
                avd_catalog_dir=avd_catalog_dir,
                fabric_data=fabric_data,
            ),
            devices,
            chunksize=8,  # TODO: Need to test with chunksize 16
        )
    )

    return [AvdCatalog(device=device, catalog=catalog) for device, catalog in zip(devices, catalogs, strict=True)]


def build_one_avd_catalog(device: str, avd_catalog_dir: str | None, fabric_data: FabricData) -> AntaCatalog:
    """Build a device catalog."""
    return get_device_anta_catalog(
        hostname=device,
        fabric_data=fabric_data,
        output_dir=avd_catalog_dir,
        logger=LOGGER,
    )


def run_batches(executor: Executor, batches: list[Batch], validated_args: dict, connection_vars: dict) -> list[ResultManager]:
    """Run all ANTA batches in parallel."""
    return list(
        executor.map(
            partial(run_one_batch, validated_args=validated_args, connection_vars=connection_vars),
            batches,
            chunksize=1,  # TODO: Need to test with chunksize 2
        )
    )


def run_one_batch(batch: Batch, validated_args: dict, connection_vars: dict) -> ResultManager:
    """Run ANTA for a single batch."""
    # Setup logging for ANTA
    log_file = get(validated_args, "anta_logging.log_file")
    if log_file:
        log_file = Path(log_file)
    log_level = get(validated_args, "anta_logging.log_level")
    setup_logging(level=log_level, file=log_file)

    tags = set(get(validated_args, "anta_runner_settings.tags", default=[])) or None

    result_manager, inventory, catalog = build_batch_objects(batch.devices, batch.catalogs, connection_vars, validated_args)

    # TODO: Implement dry-run mode
    run(anta_runner(result_manager, inventory, catalog, tags=tags))

    return result_manager


def build_batch_objects(
    devices: list[str], catalogs: list[AntaCatalog], connection_vars: dict, validated_args: dict
) -> tuple[ResultManager, AntaInventory, AntaCatalog]:
    """Build the ANTA objects required to run an ANTA batch."""
    # Initialize the ANTA objects
    result_manager = ResultManager()
    inventory = AntaInventory()
    catalog = AntaCatalog.merge_catalogs(catalogs)

    # Build the ANTA device objects and add them to the ANTA inventory
    for device in devices:
        anta_device = build_anta_device(device, connection_vars[device], validated_args)
        inventory.add_device(anta_device)

    return result_manager, inventory, catalog


def get_test_filters_for_device(device: str, catalog_filters: list[dict]) -> dict[str, Any]:
    """Get the test filters for a device from the ANTA catalogs settings.

    Parameters
    ----------
        device: The name of the device.
        catalog_filters: The ANTA catalog filters from the plugin arguments.

    Returns:
    -------
        dict: A dictionary containing the test filters for the device.
    """
    run_tests = set()
    skip_tests = set()
    input_filters = {}

    for filter_config in catalog_filters:
        device_list = get(filter_config, "device_list", default=[])
        if device not in device_list:
            continue
        run_tests.update(get(filter_config, "run_tests", default=[]))
        skip_tests.update(get(filter_config, "skip_tests", default=[]))
        device_input_filters = get(filter_config, "input_filters", default={})
        for test_name, filter_dict in device_input_filters.items():
            if test_name not in input_filters:
                input_filters[test_name] = filter_dict
            else:
                LOGGER.warning("Duplicate input filter for test '%s' found on device '%s'. Only the first provided filter will be used.", test_name, device)

    return {
        "run_tests": list(run_tests) if run_tests else None,
        "skip_tests": list(skip_tests) if skip_tests else None,
        "input_filters": input_filters if input_filters else None,
    }


def build_anta_device(device: str, device_connection_vars: dict, validated_args: dict) -> AsyncEOSDevice:
    """Build the ANTA device object for a device using the provided connection variables."""
    # Required settings to create the AsyncEOSDevice object
    required_settings = ["host", "username", "password"]

    anta_runner_settings = get(validated_args, "anta_runner_settings")

    # TODO: Confirm this is working with Ansible Vault
    device_settings = {
        "name": device,
        "host": get(device_connection_vars, "ansible_host", default=get(device_connection_vars, "inventory_hostname")),
        "username": get(device_connection_vars, "ansible_user"),
        "password": default(
            get(device_connection_vars, "ansible_password"),
            get(device_connection_vars, "ansible_httpapi_pass"),
            get(device_connection_vars, "ansible_httpapi_password"),
        ),
        "enable": get(device_connection_vars, "ansible_become", default=False),
        "enable_password": get(device_connection_vars, "ansible_become_password"),
        "port": get(
            device_connection_vars,
            "ansible_httpapi_port",
            default=(80 if get(device_connection_vars, "ansible_httpapi_use_ssl", default=False) is False else 443),
        ),
        "timeout": get(anta_runner_settings, "timeout"),
        "disable_cache": get(anta_runner_settings, "disable_cache"),
        # TODO: Need to add anta_tags to the metadata schema
        "tags": set(get(device_connection_vars, "metadata.anta_tags", default=[])),
    }

    # Make sure we found all required connection settings. Other settings have defaults in the ANTA device object
    if any(value is None for key, value in device_settings.items() if key in required_settings):
        msg = (
            f"Device '{device}' is missing required connection settings. "
            f"Please make sure all required connection variables are defined in the Ansible inventory, "
            f"following the Ansible HTTPAPI connection plugin settings: {ANSIBLE_HTTPAPI_CONNECTION_DOC}"
        )
        raise ValueError(msg)

    return AsyncEOSDevice(**device_settings)


def load_anta_catalogs(catalog_dir: str) -> AntaCatalog:
    """Load ANTA catalogs from the provided directory. Supported file formats are YAML and JSON."""
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

        LOGGER.debug("Loading ANTA catalog from %s", path_obj)
        catalog = AntaCatalog.parse(path_obj, file_format)
        catalogs.append(catalog)

    if not catalogs:
        msg = f"No valid ANTA catalogs found in directory: {catalog_dir}"
        raise ValueError(msg)

    return AntaCatalog.merge_catalogs(catalogs)


def load_structured_configs(device_list: list[str], structured_config_dir: str, structured_config_suffix: str) -> dict:
    """Load the structured configurations for the devices in the provided list from the given directory."""
    return {device: load_one_structured_config(device, structured_config_dir, structured_config_suffix) for device in device_list}


def load_one_structured_config(device: str, structured_config_dir: str, structured_config_suffix: str) -> dict[str, Any]:
    """Load the structured configuration for a device from the provided directory."""
    path = Path(structured_config_dir) / f"{device}.{structured_config_suffix}"
    if not path.exists():
        msg = f"Structured configuration file for device '{device}' not found: {path}"
        raise FileNotFoundError(msg)

    with path.open(encoding="UTF-8") as stream:
        if structured_config_suffix in {"yml", "yaml"}:
            return yaml.load(stream, Loader=yaml.CSafeLoader)
        return json.load(stream)


def setup_module_logging(result: dict) -> None:
    """Add a Handler to copy the logs from the plugin into Ansible output based on their level."""
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)
    LOGGER.addHandler(python_to_ansible_handler)

    # Set the logging level based on the Ansible verbosity level
    if display.verbosity >= 3:
        LOGGER.setLevel(logging.DEBUG)
    elif display.verbosity >= 1:
        LOGGER.setLevel(logging.INFO)
