from dependency_injector import containers, providers

from app.analyzers.keywords.keyword_builders.keyword_builder_module import KeywordBuilderModule
from app.analyzers.keywords.keyword_builders.pos_keyword_builder import PosKeywordBuilder
from app.analyzers.keywords.pos.pos_module import PosModule


@containers.override(KeywordBuilderModule)
class PosKeywordBuilderModule(containers.DeclarativeContainer):
    min_word_score = providers.Object(0.00001)

    keyword_builder = providers.ThreadSafeSingleton(PosKeywordBuilder,
                                                    pos_tags=PosModule.pos_tags,
                                                    min_word_score=min_word_score)
