from dependency_injector import containers, providers

from app.analyzers.algorithms.graph.edge_module import EdgeModule
from app.analyzers.algorithms.graph.node_unique_edges import NodeUniqueEdges


@containers.override(EdgeModule)
class UniqueEdgeModule(containers.DeclarativeContainer):
    node_edges = providers.Factory(NodeUniqueEdges)
