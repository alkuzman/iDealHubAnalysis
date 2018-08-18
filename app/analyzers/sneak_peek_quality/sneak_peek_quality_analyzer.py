from typing import List

from app.analyzers.analyzer import Analyzer
from app.model.analysis.request.analysis_request import AnalysisRequest
from app.model.analysis.request.sneak_peek_quality_analysis_request import SneakPeekQualityAnalysisRequest
from app.model.analysis.response.descriptive_analysis_score import DescriptiveAnalysisScore
from app.model.analysis.response.impl.sneak_peek_quality_analysis_impl import SneakPeekQualityAnalysisImpl
from app.model.analysis.response.sneak_peek_quality_analysis import SneakPeekQualityAnalysis


class SneakPeekQualityAnalyzer(Analyzer[SneakPeekQualityAnalysisRequest, SneakPeekQualityAnalysis]):
    def analyze(self, analysis_request: SneakPeekQualityAnalysisRequest) -> List[SneakPeekQualityAnalysis]:
        text_keywords = analysis_request.get_main_document_keywords()
        snack_peak_keywords = analysis_request.get_sneak_peek_keywords()
        text_keywords_length = len(text_keywords)
        snack_peak_keywords_length = len(snack_peak_keywords)

        total_score = 0
        covered_score = 0
        for text_keyword in text_keywords:
            total_score += text_keyword.get_score()
            for snack_peak_keyword in snack_peak_keywords:
                if text_keyword.get_phrase().lower() == snack_peak_keyword.get_phrase().lower():
                    covered_score += text_keyword.get_score()

        divider = (total_score * snack_peak_keywords_length)
        quality = 0

        if divider != 0:
            quality = (covered_score * text_keywords_length) / divider
        score = DescriptiveAnalysisScore.PURE
        if quality > 0.65:
            score = DescriptiveAnalysisScore.FAIR
        elif quality > 1:
            score = DescriptiveAnalysisScore.GOOD
        elif quality > 1.2:
            score = DescriptiveAnalysisScore.EXCELLENT
        return [SneakPeekQualityAnalysisImpl(analysis_request.get_sneak_peek(), analysis_request.get_main_document(),
                                             quality, score)]

    def accepts(self, o: AnalysisRequest) -> bool:
        return isinstance(o, SneakPeekQualityAnalysisRequest)
