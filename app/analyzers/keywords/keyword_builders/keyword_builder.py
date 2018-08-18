from abc import ABCMeta, abstractmethod
from typing import Dict, List

from app.model.keyword.keyword import Keyword

WordScores = Dict[str, float]


class KeywordImpl(Keyword):

    def __init__(self, phrase: str, score: float):
        self.phrase = phrase
        self.score = score
        self.type = "Keyword"

    def get_phrase(self) -> str:
        return self.phrase

    def get_score(self) -> float:
        return self.score


Keywords = List[KeywordImpl]


class KeywordBuilder:
    @abstractmethod
    def build(self, word_scores_dict: WordScores, pos_tokens: []) -> Keywords: pass
