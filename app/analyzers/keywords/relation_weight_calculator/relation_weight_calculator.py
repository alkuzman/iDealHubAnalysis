from abc import ABCMeta, abstractmethod
from typing import List

from app.analyzers.keywords.keyword_utils import Token


class RelationWeightCalculator(object):
    @abstractmethod
    def calculate(self, token_1: Token, token_2: Token) -> float: pass


RelationWeightCalculators = List[RelationWeightCalculator]
