from dependency_injector import containers, providers

from app.analyzers.algorithms.graph.node import Node


class NodeModule(containers.DeclarativeContainer):
    node = providers.Factory(Node)
