from typing import List, Tuple, Set

import nltk

from app.analyzers.keywords.candidate_keywords.candidate_keyword import CandidateKeyword
from app.analyzers.keywords.candidate_keywords.candidate_keyword_extractor.candidate_keyword_extractor import \
    CandidateKeywordExtractor
from app.validation.validator import Validator


class MaxLengthCandidateKeywordExtractor(CandidateKeywordExtractor):
    def __init__(self, candidate_keyword_validator: Validator[CandidateKeyword], max_keyword_length: int = 8) -> None:
        super().__init__(candidate_keyword_validator)
        self.max_keyword_length = max_keyword_length

    def get_candidate_keywords(self, pos_tokens: List[Tuple[str, str]]) -> List[CandidateKeyword]:
        candidate_keywords: Set[CandidateKeyword] = set([])

        pos_tokens_len = len(pos_tokens)
        for i in range(0, pos_tokens_len):
            candidate_keyword_pos_tokens: List[Tuple[str, str]] = []
            for j in range(i, min(i + self.max_keyword_length, pos_tokens_len)):
                pos_token = pos_tokens[j]
                if pos_token[1] in [",", "."]:
                    break
                candidate_keyword_pos_tokens.append(pos_token)
                candidate_keyword = CandidateKeyword(candidate_keyword_pos_tokens.copy())
                if self.is_valid(candidate_keyword):
                    candidate_keywords.add(candidate_keyword)
                else:
                    break

        return list(candidate_keywords)
