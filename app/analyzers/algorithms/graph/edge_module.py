from dependency_injector import containers, providers

from app.analyzers.algorithms.graph.edge import Edge
from app.analyzers.algorithms.graph.node_edges import NodeEdges


class EdgeModule(containers.DeclarativeContainer):
    edge = providers.Factory(Edge)

    node_edges = providers.Factory(NodeEdges)
