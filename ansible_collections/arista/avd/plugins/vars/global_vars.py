# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


DOCUMENTATION = r"""
---
name: global_vars
author: Arista Ansible Team (@aristanetworks)
version_added: "4.0.0"
short_description: Variable plugins to allow loading global_vars with less precedence than group_vars or host_vars
requirements:
  - This plugin should run at the `inventory` stage (default) before all other variable plugins to inject the variables before any group and host vars.
description: |-
  Loads variables from variable files specified in ansible.cfg or in the environment variable.
  Assign the loaded variables to the 'all' inventory group.
  Files are restricted by extension to one of .yaml, .json, .yml, or no extension.
  Hidden files (starting with '.') and backup files (ending with '~') are ignored.
  Only applies to inventory sources that are existing paths.

  ### ansible.cfg only example

  1. Enable the plugin in `ansible.cfg` - DO NOT REMOVE `host_group_vars`.

      ```ini
      [defaults]
      vars_plugins_enabled = arista.avd.global_vars, host_group_vars
      [vars_global_vars]
      paths = ../relative/path/to/my/global/vars/file/or/dir
      ```

  2. Run your playbook

      ```sh
      ansible-playbook -i inventory.yml playbook.yml
      ```

  ### ansible.cfg + environment variable example

  1. Enable the plugin in `ansible.cfg` - DO NOT REMOVE `host_group_vars`.

      ```ini
      [defaults]
      vars_plugins_enabled = arista.avd.global_vars, host_group_vars
      ```

  2. Run your playbook

      ```sh
      ARISTA_AVD_GLOBAL_VARS_PATHS=../relative/path/to/my/global/vars/file/or/dir ansible-playbook -i inventory.yml playbook.yml
      ```

options:
  paths:
    required: true
    type: list
    elements: string
    ini:
      - key: paths
        section: vars_global_vars
    env:
      - name: ARISTA_AVD_GLOBAL_VARS_PATHS
    description:
      - List of relative paths relative to the inventory file.
      - If path is a directory, all the valid files inside are loaded alphabetically.
      - If the environment variable is set, it takes precedence over ansible.cfg.
  stage:
    default: inventory
    choices: ["inventory"]
    description:
      - The stage during which executing the plugin. It could be 'inventory' or 'task'
      - Given the expected usage of this plugin at the beginning of the run. It is hard-coded to 'inventory'
  _valid_extensions:
    default: [".yml", ".yaml", ".json"]
    description:
      - Check all of these extensions when looking for 'variable' files, which should be YAML, JSON, or vaulted versions.
      - This affects vars_files, include_vars, inventory, and vars plugins, among others.
    ini:
      - key: yaml_valid_extensions
        section: defaults
    type: list
    elements: string
"""


from pathlib import Path
from typing import Any

from ansible.errors import AnsibleParserError
from ansible.inventory.group import Group
from ansible.inventory.host import Host
from ansible.module_utils._text import to_native
from ansible.plugins.vars import BaseVarsPlugin
from ansible.utils.vars import combine_vars

FOUND: list = []


class VarsModule(BaseVarsPlugin):
    def find_variable_source(self, path: str, loader: object) -> list:
        """Return the source files from which to load data, if the path is a directory - lookup vars file inside."""
        global_vars_paths = self.get_option("paths")
        extensions = self.get_option("_valid_extensions")

        found_files = []
        for g_path in global_vars_paths:
            try:
                opath = Path(path, g_path)
                if not opath.exists():
                    # file does not exist, skip it
                    self._display.vvv(f"Path: {opath} does not exist - skipping")
                    continue
                self._display.vvv(f"Adding Path: {opath} to global variables")
                if opath.is_dir():
                    self._display.debug(f"\tProcessing dir {opath}")
                    res = loader._get_dir_vars_files(str(opath), extensions)
                    self._display.debug(f"Found variable files {res!s}")
                    found_files.extend(res)
                else:
                    found_files.append(str(opath))

            except Exception as e:
                raise AnsibleParserError(to_native(e)) from e

        return found_files

    def get_vars(self, loader: object, path: str, entities: Any, _cache: bool = True) -> dict:
        """Return global variables for the `all` group in the inventory file."""
        global FOUND  # noqa: PLW0603 TODO: improve to avoid using global
        if not isinstance(entities, list):
            entities = [entities]

        if not FOUND:
            FOUND = self.find_variable_source(path, loader)

        variables = {}
        for entity in entities:
            if not isinstance(entity, (Host, Group)):
                # Changed the error message because the TYPE_REGEX of ansible was triggering
                # unidiomatic-typecheck because of the `or` word before the type  call...
                msg = f"Supplied entity is of type {type(entity)} but must be of type Host or Group instead"
                raise AnsibleParserError(msg)
            if entity.name != "all":
                continue

            for found_path in FOUND:
                new_data = loader.load_from_file(found_path, cache=True, unsafe=True)
                if new_data:
                    variables = combine_vars(variables, new_data)

        return variables
