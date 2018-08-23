import math
from typing import List, Dict, Tuple

from app.analyzers.keywords.candidate_keywords.candidate_keyword import CandidateKeyword
from app.analyzers.keywords.candidate_keywords.candidate_keyword_scorer.candidate_keyword_scorer import \
    CandidateKeywordScorer


class QuantileCandidateKeywordScorer(CandidateKeywordScorer):

    def __init__(self, quantile: float = 0.25) -> None:
        if quantile > 1 or quantile < 0:
            raise Exception('The quantile must be in the interval [0, 1]. But the following value vas received',
                            quantile)
        self.quantile = quantile

    def score(self, candidate_keywords: List[CandidateKeyword], word_scores: Dict[str, float]) -> \
            List[Tuple[CandidateKeyword, float]]:

        word_scores_length = len(word_scores)
        if word_scores_length == 0:
            return []

        scores = list(word_scores.values())
        scores.sort(key=lambda score: score)
        index = round(self.quantile * (word_scores_length - 1))
        ref_value = scores[index]  # .get(index, 0)

        result = \
            [
                (
                    candidate_keyword,
                    math.fsum(
                        [
                            word_scores.get(pos_token[0], 0) - ref_value
                            for pos_token in candidate_keyword.pos_tokens
                        ]
                    )
                ) for candidate_keyword in candidate_keywords
            ]
        return result
