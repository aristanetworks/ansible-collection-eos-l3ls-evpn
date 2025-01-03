# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from collections.abc import Generator
    from io import TextIOWrapper

    from .results_manager import ResultsManager


class MDReport:
    """Main class responsible for generating various sections of a markdown report based on test results.

    It aggregates different report sections, each represented by a subclass of `MDReportBase`,
    and sequentially generates their content into a markdown file.

    The `generate_report` method will loop over all the section subclasses and call their `generate_section` method.
    The final report will be generated in the same order as the `self.sections` list attribute.
    """

    def __init__(self, mdfile: TextIOWrapper, results: ResultsManager) -> None:
        """Initialize the MDReport with an open markdown file object to write to and a ResultsManager instance.

        Args:
        ----
            mdfile (TextIOWrapper): An open file object to write the markdown data into.
            results (ResultsManager): The ResultsManager instance containing all test results.
        """
        self.sections: list[MDReportBase] = [
            ValidateStateReport(mdfile, results),
            TestResultsSummary(mdfile, results),
            SummaryTotals(mdfile, results),
            SummaryTotalsDeviceUnderTest(mdfile, results),
            SummaryTotalsPerCategory(mdfile, results),
            FailedTestResultsSummary(mdfile, results),
            AllTestResults(mdfile, results),
        ]

    def generate_report(self) -> None:
        """Generate and write the various sections of the markdown report."""
        for section in self.sections:
            section.generate_section()


class MDReportBase(ABC):
    """Base class for all sections subclasses.

    Every subclasses must implement the `generate_section` method that uses the `ResultsManager` object
    to generate and write content to the provided markdown file.
    """

    def __init__(self, mdfile: TextIOWrapper, results: ResultsManager) -> None:
        """Initialize the MDReportBase with an open markdown file object to write to and a ResultsManager instance.

        Args:
        ----
            mdfile (TextIOWrapper): An open file object to write the markdown data into.
            results (ResultsManager): The ResultsManager instance containing all test results.
        """
        self.mdfile = mdfile
        self.results = results

    @abstractmethod
    def generate_section(self) -> None:
        """Abstract method to generate a specific section of the markdown report.

        Must be implemented by subclasses.
        """
        msg = "Must be implemented by subclasses"
        raise NotImplementedError(msg)

    def generate_rows(self) -> Generator[str, None, None]:
        """Generate the rows of a markdown table for a specific report section.

        Subclasses can implement this method to generate the content of the table rows.
        """
        msg = "Subclasses should implement this method"
        raise NotImplementedError(msg)

    def generate_heading_name(self) -> str:
        """Generate a formatted heading name based on the class name.

        Returns:
        -------
            str: Formatted header name.

        Example:
        -------
            `ValidateStateReport` will become Validate State Report.
        """
        class_name = self.__class__.__name__
        return re.sub(r"(?<!^)(?=[A-Z])", " ", class_name).title()

    def write_table(self, table_heading: list[str], *, last_table: bool = False) -> None:
        """Write a markdown table with a table heading and multiple rows to the markdown file.

        Args:
        ----
            table_heading (list[str]): List of strings to join for the table heading.
            last_table (bool): Flag to determine if it's the last table of the markdown file to avoid unnecessary new line.
                                Defaults to False.
        """
        self.mdfile.write("\n".join(table_heading) + "\n")
        for row in self.generate_rows():
            self.mdfile.write(row)
        if not last_table:
            self.mdfile.write("\n")

    def write_heading(self, heading_level: int) -> None:
        """Write a markdown heading to the markdown file.

        The heading name used is the class name.

        Args:
        ----
            heading_level (int): The level of the heading (1-6).

        Example:
        -------
            ## Test Results Summary
        """
        # Ensure the heading level is within the valid range of 1 to 6
        heading_level = max(1, min(heading_level, 6))
        heading_name = self.generate_heading_name()
        heading = "#" * heading_level + " " + heading_name
        self.mdfile.write(f"{heading}\n\n")

    def safe_markdown(self, text: str | None) -> str:
        """Escape markdown characters in the text to prevent markdown rendering issues.

        Args:
        ----------
            text (str): The text to escape markdown characters from.

        Returns:
        -------
            str: The text with escaped markdown characters.
        """
        # Custom field from a TestResult object can be None
        if text is None:
            return ""

        # Replace newlines with spaces to keep content on one line
        text = text.replace("\n", " ")

        # Replace backticks with single quotes
        return text.replace("`", "'")


class ValidateStateReport(MDReportBase):
    """Generate the `# Validate State Report` section of the markdown report."""

    def generate_section(self) -> None:
        """Generate the `# Validate State Report` section of the markdown report."""
        self.write_heading(heading_level=1)
        self.mdfile.write(
            """**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

""",
        )


class TestResultsSummary(MDReportBase):
    """Generate the `## Test Results Summary` section of the markdown report."""

    def generate_section(self) -> None:
        """Generate the `## Test Results Summary` section of the markdown report."""
        self.write_heading(heading_level=2)


