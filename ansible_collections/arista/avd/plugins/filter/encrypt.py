# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.encrypt"

try:
    from pyavd.j2filters import encrypt
except ImportError as e:
    encrypt = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )

DOCUMENTATION = r"""
---
name: encrypt
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "3.8.0"
short_description: Encrypt supported EOS passwords
description: |-
  The filter encrypts a clear text password into EOS passwords.
  To be used with Ansible Vault to load a password and have it encrypted on the fly by AVD in `eos_designs`.
  Note - For now this filter only supports encryption from type `7` and not type `8a` for OSPF and BGP passwords.
positional: _input
options:
  _input:
    type: string
    description: Clear text password to be encrypted.
    required: true
  passwd_type:
    type: string
    description: |-
      Type of password to encrypt.
      `bgp` and `ospf_simple` requires the `password` and `key` inputs.
      `ospf_message_digest` requires the `password`, `key`, `hash_algorithm`, `key_id` inputs.
      `isis` requires the `password`, `key` and `isis_mode` inputs.
    choices: ["bgp", "ospf_simple", "ospf_message_digest", "isis"]
    required: true
  key:
    type: string
    description: |-
      Encryption key. The value depends on the type of password.
      For BGP passwords, the key is the Neighbor IP or the BGP Peer Group Name in EOS.
      For OSPF passwords, the key is the interface name (e.g., `Ethernet1`).
      For ISIS passwords the key is the ISIS instance name (from `router isis <instance name>` or `isis enable <instance name>`).
    required: true
  hash_algorithm:
    type: string
    description: |-
      Hash algorithm to use with `passwd_type=ospf_message_digest`.
    choices: ["md5", "sha1", "sha256", "sha384", "sha512"]
  key_id:
    type: integer
    description: |-
      Key ID to use with `passwd_type=ospf_message_digest`.
    min: 1
    max: 255
  isis_mode:
    type: string
    description: ISIS encryption mode (`none`, `text`, `md5`, `sha`) or shared-secret algorithm (`sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha1-512`).
    choices: ["none", "text", "md5", "sha", "sha-1", "sha-224", "sha-256", "sha-384", "sha1-512"]
"""

EXAMPLES = r"""
---
- # Encrypt the vaulted BGP password for peer group "IPv4-UNDERLAY-PEERS"
  bgp_peer_groups:
    ipv4_underlay_peers:
      name: IPv4-UNDERLAY-PEERS
      password: "{{ bgp_vault_password | arista.avd.encrypt(passwd_type='bgp', key='IPv4-UNDERLAY-PEERS') }}"

- # Encrypt the vaulted OSPF simple password for interface "Ethernet1"
  ethernet_interfaces:
    - name: Ethernet1
      ospf_authentication: simple
      ospf_authentication_key: "{{ ospf_vault_password | arista.avd.encrypt(passwd_type='ospf_simple', key='Ethernet1') }}"

- # Encrypt the vaulted OSPF message digest password for Ethernet1, MD5 and key id 1
  ethernet_interfaces:
    - name: Ethernet1
      ospf_authentication: message-digest
      ospf_message_digest_keys:
        - id: 1
          hash_algorithm: md5
          key: "{{ ospf_vault_password | arista.avd.encrypt(passwd_type='ospf_message_digest', key='Ethernet1', hash_algorithm='md5', key_id='1') }}"
"""

RETURN = r"""
---
_value:
  description: Encrypted EOS password string.
  type: string
"""


class FilterModule:
    def filters(self) -> dict:
        return {
            "encrypt": wrap_filter(PLUGIN_NAME)(encrypt),
        }
