# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

RESULTS_MAPPING: dict[str, str] = {"success": "PASS", "failure": "FAIL", "error": "FAIL", "skipped": "SKIPPED", "unset": "NOT RUN"}
"""Mapping the results from ANTA to what we want in the AVD validate state report."""

STATS_MAPPING: dict[str, tuple] = {
    "PASS": ("total_tests_passed", "tests_passed"),
    "FAIL": ("total_tests_failed", "tests_failed", "categories_failed"),
    "SKIPPED": ("total_tests_skipped", "tests_skipped", "categories_skipped"),
    "NOT RUN": ("total_tests_not_run", "tests_not_run"),
}
"""Mapping of the test result status with the stats to update."""
