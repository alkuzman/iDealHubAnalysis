from dependency_injector import containers, providers


class PosModule(containers.DeclarativeContainer):
    pos_tags = providers.Object(["JJ", "NN", "NNP", "JJR", "JJS", "NNS", "NNPS"])
