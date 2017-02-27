from app.analyzers.algorithms.page_rank.model.edge import PageRankEdge
from app.analyzers.algorithms.page_rank.model.edges import PageRankEdges


class PageRankNode(object):

    def __init__(self, index: int, name: str, initial_score: float = 1):
        self.index = index
        self.name = name
        self.score = initial_score
        self.new_score = 0.0
        self.edges = {}
        self.total_weight = 0

    def add_edge(self, edge: PageRankEdge):
        name = edge.node.get_name()
        old_edge = self.edges.get(name)
        if old_edge is None:
            self.edges[name] = edge
        else:
            old_edge.weight += edge.weight

    def get_edges(self) -> PageRankEdges:
        return list(self.edges.values())

    def get_score(self) -> float:
        return self.score

    def get_name(self) -> str:
        return self.name

    def get_new_score(self) -> float:
        return self.new_score

    def get_index(self) -> float:
        return self.index

    def get_total_weight(self) -> float:
        return self.total_weight

    def get_error(self) -> float:
        return abs(self.score - self.new_score)

    def update(self):
        self.score = self.new_score

    def __str__(self):
        return "Index: " + str(self.index) + ", Name: " + self.name + " Score: " + self.score.__str__() + ", Edges: " + self.edges.__str__()
