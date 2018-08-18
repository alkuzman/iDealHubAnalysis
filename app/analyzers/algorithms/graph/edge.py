from app.analyzers.algorithms.graph.node import Node


class Edge(object):
    """
    Directed edge in the graph. Its represented by the origin and destination nodes
    and the strength of the relation between them.
    """

    def __init__(self, origin: Node, destination: Node, weight: float = 1):
        """
        Create new directed edge in the graph. Its described by the origin,
        the destination, and the weight.


        :param origin: node from which this edge is originating.
        :param destination: node to which this edge is pointing, the destination.
        :param weight: strength of the relation between the origin and the destination, defaults 1.
        :param args: other arbitrary arguments. Here you can keep everything may want to add in the edge.
        :param kwargs: similar to params, except that arguments can have keys from which can be accessed later.
        """
        self.origin = origin
        self.destination = destination
        self.weight = weight

    def get_origin(self) -> Node:
        """
        :return: node from which this edge is loriginating.
        """
        return self.origin

    def get_destination(self) -> Node:
        """
        :return: node to which this edge is pointing, the destination.
        """
        return self.destination

    def get_weight(self) -> float:
        """
        :return: strength of the relation between the origin and the destination.
        """
        return self.weight
