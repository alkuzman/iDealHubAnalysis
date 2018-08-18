from abc import abstractmethod, ABCMeta

from app.analyzers.algorithms.graph.graph import Graph


class PageRank(metaclass=ABCMeta):
    """
    Page rank algorithm interface.
    Page rank is an graph algorithm for ranking the nodes taking into account
    their connections.
    """

    def __init__(self, graph: Graph, threshold: float = 1.0e-6, damping_factor: float = 0.85,
                 max_iterations: int = 1000):
        """
        Initialize the page rank with standard graph implementation.
        This implementation uses :class:`Graph` and walks trough :class:`Node` and :class:`Edge`
        and performs the calculations. After calling the method ``run`` it will write new weights into the graph
        nodes. You can use those weights in order to sort the nodes by their importance in the graph.

        :param graph: the graph on which page rank will be performed
        :param threshold: defines the maximum error between the iterations. Dictates when the process will stop.
        :param damping_factor: tells how big part of the relations should be taken into account. The other part is
        random access.
        :param max_iterations: dictates the maximum number of iterations.
        """
        self.graph = graph
        self.threshold = threshold
        self.damping_factor = damping_factor
        self.max_iterations = max_iterations

    @abstractmethod
    def run(self):
        """
        Run the page algorithm. This will change node weights in the graph with the calculated ones.
        Those weights will tell how important that node is.
        """
        pass
