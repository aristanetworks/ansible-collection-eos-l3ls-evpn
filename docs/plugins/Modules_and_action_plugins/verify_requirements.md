---
# This title is used for search results
title: arista.avd.verify_requirements
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# verify_requirements

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.verify_requirements` when using this plugin.

Verify Python requirements when running AVD

## Synopsis

The `arista.avd.verify_requirements` module is an Ansible Action Plugin providing the following capabilities:

- Display the current running version of the collection
- Given a list of python requirements, verify if the installed libraries match these requirements
- Validate the ansible version against collection requirements
- Validate the collection requirements against the collection requirements
- Validate the running python version
- Emit deprecation warnings for Python and Ansible versions

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>requirements</samp> | list | True | None |  | List of strings of python requirements with pip file syntax. |
| <samp>avd_ignore_requirements</samp> | bool | False | False |  | Boolean, if set to True, the play does not stop if any requirement error is detected. |

## Examples

```yaml
- name: Verify collection requirements
  arista.avd.verify_requirements:
    requirements:
      - Jinja2 >= 2.9
      - paramiko == 2.7.1
  check_mode: false
  run_once: true
```

## Authors

- Arista Ansible Team (@aristanetworks)
