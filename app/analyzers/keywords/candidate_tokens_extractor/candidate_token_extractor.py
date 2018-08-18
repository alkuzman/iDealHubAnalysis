from abc import abstractmethod

from app.analyzers.keywords.keyword_utils import Tokens


class CandidateTokenExtractor(object):

    @abstractmethod
    def extract(self, pos_tokens: []) -> Tokens: pass
