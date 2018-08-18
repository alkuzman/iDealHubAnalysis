import abc
from abc import abstractmethod
from typing import List, Dict

from dependency_injector.providers import Provider

from app.analyzers.algorithms.graph.edge import Edge
from app.analyzers.algorithms.graph.node import Node
from app.analyzers.algorithms.graph.node_edges import NodeEdges


class Graph(metaclass=abc.ABCMeta):
    """
    This is Klupps python representation of the discrete mathematics definition for graph. Set of :class:`Node`
    instances
    interconnected by :class:`Edge`' instances which have origin, destination and weight. Read more `here`_.

    .. _here: https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)
    """

    def __init__(self, node_provider: Provider, node_edges_provider: Provider) -> None:
        """
        Create new empty graph, which defines the basic functionality. The nodes and the interconnection between
        them. For this task the Graph uses several providers, for nodes and edges.

        :param node_provider: provider for creating nodes out of raw data.
        :param node_edges_provider: provider for creating node wrappers which manage in and out edges.
        """
        super().__init__()
        self.node_provider = node_provider
        self.node_edges_provider = node_edges_provider
        self.nodes: Dict[str, NodeEdges] = {}

    def add_node(self, node: Node) -> None:
        """
        Addition or replacement of the provided node using the node name as unique identifier in this graph.

        :param node: which will be added in this graph.
        """
        old_node = self.nodes.get(node.get_name(), None)
        if old_node is None or old_node.get_node().get_weight() < node.get_weight():
            self.nodes[node.get_name()] = self.node_edges_provider(node=node)

    def create_node(self, name: str, initial_score: float = 1) -> Node:
        """
        First create and then add the node. If node with the same name exists than it will be replaced with the newly
        created node.

        :param name: unique identifier of the new node in this graph.
        :param initial_score: the initial score for this node (can change in the future).
        :return: the newly created node. Use it for any subsequent calls.
        """
        node = self.node_provider(name=name, initial_weight=initial_score)
        self.add_node(node)
        return node

    @abstractmethod
    def add_edge(self, origin: Node, destination: Node, weight: float = 1) -> Edge:
        """
        Adds new :class:`Edge` between the origin and the destination nodes, whether it is directed or undirected
        depends on the concrete implementations of this class. Whether it will have duplicate edges or not depends on
        the concrete implementation of :class:`NodeEdges`.

        :param origin: node with which the edge will start in case od directed graph.
        :param destination: node with which edge will end in case of directed graph.
        :param weight: the strength of the relation between the two nodes.
        :return: the newly created edge.
        """
        pass

    def try_add_edge(self, origin_name: str, destination_name: str, weight: float = 1) -> Edge:
        """
        Try to add new edge. This method will succeed and will call add_edge only if there are nodes with provided
        names.

        :param origin_name: the name of the origin node.
        :param destination_name: the name of the destination node.
        :param weight: strength of the relation between the two nodes.
        :raises Exception: if one of origin_name or destination_name is not found in the graph.
        """
        origin = self.get_node(origin_name)
        if origin is None:
            raise Exception("origin node with name " + origin_name + "not fund in the graph.")
        destination = self.get_node(destination_name)
        if origin is None:
            raise Exception("destination node with name " + destination_name + "not fund in the graph.")
        return self.add_edge(origin, destination, weight)

    def get_all_nodes(self) -> List[Node]:
        """
        :return: all nodes that currently are part of this graph.
        """
        return [node_edges.node for node_edges in self.nodes.values()]

    def get_node(self, node_name) -> Node:
        """
        :param node_name: unique identifier of the requested node
        :return: the node defined with the node_name if exists
        :raises Exception: if the node_name is not existent in this graph
        """
        return self.nodes[node_name].get_node()

    def get_in_edges(self, node: Node) -> List[Edge]:
        """
        Get all incoming edges for the specified node, if the node exists.

        :param node: for which incoming edges are requested
        :return: list of all incoming edges for the specified node.
        :raises Exception: if the node is not present in this graph
        """
        return self.nodes[node.get_name()].get_in_edges()

    def get_out_edges(self, node: Node) -> List[Edge]:
        """
        Get all outgoing edges for the specified node, if the node exists.

        :param node: for which outgoing edges are requested
        :return: list of all outgoing edges for the specified node.
        :raises Exception: if the node is not present in this graph
        """
        return self.nodes[node.get_name()].get_out_edges()

    def get_all_edges(self) -> List[Edge]:
        """
        :return: all edges present in this graph.
        """
        edges: List[Edge] = []
        for node_edges in self.nodes.values():
            edges.extend(node_edges.get_in_edges())
        return edges
