from app.api_model.generated.api_model_pb2 import KeywordAnalysisRequest as ApiKeywordAnalysisRequest
from app.model.analysis.request.keyword_analysis_request import KeywordAnalysisRequest
from app.model.document.document import Document
from app.model.document.document_set import DocumentSet


class KeywordAnalysisRequestApiAdapter(KeywordAnalysisRequest):
    def __init__(self, api_keyword_analysis_request: ApiKeywordAnalysisRequest, document_set: DocumentSet):
        self.api_keyword_analysis_request = api_keyword_analysis_request
        self.document_set = document_set

    def get_document(self) -> Document:
        return self.document_set.get_document(self.api_keyword_analysis_request.document_id)
