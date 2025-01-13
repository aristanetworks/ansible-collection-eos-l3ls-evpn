# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


import json
import logging
import os

import pytest
import treelib
import yaml

from ansible_collections.arista.avd.plugins.modules.inventory_to_container import (
    get_containers,
    get_device_option_value,
    get_devices,
    is_in_filter,
    is_iterable,
    is_leaf,
)
from ansible_collections.arista.avd.plugins.modules.inventory_to_container import serialize_yaml_inventory_data as serialize

IS_ITERABLE_VALID = [
    ("string1", "string2", "string3", "string4"),
    {"key1": "value1", "key2": "value2", "key3": "value3"},
    ["string1", "string2", "string3", "string4"],
    "string1",
]

IS_ITERABLE_INVALID = [None, 0]

PARENT_CONTAINER = {
    "default_parent": {
        "parent": "Tenant",
        "expected_output": {
            "all": {},
            "CVP": {"devices": ["cv_ztp", "cv_server"], "parent_container": "all"},
            "DC1": {"parent_container": "all"},
            "DC1_FABRIC": {"parent_container": "DC1"},
            "DC1_L2LEAFS": {"parent_container": "DC1_FABRIC"},
            "DC1_L2LEAF1": {"devices": ["DC1-L2LEAF1A"], "parent_container": "DC1_L2LEAFS"},
            "DC1_L2LEAF2": {"devices": ["DC1-L2LEAF2A"], "parent_container": "DC1_L2LEAFS"},
            "DC1_L3LEAFS": {"parent_container": "DC1_FABRIC"},
            "DC1_LEAF1": {"devices": ["DC1-LEAF1A", "DC1-LEAF1B"], "parent_container": "DC1_L3LEAFS"},
            "DC1_LEAF2": {"devices": ["DC1-LEAF2A", "DC1-LEAF2B"], "parent_container": "DC1_L3LEAFS"},
            "DC1_SPINES": {"devices": ["DC1-SPINE1", "DC1-SPINE2"], "parent_container": "DC1_FABRIC"},
            "DC1_SERVERS": {"devices": [], "parent_container": "DC1"},
            "DC1_TENANTS_NETWORKS": {"devices": [], "parent_container": "DC1"},
        },
    },
    "non_default_parent": {"parent": "CVP", "expected_output": {"CVP": {"parent_container": "Tenant"}}},
}

INVENTORY_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/../../inventory/inventory.yml"

ROOT_CONTAINER = "Tenant"
NON_DEFAULT_PARENT_CONTAINER = "DC2"
SEARCH_CONTAINER = "DC1_SPINES"
GET_DEVICES = ["DC1-SPINE1", "DC1-SPINE2"]
GET_DEVICE_FILTER = "SPINE2"

HOSTNAME_VALID = "test1.aristanetworks.com"
HOSTNAME_INVALID = "test1.bsn.com"
HOSTNAME_FILTER_VALID = ["arista", "aristanetworks"]
HOSTNAME_FILTER_INVALID = "aristanetworks"

TREELIB = treelib.tree.Tree()
TREELIB.create_node("Tenant", "Tenant")
TREELIB.create_node("CVP", "CVP", parent="Tenant")
TREELIB.create_node("DC1", "DC1", parent="Tenant")
TREELIB.create_node("Leaf1", "Leaf1", parent="DC1")
TREELIB.create_node("Leaf2", "Leaf2", parent="DC1")
TREELIB_VALID_LEAF = "Leaf1"
TREELIB_INVALID_LEAF = "DC1"


@pytest.fixture(scope="session")
def inventory():
    yaml.SafeLoader.add_constructor("!vault", lambda _, __: "!VAULT")
    with open(INVENTORY_FILE, encoding="utf8") as stream:
        try:
            inventory_content = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            logging.exception(e)
            return None
        return inventory_content


