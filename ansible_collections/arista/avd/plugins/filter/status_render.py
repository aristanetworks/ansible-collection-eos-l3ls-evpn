# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.status_render"

try:
    from pyavd.j2filters import status_render
except ImportError as e:
    status_render = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )

DOCUMENTATION = r"""
---
name: status_render
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "1.1.1"
short_description: Convert Text to EMOJI code.
description:
  - Returns the input value unless `rendering` is set to "github".
  - Returns `:x:` if input status string is `FAIL` and `rendering` is set to "github".
  - Returns `:white_check_mark:` if input status string is `PASS` and `rendering` is set to "github".
positional: _input
options:
  _input:
    description: Text to convert to EMOJI.
    type: string
    required: true
  rendering:
    description: Markdown Flavor to use for Emoji rendering. Only "github" is supported.
    type: string
    required: true
"""

RETURN = r"""
---
_value:
  description: Input value or GitHub Markdown emoji code.
  type: string
"""


class FilterModule:
    def filters(self) -> dict:
        return {"status_render": wrap_filter(PLUGIN_NAME)(status_render)}
