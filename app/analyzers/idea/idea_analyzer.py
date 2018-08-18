import copy

from app.analyzers.keywords.keyword_builders.keyword_builder import Keywords
from app.analyzers.keywords.keyword_extractor import KeywordExtractor
from app.model.analysis.idea_analysis import IdeaAnalysis
from app.model.analysis.problem_analysis import ProblemAnalysis
from app.model.analysis.problem_coverage import ProblemCoverage
from app.model.analysis.snack_peak_quality import SnackPeakQuality
from app.model.analysis.solution_quality import SolutionQuality
from app.model.idea import Idea
from app.model.problem import Problem


class IdeaAnalyzer(object):
    def __init__(self):
        self.keyword_extractor = KeywordExtractor()

    def analyze_idea(self, idea: Idea) -> IdeaAnalysis:
        problem_analysis = self.analyze_problem(idea.problem)
        idea_analysis = IdeaAnalysis(self.get_idea_keywords(idea),
                                     problem_analysis)
        solution_quality = SolutionQuality()
        solution_quality.problemCoverage = IdeaAnalyzer.problem_coverage(idea_analysis)
        solution_quality.snackPeakQuality = self.snack_peak_quality(idea)
        idea_analysis.solutionQuality = solution_quality
        return idea_analysis

    def analyze_problem(self, problem: Problem) -> ProblemAnalysis:
        problem_analysis = ProblemAnalysis(self.get_problem_keywords(problem))
        return problem_analysis

    @staticmethod
    def problem_coverage(idea_analysis: IdeaAnalysis) -> ProblemCoverage:
        idea_keywords = idea_analysis.keywords
        problem_keywords = idea_analysis.problem.keywords
        number_of_common_keywords = 0
        covered_keywords = []
        not_covered_keywords = []
        for keyword in problem_keywords:
            not_covered = True
            for idea_keyword in idea_keywords:
                if keyword.phrase.lower() == idea_keyword.phrase.lower():
                    number_of_common_keywords += 1
                    covered_keywords.append(copy.copy(keyword))
                    not_covered = False
                    break
            if not_covered:
                not_covered_keywords.append(copy.copy(keyword))
        length = len(problem_keywords)
        coverage = 0
        if length != 0:
            coverage = number_of_common_keywords / length
        status = 2
        if coverage < 0.66:
            status = 1
        if coverage < 0.33:
            status = 0
        problem_coverage = ProblemCoverage(status, coverage, covered_keywords, not_covered_keywords)
        return problem_coverage

    def snack_peak_quality(self, idea: Idea) -> SnackPeakQuality:
        text = [(idea.text, 1)]
        snack_peak = [(idea.snackPeak, 1)]
        text_keywords = self.keyword_extractor.extract_keywords_for_text(text)
        snack_peak_keywords = self.keyword_extractor.extract_keywords_for_text(snack_peak)
        text_keywords_length = len(text_keywords)
        snack_peak_keywords_length = len(snack_peak_keywords)

        total_score = 0
        covered_score = 0
        for text_keyword in text_keywords:
            total_score += text_keyword.score
            for snack_peak_keyword in snack_peak_keywords:
                if text_keyword.phrase.lower() == snack_peak_keyword.phrase.lower():
                    covered_score += text_keyword.score

        divider = (total_score * snack_peak_keywords_length)
        quality = 0

        if divider != 0:
            quality = (covered_score * text_keywords_length) / divider
        print(quality)
        status = False
        if quality > 1:
            status = True
        return SnackPeakQuality(status, quality)

    def get_idea_keywords(self, idea: Idea) -> Keywords:
        texts = [(idea.title, 3), (idea.snackPeak, 2), (idea.text, 1)]
        return self.keyword_extractor.extract_keywords_for_text(texts)

    def get_problem_keywords(self, problem: Problem) -> Keywords:
        texts = texts = [(problem.title, 2), (problem.text, 1)]
        return self.keyword_extractor.extract_keywords_for_text(texts)

    def get_solution_quality(self, idea: Idea) -> SolutionQuality:
        idea_analysis = self.analyze_idea(idea)
        return idea_analysis.solutionQuality
