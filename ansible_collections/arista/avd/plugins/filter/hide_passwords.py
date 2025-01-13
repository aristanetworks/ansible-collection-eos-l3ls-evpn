# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# arista.avd.hide_passwords filter
#
from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.hide_passwords"

try:
    from pyavd.j2filters import hide_passwords
except ImportError as e:
    hide_passwords = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )

DOCUMENTATION = r"""
name: hide_passwords
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "4.0.0"
short_description: Replace a value by "<removed>"
description:
  - Replace the input data by "<removed>" if the hide_passwords parameter is true
positional: _input
options:
  _input:
    description: Value to replace.
    type: raw
    required: true
  hide_passwords:
    description: Flag to indicate whether or not the string should be replaced.
    type: bool
    required: true
"""

EXAMPLES = r"""
cli_with_hidden_password: "ip ospf authentication-key 7 {{ vlan_interface.ospf_authentication_key | arista.avd.hide_passwords(true) }}"
"""

RETURN = r"""
---
_value:
  description: The original input or '<removed>'
  type: string
"""


class FilterModule:
    def filters(self) -> dict:
        return {
            "hide_passwords": wrap_filter(PLUGIN_NAME)(hide_passwords),
        }
