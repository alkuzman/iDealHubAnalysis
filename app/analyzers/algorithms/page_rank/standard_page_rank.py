from app.analyzers.algorithms.graph.graph import Graph
from app.analyzers.algorithms.graph.node import Node
from app.analyzers.algorithms.page_rank.page_rank import PageRank
from app.analyzers.algorithms.page_rank.page_rank_node import PageRankNode


class StandardPageRank(PageRank):
    def __init__(self, graph: Graph, threshold: float = 1.0e-6, damping_factor: float = 0.85,
                 max_iterations: int = 1000):
        super().__init__(graph, threshold, damping_factor, max_iterations)

    def run(self):
        i = 0
        error = 0
        nodes = [PageRankNode(node) for node in self.graph.get_all_nodes()]
        while True:
            for node in nodes:
                new_score = self.calculate_node_score(node.get_graph_node(), self.damping_factor)
                node.set_new_weight(new_score)

            for node in nodes:
                error += node.get_error()
                node.update()
            i += 1
            if error < self.threshold or i == self.max_iterations:
                break
            error = 0

    def calculate_node_score(self, node: Node, damping_factor: float) -> float:
        score = 0
        edges = self.graph.get_in_edges(node)
        for edge in edges:
            origin_total_weight = 0
            origin_out_edges = self.graph.get_out_edges(edge.get_origin())
            for origin_edge in origin_out_edges:
                origin_total_weight += origin_edge.get_weight()
            score += (edge.weight / origin_total_weight) * edge.get_origin().get_weight()
        total_score = (1 - damping_factor) + damping_factor * score
        return total_score
