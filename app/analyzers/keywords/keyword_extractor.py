from typing import List, Tuple

import nltk
from dependency_injector.providers import Provider
from nltk.tokenize import word_tokenize

from app.analyzers.algorithms.graph.graph import Graph
from app.analyzers.algorithms.graph.node import Node
from app.analyzers.algorithms.page_rank.page_rank import PageRank
from app.analyzers.keywords.candidate_tokens_extractor.candidate_token_extractor import CandidateTokenExtractor
from app.analyzers.keywords.keyword_builders.keyword_builder import Keywords, KeywordBuilder
from app.analyzers.keywords.keyword_utils import KeywordUtils
from app.analyzers.keywords.relation_weight_calculator.relation_weight_calculator import RelationWeightCalculator

NodeToken = Tuple[Node, int]
NodeTokens = List[NodeToken]
TextPiece = Tuple[str, float]
Texts = List[TextPiece]


class KeywordExtractor(object):
    def __init__(self, candidate_tokens_extractor: CandidateTokenExtractor,
                 keyword_builder: KeywordBuilder,
                 weight_calculator: RelationWeightCalculator,
                 graph_provider: Provider,
                 page_rank_provider: Provider):
        self.candidate_tokens_extractor = candidate_tokens_extractor
        self.keyword_builder = keyword_builder
        self.weight_calculator = weight_calculator
        self.graph_provider = graph_provider
        self.page_rank_provider = page_rank_provider

    def extract_keywords_for_text(self, texts: Texts) -> Keywords:
        node_tokens = []
        pos_tokens = []
        graph: Graph = self.graph_provider()
        for text_piece in texts:
            tokens = word_tokenize(text_piece[0])
            pos_tokens_piece = nltk.pos_tag(tokens)
            pos_tokens += pos_tokens_piece
            nodes = self.add_nodes(graph, pos_tokens_piece, text_piece[1])
            node_tokens += nodes

        self.add_relations(graph, node_tokens)

        graph_page_rank: PageRank = self.page_rank_provider(graph=graph)
        graph_page_rank.run()

        # Get nodes with calculated weights
        nodes = graph.get_all_nodes()
        # Order nodes by their weight descending.
        nodes.sort(key=lambda node: node.get_weight(), reverse=True)
        return self.form_keywords(nodes, pos_tokens)

    def add_nodes(self, graph: Graph, pos_tokens, initial_score: float = 1) -> NodeTokens:
        candidate_tokens = self.candidate_tokens_extractor.extract(pos_tokens)
        node_tokens = []
        for token in candidate_tokens:
            node = graph.create_node(token[0], initial_score)
            node_tokens.append((node, token[1]))
        return node_tokens

    def add_relations(self, graph: Graph, node_tokens: NodeTokens):
        length = len(node_tokens)
        for index, node_token_1 in enumerate(node_tokens):
            for j in range(index + 1, length):
                node_token_2 = node_tokens[j]
                token_1 = (node_token_1[0].get_name(), node_token_1[1])
                token_2 = (node_token_2[0].get_name(), node_token_2[1])
                weight = self.weight_calculator.calculate(token_1, token_2)

                if weight > 0:
                    graph.add_edge(node_token_1[0], node_token_2[0], weight)

    def form_keywords(self, nodes: List[Node], pos_tokens: []) -> Keywords:
        word_scores_dict = KeywordUtils.get_word_scores(nodes)
        return self.keyword_builder.build(word_scores_dict, pos_tokens)
