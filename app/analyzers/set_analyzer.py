from typing import List

from app.analyzers import KeywordAnalyzer
from app.analyzers.analyzer import Analyzer
from app.analyzers.coverage.coverage_analyzer import CoverageAnalyzer
from app.analyzers.sneak_peek_quality.sneak_peek_quality_analyzer import SneakPeekQualityAnalyzer
from app.model.analysis.request.analysis_request import AnalysisRequest
from app.model.analysis.request.analysis_request_set import AnalysisRequestSet
from app.model.analysis.request.impl.keyword_analysis_request_impl import KeywordAnalysisRequestImpl
from app.model.analysis.response.analysis import Analysis


class SetAnalyzer(Analyzer):
    def analyze(self, analysis_request: AnalysisRequestSet) -> List[Analysis]:
        keyword_analysis = []
        keyword_analysis_dict = {}
        keyword_analyzer = KeywordAnalyzer()
        for document in analysis_request.get_documents():
            keyword_analysis_request = KeywordAnalysisRequestImpl(document)
            a = keyword_analyzer.analyze(keyword_analysis_request)
            keyword_analysis.extend(a)
            keyword_analysis_dict[document.get_id()] = a

        analysis_request.set_keyword_analysis(keyword_analysis)

        analysis = []

        for keyword_analysis_request in analysis_request.get_keyword_analysis_requests():
            analysis.extend(keyword_analysis_dict[keyword_analysis_request.get_document().get_id()])

        coverage_analyzer = CoverageAnalyzer()
        for coverage_analysis_request in analysis_request.get_coverage_analysis_requests():
            coverage_analysis = coverage_analyzer.analyze(coverage_analysis_request)
            analysis.extend(coverage_analysis)

        sneak_peek_analyzer = SneakPeekQualityAnalyzer()
        for sneak_peek_analysis_request in analysis_request.get_sneak_peak_quality_analysis_requests():
            sneak_peak_quality_analysis = sneak_peek_analyzer.analyze(sneak_peek_analysis_request)
            analysis.extend(sneak_peak_quality_analysis)

        return analysis

    def accepts(self, o: AnalysisRequest) -> bool:
        return isinstance(o, AnalysisRequestSet)
