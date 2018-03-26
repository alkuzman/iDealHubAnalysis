from typing import List

from app.model.analysis.request.coverage_analysis_request import CoverageAnalysisRequest
from app.model.document.document import Document
from app.model.keyword.keyword import Keyword


class CoverageAnalysisRequestImpl(CoverageAnalysisRequest):
    def __init__(self, cover: Document, covered: Document, cover_keywords: List[Keyword],
                 covered_keywords: List[Keyword]):
        self.cover = cover
        self.covered = covered
        self.cover_keywords = cover_keywords
        self.covered_keywords = covered_keywords

    def get_cover(self) -> Document:
        return self.cover

    def get_covered(self) -> Document:
        return self.covered

    def get_cover_keywords(self) -> List[Keyword]:
        return self.cover_keywords

    def get_covered_keywords(self) -> List[Keyword]:
        return self.covered_keywords
