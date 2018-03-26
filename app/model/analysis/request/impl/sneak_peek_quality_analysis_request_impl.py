from typing import List

from app.model.analysis.request.sneak_peek_quality_analysis_request import SneakPeekQualityAnalysisRequest
from app.model.document.document import Document
from app.model.keyword.keyword import Keyword


class SneakPeekQualityAnalysisRequestImpl(SneakPeekQualityAnalysisRequest):
    def __init__(self, sneak_peek: Document, main_document: Document, sneak_peek_keywords: List[Keyword],
                 main_document_keywords: List[Keyword]):
        self.sneak_peek = sneak_peek
        self.main_document = main_document
        self.sneak_peek_keywords = sneak_peek_keywords
        self.main_document_keywords = main_document_keywords

    def get_sneak_peek(self) -> Document:
        return self.sneak_peek

    def get_main_document(self) -> Document:
        return self.main_document

    def get_sneak_peek_keywords(self) -> List[Keyword]:
        return self.sneak_peek_keywords

    def get_main_document_keywords(self) -> List[Keyword]:
        return self.main_document_keywords
