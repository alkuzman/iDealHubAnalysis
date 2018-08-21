from dependency_injector import containers, providers

from app.analyzers.algorithms.graph.edge_module import EdgeModule
from app.analyzers.algorithms.graph.graph import Graph
from app.analyzers.algorithms.graph.node_module import NodeModule


class GraphModule(containers.DeclarativeContainer):
    graph = providers.Factory(Graph,
                              node_provider=NodeModule.node.delegate(),
                              node_edges_provider=EdgeModule.node_edges.delegate())
