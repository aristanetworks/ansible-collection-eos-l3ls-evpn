# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
from asyncio import run
from concurrent.futures import Executor, ProcessPoolExecutor
from logging.handlers import QueueHandler, QueueListener
from multiprocessing import Manager, Queue, get_start_method
from pathlib import Path
from typing import TYPE_CHECKING, Any

import yaml
from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleHandler
from pyavd._utils import strip_empties_from_dict

if TYPE_CHECKING:
    from collections.abc import Mapping

    from pyavd.api.fabric_data import FabricData

PLUGIN_NAME = "arista.avd.anta_workflow"

try:
    from pyavd._anta.lib import AntaCatalog, AntaInventory, AsyncEOSDevice, MDReportGenerator, ReportCsv, ResultManager, anta_runner
    from pyavd._utils import default, get
    from pyavd.get_device_anta_catalog import get_device_anta_catalog
    from pyavd.get_fabric_data import get_fabric_data

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False

LOGGER = logging.getLogger("ansible_collections.arista.avd")
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
    "anta_catalog": {
        "type": "dict",
        "options": {
            "output_dir": {"type": "str"},
            "structured_config_dir": {"type": "str"},
            "structured_config_suffix": {"type": "str", "default": "yml", "choices": ["yml", "yaml", "json"]},
            "scope": {
                "type": "dict",
                "options": {
                    "boundary": {"type": "str", "choices": ["unlimited", "fabric", "dc", "pod", "rack"], "default": "unlimited"},
                    "allow_bgp_external": {"type": "bool"},
                    "allow_bgp_vrfs": {"type": "bool"},
                },
            },
            "filters": {
                "type": "list",
                "elements": "dict",
                "options": {
                    "device_list": {"type": "list", "elements": "str"},
                    "run_tests": {"type": "list", "elements": "str"},
                    "skip_tests": {"type": "list", "elements": "str"},
                },
            },
        },
    },
    "custom_catalog": {
        "type": "dict",
        "options": {
            "input_dir": {"type": "str"},
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
            "tags": {"type": "list", "elements": "str"},
        },
    },
    "report": {
        "type": "dict",
        "options": {
            "csv_output": {"type": "str"},
            "md_output": {"type": "str"},
            "json_output": {"type": "str"},
            "filters": {
                "type": "dict",
                "options": {
                    "hide_statuses": {
                        "type": "list",
                        "elements": "str",
                        "choices": ["success", "failure", "error", "skipped", "unset"],
                    },
                },
            },
        },
    },
}

# Global variables to share data between processes. Since the plugin is forked, these variables are inherited by child processes.
FABRIC_DATA: FabricData | None = None
STRUCTURED_CONFIGS: dict[str, dict[str, Any]] | None = None
PLUGIN_ARGS: dict[str, Any] | None = None
ANSIBLE_VARS: dict[str, dict[str, Any]] | None = None
USER_CATALOG: AntaCatalog | None = None
DRY_RUN: bool = False


class ActionModule(ActionBase):
    def run(self, tmp: Any = None, task_vars: dict | None = None) -> dict:
        global FABRIC_DATA, STRUCTURED_CONFIGS, PLUGIN_ARGS, ANSIBLE_VARS, USER_CATALOG, DRY_RUN  # noqa: PLW0603

        self._supports_check_mode = True

        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        if not HAS_PYAVD:
            msg = f"The {PLUGIN_NAME} plugin requires the 'pyavd' Python library. Got import error"
            raise AnsibleActionFail(msg)

        # NOTE: Ansible uses 'fork' even on MacOS which has 'spawn' as the default. OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES will be required for Mac users.
        if get_start_method() != "fork":
            msg = f"The {PLUGIN_NAME} plugin requires the 'fork' start method for multiprocessing"
            raise AnsibleActionFail(msg)

        # Setup the module logging using a multiprocessing manager queue
        manager = Manager()
        queue = manager.Queue(-1)
        setup_module_logging(queue)
        listener = setup_queue_listener(result, queue)

        # TODO: Get the max_workers from Ansible forks (n - 1)
        max_workers = 16

        # Get task arguments and validate them
        validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to json and back to remove any AnsibeUnsafe types
        PLUGIN_ARGS = json.loads(json.dumps(validated_args))

        device_list = get(PLUGIN_ARGS, "device_list")
        if not device_list:
            msg = "'device_list' cannot be empty"
            raise AnsibleActionFail(msg)

        # Extract only the needed hostvars from each device
        ANSIBLE_VARS = extract_hostvars(device_list, task_vars["hostvars"])
        deployed_devices = list(ANSIBLE_VARS.keys())

        structured_config_dir = get(PLUGIN_ARGS, "anta_catalog.structured_config_dir")
        custom_catalog_dir = get(PLUGIN_ARGS, "custom_catalog.input_dir")

        if structured_config_dir is None and custom_catalog_dir is None:
            msg = (
                "'structured_config_dir' must be provided to generate ANTA catalogs. "
                "Otherwise, provide a directory with user-defined custom ANTA catalogs using the 'custom_catalog.input_dir' argument"
            )
            raise AnsibleActionFail(msg)

        DRY_RUN = task_vars.get("ansible_check_mode", False)

        try:
            # Load the user-defined custom ANTA catalogs if provided
            if custom_catalog_dir is not None:
                USER_CATALOG = load_user_catalogs(custom_catalog_dir)

            # Load the structured configs and build FabricData
            if structured_config_dir is not None:
                STRUCTURED_CONFIGS = load_structured_configs(deployed_devices, structured_config_dir, get(PLUGIN_ARGS, "anta_catalog.structured_config_suffix"))
                FABRIC_DATA = get_fabric_data(structured_configs=STRUCTURED_CONFIGS, scope=get(PLUGIN_ARGS, "anta_catalog.scope"))

            # NOTE: 7 devices per batch is the sweet spot on 16 workers and 1040 devices
            # TODO: Make the batch size configurable
            with ProcessPoolExecutor(max_workers=max_workers) as executor:
                batch_results = run_anta_batches(deployed_devices, executor, batch_size=7)

            # Build the ANTA reports
            build_reports(batch_results, get(PLUGIN_ARGS, "report"))

        except Exception as error:
            # Recast errors as AnsibleActionFail
            msg = f"Error during plugin execution: {error}"
            raise AnsibleActionFail(msg) from error
        finally:
            listener.stop()
            manager.shutdown()

        return result


