# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from json import dumps
from pathlib import Path
from time import perf_counter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._anta.lib import AntaCatalog
    from .api.anta_test_spec import TestSpec
    from .api.fabric_data import FabricData

LOGGER = logging.getLogger("pyavd")


def get_device_anta_catalog(
    hostname: str,
    fabric_data: FabricData,
    output_dir: str | Path | None = None,
    custom_test_specs: list[TestSpec] | None = None,
    run_tests: list[str] | None = None,
    skip_tests: list[str] | None = None,
    input_filters: dict[str, dict] | None = None,
    *,
    logger: logging.Logger | None = None,
) -> AntaCatalog:
    """Generate an ANTA catalog for a single device.

    By default, the ANTA catalog will be generated from all tests specified in the PyAVD test index.
    The user can optionally provide a list of custom TestSpec to be added to the default PyAVD test
    index and a set of test names to skip or run.

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
    output_dir : str | Path
        Optional directory where the ANTA catalog should be saved as a YAML file.
    custom_test_specs : list[TestSpec]
        Optional user-defined list of TestSpec to be added to the default PyAVD test index.
    run_tests : list[str]
        Optional list of test names to run from the default PyAVD test index.
    skip_tests : list[str]
        Optional list of test names to skip from the default PyAVD test index. Takes precedence over `run_tests`.
    input_filters : dict[str, dict]
        Optional dictionary keyed by ANTA test names with values as a filter dictionary for that test.
    logger : logging.Logger
        Optional logger to use for logging messages. If not provided, the `pyavd` logger will be used.

    Returns:
    -------
    AntaCatalog
        The generated ANTA catalog for the device.
    """
    logger = logger or LOGGER

    from ._anta.utils import ConfigManager, create_catalog
    from ._anta.utils.index import PYAVD_TEST_INDEX, PYAVD_TEST_NAMES

    opt_params = {
        "output_dir": output_dir,
        "custom_test_specs": custom_test_specs or [],
        "run_tests": run_tests or [],
        "skip_tests": skip_tests or [],
        "input_filters": input_filters or {},
    }

    start_time = perf_counter()
    logger.debug("<%s> [get_device_anta_catalog]: Generating AVD catalog with the following parameters:\n %s", hostname, dumps(opt_params, indent=2))

    # Check for invalid test names across all filters
    invalid_tests = {
        "run_tests": set(opt_params["run_tests"]) - set(PYAVD_TEST_NAMES),
        "skip_tests": set(opt_params["skip_tests"]) - set(PYAVD_TEST_NAMES),
        "input_filters": set(opt_params["input_filters"].keys()) - set(PYAVD_TEST_NAMES),
    }

    for filter_type, invalid_names in invalid_tests.items():
        if invalid_names:
            msg = f"Invalid test names in {filter_type}: {', '.join(invalid_names)}"
            raise ValueError(msg)

    # Create the device-specific ConfigManager used to generate the inputs for the tests
    config_manager = ConfigManager(hostname, fabric_data)

    # Filter test specs based on skip_tests and run_tests
    filtered_test_specs = []

    for test in PYAVD_TEST_INDEX:
        # Skip tests explicitly mentioned in skip_tests
        if test.test_class.name in opt_params["skip_tests"]:
            continue
        # If run_tests is specified, only include tests in that set
        if opt_params["run_tests"] and test.test_class.name not in opt_params["run_tests"]:
            continue

        # Create input filters for the test if specified
        if test.test_class.name in opt_params["input_filters"]:
            test.create_input_filter(opt_params["input_filters"][test.test_class.name])

        filtered_test_specs.append(test)

    # Add custom test specs, avoiding duplicates
    filtered_test_specs.extend([test for test in opt_params["custom_test_specs"] if test not in filtered_test_specs])

    catalog = create_catalog(config_manager, filtered_test_specs, logger=logger)

    if output_dir:
        _dump_anta_catalog(hostname, catalog, output_dir)

    stop_time = perf_counter()
    logger.debug("<%s> [get_device_anta_catalog]: Generated AVD catalog in %.8f seconds", hostname, stop_time - start_time)

    return catalog


def _dump_anta_catalog(hostname: str, catalog: AntaCatalog, catalog_dir: str) -> None:
    """Dump the ANTA catalog for a device to the provided catalog directory.

    The catalog will be saved as a YAML file named after the device: `<device>.yml`.

    Parameters
    ----------
        hostname: The name of the device.
        catalog: The ANTA catalog of the device.
        catalog_dir: The directory where the ANTA catalogs should be saved.
    """
    catalog_path = Path(catalog_dir) / f"{hostname}.yml"
    catalog_dump = catalog.dump()

    with catalog_path.open(mode="w", encoding="UTF-8") as stream:
        stream.write(catalog_dump.yaml())
