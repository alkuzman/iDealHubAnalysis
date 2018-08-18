from concurrent.futures import as_completed, Executor
from typing import List, Dict

from dependency_injector.providers import Provider

from app.analyzers import KeywordAnalyzer
from app.analyzers.analyzer import Analyzer
from app.analyzers.coverage.coverage_analyzer import CoverageAnalyzer
from app.analyzers.sneak_peek_quality.sneak_peek_quality_analyzer import SneakPeekQualityAnalyzer
from app.model.analysis.request.analysis_request import AnalysisRequest
from app.model.analysis.request.analysis_request_set import AnalysisRequestSet
from app.model.analysis.request.impl.keyword_analysis_request_impl import KeywordAnalysisRequestImpl
from app.model.analysis.response.analysis import Analysis
from app.model.analysis.response.keyword_analysis import KeywordAnalysis
from app.model.document.document import Document


class SetAnalyzer(Analyzer[AnalysisRequestSet, Analysis]):
    """
    Analyzer for AnalysisRequestSet which returns List[Analysis].
    """
    def __init__(self, keyword_analyzer_provider: Provider, coverage_analyzer: CoverageAnalyzer,
                 sneak_peek_analyzer: SneakPeekQualityAnalyzer, executor: Executor):
        self.keyword_analyzer_provider = keyword_analyzer_provider
        self.coverage_analyzer = coverage_analyzer
        self.sneak_peek_analyzer = sneak_peek_analyzer
        self.executor: Executor = executor

    def analyze(self, analysis_request: AnalysisRequestSet) -> List[Analysis]:
        analysis = []

        keyword_analysis_dict = self.get_keyword_analyses(analysis_request.get_documents())
        keyword_analyses = []
        for document_id in keyword_analysis_dict:
            keyword_analyses.extend(keyword_analysis_dict[document_id])
        analysis_request.set_keyword_analysis(keyword_analyses)

        for keyword_analysis_request in analysis_request.get_keyword_analysis_requests():
            analysis.extend(keyword_analysis_dict[keyword_analysis_request.get_document().get_id()])

        for coverage_analysis_request in analysis_request.get_coverage_analysis_requests():
            coverage_analysis = self.coverage_analyzer.analyze(coverage_analysis_request)
            analysis.extend(coverage_analysis)

        for sneak_peek_analysis_request in analysis_request.get_sneak_peak_quality_analysis_requests():
            sneak_peak_quality_analysis = self.sneak_peek_analyzer.analyze(sneak_peek_analysis_request)
            analysis.extend(sneak_peak_quality_analysis)

        return analysis

    def accepts(self, o: AnalysisRequest) -> bool:
        return isinstance(o, AnalysisRequestSet)

    def get_keyword_analyses(self, documents: List[Document]) -> Dict[str, List[KeywordAnalysis]]:
        keyword_analysis_dict = {}
        future_to_keywords = {self.executor.submit(
            self.get_keyword_analysis,
            document): document.get_id()
                              for document in documents}
        for future in as_completed(future_to_keywords):
            document_id = future_to_keywords[future]
            try:
                data = future.result()
                keyword_analysis_dict[document_id] = data
            except Exception as exc:
                print('%r generated an exception: %s' % (document_id, exc))

        return keyword_analysis_dict

    def get_keyword_analysis(self, document: Document):
        keyword_analyzer: KeywordAnalyzer = self.keyword_analyzer_provider()
        return keyword_analyzer.analyze(KeywordAnalysisRequestImpl(document))
