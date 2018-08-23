from abc import ABCMeta, abstractmethod
from typing import List, Tuple

from app.analyzers.keywords.candidate_keywords.candidate_keyword import CandidateKeyword
from app.validation.validator import Validator


class CandidateKeywordExtractor(metaclass=ABCMeta):
    def __init__(self, candidate_keyword_validator: Validator[CandidateKeyword]) -> None:
        super().__init__()
        self.candidate_keyword_validator: Validator[CandidateKeyword] = candidate_keyword_validator

    def is_valid(self, candidate_keyword: CandidateKeyword) -> bool:
        if candidate_keyword is None:
            return False
        error_response = self.candidate_keyword_validator.validate(candidate_keyword)
        if len(error_response.validation_errors) > 0:
            return False
        return True

    @abstractmethod
    def get_candidate_keywords(self, pos_tokens: List[Tuple[str, str]]) -> List[CandidateKeyword]:
        pass
