# Copyright (c) 2022-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: verify_requirements
version_added: "4.0.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Verify Python requirements when running AVD
description: |-
  The `arista.avd.verify_requirements` module is an Ansible Action Plugin providing the following capabilities:

  - Display the current running version of the collection
  - Given a list of python requirements, verify if the installed libraries match these requirements
  - Validate the ansible version against collection requirements
  - Validate the collection requirements against the collection requirements
  - Validate the running python version
  - Emit deprecation warnings for Python and Ansible versions
options:
  requirements:
    description:
      - List of strings of python requirements with pip file syntax.
    required: true
    type: list
    elements: str
  avd_ignore_requirements:
    description:
      - Boolean, if set to True, the play does not stop if any requirement error is detected.
    required: false
    default: false
    type: bool
"""

EXAMPLES = r"""
- name: Verify collection requirements
  arista.avd.verify_requirements:
    requirements:
      - Jinja2 >= 2.9
      - paramiko == 2.7.1
  check_mode: false
  run_once: true
"""
