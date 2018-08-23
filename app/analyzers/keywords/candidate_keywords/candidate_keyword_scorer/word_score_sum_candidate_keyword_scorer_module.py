from dependency_injector import containers, providers

from app.analyzers.keywords.candidate_keywords.candidate_keyword_scorer.candidate_keyword_scorer_module import \
    CandidateKeywordScorerModule
from app.analyzers.keywords.candidate_keywords.candidate_keyword_scorer.word_score_sum_candidate_keyword_scorer import \
    WordScoreSumCandidateKeywordScorer


@containers.override(CandidateKeywordScorerModule)
class WordScoreSumCandidateKeywordScorerModule(containers.DeclarativeContainer):
    candidate_keyword_scorer = providers.ThreadSafeSingleton(
        WordScoreSumCandidateKeywordScorer
    )
