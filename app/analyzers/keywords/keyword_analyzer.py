from typing import List

from app.analyzers.analyzer import Analyzer
from app.analyzers.keywords.keyword_extractor import KeywordExtractor
from app.model.analysis.request.analysis_request import AnalysisRequest
from app.model.analysis.request.keyword_analysis_request import KeywordAnalysisRequest
from app.model.analysis.response.analysis import Analysis
from app.model.analysis.response.impl.keyword_analysis_impl import KeywordAnalysisImpl


class KeywordAnalyzer(Analyzer):
    def __init__(self):
        self.keyword_extractor = self.keyword_extractor = KeywordExtractor()

    def analyze(self, analysis_request: KeywordAnalysisRequest) -> List[Analysis]:
        texts = []
        for data in analysis_request.get_document().get_data():
            texts.append((data.get_content(), data.get_boost()))
        keywords = self.keyword_extractor.extract_keywords_for_text(texts)
        keyword_analysis = KeywordAnalysisImpl(analysis_request.get_document(), keywords)
        return [keyword_analysis]

    def accepts(self, o: AnalysisRequest) -> bool:
        return isinstance(o, KeywordAnalysisRequest)
