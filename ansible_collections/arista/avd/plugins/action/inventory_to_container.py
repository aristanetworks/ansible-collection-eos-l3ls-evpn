# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from typing import TYPE_CHECKING, Any

import yaml
from ansible.errors import AnsibleActionFail
from ansible.inventory.group import Group
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.plugins.action import ActionBase
from ansible.utils.display import Display

if TYPE_CHECKING:
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager

# Root container on CloudVision.
# Shall not be changed unless CloudVision changes it in the core.
CVP_ROOT_CONTAINER = "Tenant"

display = Display()


class ActionModule(ActionBase):
    def _maybe_convert_device_filter(self) -> None:
        # Converting string device filter to list
        device_filter = self._task.args.get("device_filter")
        if device_filter is not None and not isinstance(device_filter, list):
            display.debug(f"device_filter must be of type list, got '{device_filter}' of type {type(device_filter)} instead. Converting...")
            self._task.args["device_filter"] = [device_filter]

    def run(self, tmp: Any = None, task_vars: dict | None = None) -> dict:
        if task_vars is None:
            task_vars = {}

        self._maybe_convert_device_filter()

        module_args = self._task.args.copy()

        # Run regular module
        result = self._execute_module(module_name="inventory_to_container", module_args=module_args, task_vars=task_vars, tmp=tmp)

        if not result.get("failed") and module_args.get("inventory") is None and module_args.get("container_root") is not None:
            result["cvp_topology"] = self.build_cvp_topology_from_inventory(task_vars, module_args)

        # Write vars to file if set by user
        destination = module_args.get("destination")
        if destination is not None:
            # file should only contain subset of result data, so we build a smaller dict
            file_data_keys = ["cvp_configlets", "cvp_topology"]
            file_data = {key: result[key] for key in file_data_keys if key in result}

            with Path(destination).open("w", encoding="utf8") as file:
                yaml.dump(file_data, file, Dumper=AnsibleDumper)

        return result

    def build_cvp_topology_from_inventory(self, task_vars: dict, module_args: dict) -> dict:
        # Inventory Manager is the Ansible Class handling everything about hosts and groups
        inventory_manager: InventoryManager = task_vars["hostvars"]._inventory

        # Container root is the name of the Ansible group to use as root of the tree structure
        container_root = module_args["container_root"]

        # Device filter is a list with default value ["all"]
        device_filter = module_args.get("device_filter", ["all"])

        # Verify that the group referenced in 'container_root' is valid
        if container_root not in inventory_manager.groups:
            msg = f"Group '{container_root}' given as 'container_root' argument on 'arista.avd.inventory_to_container' cannot be found in Ansible inventory"
            raise AnsibleActionFail(msg)

        # cvp_topology holds the final output data
        cvp_topology = {}

        # Ansible Group object for the 'container_root' group.
        root_group: Group = inventory_manager.groups[container_root]

        # Build data for root group with hardcoded root container name as parent
        cvp_topology[container_root] = self.get_group_data(root_group, device_filter, parent_container=CVP_ROOT_CONTAINER)

        # Extract list of all groups starting from root group
        all_groups_below_root = root_group.get_descendants()

        # Build set of groups allowed to be parents.
        all_groups_from_root = all_groups_below_root.copy()
        all_groups_from_root.add(root_group)

        # Build data for each group below root
        for group in all_groups_below_root:
            cvp_topology[group.name] = self.get_group_data(group, device_filter, all_groups_from_root)

        return cvp_topology

    def get_group_data(self, group: Group, device_filter: list, all_groups_from_root: set | None = None, parent_container: str | None = None) -> dict:
        # Find parent container if not set
        if parent_container is None:
            # Only evaluate parent_groups which are part of all_groups_from_root. A group can have multiple parents.
            parent_groups: set = set(group.parent_groups).intersection(all_groups_from_root)
            # Ensure that we have only one parent group. Otherwise we cannot build a tree.
            if len(parent_groups) > 1:
                msg = (
                    f"arista.avd.inventory_to_container: Group '{group}' has more than one parent group ({parent_groups}) below the 'container_root'."
                    " Unable to build CloudVision container hierarchy."
                )
                raise AnsibleActionFail(msg)
            parent_container = parent_groups.pop().name

        # Build list of devices under the group
        devices = []
        host: Host
        for host in group.hosts:
            hostname = host.name

            # Skip devices if not passing filter
            if "all" not in device_filter and not any(element in hostname for element in device_filter):
                continue

            # Skip devices if not is_deployed
            if host.get_vars().get("is_deployed") is False:
                continue

            devices.append(hostname)

        return {
            "parent_container": parent_container,
            "devices": devices,
        }
