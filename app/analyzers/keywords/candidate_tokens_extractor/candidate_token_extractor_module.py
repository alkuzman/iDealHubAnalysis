from dependency_injector import containers, providers

from app.analyzers.keywords.candidate_tokens_extractor.candidate_token_extractor import CandidateTokenExtractor


class CandidateTokenExtractorModule(containers.DeclarativeContainer):
    candidate_token_extractor = providers.Singleton(CandidateTokenExtractor)
