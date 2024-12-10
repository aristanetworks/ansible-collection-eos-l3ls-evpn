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
short_description: Generate a SHA-512 password hash for an EOS user.
description:
  - This filter generates a SHA-512 password hash from a cleartext password for a local user. A randomly generated salt will be used
    unless the user specifies one.
positional: _input
options:
  _input:
    description: Clear text password to be hashed.
    type: string
    required: true
  salt:
    description: |-
      Salt value to be used when creating password hash.
      The salt value can only contain the characters `./`, digits `0-9`, and uppercase or lowercase letters `A-Z a-z`.
      The salt value should not be greater than 16 characters long.
      If a salt value is not included then a random salt will be generated.
    type: string
"""


EXAMPLES = r"""
---
local_users:
  # Create sha512 password hash with random salt. Note: this will create a new hash each time it is run
  - name: admin
    sha512_password: "{{ 'password123' | arista.avd.secure_hash }}"

  # Create sha512 password hash with user defined salt value
  - name: cvpadmin
    sha512_password: "{{ 'securepassword' | arista.avd.secure_hash(salt='Yar49ahkzKddRVYS') }}"
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
