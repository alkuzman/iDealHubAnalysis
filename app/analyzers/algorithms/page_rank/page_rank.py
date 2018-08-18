from app.analyzers.algorithms.page_rank.model.edge import PageRankEdge
from app.analyzers.algorithms.page_rank.model.node import PageRankNode
from app.analyzers.algorithms.page_rank.model.nodes import PageRankNodes
from app.analyzers.algorithms.page_rank.model.score_node import ScoreNode


class PageRank(ScoreNode):
    def __init__(self):
        self.nodes = {}
        self.number_of_nodes = 0

    def add_node(self, name: str, initial_score: float = 1) -> PageRankNode:
        node = self.nodes.get(name)
        if node is not None:
            return node
        node = PageRankNode(self.number_of_nodes, name, initial_score)
        self.nodes[name] = node
        self.number_of_nodes += 1
        return node

    def get_nodes(self) -> PageRankNodes:
        node_list = list(self.nodes.values())
        node_list.sort(key=lambda node: node.get_score(), reverse=True)
        return node_list

    @staticmethod
    def compare(node1: PageRankNode, node2: PageRankNode):
        if node1.get_score() < node2.get_score():
            return -1
        return 0

    def get_number_of_nodes(self) -> int:
        return self.number_of_nodes

    def add_directed_edge(self, index1: str, index2: str, weight: float = 1) -> PageRankEdge:
        node1 = self.nodes[index1]
        node2 = self.nodes[index2]

        return PageRank.add_directed_edge_with_nodes(node1, node2, weight)

    @staticmethod
    def add_directed_edge_with_nodes(node1: PageRankNode, node2: PageRankNode, weight: float = 1) -> PageRankEdge:
        edge = PageRankEdge(weight, node1)
        node1.total_weight += weight
        node2.add_edge(edge)
        return edge

    def add_undirected_edge(self, index1: str, index2: str, weight: float = 1) -> PageRankEdge:
        node1 = self.nodes[index1]
        node2 = self.nodes[index2]

        return PageRank.add_undirected_edge_with_nodes(node1, node2, weight)

    @staticmethod
    def add_undirected_edge_with_nodes(node1: PageRankNode, node2: PageRankNode, weight: float = 1) -> PageRankEdge:
        edge1 = PageRankEdge(weight, node1)
        node1.total_weight += weight
        node2.add_edge(edge1)

        edge2 = PageRankEdge(weight, node2)
        node2.total_weight += weight
        node1.add_edge(edge2)

        return edge1

    def __str__(self):
        return self.nodes.__str__()

    def evaluate(self, threshold: float = 0.0001, damping_factor: float = 0.85, max_iterations: int = 1000):
        i = 0
        error = 0
        nodes = self.nodes.values()
        while True:
            for node in nodes:
                new_score = self.calculate_node_score(node, damping_factor)
                node.new_score = new_score

            for node in nodes:
                error += node.get_error()
                node.update()
            i += 1
            if error < threshold or i == max_iterations:
                break
            error = 0

    @staticmethod
    def calculate_node_score(node: PageRankNode, damping_factor: float) -> float:
        score = 0
        edges = node.get_edges()
        for edge in edges:
            score += (edge.weight / edge.node.get_total_weight()) * edge.node.get_score()
        total_score = (1 - damping_factor) + damping_factor * score
        return total_score
