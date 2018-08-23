from dependency_injector import containers, providers


class PosModule(containers.DeclarativeContainer):
    pos_tags = providers.Object({"JJ", "JJR", "JJS", "NN", "NNS", "NNP", "NNPS"})
    all_pos_tags = providers.Object({
        "JJ", "JJR", "JJS", "NN", "NNS", "NNP", "NNPS", "CD", "CC", "DT", "EX", "FW", "IN", "MD",
        "PDT", "POS", "PRP", "PRP$", "RB", "RBR", "RBS", "RP", "TO", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "WDT",
        "WP", "WP$", "WRB"
    })
