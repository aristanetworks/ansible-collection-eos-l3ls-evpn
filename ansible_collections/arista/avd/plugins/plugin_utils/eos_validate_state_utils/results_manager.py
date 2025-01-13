# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import defaultdict

from ansible_collections.arista.avd.roles.eos_validate_state.python_modules.constants import ACRONYM_CATEGORIES

from .constants import RESULTS_MAPPING, STATS_MAPPING


class ResultsManager:
    """Manages and stores test results from eos_validate_state running ANTA.

    This class processes individual test result and maintains statistics like total tests passed, failed, and skipped.

    An instance of this class holding all results and statistics can be used to generate the validation reports.
    """

    def __init__(self, *, only_failed_tests: bool = True) -> None:
        """Initialize the ResultsManager with default values and stats counters set to 0.

        The class uses defaultdict to automatically initialize statistics for devices under test (DUT) and test categories.
        This ensures that accessing a stat for a new DUT or category will automatically create an entry with initial
        zeroed counters and empty sets for failed and skipped categories.

        Args:
        ----
            only_failed_tests (bool): Flag to determine if only failed tests are saved.
                                      Defaults to True. If set to False, all tests will be saved.
        """
        self.test_id = 0
        self.total_tests_passed = 0
        self.total_tests_failed = 0
        self.total_tests_skipped = 0
        self.total_tests_not_run = 0
        self.dut_stats = defaultdict(
            lambda: {
                "tests_passed": 0,
                "tests_failed": 0,
                "tests_skipped": 0,
                "tests_not_run": 0,
                "categories_failed": set(),
                "categories_skipped": set(),
            },
        )
        self.category_stats = defaultdict(
            lambda: {
                "tests_passed": 0,
                "tests_failed": 0,
                "tests_skipped": 0,
                "tests_not_run": 0,
            },
        )
        self.failed_tests = []
        self.all_tests = []
        self.only_failed_tests = only_failed_tests

    def _parse_result(self, result: dict) -> dict:
        """Parse a single test result and converts it into a standardized format for the reports.

        Args:
        ----
            result (dict): The test result data to parse.

        Returns:
        -------
            dict: The parsed and standardized test result.
        """
        test_categories = [
            " ".join(word.upper() if word.lower() in ACRONYM_CATEGORIES else word.title() for word in category.split())
            for category in result.get("categories", [])
        ]

        # Mapping the ANTA results
        anta_result = result.get("result", "unset")
        new_result = RESULTS_MAPPING.get(anta_result, "")

        # Create the parsed result dictionary
        return {
            "id": self.test_id,
            "dut": result.get("name", ""),
            "categories": test_categories,
            "test": result.get("test", ""),
            "description": result.get("description", ""),
            "inputs": result.get("custom_field"),
            "result": new_result,
            "messages": result.get("messages", []),
        }

    def _increment_stats(self, test_status: str, dut: str, categories: list[str]) -> None:
        """Increment test statistics based on the test result.

        Args:
        ----
            test_status (str): The test status.
            dut (str): The name of the device under test.
            categories (list[str]): The categories of the test.
        """
        stats_to_increment = STATS_MAPPING.get(test_status, ())

        for stat in stats_to_increment:
            if stat.startswith("total_"):
                setattr(self, stat, getattr(self, stat) + 1)
            elif stat.startswith("tests_"):
                self.dut_stats[dut][stat] += 1
                for category in categories:
                    self.category_stats[category][stat] += 1
            else:
                self.dut_stats[dut][stat].update(categories)

    def update_results(self, result: dict) -> None:
        """Update the internal statistics and test results based on the given test result.

        Args:
        ----
            result (dict): The test result data to be added and processed.
        """
        self.test_id += 1

        if not isinstance(result, dict):
            msg = f"Test result '{result}' must be dictionary, got {type(result).__name__}."
            raise TypeError(msg)

        parsed_result = self._parse_result(result)
        test_status = parsed_result["result"]
        categories = parsed_result["categories"]
        dut = parsed_result["dut"]

        self._increment_stats(test_status, dut, categories)

        if test_status == "FAIL":
            self.failed_tests.append(parsed_result)
        if not self.only_failed_tests:
            self.all_tests.append(parsed_result)

    @property
    def total_tests(self) -> int:
        """Calculates the total number of tests processed.

        Returns:
        -------
            int: The total number of tests.
        """
        return self.total_tests_passed + self.total_tests_failed + self.total_tests_skipped + self.total_tests_not_run

    @property
    def sorted_category_stats(self) -> dict:
        """A property that returns the category_stats dictionary sorted by key name.

        Returns:
        -------
            dict: The sorted category_stats dictionary.
        """
        return dict(sorted(self.category_stats.items()))
