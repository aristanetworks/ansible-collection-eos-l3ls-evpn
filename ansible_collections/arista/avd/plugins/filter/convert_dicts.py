# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# def arista.avd.convert_dicts
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type


from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import wrap_filter

try:
    from pyavd.j2filters.convert_dict import convert_dicts

    PYAVD_IMPORT_EXCEPTION = None
except ImportError as e:
    default = None
    PYAVD_IMPORT_EXCEPTION = e

DOCUMENTATION = r"""
---
name: convert_dicts
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "2.0"
short_description: Convert a dictionary containing nested dictionaries to a list of dictionaries.
description:
  - The filter inserts the outer dictionary keys into each list item using the primary_key `name` (the key name is
    configurable), and if there is a non-dictionary value, it inserts this value to
    secondary key (the key name is configurable), if `secondary_key` is provided.
  - This filter is intended for seamless data model migration from dictionaries to lists.
  - The filter can improve Ansible's processing performance when dealing with large dictionaries by converting them to lists of dictionaries.
  - Note - if there is a non-dictionary value with no secondary key provided, it will pass through untouched.

positional: _input
options:
  _input:
    type: any
    description: Dictionary to convert - returned untouched if not a nested dictionary/list.
    required: true
  primary_key:
    type: string
    description: Name of the primary key used when inserting outer dictionary keys into items.
    default: name
  secondary_key:
    type: string
    description: Name of the secondary key used when inserting dictionary values which are list into items.
"""

EXAMPLES = r"""
---
- hosts: localhost
  gather_facts: false
  tasks:
  - name: Show convert_dicts with default primary_key "name"
    vars:
      my_dict:
        item1:
          value: value1
        item2:
          value: value2
    ansible.builtin.debug:
      msg: "{{ item.name }}: {{ item.value }}"
    loop:
      items: "{{ my_dict | arista.avd.convert_dicts }}"

  - name: Show convert_dicts with custom primary_key "myname"
    vars:
      my_dict:
        item1:
          value: value1
        item2:
          value: value2
    ansible.builtin.debug:
      msg: "{{ item.myname }}: {{ item.value }}"
    loop: "{{ my_dict | arista.avd.convert_dicts('myname') }}"

  - name: Show convert_dicts with secondary_key "myvalue"
    vars:
      my_dict:
        item1: value1
        item2: value2
    ansible.builtin.debug:
      msg: "{{ item.name }}: {{ item.myvalue }}"
    loop: "{{ my_dict | arista.avd.convert_dicts(secondary_key='myvalue') }}"
"""

RETURN = r"""
---
_value:
  description: Returns list of dictionaries or input variable untouched if not a nested dictionary/list.
  type: any
"""


class FilterModule(object):
    def filters(self):
        return {
            "convert_dicts": wrap_filter("arista.avd.default", PYAVD_IMPORT_EXCEPTION)(convert_dicts),
        }
