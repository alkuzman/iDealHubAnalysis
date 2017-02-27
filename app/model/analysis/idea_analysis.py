from app.analyzers.keywords.keyword_builders.keyword_builder import Keywords
from app.model.analysis.document_analysis import DocumentAnalysis
from app.model.analysis.problem_analysis import ProblemAnalysis


class IdeaAnalysis(DocumentAnalysis):
    def __init__(self, keywords: Keywords, problem: ProblemAnalysis):
        self.problem = problem
        self.solutionQuality = None
        DocumentAnalysis.__init__(self, keywords)

        def reprJSON(self):
            return dict(keywords=self.keywords, problem=self.problem)
