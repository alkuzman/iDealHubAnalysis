from dependency_injector import containers, providers

from app.analyzers.algorithms.page_rank.page_rank_module import PageRankModule
from app.analyzers.algorithms.page_rank.standard_page_rank import StandardPageRank


@containers.override(PageRankModule)
class StandardPageRankModule(containers.DeclarativeContainer):
    page_rank = providers.Factory(StandardPageRank)
