<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# PyAVD

PyAVD is a python package providing some of the features from the `arista.avd` Ansible collection without requiring Ansible. PyAVD leverages the same logic as the Ansible collection, so the generated outputs should be exactly the same based on the same inputs.

PyAVD does not provide any inventory or variable management, so PyAVD cannot replace a full Ansible based solution by itself. PyAVD could serve as an element in larger framework.

Supported features:

- Validation of inputs based on the [`eos_designs` input schema](../roles/eos_designs/docs/input-variables.md).
- Generation of "avd_facts" and "structured config" to be used in other PyAVD functions.
- Validation of "structured config" based on the [`eos_cli_config_gen` input schema](../roles/eos_cli_config_gen/docs/input-variables.md).
- Generation of device configuration.
- Generation of device documentation.

Feedback is very welcome. Please use [GitHub discussions](https://github.com/aristanetworks/avd/discussions).

## Functions overview

![Arista AVD Overview](_media/pyavd_functions_dark.svg#only-dark)
![Arista AVD Overview](_media/pyavd_functions_light.svg#only-light)

## Known limitations

!!! warning

    Input data and "structured_configs" will be in-place updated by various PyAVD functions.
    Make sure to deep copy the data first if modifications are not allowed.

!!! warning

    `get_device_structured_config()`, `get_device_config()` and `get_device_doc()` are not thread-safe, so avoid running them for the same device across multiple threads.

!!! note

    - No support for inline Jinja2 or custom Jinja2 templates.
    - The logic uses the hostname as the unique identifier for each device, so overlapping hostnames will not work.
    - For `get_avd_facts()`, `fabric_name` is not used or verified and may differ between devices.
      All devices in the given inputs will be treated as one fabric.
    - `hostname` *must* be set in "structured_config" for each device. `hostname` *will* be set correctly when using `get_structured_config()`.

## Roadmap

!!! note
    Subject to change. No commitments implied.

- Add examples
- Add more tests (current coverage is 85%)
- Add network state validation similar to `eos_validate_state`.
- Add CloudVision tag integrations
- Explore support for custom Jinja2 templates.

## Installation

Install the `pyavd` Python package:

```sh
pip install pyavd
```

Python dependencies are automatically installed with above command.

### Optional requirements

To install Ansible [AVD collection Python requirements](installation/collection-installation.md#python-requirements-installation) install with extra `ansible`:

```sh
pip install pyavd[ansible]
```

## Reference

::: pyavd.validate_inputs
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true
      paths: ../../../../python-avd

::: pyavd.get_avd_facts
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true
      paths: ../../../../python-avd

::: pyavd.get_device_structured_config
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true
      paths: ../../../../python-avd

::: pyavd.validate_structured_config
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true
      paths: ../../../../python-avd

::: pyavd.get_fabric_documentation
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true
      paths: ../../../../python-avd

::: pyavd.get_device_config
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true
      paths: ../../../../python-avd

::: pyavd.get_device_doc
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true
      paths: ../../../../python-avd

::: pyavd.validation_result
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true
      paths: ../../../../python-avd

::: pyavd.api.fabric_documentation
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true
      paths: ../../../../python-avd

::: pyavd.api.interface_descriptions
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true
      paths: ../../../../python-avd

::: pyavd.api.ip_addressing
    options:
      heading_level: 3
      show_root_toc_entry: false
      show_object_full_path: true
      paths: ../../../../python-avd
