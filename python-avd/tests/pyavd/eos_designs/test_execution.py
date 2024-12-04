# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.shared_utils import SharedUtils
from pyavd._eos_designs.structured_config.execution import RegisterForExecution, StructuredConfigExecutor
from pyavd._eos_designs.structured_config.structured_config_generator import StructuredConfigGenerator
from pyavd._schema.avdschema import AvdSchema

Tenant = EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem
Vrf = EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem
L2Vlan = EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem
Svi = EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem


def test_register_for_execution() -> None:
    """We should not need to test every execution variant, since the decorator is not handling them differently."""

    class Test(StructuredConfigGenerator):
        def __init__(self) -> None:  # pylint: disable=super-init-not-called
            self.result = []

        @RegisterForExecution("pre")
        def pre_1(self) -> None:
            pass

        @RegisterForExecution("pre")
        def pre_2(self) -> None:
            pass

    test = Test()
    assert test._cls_method_execution_registry["pre"] == ["pre_1", "pre_2"]


def test_executor() -> None:
    hostvars = {
        "inventory_hostname": "testhost",
        "fabric_name": "testfabric",
        "type": "l3spine",
        "l3spine": {"defaults": {"filter": {"always_include_vrfs_in_tenants": ["tenant1", "tenant2"]}}},
        "tenants": [{"name": "tenant1", "vrfs": [{"name": "vrf2"}]}, {"name": "tenant2", "vrfs": [{"name": "vrf1"}, {"name": "vrf2"}]}],
    }
    inputs = EosDesigns._from_dict(hostvars)
    structured_config = EosCliConfigGen()

    class Test(StructuredConfigGenerator):
        @RegisterForExecution("pre")
        def pre_1(self) -> None:
            self.structured_config.vlans.append(EosCliConfigGen.VlansItem(id=len(self.structured_config.vlans) + 1, name=type(self).__name__ + "_pre_1"))

        @RegisterForExecution("pre")
        def pre_2(self) -> None:
            self.structured_config.vlans.append(EosCliConfigGen.VlansItem(id=len(self.structured_config.vlans) + 1, name=type(self).__name__ + "_pre_2"))

        @RegisterForExecution("per_vrf")
        def add_vlan_per_vrf(self, vrf: Vrf, tenant: Tenant) -> None:
            self.structured_config.vlans.append(
                EosCliConfigGen.VlansItem(
                    id=len(self.structured_config.vlans) + 1, name=type(self).__name__ + "_per_vrf_" + vrf.name + "_tenant_" + tenant.name
                )
            )

        @RegisterForExecution("post")
        def post(self) -> None:
            self.structured_config.vlans.append(EosCliConfigGen.VlansItem(id=len(self.structured_config.vlans) + 1, name=type(self).__name__ + "_post"))

    class Test2(StructuredConfigGenerator):
        @RegisterForExecution("pre")
        def pre_1(self) -> None:
            self.structured_config.vlans.append(EosCliConfigGen.VlansItem(id=len(self.structured_config.vlans) + 1, name=type(self).__name__ + "_pre_1"))

        @RegisterForExecution("per_tenant")
        def add_vlan_per_tenant(self, tenant: Tenant) -> None:
            self.structured_config.vlans.append(
                EosCliConfigGen.VlansItem(id=len(self.structured_config.vlans) + 1, name=type(self).__name__ + "_per_tenant_" + tenant.name)
            )

    executor = StructuredConfigExecutor(
        hostvars=hostvars,
        inputs=inputs,
        structured_config=structured_config,
        custom_structured_configurations=[],
        shared_utils=SharedUtils(hostvars=hostvars, inputs=inputs, templar=None, schema=AvdSchema(schema_id="eos_designs")),
        classes=(Test, Test2),
    )

    # _method_execution_registry is a dict of lists of tuples like {"pre": [(<cls instance>, "<method name>")]}
    assert executor._method_execution_registry["pre"][0][0].__class__ == Test
    assert executor._method_execution_registry["pre"][0][1] == "pre_1"
    assert executor._method_execution_registry["pre"][1][0].__class__ == Test
    assert executor._method_execution_registry["pre"][1][1] == "pre_2"
    assert executor._method_execution_registry["pre"][2][0].__class__ == Test2
    assert executor._method_execution_registry["pre"][2][1] == "pre_1"
    assert executor._method_execution_registry["per_tenant"][0][0].__class__ == Test2
    assert executor._method_execution_registry["per_tenant"][0][1] == "add_vlan_per_tenant"
    assert executor._method_execution_registry["per_vrf"][0][0].__class__ == Test
    assert executor._method_execution_registry["per_vrf"][0][1] == "add_vlan_per_vrf"
    assert executor._method_execution_registry["post"][0][0].__class__ == Test
    assert executor._method_execution_registry["post"][0][1] == "post"

    executor.execute()

    # Structured config was updated in the order of execution
    # First all the pre tasks
    assert structured_config.vlans[1] == EosCliConfigGen.VlansItem(id=1, name="Test_pre_1")
    assert structured_config.vlans[2] == EosCliConfigGen.VlansItem(id=2, name="Test_pre_2")
    assert structured_config.vlans[3] == EosCliConfigGen.VlansItem(id=3, name="Test2_pre_1")
    # Then we iterate per Tenant
    assert structured_config.vlans[4] == EosCliConfigGen.VlansItem(id=4, name="Test2_per_tenant_tenant1")
    # Inside the first Tenant we iterate per VRF
    assert structured_config.vlans[5] == EosCliConfigGen.VlansItem(id=5, name="Test_per_vrf_vrf2_tenant_tenant1")
    # Then the next Tenant
    assert structured_config.vlans[6] == EosCliConfigGen.VlansItem(id=6, name="Test2_per_tenant_tenant2")
    # Inside the second Tenant we iterate again per VRF
    assert structured_config.vlans[7] == EosCliConfigGen.VlansItem(id=7, name="Test_per_vrf_vrf1_tenant_tenant2")
    assert structured_config.vlans[8] == EosCliConfigGen.VlansItem(id=8, name="Test_per_vrf_vrf2_tenant_tenant2")
    # Finally all the post tasks
    assert structured_config.vlans[9] == EosCliConfigGen.VlansItem(id=9, name="Test_post")

    assert len(executor.graph()) > 0  # TODO: Figure out how we can validate that this mermaid diagram.
