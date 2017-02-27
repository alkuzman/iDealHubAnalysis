from app.analyzers.keywords.keyword_builders.keyword_builder import Keywords
from app.model.analysis.analysis import Analysis
from app.model.analysis.document_analysis import DocumentAnalysis


class ProblemAnalysis(DocumentAnalysis):
    def __init__(self, keywords: Keywords):
        DocumentAnalysis.__init__(self, keywords)

    def reprJSON(self):
        return dict(self.keywords)
