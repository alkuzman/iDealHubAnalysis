import os
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

from dependency_injector import containers, providers

from app.analyzers import AnalyzerRegistry, SetAnalyzer
from app.analyzers.coverage.coverage_module import CoverageModule
from app.analyzers.keywords.keyword_module import KeywordModule
from app.analyzers.sneak_peek_quality.sneak_peek_quality_module import SneakPeekQualityModule

ANALYZER_THREAD_POOL_SIZE_ENV = "APP_ANALYZER_THREAD_POOL_SIZE"


class AnalyzerModule(containers.DeclarativeContainer):
    pool_size = providers.Object(os.environ.get(ANALYZER_THREAD_POOL_SIZE_ENV) or None)
    executor = providers.Singleton(ThreadPoolExecutor,
                                   pool_size)
    set_analyzer = providers.Singleton(SetAnalyzer,
                                       keyword_analyzer_provider=KeywordModule.keyword_analyzer.delegate(),
                                       coverage_analyzer=CoverageModule.coverage_analyzer,
                                       sneak_peek_analyzer=SneakPeekQualityModule.sneak_peek_quality_analyzer,
                                       executor=executor)

    analyzer = providers.Singleton(AnalyzerRegistry,
                                   set_analyzer=set_analyzer)
