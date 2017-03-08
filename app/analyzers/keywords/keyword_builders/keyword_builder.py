from typing import Dict, Tuple, List

WordScores = Dict[str, float]


class Keyword(object):
    def __init__(self, phrase: str, score: float):
        self.phrase = phrase
        self.score = score
        self.type = "Keyword"

    def __hash__(self):
        return hash(self.phrase)

    def __eq__(self, other):
        return self.phrase.lower() == other.phrase.lower()


Keywords = List[Keyword]


class KeywordBuilder(object):
    def build(self, word_scores_dict: WordScores, pos_tokens: []) -> Keywords: pass
