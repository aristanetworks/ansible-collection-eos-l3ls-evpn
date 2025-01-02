---
# This title is used for search results
title: arista.avd.eos_designs_structured_config
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_designs_structured_config

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.eos_designs_structured_config` when using this plugin.

Generate AVD EOS Designs structured configuration

## Synopsis

The `arista.avd.eos_designs_structured_config` module is an Ansible Action Plugin providing the following capabilities:

- Validates input variables according to eos_designs schema
- Generates structured configuration
- Optionally run any custom jinja2 YAML templates and merge result onto structured configuration
- Optionally run jinja2 templating the generated structured configuration
- Optionally write structured configuration to a JSON or YAML file
- Return structured configuration as &#34;ansible_facts&#34;

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>eos_designs_custom_templates</samp> | list | False | None |  | List of dicts for Jinja2 templates to be run after generating the structured configuration |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;template</samp> | str | True | None |  | Template file. |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;options</samp> | dict | False | None |  | Template options |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list_merge</samp> | str | False | append |  | Merge strategy for lists |
| <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strip_empty_keys</samp> | bool | False | True |  | Filter out keys from the generated output if value is null/none/undefined<br>Only applies to templates. |
| <samp>dest</samp> | str | False | None |  | Destination path. If set, the output facts will also be written to this path.<br>Autodetects data format based on file suffix. &#39;.yml&#39;, &#39;.yaml&#39; -&gt; YAML, default -&gt; JSON |
| <samp>mode</samp> | str | False | None |  | File mode (ex. &#34;0o664&#34;) for dest file. See &#39;ansible.builtin.copy&#39; module for details. |
| <samp>template_output</samp> | bool | False | None |  | If true, the output data will be run through another jinja2 rendering before returning.<br>This is to resolve any input values with inline jinja using variables/facts set by the input templates. |
| <samp>validation_mode</samp> | str | False | error | Valid values:<br>- <code>error</code><br>- <code>warning</code> | Run validation in either &#34;error&#34; or &#34;warning&#34; mode.<br>Validation will validate the input variables according to the schema.<br>During validation, messages will be generated with information about the host(s) and key(s) which failed validation.<br>validation_mode:error will produce error messages and fail the task.<br>validation_mode:warning will produce warning messages. |
| <samp>cprofile_file</samp> | str | False | None |  | Filename for storing cprofile data used to debug performance issues.<br>Running cprofile will slow down performance in it self, so only set this while troubleshooting. |

## Examples

```yaml
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
```

## Authors

- Arista Ansible Team (@aristanetworks)
