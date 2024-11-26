<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Contribution Guide for the `eos_cli_config_gen` role

This document outlines the steps and checklist for contributing to the `eos_cli_config_gen` role under Arista AVD.

## Steps to add a new feature to the `eos_cli_config_gen` role

### Prepare development environment

Follow the [Development Tooling Guide](https://avd.arista.com/stable/docs/contribution/development-tooling.html).

### Schema creation

Add the schema for new feature as per EOS CLI to the appropriate schema fragments file in the `python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments` directory or create a new schema file if adding a top-level feature.

Please refer to the schema documentation for details on the various keys in the schema: [Schema Documentation](https://avd.arista.com/5.0/docs/contribution/input-variable-validation.html#schema-details).

#### Schema Guidelines

1. **Primary Key Placement:** For list-type data-models, place primary keys at the top, for readability.
2. **Key Naming:**
    - Follow EOS CLI for key names, when creating new schema keys.
    - Use plural for keys that represent multiple elements (e.g., sample_policies).
3. **Descriptions:**
    - Only add descriptions to the keys when they provide additional context beyond the key name.
    - Refer Arista documentation for description content.
    - Ensure all descriptions end with punctuation.
    - Highlight the key names in description, like - `<key_name>`.
4. **Type Conversion:**
    - Add `convert_types: [str]` for `type: int` keys.
    - Add `convert_types: [int]` for `type: str` if it can be numeric.
5. **Defaults:** Avoid using `default` in eos_cli_config_gen.
6. **Min/Max:** Specify min/max values in the schema if they are defined in the EOS CLI. Make sure to check on different hardware platforms.
7. **Valid_Values:** Specify valid options in the schema as per the EOS CLI and ensure compatibility across different hardware platforms.

### Creating Jinja2 Templates

Edit the appropriate Jinja2 templates in `pyavd/_eos_cli_config_gen/j2templates/eos` and `pyavd/_eos_cli_config_gen/j2templates/documentation` to generate the desired configuration and documentation.

When adding a top-level feature, add a new jinja2 template following the naming convention and modify the `pyavd/_eos_cli_config_gen/j2templates/eos-intended-config.j2` and `pyavd/_eos_cli_config_gen/j2templates/eos-device-documentation.j2` to add these new templates where relevant, in particular to respect EOS CLI order.

#### Jinja2 Templates Guidelines

1. **Code Indentation:** Keep less indented code to improve readability.
2. **Variable Naming:** Use meaningful variable names. Avoid short variables like `ei` for `ethernet_interface`
3. **Use AVD filters:** Use AVD filters for code optimization - [AVD Filters](https://avd.arista.com/5.0/docs/plugins/Filter_plugins/add_md_toc.html).
4. **Natural Sorting:** Use `arista.avd.natural_sort` for sorting the `for loops` after checking on EOS CLI.
5. **Defined Checks:**
    - Avoid `arista.avd.defined` check for parent keys when directly checking for child keys.
    - Avoid `arista.avd.defined` check for primary and required keys.
    - Avoid`arista.avd.defined` check when using `arista.avd.default()` and `arista.avd.natural_sort` filters.
6. **Password Security:** Avoid displaying passwords in the documentation template and use the `arista.avd.hide_passwords` filter to hide it.
7. **Config Order:** Ensure the order and indentation of configuration matches EOS CLI.
8. **Exclamation Marks:** Place exclamation marks `!` correctly as per the EOS running-config.
9. Along with EOS config template, update the documentation template as well (if required).
10. Implement only commands visible in `show running-config all` of the EOS device. We should not hide config if given by the user.
11. Validate the template using j2lint tool, run `pre-commit run j2lint --all`.

### Build Schemas and Documentation

Run `pre-commit run schemas --all` to re-generate the eos_cli_config_gen schema with any modifications. This command should be executed every time the schema is changed, even if only a description is updated.
It also updates the documentation with new options.

### Add Molecule Tests

Add some molecule tests in the `ansible_collections/arista/avd/molecule/eos_cli_config_gen` scenario exercising the new knob configuration.

When marking any key as "deprecated", move the related tests to the `eos_cli_config_gen_deprecated_vars` molecule scenario and add any missing tests if necessary.

### Run Molecule Tests

Run `molecule converge -s eos_cli_config_gen` from the path `ansible_collections/arista/avd/` to execute the molecule tests locally and generate the new expected configuration and documentation for newly added test-cases.

Check the PyAVD test coverage report by running `tox -e coverage,report` and work on improving the coverage where possible.

### Update Documentation

If the proposed feature requires any changes to the documentation, make sure to update it accordingly.
If there are any breaking changes introduced, document them in the porting guide.

### Run Pre-commit Checks

Run all pre-commit checks `pre-commit run --all` to ensure that all files added or modified are correctly following the coding standards and formatting rules.
Running these checks also ensures that the changes pass CI checks.

### Self Review The Changes

Before pushing the changes to GitHub, carefully review all the modifications.
Confirm that all new features work as intended and that existing features are unaffected. Once satisfied, proceed to push the changes to the repository.

## Checklist to review an eos_cli_config_gen PR

1. Check that all the CI checks are passing.
2. If the PR addresses an issue raised in the repository, confirm that the issue is fully resolved by the PR.
3. Refer to the Arista documentation for a deeper understanding of the proposed feature.
4. Verify that the schema adheres to EOS CLI and all relevant guidelines mentioned above.
5. Ensure that the min/max and valid-values are specified in the schema if they are defined in the EOS CLI.
6. Ensure that Jinja2 templates follow all the guidelines mentioned above.
7. Check that the template generates valid configuration and documentation, maintaining the same configuration order and indentation as EOS CLI.
8. Check out the PR in a local IDE using the instructions in the PR comment and run all tests to ensure functionality.
9. Test the generated configuration through EAPI or CVP in the ATD lab.
10. If providing code suggestions, test them locally to ensure that your proposals work as intended.
11. Check that the molecule tests are added for the new feature.
12. If any keys are marked as deprecated, ensure that the associated tests are moved to the `eos_cli_config_gen_deprecated_vars` scenario.
13. If the proposed feature requires any changes to the documentation, ensure that it is updated accordingly.
14. Approve the PR if everything looks good.
