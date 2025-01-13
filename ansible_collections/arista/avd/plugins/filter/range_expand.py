# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# range_expand filter
#


from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.range_expand"

try:
    from pyavd.j2filters import range_expand
except ImportError as e:
    range_expand = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )


DOCUMENTATION = r"""
---
name: range_expand
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "3.4.0"
short_description: Expand a range of interfaces or list of ranges and return as a list of strings.
description:
  - Provides the capabilities to expand a range of interfaces or list of ranges and return as a list of strings.
  - The filter supports VLANs, interfaces, modules, sub-interfaces, and ranges are expanded at all levels.
  - Within a single range, prefixes (ex. Ethernet, Eth, Po) are carried over to items without prefixes (see examples).
positional: _input
options:
  _input:
    description: Range as string or list of ranges.
    type: any
    required: true
"""

EXAMPLES = r"""
---
- "{{ 'Ethernet1' | range_expand }}"
# -> ["Ethernet1"]

- "{{ 'Ethernet1-2' | range_expand }}"
# -> ["Ethernet1", "Ethernet2"]

- "{{ 'Eth 3-5,7-8' | range_expand }}"
# -> ["Eth 3", "Eth 4", "Eth 5", "Eth 7", "Eth 8"]

- "{{ 'et2-6,po1-2' | range_expand }}"
# -> ["et2", "et3", "et4", "et5", "et6", "po1", "po2"]

- "{{ ['Ethernet1'] | range_expand }}"
# -> ["Ethernet1"]

- "{{ ['Ethernet 1-2', 'Eth3-5', '7-8'] | range_expand }}"
# -> ["Ethernet 1", "Ethernet 2", "Eth3", "Eth4", "Eth5", "7", "8"]

- "{{ ['Ethernet2-6', 'Port-channel1-2'] | range_expand }}"
# -> ["Ethernet2", "Ethernet3", "Ethernet4", "Ethernet5", "Ethernet6", "Port-channel1", "Port-channel2"]

- "{{ ['Ethernet1/1-2', 'Eth1-2/3-5,5/1-2'] | range_expand }}"
# -> ["Ethernet1/1", "Ethernet1/2", "Eth1/3", "Eth1/4", "Eth1/5", "Eth2/3", "Eth2/4", "Eth2/5", "Eth5/1", "Eth5/2"]

- "{{ ['Eth1.1,9-10.1', 'Eth2.2-3', 'Eth3/1-2.3-4'] | range_expand }}"
# -> ["Eth1.1", "Eth9.1", "Eth10.1", "Eth2.2", "Eth2.3", "Eth3/1.3", "Eth3/1.4", "Eth3/2.3", "Eth3/2.4"]

- "{{ '1-3' | range_expand }}"
# -> ["1", "2", "3"]

- "{{ ['1', '2', '3'] | range_expand }}"
# -> ["1", "2", "3"]

- "{{ 'vlan1-3' | range_expand }}"
# -> ["vlan1", "vlan2", "vlan3"]

- "{{ 'Et1-2/3-4/5-6' | range_expand }}"
# -> ["Et1/3/5", "Et1/3/6", "Et1/4/5", "Et1/4/6", "Et2/3/5", "Et2/3/6", "Et2/4/5", "Et2/4/6"]
"""

RETURN = r"""
---
_value:
  description: List of strings from all ranges.
  type: list
  elements: string
"""


class FilterModule:
    def filters(self) -> dict:
        return {
            "range_expand": wrap_filter(PLUGIN_NAME)(range_expand),
        }
