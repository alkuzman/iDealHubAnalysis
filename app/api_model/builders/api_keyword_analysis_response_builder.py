from app.api_model.builders.api_keywords_builder import ApiKeywordsBuilder
from app.api_model.generated.api_model_pb2 import KeywordAnalysisResponse as ApiKeywordAnalysisResponse
from app.model.analysis.response.keyword_analysis import KeywordAnalysis


class ApiKeywordAnalysisResponseBuilder:
    def __init__(self, keyword_analysis: KeywordAnalysis):
        self.keyword_analysis = keyword_analysis

    def build(self) -> ApiKeywordAnalysisResponse:
        api_keyword_analysis_response = ApiKeywordAnalysisResponse()
        api_keyword_analysis_response.document_id = self.keyword_analysis.get_document().get_id()

        keywords_builder = ApiKeywordsBuilder(self.keyword_analysis.get_keywords())

        api_keyword_analysis_response.keywords.extend(keywords_builder.build())
        return api_keyword_analysis_response
