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

from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleHandler, YamlLoader

try:
    from pyavd._utils import get, strip_empties_from_dict
    from pyavd.get_fabric_documentation import get_fabric_documentation

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


LOGGER = logging.getLogger("ansible_collections.arista.avd")
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]

ARGUMENT_SPEC = {
    "device_list": {"type": "list", "elements": "str", "required": True},
    "structured_config_dir": {"type": "str", "required": True},
    "structured_config_suffix": {"type": "str", "default": "yml"},
    "fabric_documentation_file": {"type": "str", "required": True},
    "fabric_documentation": {"type": "bool", "default": True},
    "include_connected_endpoints": {"type": "bool", "default": False},
    "mode": {"type": "str", "default": "0x664"},
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
        structured_configs = self.read_structured_configs(
            device_list=validated_args["device_list"],
            structured_config_dir=validated_args["structured_config_dir"],
            structured_config_suffix=validated_args["structured_config_suffix"],
        )
        avd_switch_facts = get(task_vars, "avd_switch_facts", required=True)
        fabric_name = get(task_vars, "fabric_name", required=True)
        output = get_fabric_documentation(
            {"avd_switch_facts": avd_switch_facts},
            structured_configs=structured_configs,
            fabric_name=fabric_name,
            fabric_documentation=validated_args["fabric_documentation"],
            include_connected_endpoints=validated_args["include_connected_endpoints"],
        )
        result["changed"] = self.write_file(
            content=output.fabric_documentation,
            filename=validated_args["fabric_documentation_file"],
            file_mode=validated_args["mode"],
        )
        return result

    def read_structured_configs(self, device_list: list[str], structured_config_dir: str, structured_config_suffix: str) -> dict[str, dict]:
        return {device: self.read_one_structured_config(Path(structured_config_dir, f"{device}.{structured_config_suffix}")) for device in device_list}

    def read_one_structured_config(self, path: Path) -> dict:
        with path.open(encoding="UTF-8") as stream:
            if path.suffix in [".yml", ".yaml"]:
                return load(stream, Loader=YamlLoader)  # noqa: S506

            # JSON
            return json.load(stream)

    def write_file(self, content: str, filename: str, file_mode: str = "0o664", dir_mode: str = "0o775") -> bool:
        """
        This function writes the file only if the content has changed.

        Parameters
        ----------
            content: The content to write
            filename: Target filename

        Returns:
        -------
            bool: Indicate if the content of filename has changed.
        """
        path = Path(filename)
        if not path.exists():
            # Create parent dirs automatically.
            path.parent.mkdir(mode=int(dir_mode, 8), parents=True, exist_ok=True)
            # Touch file
            path.touch(mode=int(file_mode, 8))
        elif path.read_text(encoding="UTF-8") == content:
            return False

        path.write_text(content, encoding="UTF-8")
        return True


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
