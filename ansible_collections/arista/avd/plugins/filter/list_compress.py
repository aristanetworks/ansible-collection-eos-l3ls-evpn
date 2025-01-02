# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# list_compress filter
#


from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.list_compress"

try:
    from pyavd.j2filters import list_compress
except ImportError as e:
    list_compress = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )

DOCUMENTATION = r"""
---
name: list_compress
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.0"
short_description: Compress a list of integers to a range string.
description:
  - Provides the capability to generate a string representing ranges of VLANs or VNIs.
positional: _input
options:
  _input:
    description: List of integers to compress into a range.
    type: list
    elements: integer
    required: true
"""

EXAMPLES = r"""
---
list1: "{{ [1,2,3,4,5] | arista.avd.list_compress }}" # -> "1-5"
list2: "{{ [1,2,3,7,8] | arista.avd.list_compress }}" # -> "1-3,7-8"
"""

RETURN = r"""
---
_value:
  description: Range string like "1-3,7-8"
  type: string
"""


class FilterModule:
    def filters(self) -> dict:
        return {
            "list_compress": wrap_filter(PLUGIN_NAME)(list_compress),
        }