class TestInventoryToContainer:
    def test_is_in_filter_default_filter(self) -> None:
        output = is_in_filter(hostname=HOSTNAME_VALID)
        assert output

    def test_is_in_filter_valid_hostname(self) -> None:
        output = is_in_filter(hostname_filter=HOSTNAME_FILTER_VALID, hostname=HOSTNAME_VALID)
        assert output

    def test_is_in_filter_invalid_hostname(self) -> None:
        output = is_in_filter(hostname_filter=HOSTNAME_FILTER_VALID, hostname=HOSTNAME_INVALID)
        assert output is False

    # TODO: Check if this is a valid testcase. Add a type check?
    def test_is_in_filter_invalid_filter(self) -> None:
        output = is_in_filter(hostname_filter=HOSTNAME_FILTER_INVALID, hostname=HOSTNAME_VALID)
        assert output

    def test_is_iterable_default_iterable(self) -> None:
        output = is_iterable()
        assert output is False

    @pytest.mark.parametrize("DATA", IS_ITERABLE_VALID)
    def test_is_iterable_valid_iterable(self, DATA) -> None:
        output = is_iterable(DATA)
        assert output

    @pytest.mark.parametrize("DATA", IS_ITERABLE_INVALID)
    def test_is_iterable_invalid_iterable(self, DATA) -> None:
        output = is_iterable(DATA)
        assert output is False

    def test_is_leaf_valid_leaf(self) -> None:
        output = is_leaf(TREELIB, TREELIB_VALID_LEAF)
        assert output

    def test_is_leaf_invalid_leaf(self) -> None:
        output = is_leaf(TREELIB, TREELIB_INVALID_LEAF)
        assert output is False

    def test_is_leaf_none_leaf(self) -> None:
        output = is_leaf(TREELIB, None)
        assert output is False

    def test_get_device_option_value_valid(self, inventory) -> None:
        data = inventory["all"]["children"]["CVP"]["hosts"]
        output = get_device_option_value(device_data_dict=data, option_name="cv_server")
        assert output
        assert isinstance(output, dict)

    def test_get_device_option_value_invalid(self, inventory) -> None:
        data = inventory["all"]["children"]["CVP"]["hosts"]
        output = get_device_option_value(device_data_dict=data, option_name="is_deployed")
        assert output is None

    def test_get_device_option_value_none(self, inventory) -> None:
        data = inventory["all"]["children"]["CVP"]["hosts"]
        output = get_device_option_value(device_data_dict=data, option_name=None)
        assert output is None

    def test_get_device_option_value_empty_data(self, inventory) -> None:
        output = get_device_option_value(device_data_dict=None, option_name="cv_server")
        assert output is None

    def test_get_devices_empty_inventory(self) -> None:
        output = get_devices(None)
        assert output is None

    def test_get_devices_default_search_container(self, inventory) -> None:
        output = get_devices(inventory)
        assert output is None

    def test_get_devices_non_default_search_container(self, inventory) -> None:
        output = get_devices(inventory, search_container=SEARCH_CONTAINER, devices=[])
        assert output == GET_DEVICES

    def test_get_devices_preexisting_devices(self, inventory) -> None:
        devices = ["TEST_DEVICE"]
        output = get_devices(inventory, search_container=SEARCH_CONTAINER, devices=devices)
        assert output == ["TEST_DEVICE", *GET_DEVICES]

    def test_get_devices_preexisting_devices_with_device_filter(self, inventory) -> None:
        output = get_devices(inventory, search_container=SEARCH_CONTAINER, devices=[], device_filter=[GET_DEVICE_FILTER])
        assert [GET_DEVICE_FILTER in item for item in output]

    @pytest.mark.parametrize("DATA", [None])
    def test_serialize_empty_inventory(self, DATA) -> None:
        output = serialize(DATA)
        assert output is None

    def test_serialize_valid_inventory(self, inventory) -> None:
        output = serialize(inventory)
        assert isinstance(output, treelib.tree.Tree)
        tree_dict = json.loads(output.to_json())
        assert next(iter(tree_dict.keys())) == ROOT_CONTAINER

    @pytest.mark.parametrize("DATA", PARENT_CONTAINER.values(), ids=PARENT_CONTAINER.keys())
    def test_serialize_parent_container(self, DATA, inventory) -> None:
        output = serialize(inventory, parent_container=DATA["parent"])
        assert isinstance(output, treelib.tree.Tree)
        tree_dict = json.loads(output.to_json())
        assert next(iter(tree_dict.keys())) == ROOT_CONTAINER

    def test_serialize_none_parent_container_with_tree_topology(self, inventory) -> None:
        tree = treelib.tree.Tree()
        output = serialize(inventory, tree_topology=tree)
        assert isinstance(output, treelib.tree.Tree)
        tree_dict = json.loads(output.to_json())
        assert next(iter(tree_dict.keys())) == "all"

    def test_serialize_non_default_parent_container_with_tree_topology(self, inventory) -> None:
        tree = treelib.tree.Tree()
        tree.create_node(NON_DEFAULT_PARENT_CONTAINER, NON_DEFAULT_PARENT_CONTAINER)
        output = serialize(inventory, parent_container=NON_DEFAULT_PARENT_CONTAINER, tree_topology=tree)
        tree_dict = json.loads(output.to_json())
        assert next(iter(tree_dict.keys())) == NON_DEFAULT_PARENT_CONTAINER

    @pytest.mark.parametrize("DATA", PARENT_CONTAINER.values(), ids=PARENT_CONTAINER.keys())
    def test_get_containers(self, DATA, inventory) -> None:
        output = get_containers(inventory, parent_container=DATA["parent"], device_filter=["all"])
        assert output == DATA["expected_output"]
