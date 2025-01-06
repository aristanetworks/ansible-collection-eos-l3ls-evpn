# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from copy import deepcopy

import pytest

from pyavd import validate_inputs
from tests.models import MoleculeHost


# eos_cli_config_gen inputs are validated by `validate_structured_config` in another file.
@pytest.mark.molecule_scenarios(
    "eos_designs_unit_tests",
    "eos_designs_deprecated_vars",
    "eos_designs_l2l2",
    "eos_designs-mpls-isis-sr-ldp",
    "eos_designs-twodc-5stage-clos",
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
)
def test_validate_inputs_with_valid_inputs(molecule_host: MoleculeHost) -> None:
    """Test validate_inputs."""
    inputs = deepcopy(molecule_host.hostvars)
    validation_result = validate_inputs(inputs)
    assert validation_result.validation_errors == []
    assert validation_result.failed is False
