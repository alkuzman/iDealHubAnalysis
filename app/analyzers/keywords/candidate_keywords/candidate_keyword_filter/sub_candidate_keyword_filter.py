from typing import List, Tuple

from app.analyzers.keywords.candidate_keywords.candidate_keyword import CandidateKeyword
from app.analyzers.keywords.candidate_keywords.candidate_keyword_filter.candidate_keyword_filter import \
    CandidateKeywordFilter


class SubCandidateKeywordFilter(CandidateKeywordFilter):
    def filter(self, candidate_keywords: List[Tuple[CandidateKeyword, float]]) -> List[Tuple[CandidateKeyword, float]]:
        result = [keyword for index, keyword in enumerate(candidate_keywords) if
                  SubCandidateKeywordFilter.should_be_taken(candidate_keywords, keyword[0], index)]
        return result

    @staticmethod
    def should_be_taken(candidate_keywords: List[Tuple[CandidateKeyword, float]],
                        candidate_keyword: CandidateKeyword,
                        index: int) -> bool:
        for i in range(0, index):
            super_candidate_keyword = candidate_keywords[i]
            if SubCandidateKeywordFilter.is_sub_keyword(candidate_keyword, super_candidate_keyword[0]):
                return False
        return True

    @staticmethod
    def is_sub_keyword(sub_keyword: CandidateKeyword, super_keyword: CandidateKeyword) -> bool:
        sub_len = len(sub_keyword.get_pos_tokens())
        super_len = len(super_keyword.get_pos_tokens())
        if sub_len > super_len:
            return False
        for i in range(0, super_len - sub_len + 1):
            sub_keyword_processed_index = 0
            for j in range(0, sub_len):
                super_word = super_keyword.get_pos_tokens()[i + j][0]
                sub_word = sub_keyword.get_pos_tokens()[j][0]
                if super_word.lower() != sub_word.lower():
                    break
                sub_keyword_processed_index = j
            if sub_keyword_processed_index == sub_len - 1:
                return True
        return False
