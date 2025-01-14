# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Centralized package to import the required components of the ANTA framework."""

from anta.catalog import AntaCatalog, AntaTestDefinition
from anta.device import AsyncEOSDevice
from anta.inventory import AntaInventory
from anta.models import AntaTest
from anta.reporter.csv_reporter import ReportCsv
from anta.reporter.md_reporter import MDReportGenerator
from anta.result_manager import ResultManager
from anta.runner import main as anta_runner

__all__ = [
    "AntaCatalog",
    "AntaInventory",
    "AntaTest",
    "AntaTestDefinition",
    "AsyncEOSDevice",
    "MDReportGenerator",
    "ReportCsv",
    "ResultManager",
    "anta_runner",
]
