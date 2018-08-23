from dependency_injector import containers, providers

from app.analyzers.keywords.candidate_keywords.candidate_keyword_extractor.candidate_keyword_extractor_module import \
    CandidateKeywordExtractorModule
from app.analyzers.keywords.candidate_keywords.candidate_keyword_filter.candidate_keyword_filter_module import \
    CandidateKeywordFilterModule
from app.analyzers.keywords.candidate_keywords.candidate_keyword_scorer.candidate_keyword_scorer_module import \
    CandidateKeywordScorerModule
from app.analyzers.keywords.keyword_builders.keyword_builder_module import KeywordBuilderModule
from app.analyzers.keywords.keyword_builders.standard_keyword_builder import StandardKeywordBuilder


@containers.override(KeywordBuilderModule)
class StandardKeywordBuilderModule(containers.DeclarativeContainer):
    keyword_builder = providers.ThreadSafeSingleton(
        StandardKeywordBuilder,
        candidate_keyword_extractor=CandidateKeywordExtractorModule.candidate_keyword_extractor,
        candidate_keyword_scorer=CandidateKeywordScorerModule.candidate_keyword_scorer,
        candidate_keyword_filter=CandidateKeywordFilterModule.candidate_keyword_filter
    )
