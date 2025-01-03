# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd.api.fabric_documentation import FabricDocumentation

if TYPE_CHECKING:
    from pyavd._eos_designs.fabric_documentation_facts import FabricDocumentationFacts


def get_fabric_documentation(
    avd_facts: dict[str, dict],
    structured_configs: dict[str, dict],
    fabric_name: str,
    fabric_documentation: bool = True,
    include_connected_endpoints: bool = False,
    topology_csv: bool = False,
    p2p_links_csv: bool = False,
) -> FabricDocumentation:
    """
    Build and return the AVD fabric documentation.

    The returned object will contain the content of the requested documentation areas:
    - Fabric documentation as Markdown, optionally including connected endpoints.
    - Topology CSV containing the physical interface connections for every device.
    - P2P links CSV containing the Routed point-to-point links.

    Args:
        avd_facts: Dictionary of avd_facts as returned from `pyavd.get_avd_facts`.
        structured_configs: Dictionary of structured configurations for all devices, keyed by hostname.
        fabric_name: Name of the fabric. Only used for the main heading in the Markdown documentation.
        fabric_documentation: Returns fabric documentation when set to True.
        include_connected_endpoints: Includes connected endpoints in the fabric documentation when set to True.
        topology_csv: Returns topology CSV when set to True.
        p2p_links_csv: Returns P2P links CSV when set to True.

    Returns:
        FabricDocumentation object containing the requested documentation areas.
    """
    # pylint: disable=import-outside-toplevel
    from pyavd._eos_designs.fabric_documentation_facts import FabricDocumentationFacts
    from pyavd.j2filters import add_md_toc

    from .constants import EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH
    from .templater import Templar
    # pylint: enable=import-outside-toplevel

    fabric_documentation_facts = FabricDocumentationFacts(avd_facts, structured_configs, fabric_name, include_connected_endpoints)
    result = FabricDocumentation()
    doc_templar = Templar(precompiled_templates_path=EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH)
    if fabric_documentation:
        fabric_documentation_facts_dict = fabric_documentation_facts.render()
        result.fabric_documentation = doc_templar.render_template_from_file("fabric_documentation.j2", fabric_documentation_facts_dict)
        if include_connected_endpoints:
            result.fabric_documentation += "\n" + doc_templar.render_template_from_file("connected_endpoints_documentation.j2", fabric_documentation_facts_dict)

        result.fabric_documentation = add_md_toc(result.fabric_documentation, skip_lines=3)

    if topology_csv:
        result.topology_csv = _get_topology_csv(fabric_documentation_facts)
    if p2p_links_csv:
        result.p2p_links_csv = _get_p2p_links_csv(fabric_documentation_facts)
    return result


def _get_topology_csv(fabric_documentation_facts: FabricDocumentationFacts) -> str:
    # pylint: disable=import-outside-toplevel
    from csv import writer
    from io import StringIO
    # pylint: enable=import-outside-toplevel

    csv_content = StringIO()
    csv_writer = writer(csv_content, lineterminator="\n")
    csv_writer.writerow(("Node Type", "Node", "Node Interface", "Peer Type", "Peer Node", "Peer Interface", "Node Interface Enabled"))
    csv_writer.writerows(fabric_documentation_facts.get_physical_links())
    csv_content.seek(0)
    return csv_content.read()


def _get_p2p_links_csv(fabric_documentation_facts: FabricDocumentationFacts) -> str:
    # pylint: disable=import-outside-toplevel
    from csv import writer
    from io import StringIO
    # pylint: enable=import-outside-toplevel

    csv_content = StringIO()
    csv_writer = writer(csv_content, lineterminator="\n")
    csv_writer.writerow(("Type", "Node", "Node Interface", "Leaf IP Address", "Peer Type", "Peer Node", "Peer Interface", "Peer IP Address"))
    csv_writer.writerows(
        (
            topology_link["type"],
            topology_link["node"],
            topology_link["node_interface"],
            topology_link["node_ip_address"],
            topology_link["peer_type"],
            topology_link["peer"],
            topology_link["peer_interface"],
            topology_link["peer_ip_address"],
        )
        for topology_link in fabric_documentation_facts.topology_links
        if topology_link["routed"]
    )
    csv_content.seek(0)
    return csv_content.read()
