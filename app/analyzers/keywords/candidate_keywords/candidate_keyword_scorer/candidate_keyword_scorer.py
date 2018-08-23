from abc import ABC, abstractmethod
from typing import List, Dict, Tuple

from app.analyzers.keywords.candidate_keywords.candidate_keyword import CandidateKeyword


class CandidateKeywordScorer(ABC):
    @abstractmethod
    def score(self, candidate_keywords: List[CandidateKeyword], word_scores: Dict[str, float]) -> \
            List[Tuple[CandidateKeyword, float]]:
        pass
