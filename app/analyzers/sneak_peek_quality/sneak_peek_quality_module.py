from dependency_injector import containers, providers

from app.analyzers.sneak_peek_quality.sneak_peek_quality_analyzer import SneakPeekQualityAnalyzer


class SneakPeekQualityModule(containers.DeclarativeContainer):
    sneak_peek_quality_analyzer = providers.Singleton(SneakPeekQualityAnalyzer)
