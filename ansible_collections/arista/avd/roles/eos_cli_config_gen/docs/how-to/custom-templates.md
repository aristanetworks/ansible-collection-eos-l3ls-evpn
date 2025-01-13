---
# This title is used for search results
title: Custom Templates for eos_cli_config_gen
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Custom Templates for eos_cli_config_gen

With Custom Templates for the `eos_cli_config_gen` role, the user can create additional CLI configurations for features not covered by the built-in templates.

## Create a Custom Template

Custom templates should be written in Jinja2.

For details on how to create Jinja2 templates, see [Templating Jinja2](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_templating.html#templating-jinja2).

Custom templates can utilize variables defined by all the AVD variable definition mechanisms. For more details, see the explanation in [Custom Structured Configuration](../../../eos_designs/docs/how-to/custom-structured-configuration.md).

Suppose the required variable is not available by any of these mechanisms. In that case, it can be defined using a custom template in the `eos_designs` role. For more details see [Custom Templates for eos_designs](../../../eos_designs/docs/how-to/custom-templates.md).

At runtime, `eos_cli_config_gen` searches for custom templates in the following location, therefore, custom templates should be saved here:

```text
<path to users AVD implementation>/playbooks/templates/<template name>
```

The "templates" folder does not exist by default, so it must be created.

## Adding the Custom Template to group vars

For the custom template to be automatically discovered and rendered by `eos_cli_config_gen`, a variable that references the template should be added to the inventory group vars.

The format of the variable should be as follows:

```yaml
custom_templates:
  - custom_template_name.j2
```

For more details, see [Extensibility with Custom Templates](https://avd.sh/en/stable/roles/eos_cli_config_gen/docs/role-configuration.html#extensibility-with-custom-templates)

## Adding the Custom Template to the `eos_cli_config_gen` Role

Custom templates are rendered automatically when the `custom_templates` variable is set. The custom templates are always rendered *after* the builtin `eos_cli_config_gen` templates.