class SummaryTotals(MDReportBase):
    """Generate the `### Summary Totals` section of the markdown report."""

    TABLE_HEADING: ClassVar[list[str]] = [
        "| Total Tests | Total Tests Passed | Total Tests Failed | Total Tests Skipped |",
        "| ----------- | ------------------ | ------------------ | ------------------- |",
    ]

    def generate_rows(self) -> Generator[str, None, None]:
        """Generate the rows of the summary totals table."""
        yield (f"| {self.results.total_tests} | {self.results.total_tests_passed} | {self.results.total_tests_failed} | {self.results.total_tests_skipped} |\n")

    def generate_section(self) -> None:
        """Generate the `### Summary Totals` section of the markdown report."""
        self.write_heading(heading_level=3)
        self.write_table(table_heading=self.TABLE_HEADING)


class SummaryTotalsDeviceUnderTest(MDReportBase):
    """Generate the `### Summary Totals Devices Under Tests` section of the markdown report."""

    TABLE_HEADING: ClassVar[list[str]] = [
        "| Device Under Test | Total Tests | Tests Passed | Tests Failed | Tests Skipped | Categories Failed | Categories Skipped |",
        "| ------------------| ----------- | ------------ | ------------ | ------------- | ----------------- | ------------------ |",
    ]

    def generate_rows(self) -> Generator[str, None, None]:
        """Generate the rows of the summary totals dut table."""
        for dut, stat in self.results.dut_stats.items():
            total_tests = stat["tests_passed"] + stat["tests_failed"] + stat["tests_skipped"] + stat["tests_not_run"]
            categories_failed = ", ".join(sorted(stat["categories_failed"]))
            categories_skipped = ", ".join(sorted(stat["categories_skipped"]))
            yield (
                f"| {dut} | {total_tests} | {stat['tests_passed']} | {stat['tests_failed']} | {stat['tests_skipped']} | {categories_failed or '-'} |"
                f" {categories_skipped or '-'} |\n"
            )

    def generate_section(self) -> None:
        """Generate the `### Summary Totals Devices Under Tests` section of the markdown report."""
        self.write_heading(heading_level=3)
        self.write_table(table_heading=self.TABLE_HEADING)


class SummaryTotalsPerCategory(MDReportBase):
    """Generate the `### Summary Totals Per Category` section of the markdown report."""

    TABLE_HEADING: ClassVar[list[str]] = [
        "| Test Category | Total Tests | Tests Passed | Tests Failed | Tests Skipped |",
        "| ------------- | ----------- | ------------ | ------------ | ------------- |",
    ]

    def generate_rows(self) -> Generator[str, None, None]:
        """Generate the rows of the summary totals per category table."""
        for category, stat in self.results.sorted_category_stats.items():
            total_tests = stat["tests_passed"] + stat["tests_failed"] + stat["tests_skipped"] + stat["tests_not_run"]
            yield f"| {category} | {total_tests} | {stat['tests_passed']} | {stat['tests_failed']} | {stat['tests_skipped']} |\n"

    def generate_section(self) -> None:
        """Generate the `### Summary Totals Per Category` section of the markdown report."""
        self.write_heading(heading_level=3)
        self.write_table(table_heading=self.TABLE_HEADING)


class FailedTestResultsSummary(MDReportBase):
    """Generate the `## Failed Test Results Summary` section of the markdown report."""

    TABLE_HEADING: ClassVar[list[str]] = [
        "| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |",
        "| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |",
    ]

    def generate_rows(self) -> Generator[str, None, None]:
        """Generate the rows of the failed test results table."""
        for result in self.results.failed_tests:
            messages = self.safe_markdown(", ".join(result["messages"]))
            categories = ", ".join(result["categories"])
            yield (
                f"| {result['id'] or '-'} | {result['dut'] or '-'} | {categories or '-'} | {result['test'] or '-'} |"
                f" {result['description'] or '-'} | {result['inputs'] or '-'} | {result['result'] or '-'} | {messages or '-'} |\n"
            )

    def generate_section(self) -> None:
        """Generate the `## Failed Test Results Summary` section of the markdown report."""
        self.write_heading(heading_level=2)
        self.write_table(table_heading=self.TABLE_HEADING)


class AllTestResults(MDReportBase):
    """Generates the `## All Test Results` section of the markdown report.

    This section is generated only if the report includes all results.
    """

    TABLE_HEADING: ClassVar[list[str]] = [
        "| ID | Device Under Test | Categories | Test | Description | Inputs | Result | Messages |",
        "| -- | ----------------- | ---------- | ---- | ----------- | ------ | -------| -------- |",
    ]

    def generate_rows(self) -> Generator[str, None, None]:
        """Generate the rows of the all test results table."""
        for result in self.results.all_tests:
            messages = self.safe_markdown(", ".join(result["messages"]))
            categories = ", ".join(result["categories"])
            yield (
                f"| {result['id'] or '-'} | {result['dut'] or '-'} | {categories or '-'} | {result['test'] or '-'} |"
                f" {result['description'] or '-'} | {result['inputs'] or '-'} | {result['result'] or '-'} | {messages or '-'} |\n"
            )

    def generate_section(self) -> None:
        """Generate the `## All Test Results` section of the markdown report.

        This section is generated only if the report includes all results.
        """
        if not self.results.only_failed_tests:
            self.write_heading(heading_level=2)
            self.write_table(table_heading=self.TABLE_HEADING, last_table=True)
