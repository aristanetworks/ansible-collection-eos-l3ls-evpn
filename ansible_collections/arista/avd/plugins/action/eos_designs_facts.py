# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


import cProfile
import pstats
from typing import Any

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschematools import AvdSchemaTools
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_templar

PLUGIN_NAME = "arista.avd.eos_designs_facts"

try:
    from pyavd._eos_designs.eos_designs_facts import EosDesignsFacts
    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.shared_utils import SharedUtils
    from pyavd._errors import AristaAvdError
except ImportError as e:
    EosDesignsFacts = EosDesigns = SharedUtils = RaiseOnUse(
        AnsibleActionFail(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )


class ActionModule(ActionBase):
    def run(self, tmp: Any = None, task_vars: dict | None = None) -> None:
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        cprofile_file = self._task.args.get("cprofile_file")
        if cprofile_file:
            profiler = cProfile.Profile()
            profiler.enable()

        self.template_output = self._task.args.get("template_output", False)
        self._validation_mode = self._task.args.get("validation_mode")

        groups = task_vars.get("groups", {})
        fabric_name = self._templar.template(task_vars.get("fabric_name", ""))
        fabric_hosts = groups.get(fabric_name, [])
        ansible_play_hosts_all = task_vars.get("ansible_play_hosts_all", [])

        # Check if fabric_name is set and that all play hosts are part Ansible group set in "fabric_name"
        if fabric_name is None or not set(ansible_play_hosts_all).issubset(fabric_hosts):
            msg = (
                "Invalid/missing 'fabric_name' variable. "
                "All hosts in the play must have the same 'fabric_name' value "
                "which must point to an Ansible Group containing the hosts."
                f"play_hosts: {ansible_play_hosts_all}"
            )
            raise AnsibleActionFail(msg)

        # This is not all the hostvars, but just the Ansible Hostvars Manager object where we can retrieve hostvars for each host on-demand.
        hostvars = task_vars["hostvars"]

        # Get updated templar instance to be passed along to our simplified "templater"
        self.templar = get_templar(self, task_vars)

        avd_switch_facts_instances = self.create_avd_switch_facts_instances(fabric_hosts, hostvars, result)
        if result.get("failed"):
            # Stop here if any of the devices failed input data validation
            return result

        avd_switch_facts = self.render_avd_switch_facts(avd_switch_facts_instances)

        avd_overlay_peers = {}
        avd_topology_peers = {}
        for host in fabric_hosts:
            host_evpn_route_servers = avd_switch_facts[host]["switch"].get("evpn_route_servers", [])
            for peer in host_evpn_route_servers:
                avd_overlay_peers.setdefault(peer, []).append(host)

            host_mpls_route_reflectors = avd_switch_facts[host]["switch"].get("mpls_route_reflectors", [])
            for peer in host_mpls_route_reflectors:
                avd_overlay_peers.setdefault(peer, []).append(host)

            host_topology_peers = avd_switch_facts[host]["switch"].get("uplink_peers", [])

            for peer in host_topology_peers:
                avd_topology_peers.setdefault(peer, []).append(host)

        result["ansible_facts"] = {
            "avd_switch_facts": avd_switch_facts,
            "avd_overlay_peers": avd_overlay_peers,
            "avd_topology_peers": avd_topology_peers,
        }

        if cprofile_file:
            profiler.disable()
            stats = pstats.Stats(profiler).sort_stats("cumtime")
            stats.dump_stats(cprofile_file)

        return result

    def create_avd_switch_facts_instances(self, fabric_hosts: list, hostvars: object, result: dict) -> dict:
        """
        Fetch hostvars for all hosts and perform data conversion & validation.

        Initialize all instances of EosDesignsFacts and insert various references into the variable space.
        Returns dict with avd_switch_facts_instances.

        Parameters
        ----------
        fabric_hosts : list
            List of hostnames
        hostvars : object
            Ansible "hostvars" object
        result : dict
            Ansible Action result dict which is inplace updated.
            failure : bool
            msg : str

        Returns:
        -------
        dict
            hostname1 : dict
                switch : <EosDesignsFacts object>,
            hostname2 : dict
                switch : <EosDesignsFacts object>,
            ...
        """
        # Load schema tools once with empty host.
        avdschematools = AvdSchemaTools(
            hostname="",
            ansible_display=display,
            schema_id="eos_designs",
            validation_mode=self._validation_mode,
            plugin_name="arista.avd.eos_designs",
        )

        avd_switch_facts = {}
        data_validation_errors = 0
        for host in fabric_hosts:
            # Fetch all templated Ansible vars for this host
            host_hostvars = dict(hostvars.get(host))

            # Set correct hostname in schema tools and perform conversion and validation
            avdschematools.hostname = host
            host_result = avdschematools.convert_and_validate_data(host_hostvars, return_counters=True)

            data_validation_errors += host_result["validation_errors"]

            if host_result.get("failed"):
                # Quickly continue if data validation failed
                result["failed"] = True
                continue

            # Add reference to dict "avd_switch_facts".
            # This is used to access EosDesignsFacts objects of other switches during rendering of one switch.
            host_hostvars["avd_switch_facts"] = avd_switch_facts

            # Load input vars into the EosDesigns data class.
            inputs = EosDesigns._from_dict(host_hostvars, load_custom_structured_config=False)

            # Initialize SharedUtils class to be passed to EosDesignsFacts below.
            shared_utils = SharedUtils(hostvars=host_hostvars, inputs=inputs, templar=self.templar, schema=avdschematools.avdschema)

            # Create an instance of EosDesignsFacts and insert into common avd_switch_facts dict
            avd_switch_facts[host] = {"switch": EosDesignsFacts(hostvars=host_hostvars, inputs=inputs, shared_utils=shared_utils)}

            # Add "switch" as a reference to the newly created EosDesignsFacts instance directly in the hostvars
            # to allow `shared_utils` to work the same when they are called from `EosDesignsFacts` or from `AvdStructuredConfig`.
            host_hostvars["switch"] = avd_switch_facts[host]["switch"]

        # Build result message
        result["msg"] = avdschematools.build_result_message(validation_errors=data_validation_errors)

        return avd_switch_facts

    def render_avd_switch_facts(self, avd_switch_facts_instances: dict) -> dict:
        """
        Run the render method on each EosDesignsFacts object.

        Parameters
        ----------
        avd_switch_facts_instances : dict of EosDesignsFacts

        Returns:
        -------
        dict
            hostname1 : dict
                switch : < switch.* facts >
            hostname2 : dict
                switch : < switch.* facts >
        """
        rendered_facts = {}
        for host in avd_switch_facts_instances:
            try:
                rendered_facts[host] = {"switch": avd_switch_facts_instances[host]["switch"].render()}
            except AristaAvdError as e:
                message = f"{str(e).removesuffix('.')} for host '{host}'."
                raise AnsibleActionFail(message=message) from e

            # If the argument 'template_output' is set, run the output data through jinja2 rendering.
            # This is to resolve any input values with inline jinja using variables/facts set by eos_designs_facts.
            if self.template_output:
                with self._templar.set_temporary_context(available_variables=avd_switch_facts_instances[host]["switch"]._hostvars):
                    rendered_facts[host]["switch"] = self._templar.template(rendered_facts[host]["switch"], fail_on_undefined=False)

        return rendered_facts
