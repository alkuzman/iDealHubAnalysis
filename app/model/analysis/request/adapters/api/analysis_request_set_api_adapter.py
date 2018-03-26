from typing import List

from app.api_model.generated.api_model_pb2 import AnalysisRequest as ApiAnalysisRequest, CoverageAnalysisRequest
from app.model.analysis.request.adapters.api.coverage_analysis_request_api_adapter import \
    CoverageAnalysisRequestApiAdapter
from app.model.analysis.request.adapters.api.keyword_analysis_request_api_adapter import \
    KeywordAnalysisRequestApiAdapter
from app.model.analysis.request.adapters.api.sneak_peek_quality_analysis_requests_api_adapter import \
    SneakPeekQualityAnalysisRequestApiAdapter
from app.model.analysis.request.analysis_request_set import AnalysisRequestSet
from app.model.analysis.request.keyword_analysis_request import KeywordAnalysisRequest
from app.model.analysis.request.sneak_peek_quality_analysis_request import SneakPeekQualityAnalysisRequest
from app.model.analysis.response.keyword_analysis import KeywordAnalysis
from app.model.document.adapters.api.document_set_api_adapter import DocumentSetApiAdapter
from app.utils.data_converters import no_boost_data_converter


class AnalysisRequestSetApiAdapter(AnalysisRequestSet):
    def __init__(self, api_analysis_request: ApiAnalysisRequest):
        self.api_analysis_request = api_analysis_request
        self.document_set = DocumentSetApiAdapter(api_analysis_request.data, api_analysis_request.documents,
                                                  no_boost_data_converter)
        self.keyword_analysis = {}

    def set_keyword_analysis(self, keyword_analysis: List[KeywordAnalysis]):
        for keyword_analysis_unit in keyword_analysis:
            self.keyword_analysis[keyword_analysis_unit.get_document().get_id()] = keyword_analysis_unit

    def get_keyword_analysis_requests(self) -> List[KeywordAnalysisRequest]:
        keyword_analysis_requests = []
        for api_keyword_analysis_request in self.api_analysis_request.keyword_analysis_requests:
            keyword_analysis_request = KeywordAnalysisRequestApiAdapter(api_keyword_analysis_request, self.document_set)
            keyword_analysis_requests.append(keyword_analysis_request)
        return keyword_analysis_requests

    def get_coverage_analysis_requests(self) -> List[CoverageAnalysisRequest]:
        coverage_analysis_requests = []
        for api_coverage_analysis_request in self.api_analysis_request.coverage_analysis_requests:
            cover_keyword_analysis = self.keyword_analysis.get(api_coverage_analysis_request.cover_document_id)
            cover_keywords = []
            if cover_keyword_analysis is not None:
                cover_keywords.extend(cover_keyword_analysis.get_keywords())
            covered_keyword_analysis = self.keyword_analysis.get(api_coverage_analysis_request.covered_document_id)
            covered_keywords = []
            if covered_keyword_analysis is not None:
                covered_keywords.extend(covered_keyword_analysis.get_keywords())
            coverage_analysis_request = CoverageAnalysisRequestApiAdapter(api_coverage_analysis_request,
                                                                          self.document_set, cover_keywords,
                                                                          covered_keywords)
            coverage_analysis_requests.append(coverage_analysis_request)
        return coverage_analysis_requests

    def get_sneak_peak_quality_analysis_requests(self) -> List[SneakPeekQualityAnalysisRequest]:
        sneak_peak_quality_analysis_requests = []
        for api_sneak_peak_quality_analysis_request in self.api_analysis_request.sneak_peek_analysis_requests:
            sneak_peak_keywords_analysis = self.keyword_analysis.get(
                api_sneak_peak_quality_analysis_request.sneak_peek_document_id)
            sneak_peak_keywords = []
            if sneak_peak_keywords_analysis is not None:
                sneak_peak_keywords.extend(sneak_peak_keywords_analysis.get_keywords())
            main_document_keywords = []
            main_document_keywords_analysis = self.keyword_analysis.get(
                api_sneak_peak_quality_analysis_request.main_document_id)
            if main_document_keywords_analysis is not None:
                main_document_keywords.extend(main_document_keywords_analysis.get_keywords())
            sneak_peak_analysis_request = SneakPeekQualityAnalysisRequestApiAdapter(
                api_sneak_peak_quality_analysis_request,
                self.document_set, sneak_peak_keywords,
                main_document_keywords)
            sneak_peak_quality_analysis_requests.append(sneak_peak_analysis_request)
        return sneak_peak_quality_analysis_requests
