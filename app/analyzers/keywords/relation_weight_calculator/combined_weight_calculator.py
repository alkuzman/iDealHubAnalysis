from app.analyzers.keywords.keyword_utils import Token
from app.analyzers.keywords.relation_weight_calculator.relation_weight_calculator import RelationWeightCalculator, \
    RelationWeightCalculators


class CombinedWeightCalculator(RelationWeightCalculator):
    def __init__(self, *args, **kwargs):
        self.calculators: RelationWeightCalculators = []
        for arg in args:
            self.calculators.append(arg)

        for arg in kwargs:
            self.calculators.append(kwargs[arg])

    def calculate(self, token_1: Token, token_2: Token) -> float:
        weight = 0.0
        for calculator in self.calculators:
            weight += calculator.calculate(token_1, token_2)
        return weight
