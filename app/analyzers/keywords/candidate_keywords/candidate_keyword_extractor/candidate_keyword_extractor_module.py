from dependency_injector import containers, providers

from app.analyzers.keywords.candidate_keywords.candidate_keyword_extractor.candidate_keyword_extractor import \
    CandidateKeywordExtractor


class CandidateKeywordExtractorModule(containers.DeclarativeContainer):
    candidate_keyword_extractor = providers.ThreadSafeSingleton(CandidateKeywordExtractor)
