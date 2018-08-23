from dependency_injector import containers, providers

from app.analyzers.keywords.candidate_keywords.candidate_keyword_scorer.candidate_keyword_scorer import \
    CandidateKeywordScorer


class CandidateKeywordScorerModule(containers.DeclarativeContainer):
    candidate_keyword_scorer = providers.ThreadSafeSingleton(CandidateKeywordScorer)