def run_anta_batches(device_list: list[str], executor: Executor, batch_size: int) -> list[ResultManager]:
    """Run ANTA in parallel batches using the provided executor."""
    # Create batches of devices
    batches = [device_list[i : i + batch_size] for i in range(0, len(device_list), batch_size)]

    # Map run_anta over the batches
    return list(executor.map(run_anta, batches))


def run_anta(devices: list[str]) -> ResultManager:
    """Run ANTA."""
    if PLUGIN_ARGS is None:
        msg = "Plugin arguments not initialized"
        raise RuntimeError(msg)

    result_manager, inventory, catalog = build_anta_runner_objects(devices)
    tags = set(get(PLUGIN_ARGS, "anta_runner_settings.tags", default=[])) or None

    run(anta_runner(result_manager, inventory, catalog, tags=tags, dry_run=DRY_RUN))

    return result_manager


def build_reports(batch_results: list[ResultManager], report_settings: dict) -> None:
    """Build the ANTA reports from the results iterator."""
    hide_statuses = get(report_settings, "filters.hide_statuses")
    csv_output_path = get(report_settings, "csv_output")
    md_output_path = get(report_settings, "md_output")
    json_output_path = get(report_settings, "json_output")

    # Merge all results
    result_manager = ResultManager()
    for manager in batch_results:
        for result in manager.results:
            result_manager.add(result)

    # Filter the results based on the hide_statuses if provided
    if hide_statuses:
        result_manager = result_manager.filter(hide=set(hide_statuses))

    # Sort the internal results list
    sorted_results = result_manager.get_results(sort_by=["name", "categories", "test", "result", "custom_field"])
    result_manager.results = sorted_results

    if csv_output_path:
        path = Path(csv_output_path)
        report_csv = ReportCsv()
        report_csv.generate(result_manager, path)

    if md_output_path:
        path = Path(md_output_path)
        md_report = MDReportGenerator()
        md_report.generate(result_manager, path)

    if json_output_path:
        path = Path(json_output_path)
        with path.open("w", encoding="UTF-8") as file:
            file.write(result_manager.json)


def extract_hostvars(device_list: list[str], hostvars: Mapping) -> dict:
    """Extract only the required hostvars for each device."""
    device_vars = {}

    for device in device_list:
        if device not in hostvars:
            msg = f"Device '{device}' not found in Ansible inventory"
            raise ValueError(msg)

        host_hostvars = hostvars[device]

        # Since we can run ANTA without any structured configs, i.e., only using user custom catalogs,
        # we honor the `is_deployed` flag in the hostvars to skip devices that are not deployed.
        if get(host_hostvars, "is_deployed", default=True) is False:
            LOGGER.warning("<%s> [anta_workflow]: skipped - device not deployed", device)
            continue

        device_vars[device] = {key: get(host_hostvars, key) for key in ANSIBLE_CONNECTION_VARS}

        # Same as above, we also honor the `anta_tags` variable if provided in the hostvars
        device_vars[device]["anta_tags"] = get(host_hostvars, "anta_tags")

    return device_vars


def build_anta_runner_objects(devices: list[str]) -> tuple[ResultManager, AntaInventory, AntaCatalog]:
    """Build the ANTA objects required to run an ANTA batch."""
    if PLUGIN_ARGS is None:
        msg = "Plugin arguments not initialized"
        raise RuntimeError(msg)

    # Create the ANTA objects
    result_manager = ResultManager()
    inventory = AntaInventory()
    catalogs = []

    if USER_CATALOG is not None:
        catalogs.append(USER_CATALOG)

    for device in devices:
        anta_device = build_anta_device(device)
        inventory.add_device(anta_device)
        if FABRIC_DATA is not None and STRUCTURED_CONFIGS is not None:
            catalog = get_device_anta_catalog(
                hostname=device,
                structured_config=STRUCTURED_CONFIGS[device],
                fabric_data=FABRIC_DATA,
                output_dir=get(PLUGIN_ARGS, "anta_catalog.output_dir"),
                **get_avd_catalog_filters(device, get(PLUGIN_ARGS, "anta_catalog.filters", default=[])),
            )
            catalogs.append(catalog)

    catalog = AntaCatalog.merge_catalogs(catalogs)

    return result_manager, inventory, catalog


