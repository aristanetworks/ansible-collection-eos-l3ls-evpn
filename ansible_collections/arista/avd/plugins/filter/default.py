# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# def arista.avd.default
#


from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.default"

try:
    from pyavd.j2filters import default
except ImportError as e:
    default = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )

DOCUMENTATION = r"""
---
name: default
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "2.0"
short_description: Returns input value if defined and is not none. Otherwise, return default value.
description: |-
  The `arista.avd.default` filter can provide the same essential capability as the built-in `default` filter.
  It will return the input value only if it's valid and, if not, provide a default value instead.
  Our custom filter requires a value to be `not undefined` and `not None` to pass through.
  Furthermore, the filter allows multiple default values as arguments, which will undergo the same validation until we find a valid default value.
  As a last resort, the filter will return `None`.
positional: _input
options:
  _input:
    description: Default value to check. Will be returned untouched if `not undefined` and `not None`.
    type: any
    required: true
  default_values:
    type: any
    description: One or more default values will be tested individually, and the first valid value will be used.
"""

EXAMPLES = r"""
---
myvalue: "{{ variable | arista.avd.default(default_value_1, default_value_2) }}"
"""

RETURN = r"""
---
_value:
  description: Input value if `not undefined` and `not None`. Otherwise, return the first defined default value or `None`.
  type: any
"""


class FilterModule:
    def filters(self) -> dict:
        return {
            "default": wrap_filter(PLUGIN_NAME)(default),
        }
