# Copyright (c) 2021-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: eos_designs_structured_config
version_added: "4.0.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Generate AVD EOS Designs structured configuration
description: |-
  The `arista.avd.eos_designs_structured_config` module is an Ansible Action Plugin providing the following capabilities:

  - Validates input variables according to eos_designs schema
  - Generates structured configuration
  - Optionally run any custom jinja2 YAML templates and merge result onto structured configuration
  - Optionally run jinja2 templating the generated structured configuration
  - Optionally write structured configuration to a JSON or YAML file
  - Return structured configuration as "ansible_facts"
options:
  eos_designs_custom_templates:
    description: List of dicts for Jinja2 templates to be run after generating the structured configuration
    required: false
    type: list
    elements: dict
    suboptions:
      template:
        description: |
          Template file.
        required: true
        type: str
      options:
        description: Template options
        required: false
        type: dict
        suboptions:
          list_merge:
            description: Merge strategy for lists
            required: false
            default: 'append'
            type: str
          strip_empty_keys:
            description:
              - Filter out keys from the generated output if value is null/none/undefined
              - Only applies to templates.
            required: false
            default: true
            type: bool
  dest:
    description:
      - Destination path. If set, the output facts will also be written to this path.
      - Autodetects data format based on file suffix. '.yml', '.yaml' -> YAML, default -> JSON
    required: false
    type: str
  mode:
    description: File mode (ex. "0o664") for dest file. See 'ansible.builtin.copy' module for details.
    required: false
    type: str
  template_output:
    description:
      - If true, the output data will be run through another jinja2 rendering before returning.
      - This is to resolve any input values with inline jinja using variables/facts set by the input templates.
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
- name: Generate device configuration in structured format
  arista.avd.eos_designs_structured_config:
    templates:
      - template: "custom_templates/custom_feature1.j2"
      - template: "custom_templates/custom_feature2.j2"
        options:
          list_merge: replace
          strip_empty_keys: false
  check_mode: false
  changed_when: false
"""
