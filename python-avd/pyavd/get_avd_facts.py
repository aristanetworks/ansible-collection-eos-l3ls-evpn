# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import ChainMap


def get_avd_facts(all_inputs: dict[str, dict]) -> dict[str, dict]:
    """
    Build avd_facts using the AVD eos_designs_facts logic.

    Variables should be converted and validated according to AVD `eos_designs` schema first using `pyavd.validate_inputs`.

    Note! No support for inline templating or jinja templates for descriptions or ip addressing

    Args:
        all_inputs: A dictionary where keys are hostnames and values are dictionaries of input variables per device.
            ```python
            {
                "<hostname1>": dict,
                "<hostname2>": dict,
                ...
            }
            ```

    Returns:
        Nested dictionary with various internal "facts". The full dict must be given as argument to `pyavd.get_device_structured_config`:
            ```python
            {"avd_switch_facts": dict, "avd_overlay_peers": dict, "avd_topology_peers": dict}
            ```
    """
    avd_switch_facts_instances = _create_avd_switch_facts_instances(all_inputs)
    avd_switch_facts = _render_avd_switch_facts(avd_switch_facts_instances)
    avd_overlay_peers, avd_topology_peers = _render_peer_facts(avd_switch_facts)

    return {
        "avd_switch_facts": avd_switch_facts,
        "avd_overlay_peers": avd_overlay_peers,
        "avd_topology_peers": avd_topology_peers,
    }


def _create_avd_switch_facts_instances(all_inputs: dict[str, dict]) -> dict:
    """
    Validate input variables and return dictionary of EosDesignsFacts instances per device.

    Args:
        all_inputs: A dictionary where keys are hostnames and values are dictionaries of input variables per device.
            ```python
            {
                "<hostname1>": dict,
                "<hostname2>": dict,
                ...
            }
            ```

    Returns:
        Dictionary with instances of EosDesignsFacts per device.
            ```python
            {
                "<hostname1>": {"switch": <EosDesignsFacts object>},
                "<hostname2>": {"switch": <EosDesignsFacts object>},
                ...
            }
            ```
    """
    # pylint: disable=import-outside-toplevel
    from ._eos_designs.eos_designs_facts import EosDesignsFacts
    from ._eos_designs.schema import EosDesigns
    from ._eos_designs.shared_utils import SharedUtils
    from .avd_schema_tools import EosDesignsAvdSchemaTools

    # pylint: enable=import-outside-toplevel

    avd_switch_facts = {}
    for hostname, hostvars in all_inputs.items():
        # Set 'inventory_hostname' on the input variables, to keep compatibility with Ansible focused code.
        # Add reference to dict "avd_switch_facts" to access EosDesignsFacts objects of other switches during rendering of one switch.
        mapped_hostvars = ChainMap(
            {"inventory_hostname": hostname, "avd_switch_facts": avd_switch_facts},
            hostvars,
        )

        # Load input vars into the EosDesigns data class.
        inputs = EosDesigns._from_dict(hostvars)

        # Initialize SharedUtils class to be passed to each python_module below.
        shared_utils = SharedUtils(hostvars=mapped_hostvars, inputs=inputs, templar=None, schema=EosDesignsAvdSchemaTools().avdschema)

        # Notice templar is set as None, so any calls to jinja templates will fail with Nonetype has no "_loader" attribute
        avd_switch_facts[hostname] = {"switch": EosDesignsFacts(hostvars=mapped_hostvars, inputs=inputs, shared_utils=shared_utils)}

    return avd_switch_facts


def _render_avd_switch_facts(avd_switch_facts_instances: dict) -> dict:
    """
    Run the render method on each EosDesignsFacts object.

    Args:
        avd_switch_facts_instances: Dictionary with instances of EosDesignsFacts per device.
            ```python
            {
                "<hostname1>": {"switch": <EosDesignsFacts object>},
                "<hostname2>": {"switch": <EosDesignsFacts object>},
                ...
            }
            ```

    Returns:
        Nested Dictionaried with rendered "avd_switch_facts" per device.
            ```python
            {
                "<hostname1>": {"switch": dict},
                "<hostname2>": {"switch": dict},
                ...
            }
            ```
    """
    return {
        hostname: {
            "switch": avd_switch_facts_instances[hostname]["switch"].render(),
        }
        for hostname in avd_switch_facts_instances
    }


def _render_peer_facts(avd_switch_facts: dict) -> tuple[dict, dict]:
    """
    Build dicts of underlay and overlay peerings based on avd_switch_facts.

    Args:
        avd_switch_facts: Nested Dictionaried with rendered "avd_switch_facts" per device.
            ```python
            {
                "<hostname1>": {"switch": dict},
                "<hostname2>": {"switch": dict},
                ...
            }
            ```

    Returns:
        avd_overlay_peers: dict
            hostname1 : list[str]
                List of switches pointing to hostname1 as route server / route reflector
            hostname2 : list[str]
                List of switches pointing to hostname2 as route server / route reflector
        avd_topology_peers: dict
            hostname1 : list[str]
                List of switches having hostname1 as uplink_switch
            hostname2 : list[str]
                List of switches having hostname2 as uplink_switch

    """
    avd_overlay_peers = {}
    avd_topology_peers = {}
    for hostname in avd_switch_facts:
        host_evpn_route_servers = avd_switch_facts[hostname]["switch"].get("evpn_route_servers", [])
        for peer in host_evpn_route_servers:
            avd_overlay_peers.setdefault(peer, []).append(hostname)

        host_mpls_route_reflectors = avd_switch_facts[hostname]["switch"].get("mpls_route_reflectors", [])
        for peer in host_mpls_route_reflectors:
            avd_overlay_peers.setdefault(peer, []).append(hostname)

        host_topology_peers = avd_switch_facts[hostname]["switch"].get("uplink_peers", [])

        for peer in host_topology_peers:
            avd_topology_peers.setdefault(peer, []).append(hostname)

    return avd_overlay_peers, avd_topology_peers
