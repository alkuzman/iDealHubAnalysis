from dependency_injector import containers, providers

from app.analyzers.keywords.candidate_keywords.candidate_keyword_filter.candidate_keyword_filter_module import \
    CandidateKeywordFilterModule
from app.analyzers.keywords.candidate_keywords.candidate_keyword_filter.combined_candidate_keyword_filter import \
    CombinedCandidateKeywordFilter
from app.analyzers.keywords.candidate_keywords.candidate_keyword_filter.sub_candidate_keyword_filter import \
    SubCandidateKeywordFilter


@containers.override(CandidateKeywordFilterModule)
class CombinedCandidateKeywordFilterModule(containers.DeclarativeContainer):
    sub_candidate_keyword_filter = providers.ThreadSafeSingleton(SubCandidateKeywordFilter)

    candidate_keyword_filter = providers.ThreadSafeSingleton(
        CombinedCandidateKeywordFilter,
        sub_candidate_keyword_filter=sub_candidate_keyword_filter
    )
