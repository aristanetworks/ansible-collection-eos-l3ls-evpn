# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import warnings
from copy import deepcopy

import pytest

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._schema.store import create_store
from tests.models import MoleculeHost

SCHEMA = create_store()["eos_designs"]

CSC_DATA = {
    "fabric_name": "test",
    "custom_structured_configuration_router_bgp": {"as": 123},
    "csc_loopback_interfaces": [{"name": "Loopback0"}],
}

CSC_TESTS = [
    # prefix, expected_data
    (
        None,
        EosDesigns._CustomStructuredConfigurations(
            [
                EosDesigns._CustomStructuredConfigurationsItem(
                    key="custom_structured_configuration_router_bgp", value=EosCliConfigGen(router_bgp=EosCliConfigGen.RouterBgp(field_as="123"))
                )
            ]
        ),
    ),  # Notice the auto conversion to string.
    (
        ["csc_"],
        EosDesigns._CustomStructuredConfigurations(
            [
                EosDesigns._CustomStructuredConfigurationsItem(
                    key="csc_loopback_interfaces",
                    value=EosCliConfigGen(loopback_interfaces=EosCliConfigGen.LoopbackInterfaces([EosCliConfigGen.LoopbackInterfacesItem(name="Loopback0")])),
                )
            ]
        ),
    ),
]


@pytest.mark.parametrize(("prefix", "expected_data"), CSC_TESTS)
def test_eos_designs_custom_structured_configuration(prefix: str | None, expected_data: EosDesigns._CustomStructuredConfigurations) -> None:
    data = CSC_DATA.copy()
    if prefix:
        data.update({"custom_structured_configuration_prefix": prefix})
    loaded_model = EosDesigns._from_dict(data)
    assert hasattr(loaded_model, "_custom_structured_configurations")
    assert isinstance(loaded_model._custom_structured_configurations, EosDesigns._CustomStructuredConfigurations)

    for entry in loaded_model._custom_structured_configurations:
        assert isinstance(entry, EosDesigns._CustomStructuredConfigurationsItem)

    assert repr(loaded_model._custom_structured_configurations) == repr(expected_data)


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
def test_eos_designs_initialize_kwargs_with_valid_data(molecule_host: MoleculeHost) -> None:
    """Test EosDesigns model with valid data."""
    inputs = deepcopy(molecule_host.hostvars)

    # The class will not accept _custom_keys to be given directly. They must be given as `_custom_data: <dict>`.
    # This is normally handled by the loader, but since we here test loading with kwargs, we need to remove any
    # custom keys from the test data.
    inputs = {k: v for k, v in inputs.items() if not str(k).startswith("_")}

    # If nothing raises, the model is accepted.
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        EosDesigns(**inputs)


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
def test_eos_designs_initialize_dict_with_valid_data(molecule_host: MoleculeHost) -> None:
    """Test EosDesigns model with valid data."""
    inputs = deepcopy(molecule_host.hostvars)

    # If nothing raises, the model is accepted.
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        EosDesigns._from_dict(inputs)
