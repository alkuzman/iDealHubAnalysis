from networkx import DiGraph, pagerank_scipy

from app.analyzers.algorithms.graph.graph import Graph
from app.analyzers.algorithms.page_rank.page_rank import PageRank


class MatrixPageRank(PageRank):
    def __init__(self, graph: Graph, threshold: float = 1.0e-6, damping_factor: float = 0.85,
                 max_iterations: int = 100):
        super().__init__(graph, threshold, damping_factor, max_iterations)
        self.external_graph = DiGraph()
        nodes = self.graph.get_all_nodes()
        for node in nodes:
            self.external_graph.add_node(node)
        self.external_graph.add_weighted_edges_from([(edge.get_origin(), edge.get_destination(), edge.get_weight())
                                                     for edge in self.graph.get_all_edges()])

    def run(self):
        nodes = self.graph.get_all_nodes()
        personalization = {node: node.get_weight() for node in nodes}
        # result = pagerank_numpy(self.external_graph,  personalization=personalization)
        result = pagerank_scipy(self.external_graph, alpha=self.damping_factor, personalization=personalization,
                                max_iter=self.max_iterations, tol=self.threshold)
        for node in nodes:
            node.set_weight(result[node])
