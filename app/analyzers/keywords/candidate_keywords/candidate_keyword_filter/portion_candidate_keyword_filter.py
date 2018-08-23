from typing import List, Tuple

from app.analyzers.keywords.candidate_keywords.candidate_keyword import CandidateKeyword
from app.analyzers.keywords.candidate_keywords.candidate_keyword_filter.candidate_keyword_filter import \
    CandidateKeywordFilter


class PortionCandidateKeywordFilter(CandidateKeywordFilter):
    def __init__(self, portion: float = 0.3, min_keywords: int = 3) -> None:
        super().__init__()
        self.portion = portion
        self.min_keywords = min_keywords

    def filter(self, candidate_keywords: List[Tuple[CandidateKeyword, float]]) -> List[Tuple[CandidateKeyword, float]]:
        candidate_len = len(candidate_keywords)
        end_index = max(round(candidate_len * self.portion), min(candidate_len, self.min_keywords))
        return candidate_keywords[0:end_index]
