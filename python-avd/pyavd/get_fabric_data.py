# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyavd.api.fabric_data import FabricData

LOGGER = logging.getLogger("pyavd")


def get_fabric_data(structured_configs: dict[str, dict], *, logger: logging.Logger | None = None) -> FabricData:
    """Create a FabricData instance from device structured configurations.

    When FabricData is initialized, it will automatically create the required mappings
    and data for the whole fabric. The same FabricData instance should be used for all
    devices in the fabric when generating the ANTA catalog using `get_device_anta_catalog`.

    Parameters
    ----------
    structured_configs : dict[str, dict]
        A dictionary where keys are hostnames and values are dictionaries of
        structured configurations per device.
        ```python
        {
            "<hostname1>": <structured_config1>,
            "<hostname2>": <structured_config2>,
            ...
        }
        The structured configuration should be converted and validated according to
        AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`.
    logger : logging.Logger
        Optional logger to use for logging messages. If not provided, the `pyavd` logger will be used.

    Returns:
    -------
    FabricData
        An instance of FabricData containing the processed fabric information.
    """
    logger = logger or LOGGER

    from pyavd.api.fabric_data import FabricData

    return FabricData(structured_configs, logger=logger)
