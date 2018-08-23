from typing import List, Tuple

from app.analyzers.keywords.candidate_keywords.candidate_keyword import CandidateKeyword
from app.analyzers.keywords.candidate_keywords.candidate_keyword_filter.candidate_keyword_filter import \
    CandidateKeywordFilter
from app.analyzers.keywords.candidate_keywords.candidate_keyword_filter.sub_candidate_keyword_filter import \
    SubCandidateKeywordFilter


class CombinedCandidateKeywordFilter(CandidateKeywordFilter):
    def __init__(self, sub_candidate_keyword_filter: SubCandidateKeywordFilter) -> None:
        self.sub_candidate_keyword_filter = sub_candidate_keyword_filter

    def filter(self, candidate_keywords: List[Tuple[CandidateKeyword, float]]) -> List[Tuple[CandidateKeyword, float]]:
        return self.sub_candidate_keyword_filter.filter(candidate_keywords)
