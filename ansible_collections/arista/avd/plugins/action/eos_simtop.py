# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
import logging
from pathlib import Path
from typing import Any

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display
from yaml import load

from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleHandler, YamlLoader, write_file

try:
    from pyavd._utils import get, strip_empties_from_dict
    from pyavd.get_simtop import get_simtop

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


LOGGER = logging.getLogger("ansible_collections.arista.avd")
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]

ARGUMENT_SPEC = {
    "structured_config_dir": {"type": "str", "required": True},
    "structured_config_suffix": {"type": "str", "default": "yml"},
    "config_dir": {"type": "str", "required": True},
    "config_suffix": {"type": "str", "default": "cfg"},
    "mode": {"type": "str", "default": "0o664"},
    "simtop_output_file": {"type": "str", "required": True},
}


class ActionModule(ActionBase):
    def run(self, tmp: Any = None, task_vars: dict | None = None) -> None:
        self._supports_check_mode = False

        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        if not HAS_PYAVD:
            msg = "The arista.avd.eos_designs_documentation' plugin requires the 'pyavd' Python library. Got import error"
            raise AnsibleActionFail(msg)

        # Setup module logging
        setup_module_logging(result)

        # Get task arguments and validate them
        validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to json and back to remove any AnsibeUnsafe types
        validated_args = json.loads(json.dumps(validated_args))

        return self.main(validated_args, task_vars, result)

    def main(self, validated_args: dict, task_vars: dict, result: dict) -> dict:
        avd_switch_facts: dict = get(task_vars, "avd_switch_facts", required=True)
        device_list = list(avd_switch_facts.keys())

        structured_configs = self.read_structured_configs(
            device_list=device_list,
            structured_config_dir=validated_args["structured_config_dir"],
            structured_config_suffix=validated_args["structured_config_suffix"],
        )
        configs = self.read_configs(
            device_list=device_list,
            config_dir=validated_args["config_dir"],
            config_suffix=validated_args["config_suffix"],
        )
        output = get_simtop(
            {"avd_switch_facts": avd_switch_facts},
            structured_configs=structured_configs,
            configs=configs,
        )
        if output.simtop:
            result["changed"] = write_file(
                content=output.simtop,
                filename=validated_args["simtop_output_file"],
                file_mode=validated_args["mode"],
            )

        return result

    def read_structured_configs(self, device_list: list[str], structured_config_dir: str, structured_config_suffix: str) -> dict[str, dict]:
        return {device: self.read_one_structured_config(device, structured_config_dir, structured_config_suffix) for device in device_list}

    def read_one_structured_config(self, device: str, structured_config_dir: str, structured_config_suffix: str) -> dict:
        path = Path(structured_config_dir, f"{device}.{structured_config_suffix}")
        if not path.exists():
            logging.warning("Could not find structured config file for '%s'. The documentation may be incomplete.", device)

        with path.open(encoding="UTF-8") as stream:
            if structured_config_suffix in ["yml", "yaml"]:
                return load(stream, Loader=YamlLoader)  # noqa: S506

            # JSON
            return json.load(stream)

    def read_configs(self, device_list: list[str], config_dir: str, config_suffix: str) -> dict[str, dict]:
        return {device: self.read_config(device, config_dir, config_suffix) for device in device_list}

    def read_one_config(self, device: str, config_dir: str, config_suffix: str) -> dict:
        path = Path(config_dir, f"{device}.{config_suffix}")
        if not path.exists():
            logging.warning("Could not find structured config file for '%s'. The documentation may be incomplete.", device)

        config = path.open(encoding="UTF-8").read()
        return config


def setup_module_logging(result: dict) -> None:
    """
    Add a Handler to copy the logs from the plugin into Ansible output based on their level.

    Parameters:
        result: The dictionary used for the ansible module results
    """
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)
    LOGGER.addHandler(python_to_ansible_handler)
    # TODO: mechanism to manipulate the logger globally for pyavd
    # Keep debug to be able to see logs with `-v` and `-vvv`
    LOGGER.setLevel(logging.DEBUG)
