from app.model.analysis.response.descriptive_analysis_score import DescriptiveAnalysisScore
from app.model.analysis.response.sneak_peek_quality_analysis import SneakPeekQualityAnalysis
from app.model.document.document import Document


class SneakPeekQualityAnalysisImpl(SneakPeekQualityAnalysis):
    def __init__(self, sneak_peek: Document, main_document: Document, score: float,
                 descriptive_score: DescriptiveAnalysisScore):
        self.sneak_peek = sneak_peek
        self.main_document = main_document
        self.score = score
        self.descriptive_score = descriptive_score

    def get_sneak_peek(self) -> Document:
        return self.sneak_peek

    def get_main_document(self) -> Document:
        return self.main_document

    def get_score(self) -> float:
        return self.score

    def get_descriptive_score(self) -> DescriptiveAnalysisScore:
        return self.descriptive_score
