import copy
from typing import List

from app.analyzers.analyzer import Analyzer
from app.model.analysis.request.analysis_request import AnalysisRequest
from app.model.analysis.request.coverage_analysis_request import CoverageAnalysisRequest
from app.model.analysis.response.coverage_analysis import CoverageAnalysis
from app.model.analysis.response.descriptive_analysis_score import DescriptiveAnalysisScore
from app.model.analysis.response.impl.coverage_analysis_impl import CoverageAnalysisImpl


class CoverageAnalyzer(Analyzer[CoverageAnalysisRequest, CoverageAnalysis]):
    def analyze(self, analysis_request: CoverageAnalysisRequest) -> List[CoverageAnalysis]:
        base_keywords = analysis_request.get_covered_keywords()
        cover_keywords = analysis_request.get_cover_keywords()
        number_of_common_keywords = 0
        covered_keywords = []
        not_covered_keywords = []
        for keyword in cover_keywords:
            not_covered = True
            for base_keyword in base_keywords:
                if keyword.get_phrase().lower() == base_keyword.get_phrase().lower():
                    number_of_common_keywords += 1
                    covered_keywords.append(copy.copy(keyword))
                    not_covered = False
                    break
            if not_covered:
                not_covered_keywords.append(copy.copy(keyword))
        length = len(cover_keywords)
        coverage = 0
        if length != 0:
            coverage = number_of_common_keywords / length
        score = DescriptiveAnalysisScore.EXCELLENT
        if coverage < 0.80:
            score = DescriptiveAnalysisScore.GOOD
        elif coverage < 0.66:
            score = DescriptiveAnalysisScore.FAIR
        elif coverage < 0.33:
            score = DescriptiveAnalysisScore.PURE
        problem_coverage = CoverageAnalysisImpl(analysis_request.get_cover(), analysis_request.get_covered(),
                                                covered_keywords, not_covered_keywords, coverage, score)
        return [problem_coverage]

    def accepts(self, o: AnalysisRequest) -> bool:
        return isinstance(o, CoverageAnalysisRequest)
