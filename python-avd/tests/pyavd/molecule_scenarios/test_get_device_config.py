# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from copy import deepcopy

import pytest

from pyavd import get_device_config, validate_structured_config
from pyavd._utils import get
from tests.models import MoleculeHost


@pytest.mark.molecule_scenarios(
    "eos_designs_unit_tests",
    "eos_designs_deprecated_vars",
    "eos_cli_config_gen",
    "eos_cli_config_gen_deprecated_vars",
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
def test_get_device_config(molecule_host: MoleculeHost) -> None:
    """Test get_device_config."""
    # Loading inputs first and then updating structured config on top.
    # This is how Ansible behaves, so we need this to generate the same configs.
    # The underlying cause is eos_cli_config_gen inputs being set in eos_designs molecule vars,
    #   which are then _not_ included in the structured_config, hence lost unless we include the
    #   inputs as well.
    structured_config: dict = deepcopy(molecule_host.hostvars)
    structured_config.update(deepcopy(molecule_host.structured_config))
    expected_config = molecule_host.config

    if not get(structured_config, "eos_cli_config_gen_configuration.enable", default=True):
        return

    # run validation on structured_config to ensure it is converted
    validate_structured_config(structured_config)

    device_config = get_device_config(structured_config)

    assert isinstance(device_config, str)
    assert device_config == expected_config
