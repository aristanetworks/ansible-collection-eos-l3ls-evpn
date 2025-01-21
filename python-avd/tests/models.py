# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from copy import deepcopy
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING

from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from yaml import CSafeLoader, load

from pyavd import get_avd_facts

if TYPE_CHECKING:
    from ansible.inventory.host import Host as AnsibleHost

REPO_ROOT = Path(__file__).parents[2]
MOLECULE_PATH = REPO_ROOT / "ansible_collections/arista/avd/molecule"
EXAMPLE_PATH = REPO_ROOT / "ansible_collections/arista/avd/examples"


class MoleculeHost:
    """Class representing one host defined in a Molecule scenario."""

    name: str
    ansible_host: AnsibleHost
    scenario: MoleculeScenario

    def __init__(self, name: str, ansible_host: AnsibleHost, scenario: MoleculeScenario) -> None:
        self.name = name
        self.ansible_host = ansible_host
        self.scenario = scenario

    @cached_property
    def structured_config(self) -> dict:
        """The intended structured config for the host, as read from the YAML file in the molecule scenario."""
        structured_config_path = self.scenario.path / "intended/structured_configs" / f"{self.name}.yml"
        if not structured_config_path.exists():
            return {}

        return load(structured_config_path.read_text(), CSafeLoader)

    @cached_property
    def config(self) -> str | None:
        """The intended EOS config for the host, as read from the cfg file in the molecule scenario."""
        config_path = self.scenario.path / "intended/configs" / f"{self.name}.cfg"
        if not config_path.exists():
            return None

        return config_path.read_text()

    @cached_property
    def doc(self) -> str | None:
        """The intended MarkDown documentation for the host, as read from the md file in the molecule scenario."""
        doc_path = self.scenario.path / "documentation/devices" / f"{self.name}.md"
        if not doc_path.exists():
            return None

        return doc_path.read_text()

    @cached_property
    def hostvars(self) -> dict:
        """The input vars for the host, as read from the Ansible inventory in the molecule scenario."""
        return json.loads(json.dumps(self.scenario._vars.get_vars(host=self.ansible_host)))


class MoleculeScenario:
    """Class representing one Molecule scenario."""

    name: str
    path: Path
    hosts: list[MoleculeHost]

    def __init__(self, name: str) -> None:
        """
        Class representing one Molecule scenario.

        Args:
            name: Molecule scenario name

        The Ansible inventory of the Molecule scenario will be parsed and MoleculeHost instances will be inserted into the `hosts` property
        for each host found in the inventory.
        """
        self.name = name
        if name.startswith("example-"):
            # Example paths
            self.path = EXAMPLE_PATH / name.removeprefix("example-")
            inventory_path = self.path / "inventory.yml"
        else:
            # Molecule paths
            self.path = MOLECULE_PATH / name
            inventory_path = self.path / "inventory/hosts.yml"

        self._inventory = InventoryManager(loader=DataLoader(), sources=[inventory_path.as_posix()])
        self._vars = VariableManager(loader=DataLoader(), inventory=self._inventory)
        self.hosts = []
        for host in self._inventory.get_hosts():
            if self.name.startswith("example-") and host.name in ["cvp", "cloudvision"]:
                # Ignore CVP devices in examples without bloating the example without test groups.
                continue
            if "IGNORE_IN_PYTEST" in [group.name for group in host.groups]:
                # Ignore members of the group IGNORE_IN_PYTEST from Molecule scenarios.
                continue
            self.hosts.append(MoleculeHost(name=host.name, ansible_host=host, scenario=self))

    @cached_property
    def avd_facts(self) -> dict:
        """The AVD facts calculated from the full Ansible inventory in the molecule scenario."""
        return get_avd_facts({host.name: deepcopy(host.hostvars) for host in self.hosts})
