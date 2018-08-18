from app.analyzers.algorithms.graph.node import Node


class PageRankNode:
    """
    Graph node in the page rank algorithm. It it wraps the :class:`Node` and adds additional information. For
    example ``new_weight`` which is used as intermediate weight between the stages of the page rank algorithm.
    """

    def __init__(self, node: Node):
        """
        Create new page rank node by wrapping the :class:`Graph` :class:`Node` and add information about the
        intermediate state ``new_weight``.

        :param node: wrapped node in this page rank node.
        """
        self.node = node
        self.new_weight = self.node.get_weight()

    def get_graph_node(self):
        """
        Get the :class:`Graph` :class:`Node`.

        :return: wrapped node in this page rank node.
        """
        return self.node

    def get_new_weight(self):
        """
        Score which is used as an intermediate state of this node between the
        iterations of the page rank algorithm.

        :return: intermediate scored of between the page rank iterations.
        """
        return self.new_weight

    def set_new_weight(self, new_weight):
        self.new_weight = new_weight

    def get_error(self) -> float:
        """
        Difference between the scores of the current iteration and the previous one, which defines the error that was
        fixed in the current iteration. According to this score page rank algorithm decides when it will stop.

        :return: error that was fixed in the current iteration.
        """
        return abs(self.get_graph_node().get_weight() - self.new_weight)

    def update(self):
        """
        After finishing one cycle (iteration) in the page rank, the new_score
        (intermediate score) becomes the actual score of this node. Call this
        method to update the score of this node.
        """
        self.get_graph_node().set_weight(self.new_weight)
