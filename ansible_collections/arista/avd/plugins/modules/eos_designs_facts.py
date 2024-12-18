# Copyright (c) 2022-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: eos_designs_facts
version_added: "3.5.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Set eos_designs facts
description:
  - |-
    The `arista.avd.eos_designs_facts` module is an Ansible Action Plugin providing the following capabilities:

    - Set `avd_switch_facts` fact containing both `switch` facts per host.
    - Set `avd_topology_peers` fact containing list of downlink switches per host.
      This list is built based on the `uplink_switches` from all other hosts.
    - Set `avd_overlay_peers` fact containing list of EVPN or MPLS overlay peers per host.
      This list is built based on the `evpn_route_servers` and `mpls_route_reflectors` from all other hosts.

  - The plugin is designed to `run_once`. With this, Ansible will set the same facts on all devices,
    so all devices can lookup values of any other device without using the slower `hostvars`.
  - The facts can also be copied to the "root" `switch` in a task run per-device (see example below)
  - The module is used in `arista.avd.eos_designs` to set facts for devices, which are then used by jinja templates
    and python module in `arista.avd.eos_designs` to generate the `structured_configuration`.
options:
  template_output:
    description:
      - If true, the output data will be run through another jinja2 rendering before returning.
        This is to resolve any input values with inline jinja using variables/facts set by the input templates.
    required: false
    type: bool
  validation_mode:
    description:
      - Run validation in either "error" or "warning" mode.
      - Validation will validate the input variables according to the schema.
      - During validation, messages will be generated with information about the host(s) and key(s) which failed validation.
      - validation_mode:error will produce error messages and fail the task.
      - validation_mode:warning will produce warning messages.
    required: false
    default: "error"
    type: str
    choices: [ "error", "warning" ]
  cprofile_file:
    description:
      - Filename for storing cprofile data used to debug performance issues.
      - Running cprofile will slow down performance in it self, so only set this while troubleshooting.
    required: false
    type: str
"""

EXAMPLES = r"""
---
- name: Set eos_designs facts
  arista.avd.eos_designs_facts:
    schema_id: eos_designs
  check_mode: false
  run_once: true

- name: Set eos_designs facts per device
  ansible.builtin.set_fact:
    switch: "{{ avd_switch_facts[inventory_hostname].switch }}"
  delegate_to: localhost
  changed_when: false
"""
