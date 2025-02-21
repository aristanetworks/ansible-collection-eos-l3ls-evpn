# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections.abc import Iterable
from copy import deepcopy

import pytest

from pyavd import get_device_anta_catalog, get_fabric_data
from tests.models import MoleculeHost, MoleculeScenario


@pytest.mark.molecule_scenarios("anta_runner")
@pytest.mark.parametrize(
    "run_config",
    [
        {"catalog_attr": "anta_catalog_default", "fabric_scope": None},
        {"catalog_attr": "anta_catalog_allow_bgp_vrfs", "fabric_scope": {"allow_bgp_vrfs": True}},
        {"catalog_attr": "anta_catalog_dc_boundary", "fabric_scope": {"boundary": "dc"}},
        {"catalog_attr": "anta_catalog_filtered", "fabric_scope": None},
    ],
)
def test_get_device_anta_catalog(molecule_scenario: MoleculeScenario, run_config: dict) -> None:
    """Test get_device_anta_catalog with different run configurations."""
    structured_configs = {host.name: deepcopy(host.structured_config) for host in molecule_scenario.hosts}
    assert len(structured_configs) == len(molecule_scenario.hosts)
    fabric_data = get_fabric_data(structured_configs, scope=run_config["fabric_scope"])
    run_tests, skip_tests = None, None

    # TODO: We could probably simplify this by having equality implemented in AntaCatalog
    for host in molecule_scenario.hosts:
        if run_config["catalog_attr"] == "anta_catalog_filtered":
            run_tests, skip_tests = _get_run_and_skip_tests(host)
        generated_catalog = get_device_anta_catalog(host.name, structured_configs[host.name], fabric_data, run_tests=run_tests, skip_tests=skip_tests)
        reference_catalog = getattr(host, run_config["catalog_attr"])
        assert len(generated_catalog.tests) == len(reference_catalog.tests)

        # Input checks for each test
        for gen_test, ref_test in zip(generated_catalog.tests, reference_catalog.tests, strict=True):
            # Check the test classes match
            assert gen_test.test == ref_test.test

            exclusions = {"exclude": {"result_overwrite", "filters"}, "exclude_unset": True, "exclude_defaults": True, "exclude_none": True}
            gen_test_inputs = gen_test.inputs.model_dump(**exclusions)
            ref_test_inputs = ref_test.inputs.model_dump(**exclusions)
            for field_name, field_value in gen_test_inputs.items():
                assert field_name in ref_test_inputs
                if isinstance(field_value, Iterable):
                    assert len(field_value) == len(ref_test_inputs[field_name])
                else:
                    assert field_value == ref_test_inputs[field_name]


def _get_run_and_skip_tests(host: MoleculeHost) -> tuple[list[str], list[str]]:
    """Get the list of run_tests and skip_tests based on the Ansible host groups applied in the `ANTA Filtered Run` molecule."""
    groups = [str(grp) for grp in host.ansible_host.get_groups()]
    run_tests = None
    skip_tests = None

    # Set the run_tests and skip_tests based on the host groups
    if "FABRIC" in groups:
        skip_tests = ["VerifyNTP"]
    if "DC1_SVC_LEAVES" in groups:
        run_tests = ["VerifyReachability"]
    if "DC2_SPINES" in groups:
        run_tests = ["VerifyLLDPNeighbors"]
        skip_tests = ["VerifyLLDPNeighbors"]

    return (run_tests, skip_tests)
