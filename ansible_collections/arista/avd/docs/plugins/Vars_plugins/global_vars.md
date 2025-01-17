---
# This title is used for search results
title: arista.avd.global_vars
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# global_vars

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.global_vars` when using this plugin.

Variable plugins to allow loading global_vars with less precedence than group_vars or host_vars

## Synopsis

Loads variables from variable files specified in ansible.cfg or in the environment variable.
Assign the loaded variables to the &#39;all&#39; inventory group.
Files are restricted by extension to one of .yaml, .json, .yml, or no extension.
Hidden files (starting with &#39;.&#39;) and backup files (ending with &#39;~&#39;) are ignored.
Only applies to inventory sources that are existing paths.

### ansible.cfg only example

1. Enable the plugin in `ansible.cfg` - DO NOT REMOVE `host_group_vars`.

    ```ini
    [defaults]
    vars_plugins_enabled = arista.avd.global_vars, host_group_vars
    [vars_global_vars]
    paths = ../relative/path/to/my/global/vars/file/or/dir
    ```

2. Run your playbook

    ```sh
    ansible-playbook -i inventory.yml playbook.yml
    ```

### ansible.cfg + environment variable example

1. Enable the plugin in `ansible.cfg` - DO NOT REMOVE `host_group_vars`.

    ```ini
    [defaults]
    vars_plugins_enabled = arista.avd.global_vars, host_group_vars
    ```

2. Run your playbook

    ```sh
    ARISTA_AVD_GLOBAL_VARS_PATHS=../relative/path/to/my/global/vars/file/or/dir ansible-playbook -i inventory.yml playbook.yml
    ```

## Requirements

The below requirements are needed on the host that executes this module.

- This plugin should run at the `inventory` stage (default) before all other variable plugins to inject the variables before any group and host vars.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>paths</samp> | list | True | None |  | List of relative paths relative to the inventory file.<br>If path is a directory, all the valid files inside are loaded alphabetically.<br>If the environment variable is set, it takes precedence over ansible.cfg. |
| <samp>stage</samp> | any | optional | inventory | Valid values:<br>- <code>inventory</code> | The stage during which executing the plugin. It could be &#39;inventory&#39; or &#39;task&#39;<br>Given the expected usage of this plugin at the beginning of the run. It is hard-coded to &#39;inventory&#39; |
| <samp>_valid_extensions</samp> | list | optional | ['.yml', '.yaml', '.json'] |  | Check all of these extensions when looking for &#39;variable&#39; files, which should be YAML, JSON, or vaulted versions.<br>This affects vars_files, include_vars, inventory, and vars plugins, among others. |

## Authors

- Arista Ansible Team (@aristanetworks)
