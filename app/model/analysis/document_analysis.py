import json

from app.analyzers.keywords.keyword_builders.keyword_builder import Keywords
from app.model.complex_encoder import ComplexEncoder


class DocumentAnalysis(object):
    def __init__(self, keywords: Keywords):
        self.keywords = keywords

    def __repr__(self):
        return json.dumps(self.__dict__, default=ComplexEncoder)
