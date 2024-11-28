# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# secure_hash filter
#


from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.secure_hash"

try:
    from pyavd.j2filters import secure_hash
except ImportError as e:
    secure_hash = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )


DOCUMENTATION = r"""
---
name: secure_hash
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "5.2.0"
short_description: Generate a sha512 password hash for a local user
description:
  - Generate a SHA512-Crypt password hash with a random salt value for a local user.
positional: _input
options:
  _input:
    description: Clear text password to be hashed.
    type: string
    required: true
"""


RETURN = r"""
---
_value:
  description:
    - the SHA512-Crypt password hash.
  type: string
"""


class FilterModule:
    def filters(self) -> dict:
        return {"secure_hash": wrap_filter(PLUGIN_NAME)(secure_hash)}
