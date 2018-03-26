from typing import List

from app.model.analysis.response.keyword_analysis import KeywordAnalysis
from app.model.document.document import Document
from app.model.keyword.keyword import Keyword


class KeywordAnalysisImpl(KeywordAnalysis):
    def __init__(self, document: Document, keywords: List[Keyword]):
        self.document = document
        self.keywords = keywords

    def get_document(self) -> Document:
        return self.document

    def get_keywords(self) -> List[Keyword]:
        return self.keywords
