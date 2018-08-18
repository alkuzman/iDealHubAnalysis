import abc
from typing import List

from app.analyzers.algorithms.graph.edge import Edge
from app.analyzers.algorithms.graph.node import Node


class NodeEdges(metaclass=abc.ABCMeta):
    """
        Node in the graph which contains the node info, but also the in and out edges. Using this node you can travel
        trough the graph and find every other node (there is a path from this node to that one).
        This class is used only by the graph, and it should not be used directly.
        """

    def __init__(self, node: Node) -> None:
        """
        Create new node with edges object. It incorporates node and all incoming and outgoing edges. Initialize
        collections of edges.

        :param node: which is the starting point from which you can get incoming and outgoing edges.
        :param args: arbitrary arguments you can define for this objects.
        :param kwargs: same as args except that they can have key from which you can access them in the future.
        """
        self.node = node

    def add_in_edge(self, edge: Edge) -> None:
        """
        Add incoming edge to this node.

        :param edge: which will be added as incoming to this node.
        """
        pass

    def add_out_edge(self, edge: Edge) -> None:
        """
        Add outgoing edge to this node.

        :param edge: which will be added as outgoing to this node.
        """
        pass

    def get_in_edges(self) -> List[Edge]:
        """
        Get all incoming edges for this node.
        """
        pass

    def get_out_edges(self) -> List[Edge]:
        """
        Get all outgoing edges for this node
        """
        pass

    def total_in_weight(self) -> float:
        """
        Get the weight of this node which is calculated as sum of all incoming nodes weight.

        :return: total incoming weight of this node.
        """
        total_weight = 0
        for edge in self.get_in_edges():
            total_weight += edge.get_weight()
        return total_weight

    def total_out_weight(self) -> float:
        """
        Get the weight of this node which is calculated as sum of all outgoing nodes weight.

        :return: total outgoing weight of this node.
        """
        total_weight = 0
        for edge in self.get_out_edges():
            total_weight += edge.get_weight()
        return total_weight

    def get_node(self) -> Node:
        """
        :return: the node described by this class.
        """
        return self.node
