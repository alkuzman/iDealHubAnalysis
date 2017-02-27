from app.analyzers.algorithms.page_rank.model.score_node import ScoreNode


class PageRankEdge(object):

    def __init__(self, weight: float, node: ScoreNode):
        self.weight = weight
        self.node = node

    def get_node(self) -> ScoreNode:
        return self.node

    def get_weight(self) -> float:
        return self.weight

    def __str__(self):
        return "Name: " + self.node.name + ", Weight: " + self.weight.__str__()
