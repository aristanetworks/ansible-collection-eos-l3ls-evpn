# Copyright (c) 2019-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

DOCUMENTATION = r"""
---
module: inventory_to_container
version_added: "1.0.0"
author: Ansible Arista Team (@aristanetworks)
short_description: Transform information from inventory to arista.cvp collection
description:
  - Transform information from ansible inventory to be able to provision CloudVision Platform using arista.cvp collection and its specific data structure.
options:
  inventory:
    description: Optional YAML inventory file to parse. If not set the loaded inventory will be parsed.
    required: false
    type: str
  container_root:
    description: Ansible group name to consider to be Root of our topology.
    required: true
    type: str
  configlet_dir:
    description: Directory where intended configurations are located.
    required: false
    type: str
  configlet_prefix:
    description: Prefix to put on configlet.
    required: false
    default: 'AVD'
    type: str
  destination:
    description: Optional path to save variable.
    required: false
    type: str
  device_filter:
    description: Filter to apply intended mode on a set of configlet.
                 If not used, then module only uses ADD mode. device_filter
                 list devices that can be modified or deleted based
                 on configlets entries.
    required: false
    default: ['all']
    type: list
    elements: str
"""

EXAMPLES = r"""
- name: generate intended variables
  inventory_to_container:
    inventory: 'inventory.yml'
    container_root: 'DC1_FABRIC'
    configlet_dir: 'intended_configs'
    configlet_prefix: 'AVD'
    device_filter: ['DC1-LE']
    # destination: 'generated_vars/{{ inventory_hostname }}.yml'
  register: cvp_vars

- name: 'Collecting facts from CVP {{ inventory_hostname }}.'
  arista.cvp.cv_facts:
  register: cvp_facts

- name: 'Create configlets on CVP {{ inventory_hostname }}.'
  arista.cvp.cv_configlet:
    cvp_facts: "{{ cvp_facts.ansible_facts }}"
    configlets: "{{ cvp_vars.cvp_configlets }}"
    configlet_filter: ["AVD"]

- name: "Building Container topology on {{ inventory_hostname }}"
  arista.cvp.cv_container:
    topology: '{{ cvp_vars.cvp_topology }}'
    cvp_facts: '{{ cvp_facts.ansible_facts }}'
    save_topology: true
"""

import traceback
from pathlib import Path
from typing import Any

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.errors import AnsibleValidationError

TREELIB_IMP_ERR = None

try:
    from treelib import Node, Tree

    HAS_TREELIB = True
except ImportError:
    HAS_TREELIB = False
    TREELIB_IMP_ERR = traceback.format_exc()
    Tree = Node = object

YAML_IMP_ERR = None
try:
    import yaml

    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    YAML_IMP_ERR = traceback.format_exc()


# Root container on CloudVision.
# Shall not be changed unless CloudVision changes it in the core.
CVP_ROOT_CONTAINER = "Tenant"


def is_in_filter(hostname_filter: list | None = None, hostname: str = "eos") -> bool:
    """
    Check if device is part of the filter or not.

    Parameters
    ----------
    hostname_filter : list, optional
        Device filter, by default ['all']
    hostname : str
        Device hostname to compare against filter.

    Returns:
    -------
    boolean
        True if device hostname is part of filter. False if not.
    """
    # W102 Workaround to avoid list as default value.
    if hostname_filter is None:
        hostname_filter = ["all"]

    return "all" in hostname_filter or any(element in hostname for element in hostname_filter)


def is_iterable(testing_object: Any = None) -> bool | None:
    """
    Test if an object is iterable or not.

    Test if an object is iterable or not. If yes return True, else return False.

    Parameters
    ----------
    testing_object : any, optional
        Object to test if it is iterable or not, by default None
    """
    try:
        iter(testing_object)
    except TypeError:
        return False

    return True


def is_leaf(tree: Tree, nid: Node) -> bool:
    """
    Test if NodeID is a leaf with no nid attached to it.

    Parameters
    ----------
    tree : Tree
        Tree where NID is defined.
    nid : Node
        NodeID to test.

    Returns:
    -------
    boolean
        True if node is a leaf, false in other situation
    """
    return bool(nid and len(tree.is_branch(nid)) == 0)


