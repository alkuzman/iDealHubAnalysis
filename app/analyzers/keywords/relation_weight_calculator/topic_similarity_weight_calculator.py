from app.analyzers.keywords.keyword_utils import Token
from app.analyzers.keywords.relation_weight_calculator.relation_weight_calculator import RelationWeightCalculator
from app.data_import.topics.word_similarity import WordSimilarity


class TopicSimilarityWeightCalculator(RelationWeightCalculator):
    def __init__(self, min_similarity: int = 0.5):
        self.word_similarity = WordSimilarity()
        self.min_similarity = min_similarity

    def calculate(self, token_1: Token, token_2: Token) -> float:
        word_1 = token_1[0]
        word_2 = token_2[0]
        similarity = self.word_similarity.get_similarity(word_1.lower(), word_2.lower())
        if similarity > self.min_similarity:
            return similarity
        return 0
