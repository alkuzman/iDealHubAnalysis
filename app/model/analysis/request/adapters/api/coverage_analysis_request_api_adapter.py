from typing import List

from app.api_model.generated.api_model_pb2 import CoverageAnalysisRequest as ApiCoverageAnalysisRequest
from app.model.analysis.request.coverage_analysis_request import CoverageAnalysisRequest
from app.model.document.document import Document
from app.model.document.document_set import DocumentSet
from app.model.keyword.keyword import Keyword


class CoverageAnalysisRequestApiAdapter(CoverageAnalysisRequest):
    def __init__(self, api_coverage_analysis_request: ApiCoverageAnalysisRequest, document_set: DocumentSet,
                 cover_keywords: List[Keyword], covered_keywords: List[Keyword]):
        self.api_coverage_analysis_request = api_coverage_analysis_request
        self.document_set = document_set
        self.cover_keywords = cover_keywords
        self.covered_keywords = covered_keywords

    def get_cover(self) -> Document:
        return self.document_set.get_document(self.api_coverage_analysis_request.cover_document_id)

    def get_covered(self) -> Document:
        return self.document_set.get_document(self.api_coverage_analysis_request.covered_document_id)

    def get_cover_keywords(self) -> List[Keyword]:
        return self.cover_keywords

    def get_covered_keywords(self) -> List[Keyword]:
        return self.covered_keywords
