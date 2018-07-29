from dependency_injector import containers, providers

from app.analyzers.coverage.coverage_analyzer import CoverageAnalyzer


class CoverageModule(containers.DeclarativeContainer):
    coverage_analyzer = providers.Singleton(CoverageAnalyzer)
