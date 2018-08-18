from dependency_injector.providers import Provider

from app.analyzers.algorithms.graph.edge import Edge
from app.analyzers.algorithms.graph.graph import Graph
from app.analyzers.algorithms.graph.node import Node


class UndirectedGraph(Graph):
    """
    Represents the `Undirected Graph`_, graph in which edges don't have direction and don't have
    source node and destination node. This graph can be used if you want to present
    two way relations. It uses :class:`Node` and :class:`Edge` classes to build the
    graph. :class:`Edge` is directed by nature so it mimics undirected by adding two edges every time
    in each direction.

    .. _Undirected Graph: https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Undirected_graph
    """

    def __init__(self, node_provider: Provider, node_edges_provider: Provider, edge_provider: Provider) -> None:
        """
        Create new undirected graph by passing providers for :class:`Node`, :class:`Edge`, and only internally used
        :class:`NodeEdges`.

        :param node_provider: provider factory for nodes.
        :param node_edges_provider: provider factory for node edges class. Used only internally.
        :param edge_provider: provider factory for directed edges.
        """
        super().__init__(node_provider, node_edges_provider)
        self.edge_provider = edge_provider

    def add_edge(self, origin: Node, destination: Node, weight: float = 1) -> Edge:
        """
        Add undirected edge between the origin and the destination. It will create two identical edges in both
        directions.

        :param origin: node which is one side of the edge.
        :param destination: node which is the other side of the edge.
        :param weight: the strength of the relation between the two nodes.
        :return: the newly created edge (the originally requested one.
        """
        self.add_node(origin)
        self.add_node(destination)

        origin_edges = self.nodes[origin.get_name()]
        destination_edges = self.nodes[destination.get_name()]

        edge: Edge = self.edge_provider(origin=origin, destination=destination, weight=weight)
        origin_edges.add_out_edge(edge)
        destination_edges.add_in_edge(edge)

        original_edge = edge
        edge: Edge = self.edge_provider(origin=destination, destination=origin, weight=weight)
        origin_edges.add_in_edge(edge)
        destination_edges.add_out_edge(edge)
        return original_edge
