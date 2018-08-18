from abc import abstractmethod
from typing import List, TypeVar, Generic

from app.model.analysis.request.analysis_request import AnalysisRequest
from app.model.analysis.response.analysis import Analysis

INPUT = TypeVar('INPUT', bound=AnalysisRequest)
OUTPUT = TypeVar('OUTPUT', bound=Analysis)


class Analyzer(Generic[INPUT, OUTPUT]):
    @abstractmethod
    def analyze(self, analysis_request: INPUT) -> List[OUTPUT]:
        pass

    @abstractmethod
    def accepts(self, o: AnalysisRequest) -> bool:
        pass
