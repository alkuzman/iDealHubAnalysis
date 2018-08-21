from dependency_injector import containers, providers

from app.analyzers.algorithms.page_rank.matrix_page_rank import MatrixPageRank
from app.analyzers.algorithms.page_rank.page_rank_module import PageRankModule


@containers.override(PageRankModule)
class MatrixPageRankModule(containers.DeclarativeContainer):
    page_rank = providers.Factory(MatrixPageRank)
