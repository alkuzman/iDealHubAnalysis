from typing import List

from app.api_model.generated.api_model_pb2 import SneakPeekAnalysisRequest as ApiSneakPeekAnalysisRequest
from app.model.analysis.request.sneak_peek_quality_analysis_request import SneakPeekQualityAnalysisRequest
from app.model.document.document import Document
from app.model.document.document_set import DocumentSet
from app.model.keyword.keyword import Keyword


class SneakPeekQualityAnalysisRequestApiAdapter(SneakPeekQualityAnalysisRequest):
    def __init__(self, api_sneak_peek_analysis_request: ApiSneakPeekAnalysisRequest, document_set: DocumentSet,
                 sneak_peek_keywords: List[Keyword], main_document_keywords: List[Keyword]):
        self.api_sneak_peek_analysis_request = api_sneak_peek_analysis_request
        self.document_set = document_set
        self.sneak_peek_keywords = sneak_peek_keywords
        self.main_document_keywords = main_document_keywords

    def get_sneak_peek(self) -> Document:
        return self.document_set.get_document(self.api_sneak_peek_analysis_request.sneak_peek_document_id)

    def get_main_document(self) -> Document:
        return self.document_set.get_document(self.api_sneak_peek_analysis_request.main_document_id)

    def get_sneak_peek_keywords(self) -> List[Keyword]:
        return self.sneak_peek_keywords

    def get_main_document_keywords(self) -> List[Keyword]:
        return self.main_document_keywords

