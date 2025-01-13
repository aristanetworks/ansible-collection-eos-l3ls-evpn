# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import csv
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator
    from io import TextIOWrapper

    from .results_manager import ResultsManager


class CSVReport:
    """Generate and writes the validation CSV report based on test results managed by ResultsManager."""

    def __init__(self, csvfile: TextIOWrapper, results: ResultsManager) -> None:
        """Initialize the CSVReport with an open CSV file object to write to and a ResultsManager instance.

        Args:
        ----
            csvfile (TextIOWrapper): An open file object to write the CSV data into.
            results (ResultsManager): The ResultsManager instance containing all test results.
        """
        self.csvfile = csvfile
        self.results = results

    def generate_rows(self) -> Generator[dict, None, None]:
        """Generate rows of test result data for the CSV report.

        Results are sourced from `failed_tests` or `all_tests`, based on whether the report includes only failed tests or all results.

        Yields:
        ------
            Generator[dict, None, None]: A generator of test result dictionaries representing CSV rows.
        """
        results = self.results.failed_tests if self.results.only_failed_tests else self.results.all_tests

        for result in results:
            yield {
                **result,
                "messages": ";".join(result["messages"]),
                "categories": ";".join(result["categories"]),
            }

    def generate_report(self) -> None:
        """Generate and writes the CSV report using the collected test results."""
        fieldnames = ["id", "dut", "categories", "test", "description", "inputs", "result", "messages"]
        writer = csv.DictWriter(self.csvfile, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()

        for row in self.generate_rows():
            writer.writerow(row)