def get_configlet(src_folder: str = "", prefix: str = "AVD", extension: str = "cfg", device_filter: list | None = None) -> dict:
    """
    Get available configlets to deploy to CVP.

    Parameters
    ----------
    src_folder : str, optional
        Path where to find configlet, by default ""
    prefix : str, optional
        Prefix to append to configlet name, by default 'AVD'
    extension : str, optional
        File extension to lookup configlet file, by default 'cfg'
    device_filter: list, optional
        List of filter to compare device configlet and to select only a subset of configlet.

    Returns:
    -------
    dict
        Dictionary of configlets found in source folder.
    """
    # W102 Workaround to avoid list as default value.
    if device_filter is None:
        device_filter = ["all"]

    src_configlets = Path(src_folder).glob(f"*.{extension}")
    configlets = {}
    for file in src_configlets:
        # Build structure only if configlet match device_filter.
        if is_in_filter(hostname=file.stem, hostname_filter=device_filter):
            name = f"{prefix}_{file.stem}" if prefix != "none" else file.stem
            with file.open(encoding="utf8") as stream:
                data = stream.read()
            configlets[name] = data
    return configlets


def get_device_option_value(device_data_dict: dict, option_name: str) -> str | None:
    """
    get_device_option_value Extract value of a host_var defined in inventory file.

    Read all variables under device in inventory.yml and return value.
    If not found return None

    Parameters
    ----------
    device_data_dict : dict
        Dict of options defined under device.
    option_name : string
        Name of option searched by function.

    Returns:
    -------
    string
        Value set for variable, else None
    """
    if is_iterable(device_data_dict):
        return next(
            (value for option, value in device_data_dict.items() if option_name == option),
            None,
        )
    return None


def serialize_yaml_inventory_data(dict_inventory: dict, parent_container: str | None = None, tree_topology: Tree | None = None) -> Tree:
    """
    Build a tree topology from YAML inventory file content.

    Parameters
    ----------
    dict_inventory : dict
        Inventory YAML content.
    parent_container : str, optional
        Registration of container N-1 for recursive function, by default None
    tree_topology : Tree, optional
        Tree topology built over iteration, by default None

    Returns:
    -------
    Tree
        complete container tree topology.
    """
    if is_iterable(dict_inventory):
        # Working with ROOT container for Fabric
        if tree_topology is None:
            # initiate tree topology and add ROOT under Tenant
            tree_topology = Tree()
            tree_topology.create_node("Tenant", "Tenant")
            parent_container = "Tenant"

        # Recursive Inventory read
        for k1, v1 in dict_inventory.items():
            # Read a leaf
            if is_iterable(v1) and "children" not in v1:
                tree_topology.create_node(k1, k1, parent=parent_container)
            # If subgroup has kids
            if is_iterable(v1) and "children" in v1:
                tree_topology.create_node(k1, k1, parent=parent_container)
                serialize_yaml_inventory_data(dict_inventory=v1["children"], parent_container=k1, tree_topology=tree_topology)
            elif k1 == "children" and is_iterable(v1):
                # Extract sub-group information
                for k2, v2 in v1.items():
                    # Add subgroup to tree
                    tree_topology.create_node(k2, k2, parent=parent_container)
                    serialize_yaml_inventory_data(dict_inventory=v2, parent_container=k2, tree_topology=tree_topology)
        return tree_topology
    return None


