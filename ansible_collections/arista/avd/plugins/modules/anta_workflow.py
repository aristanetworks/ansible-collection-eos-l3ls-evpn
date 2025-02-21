# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
ANSIBLE_METADATA = {"metadata_version": "1.0", "status": ["preview"]}

DOCUMENTATION = r"""
---
module: anta_workflow
version_added: "5.3.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Uses ANTA from Ansible
description:
  - The `arista.avd.anta_workflow` module is an Ansible Action Plugin to leverage the ANTA test
    framework to validate that the generated structured configurations by AVD are applied to the
    devices and that the deployed network is working correctly. It can also be used to execute
    user-defined ANTA test catalogs in conjunction with the Ansible inventory, providing similar
    functionality and options as the ANTA CLI while benefiting from Ansible's inventory management
    capabilities.
  - |-
    The plugin offers the following capabilities:
        - Generating a per-device test catalog based on the AVD structured_config.
        - WIP
options:
  device_list:
    description: List of devices to run ANTA tests against. These devices must be defined in the Ansible inventory.
    type: list
    required: true
    elements: str
  anta_catalog:
    description: WIP
    type: dict
    suboptions:
      output_dir:
        description: WIP
        type: str
      structured_config_dir:
        description: WIP
        type: str
      structured_config_suffix:
        description: WIP
        type: str
      scope:
        description: WIP
        type: dict
        suboptions:
          boundary:
            description: WIP
            type: str
            choices: ["unlimited", "fabric", "dc", "pod", "rack"]
            default: "unlimited"
          allow_bgp_external:
            description: WIP
            type: bool
            default: false
          allow_bgp_vrfs:
            description: WIP
            type: bool
            default: false
      filters:
        description: WIP
        type: list
        elements: dict
        suboptions:
          device_list:
            description: WIP
            type: list
            elements: str
          run_tests:
            description: WIP
            type: list
            elements: str
          skip_tests:
            description: WIP
            type: list
            elements: str
  custom_catalog:
    description: WIP
    type: dict
    suboptions:
      input_dir:
        description: WIP
        type: str
  anta_logging:
    description: WIP
    type: dict
    suboptions:
      log_dir:
        description: WIP
        type: str
  anta_runner_settings:
    description: WIP
    type: dict
    suboptions:
      timeout:
        description: WIP
        type: float
        default: 30.0
      batch_size:
        description: WIP
        type: int
        default: 5
      dry_run:
        description: WIP
        type: bool
        default: false
      tags:
        description: WIP
        type: list
        elements: str
  report:
    description: WIP
    type: dict
    suboptions:
      fabric_data_output:
        description: WIP
        type: str
      csv_output:
        description: WIP
        type: str
      md_output:
        description: WIP
        type: str
      json_output:
        description: WIP
        type: str
      filters:
        description: WIP
        type: dict
        suboptions:
          hide_statuses:
            description: WIP
            type: list
            elements: str
            choices: ["success", "failure", "error", "skipped", "unset"]
seealso:
  - name: ANTA website
    description: Documentation for the ANTA test framework
    link: https://anta.arista.com
notes:
  - Documentation is a work in progress.
"""

EXAMPLES = r"""
- name: Run ANTA
  arista.avd.anta_workflow:
    device_list: "{{ ansible_play_hosts }}"
    anta_catalog:
      output_dir: "/my_avd_project/anta/catalogs"
      structured_config_dir: "/my_avd_project/intended/structured_configs"
      structured_config_suffix: ".yml"
      scope:
        boundary: "fabric"
        allow_bgp_external: true
        allow_bgp_vrfs: true
      filters:
        skip_tests:
          - VerifyNTP
    custom_catalog:
      input_dir: "/my_avd_project/anta/my_catalogs"
    anta_logging:
      log_dir: "/my_avd_project/anta/logs"
    report:
      fabric_data_output: "/my_avd_project/anta/reports/fabric_data.json"
      csv_output: "/my_avd_project/anta/reports/anta_results.csv"
      md_output: "/my_avd_project/anta/reports/anta_results.md"
      json_output: "/my_avd_project/anta/reports/anta_results.json"
      filters:
        hide_statuses:
          - success
  register: anta
  delegate_to: localhost
  run_once: true
"""
