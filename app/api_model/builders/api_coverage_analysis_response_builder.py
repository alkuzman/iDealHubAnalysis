from app.api_model.builders.api_descriptive_analysis_score_builder import ApiDescriptiveAnalysisScoreBuilder
from app.api_model.builders.api_keywords_builder import ApiKeywordsBuilder
from app.api_model.generated.api_model_pb2 import CoverageAnalysisResponse as ApiCoverageAnalysisResponse
from app.model.analysis.response.coverage_analysis import CoverageAnalysis


class ApiCoverageAnalysisResponseBuilder:
    def __init__(self, coverage_analysis: CoverageAnalysis):
        self.coverage_analysis = coverage_analysis

    def build(self) -> ApiCoverageAnalysisResponse:
        api_coverage_analysis_response = ApiCoverageAnalysisResponse()
        api_coverage_analysis_response.coverage = self.coverage_analysis.get_score()

        api_descriptive_analysis_score_builder = ApiDescriptiveAnalysisScoreBuilder(
            self.coverage_analysis.get_descriptive_score())
        api_coverage_analysis_response.descriptive_coverage = api_descriptive_analysis_score_builder.build()

        api_coverage_analysis_response.cover_document_id = self.coverage_analysis.get_cover().get_id()
        api_coverage_analysis_response.covered_document_id = self.coverage_analysis.get_covered().get_id()

        covered_keywords_builder = ApiKeywordsBuilder(self.coverage_analysis.get_covered_keywords())
        api_coverage_analysis_response.covered_keywords.extend(covered_keywords_builder.build())

        not_covered_keywords_builder = ApiKeywordsBuilder(self.coverage_analysis.get_not_covered_keywords())
        api_coverage_analysis_response.not_covered_keywords.extend(not_covered_keywords_builder.build())
        return api_coverage_analysis_response
