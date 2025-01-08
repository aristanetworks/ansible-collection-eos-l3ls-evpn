# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from time import perf_counter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    from ._anta.lib import AntaCatalog
    from .api.anta_test_spec import TestSpec
    from .api.fabric_data import FabricData

LOGGER = getLogger(__name__)


def get_device_anta_catalog(
    hostname: str,
    structured_config: dict,
    fabric_data: FabricData,
    output_dir: str | Path | None = None,
    custom_test_specs: list[TestSpec] | None = None,
    run_tests: list[str] | None = None,
    skip_tests: list[str] | None = None,
    ignore_is_deployed: bool = False,
) -> AntaCatalog:
    """Generate an ANTA catalog for a single device.

    By default, the ANTA catalog will be generated from all tests specified in the PyAVD test index.
    The user can optionally provide a list of custom TestSpec to be added to the default PyAVD test
    index and a set of test names to skip or run.

    When creating test definitions for the catalog, PyAVD will use the FabricData instance containing
    the required mappings and data of all devices in the fabric. Make sure to create a single FabricData
    using the `get_fabric_data` function of PyAVD and use it for all devices in the fabric.

    Test definitions can be omitted from the catalog if the required data is not available for a specific device.
    You can configure logging and set the log level to DEBUG to see which test definitions are skipped and the reason why.

    Parameters
    ----------
    hostname : str
        The hostname of the device for which the catalog is being generated.
    fabric_data : FabricData
        Contains relevant devices data and mappings of all devices in the fabric to generate the catalog.
        The instance must be created using the `get_fabric_data` function of PyAVD.
    output_dir : str | Path
        Optional output directory where the ANTA catalog should be saved as a JSON file.
    custom_test_specs : list[TestSpec]
        Optional user-defined list of TestSpec to be added to the default PyAVD test index.
    run_tests : list[str]
        Optional list of test names to run from the default PyAVD test index.
    skip_tests : list[str]
        Optional list of test names to skip from the default PyAVD test index. Takes precedence over `run_tests`.
    ignore_is_deployed : bool
        If set to True, the catalog will be generated even if the device is marked as not deployed (is_deployed=False).

    Returns:
    -------
    AntaCatalog
        The generated ANTA catalog for the device.
    """
    from ._anta.factories import create_catalog
    from ._anta.index import PYAVD_TEST_INDEX, PYAVD_TEST_NAMES
    from ._anta.lib import AntaCatalog
    from ._anta.utils import dump_anta_catalog

    # Normalize input parameters
    custom_test_specs = custom_test_specs or []
    run_tests = run_tests or []
    skip_tests = skip_tests or []

    start_time = perf_counter()
    LOGGER.debug(
        "<%s>: generating catalog with options (run_tests=%s, skip_tests=%s, output_dir=%s, ignore_is_deployed=%s)",
        hostname,
        run_tests,
        skip_tests,
        output_dir,
        ignore_is_deployed,
    )

    if ignore_is_deployed is False and not fabric_data.devices[hostname].is_deployed:
        LOGGER.debug("<%s>: device is not deployed, returning an empty catalog", hostname)
        return AntaCatalog()

    # Check for invalid test names across all filters
    invalid_tests = {
        "run_tests": set(run_tests) - set(PYAVD_TEST_NAMES),
        "skip_tests": set(skip_tests) - set(PYAVD_TEST_NAMES),
    }

    for filter_type, invalid_names in invalid_tests.items():
        if invalid_names:
            msg = f"Invalid test names in {filter_type}: {', '.join(invalid_names)}"
            raise ValueError(msg)

    # Filter test specs based on skip_tests and run_tests
    filtered_test_specs = []

    for test in PYAVD_TEST_INDEX:
        # Skip tests explicitly mentioned in skip_tests
        if test.test_class.name in skip_tests:
            continue
        # If run_tests is specified, only include tests in that set
        if run_tests and test.test_class.name not in run_tests:
            continue

        filtered_test_specs.append(test)

    # Add custom test specs, avoiding duplicates
    filtered_test_specs.extend([test for test in custom_test_specs if test not in filtered_test_specs])

    catalog = create_catalog(hostname, structured_config, fabric_data, filtered_test_specs)

    if output_dir:
        dump_anta_catalog(hostname, catalog, output_dir)

    stop_time = perf_counter()
    LOGGER.debug("<%s>: generated catalog in %.4f seconds", hostname, stop_time - start_time)

    return catalog
