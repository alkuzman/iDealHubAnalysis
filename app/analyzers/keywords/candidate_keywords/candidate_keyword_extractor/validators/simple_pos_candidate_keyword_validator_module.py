from dependency_injector import containers, providers

from app.analyzers.keywords.candidate_keywords.candidate_keyword_extractor.validators\
    .candidate_keyword_validator_module import \
    CandidateKeywordValidatorModule
from app.analyzers.keywords.candidate_keywords.candidate_keyword_extractor.validators\
    .simple_pos_candidate_keyword_validator import \
    SimplePosCandidateKeywordValidator
from app.analyzers.keywords.pos.pos_module import PosModule


@containers.override(CandidateKeywordValidatorModule)
class SimplePosCandidateKeywordValidatorModule(containers.DeclarativeContainer):
    candidate_keyword_validator = providers.ThreadSafeSingleton(
        SimplePosCandidateKeywordValidator,
        pos_tags=PosModule.pos_tags
    )
