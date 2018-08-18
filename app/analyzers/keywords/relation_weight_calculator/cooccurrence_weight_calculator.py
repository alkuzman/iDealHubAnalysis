from app.analyzers.keywords.keyword_utils import Token
from app.analyzers.keywords.relation_weight_calculator.relation_weight_calculator import RelationWeightCalculator


class CooccurrenceWeightCalculator(RelationWeightCalculator):
    def __init__(self, window_size: int):
        self.window_size = window_size

    def calculate(self, token_1: Token, token_2: Token) -> float:
        position1 = token_1[1]
        position2 = token_2[1]
        # calculate positional difference between two nodes (words) in the text
        difference = abs(position1 - position2)
        if difference == 0 or difference >= self.window_size:
            return 0
        return 1 / difference