from app.model.analysis.request.keyword_analysis_request import KeywordAnalysisRequest
from app.model.document.document import Document


class KeywordAnalysisRequestImpl(KeywordAnalysisRequest):
    def __init__(self, document: Document):
        self.document = document

    def get_document(self) -> Document:
        return self.document
