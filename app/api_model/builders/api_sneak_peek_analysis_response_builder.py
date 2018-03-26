from app.api_model.builders.api_descriptive_analysis_score_builder import ApiDescriptiveAnalysisScoreBuilder
from app.api_model.generated.api_model_pb2 import SneakPeekAnalysisResponse as ApiSneakPeekAnalysisResponse
from app.model.analysis.response.sneak_peek_quality_analysis import SneakPeekQualityAnalysis


class ApiSneakPeekAnalysisResponseBuilder:
    def __init__(self, sneak_peek_quality_analysis: SneakPeekQualityAnalysis):
        self.sneak_peek_quality_analysis = sneak_peek_quality_analysis

    def build(self) -> ApiSneakPeekAnalysisResponse:
        api_sneak_peek_analysis_response = ApiSneakPeekAnalysisResponse()
        api_sneak_peek_analysis_response.quality = self.sneak_peek_quality_analysis.get_score()

        api_descriptive_analysis_score_builder = ApiDescriptiveAnalysisScoreBuilder(
            self.sneak_peek_quality_analysis.get_descriptive_score())
        api_sneak_peek_analysis_response.descriptive_quality = api_descriptive_analysis_score_builder.build()

        api_sneak_peek_analysis_response.sneak_peek_document_id = self.sneak_peek_quality_analysis.get_sneak_peek().get_id()
        api_sneak_peek_analysis_response.main_document_id = self.sneak_peek_quality_analysis.get_main_document().get_id()
        return api_sneak_peek_analysis_response
