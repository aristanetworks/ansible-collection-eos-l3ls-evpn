# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass

from pyavd.j2filters import natural_sort


@dataclass(frozen=True)
class Edge:
    nodes: frozenset[str]
    node_data: frozenset[tuple[str, tuple]]


class Topology:
    edges: set[Edge]
    node_edges: dict[str, set[Edge]]

    def __init__(self) -> None:
        self.edges = set()
        self.node_edges = {}

    def add_edge(self, node1: str, node2: str, node1_data: tuple, node2_data: tuple) -> Edge:
        edge = Edge(nodes=frozenset((node1, node2)), node_data=frozenset(((node1, node1_data), (node2, node2_data))))
        self.edges.add(edge)
        self.node_edges.setdefault(node1, set()).add(edge)
        self.node_edges.setdefault(node2, set()).add(edge)
        return edge

    def get_edges(self) -> tuple[Edge]:
        return tuple(self.edges)

    def get_edges_by_node(self) -> dict[str, tuple[Edge]]:
        return {node: tuple(edges) for node, edges in self.node_edges.items()}

    def get_edges_by_node_unidirectional_sorted(self) -> dict[str, tuple[Edge]]:
        edges_done = set()
        edges_by_node = {}
        for node in natural_sort(self.node_edges):
            uni_edges = self.node_edges[node].difference(edges_done)
            edges_by_node[node] = tuple(uni_edges)
            edges_done.update(uni_edges)

        return edges_by_node
