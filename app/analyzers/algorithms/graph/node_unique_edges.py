from operator import eq
from typing import Dict, List

from app.analyzers.algorithms.graph.edge import Edge
from app.analyzers.algorithms.graph.node import Node
from app.analyzers.algorithms.graph.node_edges import NodeEdges


class NodeUniqueEdges(NodeEdges):
    """
    Node with no duplicate edges. It implements the node edges class with only unique edges in mind.
    """

    def __init__(self, node: Node) -> None:
        """
        Create new node with edges object. It incorporates node and all incoming and outgoing edges. Initialize
        collections of edges.

        :param node: which is the starting point from which you can get incoming and outgoing edges.
        """
        super().__init__(node)
        self.in_edges: Dict[str, Edge] = dict()
        self.out_edges: Dict[str, Edge] = dict()

    def add_in_edge(self, edge: Edge) -> None:
        """
        Add new incoming edge. If the edge already exists then the weight is altered to be the old weight (of the old
        edge) plus the new weight (of the new edge). weight = old_weight + new_weight.

        :param edge: new incoming edge which will be added to this node.
        """
        if not eq(self.node, edge.get_destination()):
            raise Exception("In order to add edge as incoming, the destination should be the equal to this node but "
                            "they differ.", self.node, edge.get_destination())

        origin_name = edge.get_origin().get_name()
        old_edge = self.in_edges.get(origin_name)
        self.in_edges[origin_name] = edge
        if old_edge is not None:
            edge.weight += old_edge.weight

    def add_out_edge(self, edge: Edge) -> None:
        """
        Add new outgoing edge.

        :param edge: new outgoing edge which will be added to this node.
        """
        if not eq(self.node, edge.get_origin()):
            raise Exception("In order to add edge as outgoing, the source should be the equal to this node but they "
                            "differ.", self.node, edge.get_origin())

        destination_name = edge.get_destination().get_name()
        self.out_edges[destination_name] = edge

    def get_in_edges(self) -> List[Edge]:
        """
        :return: all incoming edges of this node.
        """
        return list(self.in_edges.values())

    def get_out_edges(self) -> List[Edge]:
        """
        :return: all outgoing edges of this node.
        """
        return list(self.out_edges.values())
