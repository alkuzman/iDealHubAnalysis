from dependency_injector.providers import Provider

from app.analyzers.algorithms.graph.edge import Edge
from app.analyzers.algorithms.graph.graph import Graph
from app.analyzers.algorithms.graph.node import Node


class DirectedGraph(Graph):
    """
    Represents the `Directed Graph`_, graph in which edges are directed and have
    source node and destination node. This graph can be used if you want to present
    one way relations. It uses :class:`Node` and :class:`Edge` classes to build the
    graph. :class:`Edge` is directed by nature.

    .. _Directed Graph: https://en.wikipedia.org/wiki/Directed_graph
    """

    def __init__(self, node_provider: Provider, node_edges_provider: Provider, edge_provider: Provider) -> None:
        """
        Create new directed graph by passing providers for :class:`Node`, :class:`Edge`, and only internally used
        :class:`NodeEdges`.

        :param node_provider: provider factory for nodes.
        :param node_edges_provider: provider factory for node edges class. Used only internally.
        :param edge_provider: provider factory for directed edges.
        """
        super().__init__(node_provider, node_edges_provider)
        self.edge_provider = edge_provider

    def add_edge(self, origin: Node, destination: Node, weight: float = 1) -> Edge:
        """
        Add directed edge between the origin and the destination.

        :param origin: node with which the edge will start.
        :param destination: node with which edge will end.
        :param weight: the strength of the relation between the two nodes.
        :return: the newly created edge.
        """
        self.add_node(origin)
        self.add_node(destination)

        origin_edges = self.nodes[origin.get_name()]
        destination_edges = self.nodes[destination.get_name()]

        edge: Edge = self.edge_provider(origin=origin, destination=destination, weight=weight)
        origin_edges.add_out_edge(edge)
        destination_edges.add_in_edge(edge)
        return edge
