from dependency_injector import containers, providers

from app.analyzers.keywords.candidate_keywords.candidate_keyword_filter.candidate_keyword_filter_module import \
    CandidateKeywordFilterModule
from app.analyzers.keywords.candidate_keywords.candidate_keyword_filter.portion_candidate_keyword_filter import \
    PortionCandidateKeywordFilter


@containers.override(CandidateKeywordFilterModule)
class PortionCandidateKeywordFilterModule(containers.DeclarativeContainer):
    min_keywords = providers.Object(3)
    portion = providers.Object(0.3)

    candidate_keyword_filter = providers.ThreadSafeSingleton(
        PortionCandidateKeywordFilter,
        portion=portion,
        min_keywords=min_keywords
    )
