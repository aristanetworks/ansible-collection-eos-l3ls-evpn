# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# def arista.avd.add_md_toc
#


from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.add_md_toc"

try:
    from pyavd.j2filters import add_md_toc
except ImportError as e:
    add_md_toc = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )

DOCUMENTATION = r"""
---
name: add_md_toc
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "3.2"
requirements:
  - md_toc
short_description: Parse the input Markdown and add a Table of Contents between the toc_markers.
description:
  - The filter is used in `arista.avd.eos_designs` to create a table of contents for Fabric Documentation.
  - The filter is also used in `arista.avd.eos_cli_config_gen` to create a table of contents for Device Documentation.
positional: _input
options:
  _input:
    description: Markdown to process.
    type: string
    required: true
  skip_lines:
    type: integer
    description: Skip the first x lines when parsing the input Markdown.
    default: 0
  toc_levels:
    type: integer
    description: How many levels of headings will be included in the TOC.
    default: 3
  toc_marker:
    type: string
    description: TOC will be inserted or updated between two of markers in the input Markdown.
    default: "<!-- toc -->"
"""

EXAMPLES = r"""
---
tasks:
- name: Generate fabric documentation
  run_once: true
  delegate_to: localhost
  check_mode: false
  copy:
    content: "{{ lookup('template','documentation/fabric-documentation.j2') | arista.avd.add_md_toc(skip_lines=3) }}"
    dest: "{{ fabric_dir }}/{{ fabric_name }}-documentation.md"
    mode: "0o664"
"""

RETURN = r"""
---
_value:
  description: Markdown with TOC inserted between the toc_markers.
  type: string
"""


class FilterModule:
    def filters(self) -> dict:
        return {"add_md_toc": wrap_filter(PLUGIN_NAME)(add_md_toc)}
