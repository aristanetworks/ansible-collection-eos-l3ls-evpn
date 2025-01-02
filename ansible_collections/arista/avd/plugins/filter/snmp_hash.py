# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# snmp_hash filter
#


from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.snmp_hash"

try:
    from pyavd.j2filters import snmp_hash
except ImportError as e:
    snmp_hash = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )

DOCUMENTATION = r"""
---
name: snmp_hash
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "3.6.0"
short_description: Compute localized SNMP passphrases
description:
  - Key localization as described in [RFC 2574 section 2.6](https://www.rfc-editor.org/rfc/rfc2574.html#section-2.6)
positional: _input
options:
  _input:
    description: Dictionary with SNMP passphrase details.
    type: dictionary
    required: true
    suboptions:
      passphrase:
        type: string
        required: true
        description:
          - The passphrase to localize.
          - This is the "auth" passphrase when the `priv` argument is not set.
          - If `priv` is set, it is the "priv" passphrase.
      auth:
        type: string
        description: Auth type
        choices: ["md5", "sha", "sha224", "sha256", "sha384", "sha512"]
        required: true
      engine_id:
        type: string
        description: A hexadecimal string containing the engine_id to be used to localize the passphrase
        required: true
      priv:
        type: string
        description: Priv type
        choices: ["des", "aes", "aes192", "aes256"]
"""


RETURN = r"""
---
_value:
  description:
    - The localized key generated from the passphrase using `auth` type.
    - If required the key is truncated to match the appropriate keylength for the `priv` type.
  type: string
"""


class FilterModule:
    def filters(self) -> dict:
        return {"snmp_hash": wrap_filter(PLUGIN_NAME)(snmp_hash)}
