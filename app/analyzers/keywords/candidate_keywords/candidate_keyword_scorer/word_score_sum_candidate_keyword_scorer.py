import math
from typing import List, Dict, Tuple

from app.analyzers.keywords.candidate_keywords.candidate_keyword import CandidateKeyword
from app.analyzers.keywords.candidate_keywords.candidate_keyword_scorer.candidate_keyword_scorer import \
    CandidateKeywordScorer


class WordScoreSumCandidateKeywordScorer(CandidateKeywordScorer):
    def score(self, candidate_keywords: List[CandidateKeyword], word_scores: Dict[str, float]) -> \
            List[Tuple[CandidateKeyword, float]]:
        result = \
            [
                (
                    candidate_keyword,
                    math.fsum(
                        [
                            word_scores.get(pos_token[0], 0)
                            for pos_token in candidate_keyword.pos_tokens
                        ]
                    )
                ) for candidate_keyword in candidate_keywords
            ]
        return result
