# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from anta.catalog import AntaCatalog

    from ._anta.utils import FabricData, TestSpec

LOGGER = logging.getLogger("pyavd")


def get_device_anta_catalog(
    hostname: str,
    fabric_data: FabricData,
    custom_test_specs: list[TestSpec] | None = None,
    skip_tests: set[str] | None = None,
    *,
    logger: logging.Logger | None = None,
) -> AntaCatalog:
    """Generate an ANTA catalog for a single device.

    By default, the ANTA catalog will be generated from all tests specified in the PyAVD test index,
    loaded from the `pyavd._anta.utils.test_loader` module. The user can optionally provide a list of
    custom TestSpec to be added to the default PyAVD test index and a set of test names to skip.

    When creating test definitions for the catalog, PyAVD will use the FabricData instance containing
    the structured configurations of all devices in the fabric. Test definitions can be omitted from
    the catalog if the required data is not available for a specific device. You can pass a custom
    logger and set the log level to DEBUG to see which test definitions are skipped and the reason why.

    Parameters
    ----------
    hostname : str
        The hostname of the device for which the catalog is being generated.
    fabric_data : FabricData
        Contains relevant data (e.g. structured configurations, loopback mappings, etc.)
        of all devices in the fabric to generate the catalog.
        The instance must be created using the `get_fabric_data` function of this module.
    custom_test_specs : list[TestSpec]
        Optional user-defined list of TestSpec to be added to the default PyAVD test index.
    skip_tests : set[str]
        Optional set of test names to skip from the default PyAVD test index.
    logger : logging.Logger
        Optional logger to use for logging messages. If not provided, the `pyavd` logger will be used.

    Returns:
    -------
    AntaCatalog
        The generated ANTA catalog for the device.
    """
    logger = logger or LOGGER

    from ._anta.utils import ConfigManager, create_catalog
    from ._anta.utils.index import PYAVD_TEST_INDEX

    custom_test_specs = custom_test_specs or []
    skip_tests = skip_tests or set()

    # Create the device-specific ConfigManager used to generate the inputs for the tests
    config_manager = ConfigManager(hostname, fabric_data)

    # Filter out skipped tests and add custom test specs
    filtered_test_specs = [test for test in PYAVD_TEST_INDEX if test.test_class.name not in skip_tests]
    filtered_test_specs.extend([test for test in custom_test_specs if test not in filtered_test_specs])

    return create_catalog(config_manager, filtered_test_specs, logger=logger)
