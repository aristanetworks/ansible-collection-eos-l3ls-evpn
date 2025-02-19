# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from copy import deepcopy

import pytest

from pyavd import validate_structured_config
from pyavd._errors import AvdValidationError
from pyavd.avd_schema_tools import AvdSchemaTools
from tests.models import MoleculeHost

SCHEMA = AvdSchemaTools(schema_id="eos_cli_config_gen").avdschema._schema


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
def test_validate_structured_config_with_valid_data(molecule_host: MoleculeHost) -> None:
    """Test validate_structured_config."""
    if molecule_host.scenario.name.startswith("eos_cli_config_gen"):
        structured_config = deepcopy(molecule_host.hostvars)
    else:
        structured_config = deepcopy(molecule_host.structured_config)

    validation_result = validate_structured_config(structured_config)
    assert validation_result.validation_errors == []
    assert validation_result.failed is False


@pytest.mark.molecule_scenarios(
    "eos_designs_unit_tests",
    "eos_designs_deprecated_vars",
)
def test_validate_structured_config_with_invalid_data(molecule_host: MoleculeHost) -> None:
    """Test validate_structured_config."""
    if molecule_host.scenario.name.startswith("eos_cli_config_gen"):
        structured_config = deepcopy(molecule_host.hostvars)
    else:
        structured_config = deepcopy(molecule_host.structured_config)

    updated = False
    # Insert a bad key in a random dict (making sure the dict is covered by the schema)
    for key, value in structured_config.items():
        if not isinstance(value, dict) or "structured_config" in key or key not in SCHEMA["keys"]:
            continue
        value.update({"invalid_key": "some_value"})
        updated = True
        break

    # No dict found, so we insert our own instead
    if not updated:
        structured_config.update({"router_bgp": {"invalid_key": "some_value"}})

    validation_result = validate_structured_config(structured_config)
    assert validation_result.failed is True
    assert len(validation_result.validation_errors) >= 1
    assert isinstance(validation_result.validation_errors[0], AvdValidationError)
    assert "invalid_key" in str(validation_result.validation_errors[0])
