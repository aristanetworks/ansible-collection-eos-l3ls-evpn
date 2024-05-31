# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# def arista.avd.default
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type


from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import wrap_filter

try:
    from pyavd.j2filters.default import default

    PYAVD_IMPORT_EXCEPTION = None
except ImportError as e:
    default = None
    PYAVD_IMPORT_EXCEPTION = e

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


class FilterModule(object):
    def filters(self):
        return {
            "default": wrap_filter("arista.avd.default", PYAVD_IMPORT_EXCEPTION)(default),
        }
