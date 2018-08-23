from dependency_injector import containers, providers

from app.analyzers.keywords.candidate_keywords.candidate_keyword_scorer.candidate_keyword_scorer_module import \
    CandidateKeywordScorerModule
from app.analyzers.keywords.candidate_keywords.candidate_keyword_scorer.quantile_candidate_keyword_scorer import \
    QuantileCandidateKeywordScorer


@containers.override(CandidateKeywordScorerModule)
class QuantileCandidateKeywordScorerModule(containers.DeclarativeContainer):
    candidate_keyword_scorer = providers.ThreadSafeSingleton(
        QuantileCandidateKeywordScorer
    )