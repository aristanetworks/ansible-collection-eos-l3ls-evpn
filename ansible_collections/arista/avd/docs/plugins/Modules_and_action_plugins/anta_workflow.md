---
# This title is used for search results
title: arista.avd.anta_workflow
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# anta_workflow

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.anta_workflow` when using this plugin.

!!! warning "This module is in **preview** mode"
    This module is not guaranteed to have a backwards compatible interface.

Uses ANTA from Ansible

## Synopsis

The `arista.avd.anta_workflow` module is an Ansible Action Plugin to leverage the ANTA test framework to validate that the generated structured configurations by AVD are applied to the devices and that the deployed network is working correctly. It can also be used to execute user-defined ANTA test catalogs in conjunction with the Ansible inventory, providing similar functionality and options as the ANTA CLI while benefiting from Ansible&#39;s inventory management capabilities.

The plugin offers the following capabilities:
    - Generating a per-device test catalog based on the AVD structured_config.
    - WIP

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>device_list</samp> | list | True | None |  | List of devices to run ANTA tests against. These devices must be defined in the Ansible inventory. |
| <samp>anta_catalog</samp> | dict | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;output_dir</samp> | str | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config_dir</samp> | str | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config_suffix</samp> | str | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;scope</samp> | dict | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundary</samp> | str | optional | unlimited | Valid values:<br>- <code>unlimited</code><br>- <code>fabric</code><br>- <code>dc</code><br>- <code>pod</code><br>- <code>rack</code> | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_bgp_external</samp> | bool | optional | False |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_bgp_vrfs</samp> | bool | optional | False |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;filters</samp> | list | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;device_list</samp> | list | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;run_tests</samp> | list | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;skip_tests</samp> | list | optional | None |  | WIP |
| <samp>custom_catalog</samp> | dict | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;input_dir</samp> | str | optional | None |  | WIP |
| <samp>anta_logging</samp> | dict | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;log_dir</samp> | str | optional | None |  | WIP |
| <samp>anta_runner_settings</samp> | dict | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp> | float | optional | 30.0 |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;batch_size</samp> | int | optional | 5 |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;dry_run</samp> | bool | optional | False |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;tags</samp> | list | optional | None |  | WIP |
| <samp>report</samp> | dict | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;fabric_data_output</samp> | str | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;csv_output</samp> | str | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;md_output</samp> | str | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;json_output</samp> | str | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;filters</samp> | dict | optional | None |  | WIP |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hide_statuses</samp> | list | optional | None | Valid values:<br>- <code>success</code><br>- <code>failure</code><br>- <code>error</code><br>- <code>skipped</code><br>- <code>unset</code> | WIP |

## Notes

- Documentation is a work in progress.

## See Also

- ANTA website: [https://anta.arista.com](https://anta.arista.com)<br>Documentation for the ANTA test framework

## Examples

```yaml
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
```

## Authors

- Arista Ansible Team (@aristanetworks)
