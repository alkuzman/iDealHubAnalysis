from typing import List

from app.analyzers.analyzer import Analyzer
from app.model.analysis.request.analysis_request import AnalysisRequest
from app.model.analysis.response.analysis import Analysis


class AnalyzerRegistry(Analyzer):
    def __init__(self):
        self.registry = []

    def register(self, analyzer: Analyzer):
        self.registry.append(analyzer)

    def get(self, o: AnalysisRequest) -> Analyzer:
        for analyzer in self.registry:
            if analyzer.accepts(o):
                return analyzer

    def analyze(self, analysis_request: AnalysisRequest) -> List[Analysis]:
        analyzer = self.get(analysis_request)
        if analyzer is None:
            raise Exception("No analyzer found for: " + str(type(AnalysisRequest)))
        return analyzer.analyze(analysis_request)

    def accepts(self, o: AnalysisRequest) -> bool:
        return True
