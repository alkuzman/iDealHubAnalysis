from dependency_injector import containers, providers

from app.analyzers.algorithms.graph.edge_module import EdgeModule
from app.analyzers.algorithms.graph.graph_module import GraphModule
from app.analyzers.algorithms.graph.node_module import NodeModule
from app.analyzers.algorithms.graph.undirected_graph import UndirectedGraph


@containers.override(GraphModule)
class UndirectedGraphModule(containers.DeclarativeContainer):
    graph = providers.Factory(UndirectedGraph,
                              node_provider=NodeModule.node.delegate(),
                              node_edges_provider=EdgeModule.node_edges.delegate(),
                              edge_provider=EdgeModule.edge.delegate())