def get_devices(dict_inventory: dict | None, search_container: str | None = None, devices: list[str] | None = None, device_filter: list | None = None) -> list:
    """
    Get devices attached to a container.

    Parameters
    ----------
    dict_inventory : dict
        Inventory YAML content.
    search_container : str, optional
        Container to look for, by default None
    devices : str, optional
        List of found devices attached to container, by default empty list []
    device_filter: list, optional
        List of filter to compare device name and to select only a subset of devices.

    Returns:
    -------
    list
        List of found devices.
    """
    # W102 Workaround to avoid list as default value.
    if device_filter is None:
        device_filter = ["all"]
    if dict_inventory is None:
        return devices

    for k1, v1 in dict_inventory.items():
        # Read a leaf
        if k1 == search_container and is_iterable(v1) and "hosts" in v1:
            for dev, data in v1["hosts"].items():
                if (
                    is_in_filter(hostname_filter=device_filter, hostname=dev)
                    and get_device_option_value(device_data_dict=data, option_name="is_deployed") is not False
                ):
                    devices.append(dev)
        # If subgroup has kids
        if is_iterable(v1) and "children" in v1:
            get_devices(dict_inventory=v1["children"], search_container=search_container, devices=devices, device_filter=device_filter)
        elif k1 == "children" and is_iterable(v1):
            # Extract sub-group information
            for v2 in v1.values():
                get_devices(dict_inventory=v2, search_container=search_container, devices=devices, device_filter=device_filter)
    return devices


def get_containers(inventory_content: dict, parent_container: str, device_filter: list | None) -> dict:
    """
    get_containers - Build Container topology to build on CoudVision.

    Parameters
    ----------
    inventory_content : dict
        Inventory loaded using a YAML input.
    parent_container : string
        Root of tree lookup
    device_filter : list, optional
        List of filter to compare device name and to select only a subset of devices.

    Returns:
    -------
    JSON
        CVP Container structure to use with cv_container.
    """
    serialized_inventory = serialize_yaml_inventory_data(dict_inventory=inventory_content)
    tree_dc = serialized_inventory.subtree(parent_container)
    container_list = [tree_dc[node].tag for node in tree_dc.expand_tree()]
    container_json = {}
    for container in container_list:
        data = {}
        if container != CVP_ROOT_CONTAINER:
            parent = tree_dc.parent(container)
            if container == parent_container:
                data["parent_container"] = CVP_ROOT_CONTAINER
            elif parent.tag != CVP_ROOT_CONTAINER:
                if is_leaf(tree=tree_dc, nid=container):
                    devices = get_devices(dict_inventory=inventory_content, search_container=container, devices=[], device_filter=device_filter)
                    data["devices"] = devices
                data["parent_container"] = parent.tag
            container_json[container] = data
    return container_json


def main() -> None:
    """Main entry point for module execution."""
    argument_spec = {
        "inventory": {"type": "str", "required": False},
        "container_root": {"type": "str", "required": True},
        "configlet_dir": {"type": "str", "required": False},
        "configlet_prefix": {"type": "str", "required": False, "default": "AVD"},
        "destination": {"type": "str", "required": False},
        "device_filter": {"type": "list", "elements": "str", "default": "all"},
    }

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)
    result = {"changed": False}

    if not HAS_YAML:
        module.fail_json(msg="yaml lib is required for this module")

    # Build cv_container structure from YAML inventory.
    # Notice that if 'inventory' is not set, the action plugin will append the CVP_TOPOLOGY based on the loaded inventory.
    if module.params["inventory"] is not None and module.params["container_root"] is not None:
        if not HAS_TREELIB:
            module.fail_json(msg="Treelib lib is required for this module, when reading inventory from YAML inventory file")

        # "ansible-avd/examples/evpn-l3ls-cvp-deployment/inventory.yml"
        inventory_file = module.params["inventory"]
        parent_container = module.params["container_root"]
        # Build containers & devices topology
        inventory_content = ""
        with Path(inventory_file).open(encoding="utf8") as stream:
            try:
                # add a constructor to return "!VAULT" for inline vault variables
                # to avoid the parse
                yaml.SafeLoader.add_constructor("!vault", lambda _, __: "!VAULT")
                inventory_content = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                msg = "Failed to parse inventory file"
                raise AnsibleValidationError(msg) from exc
        result["cvp_topology"] = get_containers(
            inventory_content=inventory_content,
            parent_container=parent_container,
            device_filter=module.params["device_filter"],
        )

    # If set, build configlet topology
    if module.params["configlet_dir"] is not None:
        result["cvp_configlets"] = get_configlet(
            src_folder=module.params["configlet_dir"],
            prefix=module.params["configlet_prefix"],
            device_filter=module.params["device_filter"],
        )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