def get_avd_catalog_filters(device: str, avd_catalog_filters: list[dict]) -> dict[str, list[str] | None]:
    """Get the test filters for a device from the provided AVD catalog filters.

    More specific filters (appearing later in the list) completely override earlier ones.
    For example, if a device matches both a group filter and an individual filter,
    the individual filter's tests will completely replace the group's tests.
    """
    final_filters = {"run_tests": None, "skip_tests": None}

    for filter_config in avd_catalog_filters:
        if device in get(filter_config, "device_list", default=[]):
            run_tests = get(filter_config, "run_tests")
            skip_tests = get(filter_config, "skip_tests")

            # Override previous filters if new ones are specified
            if run_tests is not None:
                if final_filters["run_tests"] is not None:
                    LOGGER.info("<%s> [filter] run_tests overridden from %s to %s", device, final_filters["run_tests"], run_tests)
                final_filters["run_tests"] = list(set(run_tests))

            if skip_tests is not None:
                if final_filters["skip_tests"] is not None:
                    LOGGER.info("<%s> [filter] skip_tests overridden from %s to %s", device, final_filters["skip_tests"], skip_tests)
                final_filters["skip_tests"] = list(set(skip_tests))

    return final_filters


def build_anta_device(device: str) -> AsyncEOSDevice:
    """Build the ANTA device object for a device using the provided connection variables."""
    if ANSIBLE_VARS is None or PLUGIN_ARGS is None:
        msg = "Required global variables not initialized"
        raise RuntimeError(msg)

    # Required settings to create the AsyncEOSDevice object
    required_settings = ["host", "username", "password"]

    anta_runner_settings = get(PLUGIN_ARGS, "anta_runner_settings")
    device_vars = ANSIBLE_VARS[device]

    # TODO: Confirm this is working with Ansible Vault
    device_settings = {
        "name": device,
        "host": get(device_vars, "ansible_host", default=get(device_vars, "inventory_hostname")),
        "username": get(device_vars, "ansible_user"),
        "password": default(
            get(device_vars, "ansible_password"),
            get(device_vars, "ansible_httpapi_pass"),
            get(device_vars, "ansible_httpapi_password"),
        ),
        "enable": get(device_vars, "ansible_become", default=False),
        "enable_password": get(device_vars, "ansible_become_password"),
        "port": get(
            device_vars,
            "ansible_httpapi_port",
            default=(80 if get(device_vars, "ansible_httpapi_use_ssl", default=False) is False else 443),
        ),
        "timeout": get(anta_runner_settings, "timeout"),
        "tags": set(get(device_vars, "anta_tags", default=[])),
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


def load_user_catalogs(catalog_dir: str) -> AntaCatalog:
    """Load user-defined ANTA custom catalogs from the provided directory. Supported file formats are YAML and JSON."""
    supported_formats = {".yml": "yaml", ".yaml": "yaml", ".json": "json"}
    catalogs = []

    for path_obj in Path(catalog_dir).iterdir():
        # Skip directories and non-files
        if not path_obj.is_file():
            continue

        file_format = supported_formats.get(path_obj.suffix.lower())
        if not file_format:
            LOGGER.warning("[anta_workflow]: skipped catalog file %s - unsupported format", path_obj)
            continue

        LOGGER.info("[anta_workflow]: loading catalog from %s", path_obj)
        catalog = AntaCatalog.parse(path_obj, file_format)
        catalogs.append(catalog)

    if not catalogs:
        LOGGER.info("[anta_workflow]: no user-defined custom ANTA catalogs found in directory: %s", catalog_dir)

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


def setup_queue_listener(result: dict, queue: Queue) -> QueueListener:
    """Setup and start the queue listener with the Ansible handler."""
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)
    listener = QueueListener(queue, python_to_ansible_handler, respect_handler_level=True)
    listener.start()
    return listener


def setup_module_logging(queue: Queue) -> None:
    """Setup logging for the module. All logs will be sent to the provided queue."""
    # TODO: Improve ANTA logs (httpx, asyncssh, etc.)

    # Create a handler to send logs to the queue
    handler = QueueHandler(queue)

    # Add the handler to the root logger and set the level based on Ansible verbosity
    root = logging.getLogger()
    root.addHandler(handler)
    if display.verbosity >= 3:
        root.setLevel(logging.DEBUG)
    elif display.verbosity >= 1:
        root.setLevel(logging.INFO)
        # HTTPX is too verbose at INFO level
        logging.getLogger("httpx").setLevel(logging.WARNING)
        logging.getLogger("anta").setLevel(logging.WARNING)
