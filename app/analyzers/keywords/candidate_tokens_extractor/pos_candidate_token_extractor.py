from app.analyzers.keywords.candidate_tokens_extractor.candidate_token_extractor import CandidateTokenExtractor, \
    Tokens

my_pos_tags = ["JJ", "NN", "NNP", "JJR", "JJS", "NNS", "NNPS"]


class PosCandidateTokenExtractor(CandidateTokenExtractor):

    def __init__(self, pos_tags: [] = my_pos_tags):
        self.pos_tags = pos_tags

    def extract(self, pos_tokens: []) -> Tokens:
        candidate_tokens = []
        for index, token in enumerate(pos_tokens):
            if token[1] in self.pos_tags:
                candidate_tokens.append((token[0], index + 1))
        return candidate_tokens
