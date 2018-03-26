from typing import List

from app.api_model.builders.api_coverage_analysis_response_builder import ApiCoverageAnalysisResponseBuilder
from app.api_model.builders.api_keyword_analysis_response_builder import ApiKeywordAnalysisResponseBuilder
from app.api_model.builders.api_sneak_peek_analysis_response_builder import ApiSneakPeekAnalysisResponseBuilder
from app.api_model.generated.api_model_pb2 import AnalysisRequest as ApiAnalysisRequest, \
    AnalysisResponse as ApiAnalysisResponse
from app.model.analysis.analysis import Analysis
from app.model.analysis.response.coverage_analysis import CoverageAnalysis
from app.model.analysis.response.keyword_analysis import KeywordAnalysis
from app.model.analysis.response.sneak_peek_quality_analysis import SneakPeekQualityAnalysis


class ApiAnalysisResponseBuilder:
    def __init__(self, api_analysis_request: ApiAnalysisRequest, analysis: List[Analysis]):
        self.analysis_request = api_analysis_request
        self.analysis = analysis

    def build(self) -> ApiAnalysisResponse:
        analysis_response = ApiAnalysisResponse()
        analysis_response.data.extend(self.analysis_request.data)
        analysis_response.documents.extend(self.analysis_request.documents)
        for a in self.analysis:
            if isinstance(a, KeywordAnalysis):
                keyword_analysis_builder = ApiKeywordAnalysisResponseBuilder(a)
                analysis_response.keyword_analysis_responses.extend([keyword_analysis_builder.build()])
            if isinstance(a, CoverageAnalysis):
                api_coverage_analysis_response_builder = ApiCoverageAnalysisResponseBuilder(a)
                analysis_response.coverage_analysis_responses.extend([api_coverage_analysis_response_builder.build()])
            if isinstance(a, SneakPeekQualityAnalysis):
                api_sneak_peek_analysis_response_builder = ApiSneakPeekAnalysisResponseBuilder(a)
                analysis_response.sneak_peek_analysis_responses.extend(
                    [api_sneak_peek_analysis_response_builder.build()])
        return analysis_response
