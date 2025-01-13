# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from json import JSONDecodeError, load
from typing import TYPE_CHECKING, Any

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils import CSVReport, MDReport, ResultsManager
from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_validated_path, get_validated_value

if TYPE_CHECKING:
    from collections.abc import Generator
    from pathlib import Path

PLUGIN_NAME = "arista.avd.eos_validate_state_reports"

try:
    from pyavd._utils import get
except ImportError as e:
    get = RaiseOnUse(
        AnsibleActionFail(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )


def _test_results_gen(input_path: Path) -> Generator[dict, None, None]:
    """Generate test results from a JSON file for a specific host.

    This function opens the JSON results file created by the `eos_validate_state_runner` action plugin
    and yields each test result as a dictionary.

    Args:
    ----
      input_path (Path): Path to the JSON file containing test results for a host.

    Yields:
    ------
      Generator[dict, None, None]: Test result as a dictionary.
    """
    with input_path.open(encoding="UTF-8") as file:
        yield from load(file)


class ActionModule(ActionBase):
    # @cprofile()
    def run(self, tmp: Any = None, task_vars: dict | None = None) -> dict:
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # Get task arguments and validate them
        try:
            only_failed_tests = get_validated_value(data=self._task.args, key="only_failed_tests", expected_type=bool, default_value=False)
            validation_report_csv = get_validated_value(data=self._task.args, key="validation_report_csv", expected_type=bool, default_value=True)
            validation_report_md = get_validated_value(data=self._task.args, key="validation_report_md", expected_type=bool, default_value=True)
            csv_report_path = get_validated_path(path_input=self._task.args.get("csv_report_path"), parent=True) if validation_report_csv else None
            md_report_path = get_validated_path(path_input=self._task.args.get("md_report_path"), parent=True) if validation_report_md else None
            test_results_dir = get_validated_path(path_input=self._task.args.get("test_results_dir"), parent=False)
        except (TypeError, ValueError, FileNotFoundError) as error:
            msg = f"Failed to validate task arguments: {error}"
            raise AnsibleActionFail(msg) from error

        # This is not all the hostvars, but just the Ansible Hostvars Manager object where we can retrieve hostvars for each host on-demand
        hostvars = task_vars["hostvars"]
        # For now we support the existing behavior of eos_validate_state, all hosts from the play
        ansible_play_hosts_all = task_vars.get("ansible_play_hosts_all", [])

        try:
            # Initialize an empty ResultsManager that will be used to store results and statistics
            test_results = ResultsManager(only_failed_tests=only_failed_tests)
            for host in sorted(ansible_play_hosts_all):
                host_hostvars = hostvars[host]
                # Hosts marked as not deployed do not have any results
                if not get(host_hostvars, "is_deployed", default=True):
                    display.warning(f"No test results for host {host} since 'is_deployed' is False")
                    continue
                try:
                    # Getting the host results JSON file saved by eos_validate_state_runner action plugin
                    result_path = get_validated_path(path_input=test_results_dir / f"{host}-results.json", parent=False)
                    # Process the host test results
                    try:
                        for test_result in _test_results_gen(input_path=result_path):
                            test_results.update_results(test_result)
                    except TypeError as error:
                        display.warning(f"Failed to update the test results of host {host}: {error}")
                except (JSONDecodeError, OSError, TypeError, FileNotFoundError) as error:
                    display.warning(f"Failed to load the test results of host {host}: {error}")

            # Generate the reports
            if validation_report_csv:
                with csv_report_path.open("w", encoding="UTF-8") as report_file:
                    csv_report = CSVReport(report_file, test_results)
                    csv_report.generate_report()
            if validation_report_md:
                with md_report_path.open("w", encoding="UTF-8") as report_file:
                    md_report = MDReport(report_file, test_results)
                    md_report.generate_report()

        except Exception as error:
            msg = f"Error during plugin execution: {error}"
            raise AnsibleActionFail(msg) from error

        return result
