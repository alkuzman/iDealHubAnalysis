from typing import List, Tuple

import matplotlib.pyplot as plt

from app.analyzers.keywords.candidate_keywords.candidate_keyword import CandidateKeyword
from app.analyzers.keywords.candidate_keywords.candidate_keyword_extractor.candidate_keyword_extractor import \
    CandidateKeywordExtractor
from app.analyzers.keywords.candidate_keywords.candidate_keyword_filter.candidate_keyword_filter import \
    CandidateKeywordFilter
from app.analyzers.keywords.candidate_keywords.candidate_keyword_scorer.candidate_keyword_scorer import \
    CandidateKeywordScorer
from app.analyzers.keywords.keyword_builders.keyword_builder import KeywordBuilder, WordScores, Keywords, KeywordImpl


class StandardKeywordBuilder(KeywordBuilder):
    """
    This keyword builder uses :class:`CandidateKeywordExtractor` to get candidate keywords, then it
    uses :class:`CandidateKeywordScorer` to attach scores to each keyword and then uses
    :class:`CandidateKeywordFilter` in order to filter the keywords that either have bet score or don't make sense.
    """

    def __init__(self,
                 candidate_keyword_extractor: CandidateKeywordExtractor,
                 candidate_keyword_scorer: CandidateKeywordScorer,
                 candidate_keyword_filter: CandidateKeywordFilter) -> None:
        """
        Create new standard keyword builder which uses :class:`CandidateKeywordExtractor`,
        :class:`CandidateKeywordScorer`, and :class:`CandidateKeywordFilter`

        :param candidate_keyword_extractor: which helps with extracting candidate keywords from pos tags.
        :param candidate_keyword_scorer: scores and sorts the candidate keywords (descending) by score.
        :param candidate_keyword_filter: filters the scored keywords, so only the most relevant remain.
        """
        super().__init__()
        self.candidate_keyword_extractor = candidate_keyword_extractor
        self.candidate_keyword_scorer = candidate_keyword_scorer
        self.candidate_keyword_filter = candidate_keyword_filter

    def build(self, word_scores_dict: WordScores, pos_tokens: []) -> Keywords:
        candidate_keywords = self.candidate_keyword_extractor.get_candidate_keywords(pos_tokens)
        scored_candidate_keywords = self.candidate_keyword_scorer.score(candidate_keywords, word_scores_dict)
        scored_candidate_keywords.sort(key=lambda keyword: keyword[1], reverse=True)
        final_candidate_keywords = self.candidate_keyword_filter.filter(scored_candidate_keywords)
        # x = range(0, len(final_candidate_keywords))
        # y = [candidate_keyword[1] for candidate_keyword in final_candidate_keywords]
        # plt.plot(x, y, 'ro')
        # plt.show()
        return self.convert(final_candidate_keywords)

    @staticmethod
    def convert(final_candidate_keywords: List[Tuple[CandidateKeyword, float]]):
        return [
            KeywordImpl(
                " ".join([pos_token[0]
                          for pos_token in candidate_keyword[0].pos_tokens]),
                candidate_keyword[1]
            )
            for candidate_keyword in final_candidate_keywords
        ]
