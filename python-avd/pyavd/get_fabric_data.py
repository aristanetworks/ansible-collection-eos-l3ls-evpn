# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    from pyavd.api.fabric_data import FabricData


def get_fabric_data(structured_configs: dict[str, dict], scope: dict | None = None, filename: str | Path | None = None) -> FabricData:
    """Create a FabricData instance from device structured configurations.

    When FabricData is created, it will automatically create the required mappings
    and data for the whole fabric. The same FabricData instance should be used for all
    devices in the fabric when generating the ANTA catalog using `get_device_anta_catalog`.

    Parameters
    ----------
    structured_configs : dict[str, dict]
        A dictionary where keys are hostnames and values are dictionaries of
        structured configurations per device.
        ```python
        {
            "hostname1": {structured_config1},
            "hostname2": {structured_config2},
            ...
        }
        ```
        The structured configuration should be converted and validated according to
        AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`.
    scope : dict | None
        An optional scope dictionary to define the fabric's test input generation scope.
        The dictionary should contain the following:
        ```python
        {
            "boundary": "unlimited" | "fabric" | "dc" | "pod" | "rack",
            "allow_bgp_external": bool,  # Allow BGP peers that are external to the fabric boundary
            "allow_bgp_vrfs": bool,  # Allow BGP peers in VRFs
        }
        ```
    filename : str | Path | None
        An optional filename or path to save the FabricData instance as a JSON file.

    Returns:
    -------
    FabricData
        An instance of FabricData containing the processed fabric information.
    """
    from pyavd._anta.utils import dump_fabric_data
    from pyavd.api.fabric_data import FabricData

    fabric_data = FabricData.create(structured_configs, scope)
    if filename:
        dump_fabric_data(filename, fabric_data)

    return fabric_data
