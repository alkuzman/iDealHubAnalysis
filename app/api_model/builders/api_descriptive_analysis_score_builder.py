from app.api_model.generated.api_model_pb2 import DescriptiveAnalysisScore as ApiDescriptiveAnalysisScore
from app.model.analysis.response.descriptive_analysis_score import DescriptiveAnalysisScore


class ApiDescriptiveAnalysisScoreBuilder:
    def __init__(self, score: DescriptiveAnalysisScore):
        self.score = score

    def build(self) -> ApiDescriptiveAnalysisScore:
        if self.score == DescriptiveAnalysisScore.PURE:
            return ApiDescriptiveAnalysisScore.Value("PURE")
        elif self.score == DescriptiveAnalysisScore.FAIR:
            return ApiDescriptiveAnalysisScore.Value("FAIR")
        elif self.score == DescriptiveAnalysisScore.GOOD:
            return ApiDescriptiveAnalysisScore.Value("GOOD")
        elif self.score == DescriptiveAnalysisScore.EXCELLENT:
            return ApiDescriptiveAnalysisScore.Value("EXCELLENT")
        raise Exception("Not mapped DescriptiveAnalysisScore found.")
