from dependency_injector import containers, providers

from app.analyzers.keywords.candidate_tokens_extractor.candidate_token_extractor_module import \
    CandidateTokenExtractorModule
from app.analyzers.keywords.candidate_tokens_extractor.pos_candidate_token_extractor import PosCandidateTokenExtractor
from app.analyzers.keywords.pos.pos_module import PosModule


@containers.override(CandidateTokenExtractorModule)
class PosCandidateTokenExtractorModule(containers.DeclarativeContainer):
    candidate_token_extractor = providers.ThreadSafeSingleton(PosCandidateTokenExtractor,
                                                              pos_tags=PosModule.pos_tags)
