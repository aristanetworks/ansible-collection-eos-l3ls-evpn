<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Contribution Guide for `eos_cli_config_gen` role

This document outlines the steps and checklist for contributing to the `eos_cli_config_gen` role under Arista AVD.

## Steps to add a new feature to eos_cli_config_gen role

### Schema creation

Add the schema for new feature as per EOS CLI to the appropriate schema fragments file in the `pyavd/_eos_cli_config_gen/schema/schema_fragments` directory or create a new schema file if adding a top-level feature.

#### Schema Guidelines

1. **Primary Key Placement:** For list-type data-models, place primary keys at the top, for readability.
2. **Key Naming:** 
- Follow EOS CLI for key names, when creating new schema keys.
- Use plural for keys that represent multiple elements (e.g., sample_policies).
3. **Descriptions:** 
- Only add descriptions to the keys when they provide additional context beyond the key name.
- Refer Arista docs for description content.
- Ensure all descriptions end with punctuation.
- Highlight the key names in description, like - `<key_name>`.
4. **Type Conversion:** Add `convert_types: [str]` for `type: int` keys.
5. **Defaults:** Avoid using `defaults` in eos_cli_config_gen.

### Creating Jinja2 Templates

Edit the appropriate Jinja2 templates in `pyavd/_eos_cli_config_gen/j2templates/eos` and `pyavd/_eos_cli_config_gen/j2templates/documentation` to generate the desired configuration and documentation.

Add new template if adding a top-level feature, also modify the `pyavd/_eos_cli_config_gen/j2templates/eos-device-documentation.j2` and `pyavd/_eos_cli_config_gen/j2templateseos-intended-config.j2` to add these new templates, trying to respect the order in the EOS CLI.

#### Jinja2 Templates Guidelines

1. **Code Indentation:** Keep less indented code to improve readability.
2. **Variable Naming:** Use meaningful variable names.
3. **Natural Sorting:** Use `arista.avd.natural_sort` for sorting the `for loops` after checking on EOS CLI.
4. **Defined Checks:** 
- Avoid `arista.avd.defined` check for parent keys when directly checking for child keys.
- No need to add `arista.avd.defined` check When using `arista.avd.default()` filter.
5. **Password Security:** Do not display passwords or password types in documentation template; use
`arista.avd.hide_passwords` filter.
6. **Config Order:** Ensure the order of configuration matches EOS CLI.
7. **Exclamation Marks:** Place exclamation marks `!` correctly as per the EOS running-config.
8. Along with EOS config template, update the documentation template as well (if required).
9. Implement only those commands whoes output is seen on EOS device running-config.

### Build Schemas and Documentation

Run `pre-commit run schemas --all` to re-generate the eos_cli_config_gen schema with any modifications. This command should be executed every time the schema is changed, even if only a description is updated. 
It also updates the documentation with new options.

### Add Molecule Tests

Add some molecule tests in the `ansible_collections/arista/avd/molecule/eos_cli_config_gen` scenario exercising the new knob configuration.

When marking any key as "deprecated," move the related tests to the `eos_cli_config_gen_deprecated_vars` molecule scenario and add any missing tests if necessary.

### Run Molecule Tests

Run `molecule converge -s eos_cli_config_gen` from the path `ansible_collections/arista/avd/` to execute the molecule tests locally and generate the new expected configuration and documentation for newly added test-cases.

### Run Pre-commit Checks

Run all pre-commit checks `pre-commit run --all` to ensure that all files added or modified are correctly following the coding standards and formatting rules.
Running these checks also ensures that the changes pass CI checks.

### Self Review The Changes

Before pushing the changes to GitHub, carefully review all modifications.
Confirm that all new features work as intended and that existing features are unaffected. Once satisfied, proceed to push the changes to the repository.
