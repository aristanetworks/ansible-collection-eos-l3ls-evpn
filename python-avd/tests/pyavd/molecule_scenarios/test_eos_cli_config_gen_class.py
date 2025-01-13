# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import warnings
from copy import deepcopy

import pytest

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._schema.store import create_store
from tests.models import MoleculeHost

SCHEMA = create_store()["eos_cli_config_gen"]


@pytest.mark.molecule_scenarios(
    "eos_designs_unit_tests",
    "eos_designs_deprecated_vars",
    "eos_designs_l2l2",
    "eos_designs-mpls-isis-sr-ldp",
    # TODO: "eos_designs-twodc-5stage-clos", # Remove inline jinja
    "evpn_underlay_ebgp_overlay_ebgp",
    "evpn_underlay_isis_overlay_ibgp",
    "evpn_underlay_ospf_overlay_ebgp",
    "evpn_underlay_rfc5549_overlay_ebgp",
    "example-campus-fabric",
    # TODO: "example-cv-pathfinder", # Work around Ansible vault
    "example-dual-dc-l3ls",
    "example-isis-ldp-ipvpn",
    "example-l2ls-fabric",
    "example-single-dc-l3ls",
    "eos_cli_config_gen",
    "eos_cli_config_gen_deprecated_vars",
)
def test_eos_cli_config_gen_initialize_dict_with_valid_data(molecule_host: MoleculeHost) -> None:
    """Test EosCliConfigGen model with valid data."""
    if molecule_host.scenario.name.startswith("eos_cli_config_gen"):
        structured_config = deepcopy(molecule_host.hostvars)
    else:
        structured_config = deepcopy(molecule_host.structured_config)

    # If nothing raises, the model is accepted.
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        EosCliConfigGen._from_dict(structured_config)


@pytest.mark.molecule_scenarios(
    "eos_designs_unit_tests",
    "eos_designs_deprecated_vars",
    "eos_designs_l2l2",
    "eos_designs-mpls-isis-sr-ldp",
    # TODO: "eos_designs-twodc-5stage-clos", # Remove inline jinja
    "evpn_underlay_ebgp_overlay_ebgp",
    "evpn_underlay_isis_overlay_ibgp",
    "evpn_underlay_ospf_overlay_ebgp",
    "evpn_underlay_rfc5549_overlay_ebgp",
    "example-campus-fabric",
    # TODO: "example-cv-pathfinder", # Work around Ansible vault
    "example-dual-dc-l3ls",
    "example-isis-ldp-ipvpn",
    "example-l2ls-fabric",
    "example-single-dc-l3ls",
    "eos_cli_config_gen",
    "eos_cli_config_gen_deprecated_vars",
)
def test_eos_cli_config_gen_initialize_kwargs_with_valid_data(molecule_host: MoleculeHost) -> None:
    """Test EosCliConfigGen model with valid data."""
    if molecule_host.scenario.name.startswith("eos_cli_config_gen"):
        structured_config = deepcopy(molecule_host.hostvars)
    else:
        structured_config = deepcopy(molecule_host.structured_config)

    # If nothing raises, the model is accepted.
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        EosCliConfigGen(**structured_config)
