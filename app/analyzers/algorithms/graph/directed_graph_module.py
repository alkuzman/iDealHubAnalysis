from dependency_injector import containers, providers

from app.analyzers.algorithms.graph.directed_graph import DirectedGraph
from app.analyzers.algorithms.graph.edge_module import EdgeModule
from app.analyzers.algorithms.graph.graph_module import GraphModule
from app.analyzers.algorithms.graph.node_module import NodeModule


@containers.override(GraphModule)
class DirectedGraphModule(containers.DeclarativeContainer):
    graph = providers.Factory(DirectedGraph,
                              node_provider=NodeModule.node.delegate(),
                              node_edges_provider=EdgeModule.node_edges.delegate(),
                              edge_provider=EdgeModule.edge.delegate())
