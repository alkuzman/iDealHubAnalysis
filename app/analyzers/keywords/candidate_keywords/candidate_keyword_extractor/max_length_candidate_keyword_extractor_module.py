from dependency_injector import containers, providers

from app.analyzers.keywords.candidate_keywords.candidate_keyword_extractor.candidate_keyword_extractor_module import \
    CandidateKeywordExtractorModule
from app.analyzers.keywords.candidate_keywords.candidate_keyword_extractor.max_length_candidate_keyword_extractor \
    import MaxLengthCandidateKeywordExtractor
from app.analyzers.keywords.candidate_keywords.candidate_keyword_extractor.validators \
    .candidate_keyword_validator_module import \
    CandidateKeywordValidatorModule


@containers.override(CandidateKeywordExtractorModule)
class MaxLengthCandidateKeywordExtractorModule(containers.DeclarativeContainer):
    max_length = providers.Object(8)

    candidate_keyword_extractor = providers.ThreadSafeSingleton(
        MaxLengthCandidateKeywordExtractor,
        candidate_keyword_validator=CandidateKeywordValidatorModule.candidate_keyword_validator,
        max_keyword_length=max_length
    )
