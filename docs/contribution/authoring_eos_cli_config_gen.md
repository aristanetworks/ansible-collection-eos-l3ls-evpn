<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Contribution Guide for the `eos_cli_config_gen` role

This document outlines the steps and checklist for contributing to the `eos_cli_config_gen` role under Arista AVD.

## Steps to add a new feature to the `eos_cli_config_gen` role

1. Prepare development environment.
2. Create the schema.
3. Develop Jinja2 templates (eos and documentation).
4. Run pre-commit to build schema and templates
5. Validate With Molecule Tests
6. Update documentation as needed.
7. Run pre-commit checks to ensure compliance.
8. Review all changes before submission.
9. Raise a PR to the Arista AVD GitHub repository

### Prepare development environment

Follow the [Development Tooling Guide](https://avd.arista.com/stable/docs/contribution/development-tooling.html).

### Schema creation

Add the schema for new feature as per EOS CLI to the appropriate schema fragments file in the `python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments` directory or create a new schema file if adding a top-level feature.

Please refer to the schema documentation for details on the various keys in the schema: [Schema Documentation](https://avd.arista.com/stable/docs/contribution/input-variable-validation.html).

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
8. **Required:** Set `required: true` if the key must be provided to produce a valid configuration.

### Creating Jinja2 Templates

Edit the appropriate Jinja2 templates in `python-avd/pyavd/_eos_cli_config_gen/j2templates/eos` and `python-avd/pyavd/_eos_cli_config_gen/j2templates/documentation` to generate the desired configuration and documentation.

When adding a top-level feature, add a new Jinja2 template following the naming convention and modify the `python-avd/pyavd/_eos_cli_config_gen/j2templates/eos-intended-config.j2` and `python-avd/pyavd/_eos_cli_config_gen/j2templates/eos-device-documentation.j2` to add these new templates where relevant, in particular to respect EOS CLI order.

#### Jinja2 Templates Guidelines

1. **Code Indentation:** Keep less indented code to improve readability.
2. **Variable Naming:** Use meaningful variable names. Avoid short variables like `ei` for `ethernet_interface`
3. **Use AVD filters:** Use AVD filters for code optimization - [AVD Filters](https://avd.arista.com/5.1/docs/plugins/Filter_plugins/add_md_toc.html).
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

### Run pre-commit to build schemas and documentation

Run `pre-commit run --all`, this will trigger recompiling the schemas and the templates you have created.

!!! Note

    When using Ansible (either through molecule or from a test repo), AVD is able to detect when it is running from source, and recompiles schemas and templates automatically during the "Verify Requirements" step, as outlined in the [Development Tooling Guide](https://avd.arista.com/stable/docs/contribution/development-tooling.html).

    However, if you are using pyavd or need to manually recompile the schemas and templates for any other reason, you can run the following commands:

    `pre-commit run schemas --all` to regenerate the eos_cli_config_gen schema.
    `pre-commit run templates --all` to regenerate the templates.

    These commands should be executed whenever the schema or templates are modified, even if only a description is updated.

### Validate Changes and Test Configurations

1. Add some molecule tests in the `ansible_collections/arista/avd/molecule/eos_cli_config_gen` scenario or other relevant molecule scenario exercising the new knob configuration.
2. Update the `host_vars` files:
   - Modify or add the `molecule/<scenario_name>/host_vars/hostX/<key_name>.yml` file to include the new configuration knobs.
   - If multiple files are required to cover all the test cases:
     - Add the additional test cases to the next host directory, e.g., `host_vars/host2/<key_name>.yml`, `host_vars/host3/<key_name>.yml`, etc.
     - Ensure each file represents unique scenarios or configurations to validate different combinations.
   - Ensure that the new keys are thoroughly tested with various valid values and edge cases.
3. When marking any key as "deprecated", move the related tests to the `eos_cli_config_gen_deprecated_vars` molecule scenario and add any missing tests if necessary.
4. Run `molecule converge -s <scenario_name>` from the path `ansible_collections/arista/avd/` to execute the molecule tests locally and generate the new expected configuration and documentation for newly added test-cases.
5. To execute all the molecule scenarios, run `make refresh-facts` from the path `ansible_collections/arista/avd/molecule` and verify the tests.
6. Check the PyAVD test coverage report by running `tox -e coverage,report` and work on improving the coverage where possible.
7. Test the generated configuration using eAPI or CloudVision in a relevant lab, if available, to ensure it works as intended.

!!! Note

    Running `make refesh-facts` can be long and it can be preferable to rerun only the required scenarios using `molecule converge -s <scenario_name>` multiple times.

### Update Documentation

If the proposed feature requires any changes to the documentation, make sure to update it accordingly.

### Run Pre-commit Checks

Run all pre-commit checks `pre-commit run --all` to ensure that all files added or modified are correctly following the coding standards and formatting rules. Running these checks also ensures that the changes pass CI checks.

!!! Note

    Breaking changes should be documented in the release notes / porting guide. Please advise a maintainer on the PR.

### Self Review The Changes

1. Before pushing the changes to GitHub, carefully review all the modifications.
2. Confirm that all new features work as intended and that existing features are unaffected.
3. Once satisfied, proceed to push the changes to the repository.

### Raise a PR to the Arista AVD GitHub repository

1. After completing the self-review, raise a pull request (PR) to the Arista AVD GitHub repository for further review and integration.
2. Use draft PRs when the changes are not ready for review.
3. Tag maintainers with questions, even after pushing changes, for clarity and guidance, or discuss in the related issue if needed.

## Checklist to review an eos_cli_config_gen Pull Request

- [ ] Check that all the CI checks are passing.
- [ ] If the PR addresses an issue raised in the repository, confirm that the issue is fully resolved by the PR.
- [ ] Refer to the Arista EOS documentation for a deeper understanding of the proposed feature.
- [ ] Tag maintainers with questions or concerns regarding the proposed changes.
- [ ] Verify that the schema adheres to EOS CLI and all relevant guidelines mentioned above.
- [ ] Ensure that the min/max and valid-values are specified in the schema if they are defined in the EOS CLI.
- [ ] Ensure that Jinja2 templates follow all the guidelines mentioned above.
- [ ] Check that the template generates valid configuration and documentation, maintaining the same configuration order and indentation as EOS CLI.
- [ ] Check out the PR in a local IDE using the instructions in the PR comment and run all tests to ensure functionality.
- [ ] Test the generated configuration via eAPI or CloudVision in a relevant lab, if available. Otherwise, mention in your review comment that lab verification was not possible.
- [ ] Add inline suggestions whenever possible, and if providing code suggestions, test them locally to ensure they work as intended.
- [ ] Check that the molecule tests are added for the new feature.
- [ ] If any keys are marked as deprecated, ensure that the associated tests are moved to the `eos_cli_config_gen_deprecated_vars` scenario.
- [ ] If the proposed feature requires any changes to the documentation, ensure that it is updated accordingly.
- [ ] Approve the PR if everything looks good.
