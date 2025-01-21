# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from copy import deepcopy

import pytest

from pyavd import get_device_doc, validate_structured_config
from pyavd._utils import get
from tests.models import MoleculeHost


@pytest.mark.molecule_scenarios(
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
def test_get_device_doc(molecule_host: MoleculeHost) -> None:
    """Test get_device_config."""
    # Loading inputs first and then updating structured config on top.
    # This is how Ansible behaves, so we need this to generate the same configs.
    # The underlying cause is eos_cli_config_gen inputs being set in eos_designs molecule vars,
    #   which are then _not_ included in the structured_config, hence lost unless we include the
    #   inputs as well.
    structured_config: dict = deepcopy(molecule_host.hostvars)
    structured_config.update(deepcopy(molecule_host.structured_config))

    if not get(structured_config, "eos_cli_config_gen_documentation.enable", default=True):
        return

    # TODO: Deprecated, remove in 6.0.0
    if not get(structured_config, "generate_device_documentation", default=True):
        return

    # run validation on structured_config to ensure it is covered
    validate_structured_config(structured_config)

    expected_doc = molecule_host.doc
    add_md_toc = get(structured_config, "eos_cli_config_gen_documentation.toc", default=True)
    device_doc = get_device_doc(structured_config, add_md_toc=add_md_toc)

    assert isinstance(device_doc, str)
    assert device_doc == expected_doc
