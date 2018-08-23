from dependency_injector import containers, providers

from app.analyzers.keywords.candidate_keywords.candidate_keyword_filter.candidate_keyword_filter import \
    CandidateKeywordFilter


class CandidateKeywordFilterModule(containers.DeclarativeContainer):
    candidate_keyword_filter = providers.ThreadSafeSingleton(CandidateKeywordFilter)
