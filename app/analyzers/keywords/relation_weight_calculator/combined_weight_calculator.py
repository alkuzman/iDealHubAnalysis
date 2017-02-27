from app.analyzers.keywords.keyword_utils import Token
from app.analyzers.keywords.relation_weight_calculator.relation_weight_calculator import RelationWeightCalculator, \
    RelationWeightCalculators


class CombinedWeightCalculator(RelationWeightCalculator):
    def __init__(self, calculators: RelationWeightCalculators):
        self.calculators = calculators

    def calculate(self, token_1: Token, token_2: Token) -> float:
        weight = 0.0
        for calculator in self.calculators:
            weight += calculator.calculate(token_1, token_2)
        return weight
