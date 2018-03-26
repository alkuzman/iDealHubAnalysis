from typing import List

from app.model.analysis.response.coverage_analysis import CoverageAnalysis
from app.model.analysis.response.descriptive_analysis_score import DescriptiveAnalysisScore
from app.model.document.document import Document
from app.model.keyword.keyword import Keyword


class CoverageAnalysisImpl(CoverageAnalysis):
    def __init__(self, cover: Document, covered: Document, covered_keywords: List[Keyword],
                 not_covered_keywords: List[Keyword], score: float, descriptive_score: DescriptiveAnalysisScore):
        self.cover = cover
        self.covered = covered
        self.covered_keywords = covered_keywords
        self.not_covered_keywords = not_covered_keywords
        self.score = score
        self.descriptive_score = descriptive_score

    def get_cover(self) -> Document:
        return self.cover

    def get_covered(self) -> Document:
        return self.covered

    def get_covered_keywords(self) -> List[Keyword]:
        return self.covered_keywords

    def get_not_covered_keywords(self) -> List[Keyword]:
        return self.not_covered_keywords

    def get_score(self) -> float:
        return self.score

    def get_descriptive_score(self) -> DescriptiveAnalysisScore:
        return self.descriptive_score
