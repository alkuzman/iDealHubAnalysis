from typing import List, Tuple

import nltk
from nltk.tokenize import word_tokenize

from app.analyzers.algorithms.page_rank.model.node import PageRankNode
from app.analyzers.algorithms.page_rank.model.nodes import PageRankNodes
from app.analyzers.algorithms.page_rank.page_rank import PageRank
from app.analyzers.keywords.candidate_tokens_extractor.candidate_token_extractor import CandidateTokenExtractor
from app.analyzers.keywords.candidate_tokens_extractor.pos_candidate_token_extractor import PosCandidateTokenExtractor
from app.analyzers.keywords.keyword_builders.keyword_builder import Keywords, KeywordBuilder
from app.analyzers.keywords.keyword_builders.pos_keyword_builder import PosKeywordBuilder
from app.analyzers.keywords.keyword_utils import KeywordUtils
from app.analyzers.keywords.relation_weight_calculator.combined_weight_calculator import CombinedWeightCalculator
from app.analyzers.keywords.relation_weight_calculator.cooccurrence_weight_calculator import \
    CooccurrenceWeightCalculator
from app.analyzers.keywords.relation_weight_calculator.relation_weight_calculator import RelationWeightCalculator
from app.analyzers.keywords.relation_weight_calculator.topic_similarity_weight_calculator import \
    TopicSimilarityWeightCalculator

NodeToken = Tuple[PageRankNode, int]
NodeTokens = List[NodeToken]
my_weight_calculator = CombinedWeightCalculator([CooccurrenceWeightCalculator(), TopicSimilarityWeightCalculator()])
TextPiece = Tuple[str, int]
Texts = List[TextPiece]


class KeywordExtractor(object):
    def __init__(self, candidate_tokens_extractor: CandidateTokenExtractor = PosCandidateTokenExtractor(),
                 weight_calculator: RelationWeightCalculator = my_weight_calculator,
                 keyword_builder: KeywordBuilder = PosKeywordBuilder()):
        self.page_rank = None
        self.candidate_tokens_extractor = candidate_tokens_extractor
        self.keyword_builder = keyword_builder
        self.weight_calculator = weight_calculator

    def extract_keywords_for_text(self, texts: Texts) -> Keywords:
        node_tokens = []
        pos_tokens = []
        self.page_rank = PageRank()
        for text_piece in texts:
            tokens = word_tokenize(text_piece[0])
            pos_tokens_piece = nltk.pos_tag(tokens)
            print(pos_tokens_piece)
            pos_tokens += pos_tokens_piece
            nodes = self.add_nodes(pos_tokens_piece, text_piece[1])
            node_tokens += nodes

        self.add_relations(node_tokens)

        self.page_rank.evaluate()
        nodes = self.page_rank.get_nodes()
        print("Number of nodes: ", len(nodes))
        return self.form_keywords(nodes, pos_tokens)

    def add_nodes(self, pos_tokens, initial_score: int = 1) -> NodeTokens:
        candidate_tokens = self.candidate_tokens_extractor.extract(pos_tokens)
        node_tokens = []
        for token in candidate_tokens:
            node = self.page_rank.add_node(token[0], initial_score)
            node_tokens.append((node, token[1]))
        return node_tokens

    def add_relations(self, node_tokens: NodeTokens, window_size: int = 2):

        length = len(node_tokens)
        for index, node_token_1 in enumerate(node_tokens):
            for j in range(index + 1, length):
                node_token_2 = node_tokens[j]
                token_1 = (node_token_1[0].get_name(), node_token_1[1])
                token_2 = (node_token_2[0].get_name(), node_token_2[1])
                weight = self.weight_calculator.calculate(token_1, token_2)

                if weight > 0:
                    self.page_rank.add_undirected_edge_with_nodes(node_token_1[0], node_token_2[0], weight)

    def form_keywords(self, nodes: PageRankNodes, pos_tokens: []) -> Keywords:
        word_scores_dict = KeywordUtils.get_word_scores(nodes)
        return self.keyword_builder.build(word_scores_dict, pos_tokens)
