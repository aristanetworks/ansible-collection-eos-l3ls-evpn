# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

import yaml
from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschematools import AvdSchemaTools
from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleContextFilter, PythonToAnsibleHandler, YamlLoader, cprofile, get_templar

try:
    from pyavd import get_device_config, get_device_doc
    from pyavd._utils import strip_empties_from_dict, template
    from pyavd.j2filters import add_md_toc

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


CUSTOM_TEMPLATES_CFG_TEMPLATE = "eos/custom-templates.j2"
CUSTOM_TEMPLATES_DOC_TEMPLATE = "documentation/custom-templates.j2"

LOGGER = logging.getLogger("ansible_collections.arista.avd")
# Avoid duplicate logs in debug files
LOGGER.propagate = False

ARGUMENT_SPEC = {
    "structured_config_filename": {"type": "str"},
    "config_filename": {"type": "str"},
    "documentation_filename": {"type": "str"},
    "read_structured_config_from_file": {"type": "bool", "default": True},
    "validation_mode": {"type": "str", "default": "error"},
    "generate_device_config": {"type": "bool", "default": True},
    "generate_device_doc": {"type": "bool", "default": True},
    "device_doc_toc": {"type": "bool", "default": True},
    "cprofile_file": {"type": "str"},
}


class ActionModule(ActionBase):
    """Action Module for eos_cli_config_gen."""

    @cprofile()
    def run(self, tmp: Any = None, task_vars: dict | None = None) -> None:
        """Ansible Action entry point."""
        if task_vars is None:
            task_vars = {}

        if not HAS_PYAVD:
            msg = "The arista.avd.eos_cli_config_gen' plugin requires the 'pyavd' Python library. Got import error"
            raise AnsibleActionFail(msg)

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # Setup module logging
        hostname = task_vars["inventory_hostname"]
        setup_module_logging(hostname, result)

        return self.main(task_vars, result)

    def main(self, task_vars: dict, result: dict) -> dict:
        """Main function in charge of validating the input variables and generating the device configuration and documentation."""
        LOGGER.debug("Validating task arguments...")
        validated_args = self.validate_args()
        LOGGER.debug("Validating task arguments [done].")

        try:
            # Read structured config from file or task_vars and run templating to handle inline jinja.
            LOGGER.debug("Preparing task vars...")
            task_vars = self.prepare_task_vars(
                task_vars,
                validated_args.get("structured_config_filename"),
                read_structured_config_from_file=validated_args["read_structured_config_from_file"],
            )
            LOGGER.debug("Preparing task vars [done].")

            LOGGER.debug("Validating structured configuration...")
            # result dict will be in-place updated.
            self.validate_task_vars(
                hostname=task_vars["inventory_hostname"],
                validation_mode=validated_args["validation_mode"],
                task_vars=task_vars,
                result=result,
            )
            LOGGER.debug("Validating structured configuration [done].")
        except Exception as e:
            LOGGER.exception(e)  # noqa: TRY401 TODO: Improve code
            return result

        if result.get("failed"):
            # Something failed in schema validation.
            return result

        has_custom_templates = bool(task_vars.get("custom_templates"))
        try:
            if validated_args["generate_device_config"]:
                LOGGER.debug("Rendering configuration...")
                device_config = get_device_config(task_vars)

                if has_custom_templates:
                    LOGGER.debug("Rendering config custom templates...")
                    rendered_custom_templates = self.render_template_with_ansible_templar(task_vars, CUSTOM_TEMPLATES_CFG_TEMPLATE)
                    # Need to handle if `end` has been rendered already
                    if device_config.endswith("!\nend\n"):
                        device_config = device_config[:-6] + rendered_custom_templates + "!\nend\n"
                    else:
                        device_config += rendered_custom_templates
                    LOGGER.debug("Rendering config custom templates [done].")

                result["changed"] = self.write_file(device_config, validated_args["config_filename"])
                LOGGER.debug("Rendering configuration [done].")

            if validated_args["generate_device_doc"]:
                LOGGER.debug("Rendering documentation...")
                device_doc = get_device_doc(task_vars, add_md_toc=False)

                if has_custom_templates:
                    LOGGER.debug("Rendering documentation custom templates...")
                    device_doc += self.render_template_with_ansible_templar(task_vars, CUSTOM_TEMPLATES_DOC_TEMPLATE)
                    LOGGER.debug("Rendering documentation custom templates [done].")

                if validated_args["device_doc_toc"]:
                    device_doc = add_md_toc(device_doc, skip_lines=3)

                file_changed = self.write_file(device_doc, validated_args["documentation_filename"])
                result["changed"] = result.get("changed") or file_changed
                LOGGER.debug("Rendering documentation [done].")

        except Exception as error:
            # Recast errors as AnsibleActionFail
            msg = f"Error during plugin execution: {error}"
            raise AnsibleActionFail(msg) from error

        return result

    def validate_args(self) -> dict:
        """Get task arguments and validate them."""
        validation_result, validated_args = self.validate_argument_spec(
            ARGUMENT_SPEC,
            required_if=[
                ("read_structured_config_from_file", True, ("structured_config_filename",)),
                ("generate_device_config", True, ("config_filename",)),
                ("generate_device_doc", True, ("documentation_filename",)),
            ],
        )
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to json and back to remove any AnsibeUnsafe types
        return json.loads(json.dumps(validated_args))

    def prepare_task_vars(self, task_vars: dict, structured_config_filename: str, *, read_structured_config_from_file: bool) -> dict:
        """Read the structured_config and render inline Jinja.

        Parameters
        ----------
            task_vars: Dictionary of task variables
            structured_config_filename: The filename where the structured_config for the device is stored.
            read_structured_config_from_file: Flag to indicate whether or not the structured_config_filname should be read.

        Returns:
        -------
            dict: Task vars updated with the structured_config content if read and all inline Jinja rendered.

        Raises:
        ------
            AnsibleActionFail: If templating fails.

        """
        if read_structured_config_from_file:
            task_vars.update(read_vars(structured_config_filename))

        # Read ansible variables and perform templating to support inline jinja2
        for var, value in task_vars.items():
            # TODO: - reevaluate these variables
            if str(var).startswith(("ansible", "molecule", "hostvars", "vars", "avd_switch_facts")):
                continue
            if self._templar.is_template(value):
                # Var contains a jinja2 template.
                try:
                    task_vars[var] = self._templar.template(value, fail_on_undefined=False)
                except Exception as e:
                    msg = f"Exception during templating of task_var '{var}': '{e}'"
                    raise AnsibleActionFail(msg) from e

        if not isinstance(task_vars, dict):
            # Corner case for ansible-test where the passed task_vars is a nested chain-map
            task_vars = dict(task_vars)

        return task_vars

    def validate_task_vars(self, hostname: str, validation_mode: str, task_vars: dict, result: dict) -> None:
        # Load schema tools for input schema
        input_schema_tools = AvdSchemaTools(
            hostname=hostname,
            ansible_display=display,
            schema_id="eos_cli_config_gen",
            validation_mode=validation_mode,
            plugin_name="arista.avd.eos_cli_config_gen",
        )
        result.update(input_schema_tools.convert_and_validate_data(task_vars))

    def render_template_with_ansible_templar(self, task_vars: dict, templatefile: str) -> str:
        """Render a template with the Ansible Templar."""
        # Get updated templar instance to be passed along to our simplified "templater"
        if not hasattr(self, "ansible_templar"):
            self.ansible_templar = get_templar(self, task_vars)

        return template(templatefile, task_vars, self.ansible_templar)

    def write_file(self, content: str, filename: str) -> bool:
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
        if path.exists():
            if path.read_text(encoding="UTF-8") == content:
                return False

        else:
            # Create parent dirs automatically.
            path.parent.mkdir(mode=0o775, parents=True, exist_ok=True)
            # Touch file
            path.touch(mode=0o664)

        path.write_text(content, encoding="UTF-8")
        return True


