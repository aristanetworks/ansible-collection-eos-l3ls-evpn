# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
class FabricDocumentation:
    """
    Object containing the requested documentation.

    Attributes:
        fabric_documentation: Fabric Documentation as Markdown.
        topology_csv: Topology CSV containing the physical interface connections for every device.
        p2p_links_csv: P2P links CSV containing the Routed point-to-point links.
        toc: Generate the table of content(TOC) on fabric documentation.
    """

    fabric_documentation: str = ""
    topology_csv: str = ""
    p2p_links_csv: str = ""
    toc: str = ""
