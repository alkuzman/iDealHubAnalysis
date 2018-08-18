from dependency_injector import containers, providers

from app.analyzers.algorithms.page_rank.page_rank import PageRank


class PageRankModule(containers.DeclarativeContainer):
    page_rank = providers.Factory(PageRank)
