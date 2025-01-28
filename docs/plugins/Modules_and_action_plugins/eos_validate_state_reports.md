---
# This title is used for search results
title: arista.avd.eos_validate_state_reports
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_validate_state_reports

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.eos_validate_state_reports` when using this plugin.

Generates validation reports for the eos_validate_state role

## Synopsis

The `arista.avd.eos_validate_state_reports` module is an Ansible Action Plugin designed to generate
validation reports from the test results produced by the ANTA test framework.

This plugin requires a JSON file for each host in the Ansible play, containing all test results. The JSON file
is created automatically by the `eos_validate_state_runner` plugin and is saved in the test results directory
with the following naming convention `&lt;inventory_hostname&gt;-results.json`.

The plugin offers the following functionalities:

- It aggregates all test results from every host in the Ansible play and generates a CSV report.
- It produces a detailed Markdown report with various sections presenting key statistics derived from the results.
- The design allows for easy extension to support additional report formats in the future.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>validation_report_csv</samp> | bool | optional | True |  | Indicates whether a CSV report should be generated. |
| <samp>validation_report_md</samp> | bool | optional | True |  | Indicates whether a Markdown report should be generated. |
| <samp>only_failed_tests</samp> | bool | optional | False |  | Determines if the generated reports should include only the failed tests. |
| <samp>csv_report_path</samp> | str | optional | None |  | The absolute path where the CSV report will be saved.<br>Required if `validation_report_csv` is set to `True`. |
| <samp>md_report_path</samp> | str | optional | None |  | The absolute path where the Markdown report will be saved.<br>Required if `validation_report_md` is set to `True`. |
| <samp>test_results_dir</samp> | any | optional | None |  | The directory where the test results JSON file for each host will be saved. |
| <samp>cprofile_file</samp> | any | optional | None |  | The filename for storing cProfile data, useful for debugging performance issues.<br>Be aware that enabling cProfile can affect performance, so use it only for troubleshooting. |

## Notes

- Enabling the cProfile feature for performance profiling may impact the plugin&#39;s performance, especially in production environments.
- Hosts with `is_deployed` is False are automatically skipped, and no test results are processed for these hosts.

## See Also

- ANTA website: [https://anta.arista.com](https://anta.arista.com)<br>Documentation for the ANTA test framework

## Examples

```yaml
- name: Generate validation reports from ANTA test results
  arista.avd.eos_validate_state_reports:
    csv_report_path: "/my_avd_project/reports/my-fabric-state.csv"
    md_report_path: "/my_avd_project/reports/my-fabric-state.md"
    validation_report_csv: true
    validation_report_md: true
    only_failed_tests: false
  delegate_to: localhost
  run_once: true
```

## Authors

- Arista Ansible Team (@aristanetworks)
