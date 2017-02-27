from typing import Tuple, List

from app.analyzers.algorithms.page_rank.model.nodes import PageRankNodes
from app.analyzers.keywords.keyword_builders.keyword_builder import WordScores

Token = Tuple[str, int]
Tokens = List[Token]


class KeywordUtils(object):

    @staticmethod
    def get_word_scores(nodes: PageRankNodes) -> WordScores:
        word_scores_dict = {}
        for node in nodes:
            word_scores_dict[node.get_name()] = node.get_score()

        return word_scores_dict