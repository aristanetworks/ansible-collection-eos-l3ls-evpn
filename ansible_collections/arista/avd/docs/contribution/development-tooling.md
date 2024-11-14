<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Development Tooling

- To assist the AVD development community, we provide guidance to develop with two primary methods: VSCode dev containers or local Python environment.
  - You may also choose your own development methodology, however we may not be able to provide assistance in a timely manner.
- This guide provides additional information about the development tools leveraged in the project: pre-commit, Molecule and ansible-test.
- Please report any issues and optimization suggestions regarding the development workflow via [Github discussions board](https://github.com/aristanetworks/avd/discussions).

!!! note
    The examples in this guide assume a Linux or macOS based operating system, however, it does not go into details on how to install common development tooling as this differs between operating systems.

## Development environments

Before setting up your development environment, create a fork of the [GitHub AVD project](https://github.com/aristanetworks/avd) and clone your fork to a local directory.

Recommended directory structure:

```shell
├── avd <- Clone of forked avd GitHub repository
└── avd-venv <- Python virtual environment, applicable only when leveraging a Local Python environment.
```

### VSCode Dev Containers

To facilitate onboarding of development the AVD project builds [Dev Containers](../containers/overview.md) with all the required tools to get started.
Before you can leverage the VSCode Dev Container ensure to have the following tools installed on your workstation:

- [Docker](https://docs.docker.com/engine/install/).
- [Visual Studio Code](https://code.visualstudio.com/) and the [Dev Container](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.

The AVD repository contains a devcontainer definition at the root of the project.
This will be executed automatically by VSCode by following these steps:

1. Start VSCode on your worksation
2. Select "File/Open Folder..." and open the cloned avd GitHub repository (your fork).
3. A pop up will appear with "Folder contains a Dev Container configuration file. Reopen folder to develop in a container." Select "Reopen in Container".
4. VScode will re-open and start in the AVD Dev Container.

!!! Warning
    Note, at this time the AVD Dev Container doesn't support docker-in-docker, therefore some of the tests that rely on Docker can not be performed locally. Please rely on the CI pipeline results and logs for troubleshooting.

### Local Python environments

Developing with your local Python environment requires you to configure and install the AVD project development tools and dependencies installed on your workstation:

- [Python 3.10](https://docs.python.org/) or later and [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html).
- Additional AVD Python package dependencies.
- [Make](https://www.gnu.org/software/make/manual/make.html): Leveraged for automating software building and test procedures.
- [Docker](https://docs.docker.com/engine/install/) (Optional): Some of the tests require docker to be executed locally and useful when troubleshooting failures of the CI pipeline.

Recommended steps with Python virtual environment:

1. Create and activate a Python virtual environment.
2. Install Python requirements located in the AVD repository: [requirements-dev.txt](https://github.com/aristanetworks/avd/blob/devel/ansible_collections/arista/avd/requirements-dev.txt).

!!! note
    Ensure the virtual environment is located outside of the AVD project directory.

```shell
# Create a Python virtual environment `python -m venv <virtual-environment-name>`.
python3 -m venv avd-venv

# Activate Python virtual environment `source <virtual-environment-name>/bin/activate`.
source avd-venv/bin/activate

# Install AVD project requirements-dev.txt and requirements.txt in your Python Virtual environment.
# The installation _must_ be performed from the root of the cloned avd repository.
cd avd
# Requirements files are located in `ansible_collections/arista/avd` of the avd repository.
pip3 install -r ansible_collections/arista/avd/requirements-dev.txt --upgrade
```

!!! note
    It is important to confirm the Python interpreter Ansible is using.
    You may be required to set `ansible_python_interpreter` in your Ansible inventory.
    For more information consult with the [Ansible documentation](https://docs.ansible.com/ansible/latest/reference_appendices/python_3_support.html#using-python-3-on-the-managed-machines-with-commands-and-playbooks).

## Running from source

Ansible-AVD is able to detect when it is running from source, and will prepend the Python Path with the path to the PyAVD source. This ensures that running Ansible-AVD from source will also use PyAVD from the same source.

The modification of the Python Path is logged as a warning in the Ansible output.

TODO: Add picture.

When running from source, the `verify_requirements` action will check if any schema fragment or templates has changed locally and if so, will recompile on the fly either or both as
required for `eos_cli_config_gen` and `eos_designs`, allowing a seamless development workflow while using Ansible.
When using pyavd, it is required to run pre-commit to achieve the same.

## Pre-commit

- [pre-commit](https://github.com/aristanetworks/avd/blob/devel/.pre-commit-config.yaml) can run standard hooks on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements.
- Pointing these issues out before code review allows a code reviewer to focus on the architecture of a change while not wasting time with trivial style nitpicks.
- Additionally, the AVD project leverages pre-commit hooks to build and update the AVD schemas, templates and documentation artifacts.

### Install pre-commit hook

Configure pre-commit git hook, to automatically run pre-commit. This is optional, but highly recommended!

```shell
# Change to directory to your cloned avd repository.
cd avd

# Install pre-commit hooks to run automatically.
pre-commit install
```

### Run pre-commit manually

To run `pre-commit` manually before you commit, use this command:

```shell
# Change to directory to your cloned avd repository.
cd avd

# Run pre-commit hooks on all staged files.
# The command will automatically detect changed files using `git status` and run tests according to their type.
pre-commit run

# Run pre-commit hooks on all un-staged and staged files.
pre-commit run --all

# Run specific pre-commit schemas hook on all un-staged and staged files.
pre-commit run schemas --all
```

!!! note
    This process is also implemented in the project CI to ensure code quality and compliance.
    All pre-commit checks must pass, therefore we highly recommend running this workflow before committing changes!

    Pre-commit will fail if any files are changed by the pre-commit hooks. Make sure to review the changes, commit them and rerun pre-commit.

## Molecule

The [Molecule](https://ansible.readthedocs.io/projects/molecule/) project is designed to aid in developing and testing of Ansible roles.

The AVD project leverages Molecule for:

- Static integration test on the following Ansible roles:
  - `eos_designs`
  - `eos_cli_config_gen`
  - `eos_validate_state`
  - `eos_config_deploy_cvp`
  - `dhcp_provisioner` (requires docker)
- End-to-end systems integration tests on the following CloudVision role and module:
  - `cv_deploy`
  - `cv_workflow`

The Molecule scenarios are located under the `molecule` directory at the root of the collection (`ansible_collections/arista/avd/molecule`).

The directory name of each Molecule scenario folder is used as the `--scenario-name` when executing Molecule, i.e: `eos_cli_config_gen`, `eos_designs_unit_tests`.

### Executing Molecule with makefile method

To run the Molecule tests locally to generate the new expected configuration and documentation leverage Makefile located in the `ansible_collections/arista/avd/molecule` directory.

The Makefile supports the following targets:

- `help`: Display available make target and descriptions.
- `converge`: Execute molecule "converge" sequence. Specify scenario name with `MOLECULE=<scenario_name>` (default: `eos_cli_config_gen`) and Ansible options with `ANSIBLE_OPTIONS=<options>` (default: `--forks 5`).
  - This is the recommended way for development, as it is quicker and does not execute idempotency checks.
- `test`: Execute molecule "test" sequence. Specify scenario name with `MOLECULE=<scenario_name>` (default: `eos_cli_config_gen`) and Ansible options with `ANSIBLE_OPTIONS=<options>` (default: `--forks 5`).
  - This is executed as part of the CI and tests for idempotency.
- `refresh-facts`: Run all "eos_designs" and "eos_cli_config_gen" [molecule scenarios](https://github.com/aristanetworks/avd/blob/devel/ansible_collections/arista/avd/molecule/MOLECULE_SCENARIOS.txt).

!!! info
    `make refresh-facts` can be useful when you change common template or structured configuration output.
    Note that it will take a significant amount of local resources and several minutes/hours to execute.

In the majority of new features or bug fixes, the process is the following:

1. Update scenario inventory when required. It is ok to extend an existing host to cover a new test. When in doubt, consult with a maintainer.
2. Update group and host variables in the scenario and ensure to cover all use cases of the feature.
3. Run `make converge` target within the `molecule` directory to generate artifacts. Examples:

    ```shell
    # Change to molecule directory
    cd ansible_collections/arista/avd/molecule

    # Run eos_designs_unit_tests scenario to generate artifacts
    make converge MOLECULE=eos_designs_unit_tests

    # Run eos_designs_unit_tests scenario with verbosity `-vvv` and max forks of 10 `--forks 10`.
    make converge MOLECULE=eos_designs_unit_tests ANSIBLE_OPTIONS="-vvv --forks 10"

    # Run eos_cli_config_gen scenario with limit.
    make converge ANSIBLE_OPTIONS="--limit logging"
    ```

4. Review generated artifacts and test results on an EOS device to confirm syntax and working configuration.
5. Commit generated artifacts.

!!! info
    Molecule scenarios are also executed in the project CI to ensure code quality and compliance and tested against various versions of `ansible-core` and other Python dependencies.

### Executing Molecule with advanced CLI syntax

You may also run Molecule by leveraging its CLI syntax directly from the root of the collection path: `ansible_collections/arista/avd`.

Examples:

```shell
# Change to root collection directory
cd ansible_collections/arista/avd

# Run eos_cli_config_gen scenario
molecule converge -s eos_cli_config_gen

# Run eos_cli_config_gen scenario limiting to "logging" host only
molecule converge -s eos_cli_config_gen -- --limit logging

# Run eos_designs unit_test scenario with verbosity
molecule converge -s eos_designs_unit_tests -- -vvv
```

## Ansible-test

The AVD project leverages [ansible-test](https://www.ansible.com/blog/introduction-to-ansible-test/) to run sanity, unit and integration tests for the `arista.avd` Ansible Collection.

Testing is performed automatically as part of the CI pipeline. If troubleshooting is required, a Makefile at the root of the `avd` repository supports the following targets to execute `ansible-test`:

- `sanity`: Run ansible-test sanity validation.
- `unit-tests`: Run unit test cases using ansible-test. Optionally specify `ANSIBLE_TEST_MODE=<venv|docker>` (default: `venv`).
- `integration-tests`: Run integration test cases using `ansible-test`. Optionally specify `ANSIBLE_TEST_MODE=<venv|docker>` (default: `venv`).

Examples:

```shell
# Run ansible-test sanity validation.
make sanity

# Run unit test cases using ansible-test with venv (default)
make unit-tests

# Run integration test cases using ansible-test with docker.
make integration-tests ANSIBLE_TEST_MODE=docker
```

## Tox

The AVD project leverages [Tox](https://tox.wiki/) to run unit and integration of the `pyavd` Python package.

Testing is performed automatically as part of the CI pipeline. If troubleshooting is required, a Makefile at the root of the `avd` repository supports the following targets to execute `tox`:

- `pyavd-test`: Test PyAVD Python code with tox.

Example:

```shell
# Run tox on pyavd
make pyavd-test
```
