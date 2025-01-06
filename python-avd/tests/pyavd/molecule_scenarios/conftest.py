# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from itertools import chain

import pytest

from tests.models import MoleculeHost, MoleculeScenario

MOLECULE_SCENARIOS: dict[str, MoleculeScenario] = {}


def get_test_id(host: MoleculeHost) -> str:
    return f"{host.scenario.name}__{host.name}"


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    """
    Generate MoleculeHost or MoleculeScenario instances for the scenarios given with pytest.mark.molecule_scenarios(<scenario>, <scenario>).

    The generated objects are inserted with parametrize to generate a test case for each.

    Reads/updates MOLECULE_SCENARIOS for caching.
    """
    molecule_scenario_names = chain.from_iterable(list(mark.args) for mark in metafunc.definition.iter_markers(name="molecule_scenarios"))
    molecule_scenarios: list[MoleculeScenario] = []
    for molecule_scenario_name in molecule_scenario_names:
        if molecule_scenario_name not in MOLECULE_SCENARIOS:
            # Using this method since setdefault triggers init of the class which is expensive.
            MOLECULE_SCENARIOS[molecule_scenario_name] = MoleculeScenario(molecule_scenario_name)
        molecule_scenarios.append(MOLECULE_SCENARIOS[molecule_scenario_name])

    if "molecule_host" in metafunc.fixturenames:
        metafunc.parametrize("molecule_host", chain.from_iterable(scenario.hosts for scenario in molecule_scenarios), ids=get_test_id)

    elif "molecule_scenario" in metafunc.fixturenames:
        metafunc.parametrize("molecule_scenario", molecule_scenarios, ids=lambda scenario: scenario.name)
