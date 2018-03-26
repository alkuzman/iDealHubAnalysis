import abc
from typing import List

from app.model.analysis.request.analysis_request import AnalysisRequest
from app.model.analysis.response.analysis import Analysis


class Analyzer:
    @abc.abstractclassmethod
    def analyze(self, analysis_request: AnalysisRequest) -> List[Analysis]:
        pass

    @abc.abstractclassmethod
    def accepts(self, o: AnalysisRequest) -> bool:
        pass
