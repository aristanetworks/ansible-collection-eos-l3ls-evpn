---
# This title is used for search results
title: arista.avd.eos_designs_documentation
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_designs_documentation

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.eos_designs_documentation` when using this plugin.

Generate AVD Fabric Documentation

## Synopsis

The `arista.avd.eos_designs_documentation` module is an Ansible Action Plugin providing the following capabilities:

- Generate fabric documentation using AVD facts and structured configuration files.
- Optionally include connected endpoints documentation.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>structured_config_dir</samp> | str | True | None |  | Path to directory containing files with AVD structured configurations. |
| <samp>structured_config_suffix</samp> | str | optional | yml |  | File suffix for AVD structured configuration files. |
| <samp>fabric_documentation_file</samp> | str | True | None |  | Path to output Markdown file. |
| <samp>mode</samp> | str | optional | 0o664 |  | Mode of output files. |
| <samp>fabric_documentation</samp> | bool | optional | True |  | Generate fabric documentation. |
| <samp>include_connected_endpoints</samp> | bool | optional | False |  | Include connected endpoints in fabric documentation. |
| <samp>topology_csv_file</samp> | str | True | None |  | Path to output topology CSV file. |
| <samp>topology_csv</samp> | bool | optional | False |  | Generate Topology CSV with all interfaces towards other devices. |
| <samp>p2p_links_csv_file</samp> | str | True | None |  | Path to output P2P links CSV file. |
| <samp>p2p_links_csv</samp> | bool | optional | False |  | Generate P2P links CSV with all routed point-to-point links between devices. |

## Examples

```yaml
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
```

## Authors

- Arista Ansible Team (@aristanetworks)