def setup_module_logging(hostname: str, result: dict) -> None:
    """
    Add a Handler to copy the logs from the plugin into Ansible output based on their level.

    Parameters
    ----------
        hostname: Current Inventory device being used to augment the logs with <hostname>
        result: The dictionary used for the ansible module results
    """
    python_to_ansible_filter = PythonToAnsibleContextFilter(hostname)
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)
    python_to_ansible_handler.addFilter(python_to_ansible_filter)
    LOGGER.addHandler(python_to_ansible_handler)
    # TODO: mechanism to manipulate the logger globally for pyavd
    LOGGER.setLevel(logging.DEBUG)


def read_vars(filename: Path | str) -> dict:
    """Read the file at filename and return the content as dict.

    The function supports either `json` or `yaml` format.

    Parameters
    ----------
        filename: The path to the file to read as a string or a Path.

    Returns:
    -------
        dict: The content of the file as dict or an empty dict if the file does not exist.

    Raises:
    ------
        NotImplementedError: If the file extension is not json, yml or yaml.
    """
    if not isinstance(filename, Path):
        filename = Path(filename)

    if not filename.exists():
        LOGGER.debug("File %s does not exist, skipping reading variables...", filename)
        return {}

    with filename.open(mode="r", encoding="UTF-8") as stream:
        if filename.suffix in [".yml", ".yaml"]:
            return yaml.load(stream, Loader=YamlLoader)  # noqa: S506 TODO: Figure out if we can move to safeloader everywhere
        if filename.suffix == ".json":
            return json.load(stream)

        msg = f"Unsupported file suffix for file '{filename}'"
        raise NotImplementedError(msg)
