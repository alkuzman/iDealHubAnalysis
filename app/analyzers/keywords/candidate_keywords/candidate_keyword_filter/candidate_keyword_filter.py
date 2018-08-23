from abc import ABC, abstractmethod
from typing import List, Tuple

from app.analyzers.keywords.candidate_keywords.candidate_keyword import CandidateKeyword


class CandidateKeywordFilter(ABC):
    @abstractmethod
    def filter(self, candidate_keywords: List[Tuple[CandidateKeyword, float]]) -> List[Tuple[CandidateKeyword, float]]:
        pass
