from dependency_injector import containers, providers

from app.analyzers import KeywordAnalyzer
from app.analyzers.algorithms.graph.graph_module import GraphModule
from app.analyzers.algorithms.page_rank.page_rank_module import PageRankModule
from app.analyzers.keywords.candidate_tokens_extractor.candidate_token_extractor_module import \
    CandidateTokenExtractorModule
from app.analyzers.keywords.keyword_builders.keyword_builder_module import KeywordBuilderModule
from app.analyzers.keywords.keyword_extractor import KeywordExtractor
from app.analyzers.keywords.relation_weight_calculator.relation_weight_calculator_module import \
    RelationWeightCalculatorModule


class KeywordModule(containers.DeclarativeContainer):
    keyword_extractor = providers \
        .ThreadLocalSingleton(KeywordExtractor,
                              candidate_tokens_extractor=CandidateTokenExtractorModule.candidate_token_extractor,
                              keyword_builder=KeywordBuilderModule.keyword_builder,
                              weight_calculator=RelationWeightCalculatorModule.relation_weight_calculator,
                              graph_provider=GraphModule.graph.delegate(),
                              page_rank_provider=PageRankModule.page_rank.delegate())

    keyword_analyzer = providers.ThreadLocalSingleton(KeywordAnalyzer,
                                                      keyword_extractor=keyword_extractor)
