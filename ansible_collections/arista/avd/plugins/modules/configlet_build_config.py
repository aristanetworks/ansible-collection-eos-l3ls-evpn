# Copyright (c) 2019-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


DOCUMENTATION = r"""
---
module: configlet_build_config
version_added: "1.0.0"
author: EMEA AS Team (@aristanetworks)
short_description: Build arista.cvp.configlet configuration.
description:
  - Build configuration to publish configlets to Cloudvision.
options:
  configlet_dir:
    description: Directory where configlets are located.
    required: true
    type: str
  configlet_prefix:
    description: Prefix to append on configlet.
    required: true
    type: str
  destination:
    description: File where to save information.
    required: false
    type: str
  configlet_extension:
    description: File extension to look for.
    required: false
    type: str
    default: 'conf'
"""

EXAMPLES = r"""
# tasks file for configlet_build_config
- name: generate intended variables
  configlet_build_config:
    configlet_dir: '/path/to/configlets/folder/'
    configlet_prefix: 'AVD_'
    configlet_extension: 'cfg'
"""

import traceback
from pathlib import Path

from ansible.module_utils.basic import AnsibleModule

YAML_IMP_ERR = None
try:
    import yaml

    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    YAML_IMP_ERR = traceback.format_exc()


def get_configlet(src_folder: str = "", prefix: str = "AVD", extension: str = "cfg") -> dict:
    """
    Get available configlets to deploy to CVP.

    Parameters
    ----------
    src_folder : str, optional
        Path where to find configlet, by default ""
    prefix : str, optional
        Prefix to append to configlet name, by default 'AVD'
    extension : str, optional
        File extension to lookup configlet file, by default 'cfg'

    Returns:
    -------
    dict
        Dictionary of configlets found in source folder.
    """
    src_configlets = Path(src_folder).glob(f"*.{extension}")
    configlets = {}
    for file in src_configlets:
        name = prefix + "_" + file.stem if prefix != "none" else file.stem
        with file.open(encoding="utf8") as stream:
            data = stream.read()
        configlets[name] = data
    return configlets


def main() -> None:
    """Main entry point for module execution."""
    argument_spec = {
        "configlet_dir": {"type": "str", "required": True},
        "configlet_prefix": {"type": "str", "required": True},
        "configlet_extension": {"type": "str", "required": False, "default": "conf"},
        "destination": {"type": "str", "required": False, "default": None},
    }

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)
    result = {"changed": False}

    if not HAS_YAML:
        module.fail_json(msg="yaml lib is required for this module")

    # If set, build configlet topology
    if module.params["configlet_dir"] is not None:
        result["cvp_configlets"] = get_configlet(
            src_folder=module.params["configlet_dir"],
            prefix=module.params["configlet_prefix"],
            extension=module.params["configlet_extension"],
        )

    # Write vars to file if set by user
    if module.params["destination"] is not None:
        with Path(module.params["destination"]).open("w", encoding="utf8") as file:
            yaml.dump(result, file)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
