from dependency_injector import containers, providers

from app.analyzers.keywords.keyword_builders.keyword_builder import KeywordBuilder


class KeywordBuilderModule(containers.DeclarativeContainer):
    keyword_builder = providers.ThreadSafeSingleton(KeywordBuilder)
