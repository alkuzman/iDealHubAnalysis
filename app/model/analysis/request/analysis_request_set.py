import abc
from typing import List

from app.model.analysis.request.analysis_request import AnalysisRequest
from app.model.analysis.request.coverage_analysis_request import CoverageAnalysisRequest
from app.model.analysis.request.keyword_analysis_request import KeywordAnalysisRequest
from app.model.analysis.request.sneak_peek_quality_analysis_request import SneakPeekQualityAnalysisRequest
from app.model.analysis.response.keyword_analysis import KeywordAnalysis


class AnalysisRequestSet(AnalysisRequest):
    @abc.abstractclassmethod
    def get_keyword_analysis_requests(self) -> List[KeywordAnalysisRequest]:
        pass

    @abc.abstractclassmethod
    def get_coverage_analysis_requests(self) -> List[CoverageAnalysisRequest]:
        pass

    @abc.abstractclassmethod
    def get_sneak_peak_quality_analysis_requests(self) -> List[SneakPeekQualityAnalysisRequest]:
        pass

    @abc.abstractclassmethod
    def set_keyword_analysis(self, keyword_analysis: List[KeywordAnalysis]):
        pass

    def get_analysis_requests(self) -> List[AnalysisRequest]:
        analysis_requests = []
        analysis_requests.extend(self.get_keyword_analysis_requests())
        analysis_requests.extend(self.get_coverage_analysis_requests())
        analysis_requests.extend(self.get_sneak_peak_quality_analysis_requests())
        return analysis_requests

    def get_documents(self):
        document_ids = {}
        documents = []
        analysis_requests = self.get_analysis_requests()
        for request in analysis_requests:
            request_documents = request.get_documents()
            for request_document in request_documents:
                if request_document.get_id() in document_ids:
                    continue
                document_ids[request_document.get_id()] = True
                documents.append(request_document)
        return documents
