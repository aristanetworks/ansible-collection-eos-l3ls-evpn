# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: set_vars
version_added: "4.0.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Set vars as ansible_facts.
description:
  - Set vars as ansible_facts.
  - Ansible will copy these into vars in the global namespace as well.
  - Arguments are treated as one dict so all arguments will be set as vars.
options: {}
"""

EXAMPLES = r"""
- name: Remove avd_switch_facts
  arista.avd.set_vars:
    avd_switch_facts: null
  run_once: true
  check_mode: false
"""
