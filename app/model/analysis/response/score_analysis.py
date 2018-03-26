import abc

from app.model.analysis.response.analysis import Analysis
from app.model.analysis.response.descriptive_analysis_score import DescriptiveAnalysisScore


class ScoreAnalysis(Analysis):
    """
    One analysis for given list of documents which is described with score
    """

    @abc.abstractclassmethod
    def get_score(self) -> float:
        """
        :return: score of the done analysis.
            """
        pass

    @abc.abstractclassmethod
    def get_descriptive_score(self) -> DescriptiveAnalysisScore:
        """
        :return: descriptive (human/machine readable) score of the done analysis.
            """
        pass
