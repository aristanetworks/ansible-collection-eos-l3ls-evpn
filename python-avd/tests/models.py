# Copyright (c) 2024 Arista Networks, Inc.
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


class MoleculeHost:
    name: str
    ansible_host: AnsibleHost
    scenario: MoleculeScenario

    def __init__(self, name: str, ansible_host: AnsibleHost, scenario: MoleculeScenario) -> None:
        self.name = name
        self.ansible_host = ansible_host
        self.scenario = scenario

    @cached_property
    def structured_config(self) -> dict:
        structured_config_path = self.scenario.path / "intended/structured_configs" / f"{self.name}.yml"
        if not structured_config_path.exists():
            return {}

        return load(structured_config_path.read_text(), CSafeLoader)

    @cached_property
    def config(self) -> str | None:
        config_path = self.scenario.path / "intended/configs" / f"{self.name}.cfg"
        if not config_path.exists():
            return None

        return config_path.read_text()

    @cached_property
    def doc(self) -> str | None:
        doc_path = self.scenario.path / "documentation/devices" / f"{self.name}.md"
        if not doc_path.exists():
            return None

        return doc_path.read_text()

    @cached_property
    def hostvars(self) -> dict:
        return json.loads(json.dumps(self.scenario._vars.get_vars(host=self.ansible_host)))


class MoleculeScenario:
    name: str
    path: Path
    hosts: list[MoleculeHost]

    def __init__(self, name: str) -> None:
        self.name = name
        self.path = MOLECULE_PATH / name
        self._inventory = InventoryManager(loader=DataLoader(), sources=[(self.path / "inventory/hosts.yml").as_posix()])
        self._vars = VariableManager(loader=DataLoader(), inventory=self._inventory)
        self.hosts = []
        for host in self._inventory.get_hosts():
            if "IGNORE_IN_PYTEST" in [group.name for group in host.groups]:
                continue
            self.hosts.append(MoleculeHost(name=host.name, ansible_host=host, scenario=self))

    @cached_property
    def avd_facts(self) -> dict:
        return get_avd_facts({host.name: deepcopy(host.hostvars) for host in self.hosts})
