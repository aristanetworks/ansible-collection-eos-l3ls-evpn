# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: eos_designs_documentation
version_added: "5.0.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Generate AVD Fabric Documentation
description: |-
  The `arista.avd.eos_simtop` module is an Ansible Action Plugin providing the following capabilities:

  - Generate simtop using AVD facts and configuration files
options:
  structured_config_dir:
    description: Path to directory containing files with AVD structured configurations.
    required: true
    type: str
  structured_config_suffix:
    description: File suffix for AVD structured configuration files.
    default: "yml"
    type: str
  configs_dir:
    description: Path to directory containing files with AVD actual device configurations.
    required: true
    type: str
  configs_suffix:
    description: File suffix for AVD actual device configuration files.
    default: "cfg"
    type: str
  simtop_output_file:
    description: Path to output simtop file.
    required: true
    type: str
  mode:
    description: Mode of output files.
    default: "0o664"
    type: str
"""

EXAMPLES = r"""
---

- name: Generate fabric documentation
  arista.avd.eos_designs_documentation:
    structured_config_dir: "{{ structured_dir }}"
    structured_config_suffix: "{{ avd_structured_config_file_format }}"
    fabric_documentation_file: "{{ fabric_dir }}/{{ fabric_name }}-documentation.md"
    fabric_documentation: "{{ eos_designs_documentation.enable | arista.avd.default(true) }}"
    include_connected_endpoints: "{{ eos_designs_documentation.connected_endpoints | arista.avd.default(false) }}"
    topology_csv_file: "{{ fabric_dir }}/{{ fabric_name }}-topology.csv"
    topology_csv: "{{ eos_designs_documentation.topology_csv | arista.avd.default(true) }}"
    p2p_links_csv_file: "{{ fabric_dir }}/{{ fabric_name }}-topology.csv"
    p2p_links_csv: "{{ eos_designs_documentation.p2p_links_csv | arista.avd.default(true) }}"
    mode: "0o664"
  delegate_to: localhost
  check_mode: false
  run_once: true
"""

# TODO: RETURN
