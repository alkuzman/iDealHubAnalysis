from dependency_injector import containers, providers

from app.analyzers.keywords.candidate_keywords.candidate_keyword_extractor.validators.candidate_keyword_validator \
    import \
    CandidateKeywordValidator


class CandidateKeywordValidatorModule(containers.DeclarativeContainer):
    candidate_keyword_validator = providers.ThreadSafeSingleton(CandidateKeywordValidator)
