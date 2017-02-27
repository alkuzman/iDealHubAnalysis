from app.analyzers.keywords.keyword_extractor import KeywordExtractor
from app.model.analysis.idea_analysis import IdeaAnalysis
from app.model.analysis.problem_analysis import ProblemAnalysis
from app.model.analysis.solution_quality import SolutionQuality
from app.model.analysis.solution_quality_status import SolutionQualityStatus
from app.model.idea import Idea
from app.model.problem import Problem


class IdeaAnalyzer(object):
    def __init__(self):
        self.keyword_extractor = KeywordExtractor()

    def analyze_idea(self, idea: Idea) -> IdeaAnalysis:
        texts = [(idea.title, 3), (idea.snackPeak, 2), (idea.text, 1)]
        problem_analysis = self.analyze_problem(idea.problem)
        idea_analysis = IdeaAnalysis(self.keyword_extractor.extract_keywords_for_text(texts),
                                     problem_analysis)
        self.solution_quality(idea_analysis)
        return idea_analysis

    def analyze_problem(self, problem: Problem) -> ProblemAnalysis:
        texts = [(problem.title, 2), (problem.text, 1)]
        problem_analysis = ProblemAnalysis(self.keyword_extractor.extract_keywords_for_text(texts))
        return problem_analysis

    def solution_quality(self, idea_analysis: IdeaAnalysis):
        idea_keywords = idea_analysis.keywords
        problem_keywords = idea_analysis.problem.keywords
        number_of_common_keywords = 0
        for keyword in problem_keywords:
            for idea_keyword in idea_keywords:
                if keyword.phrase.lower() == idea_keyword.phrase.lower():
                    number_of_common_keywords += 1
                    print(idea_keyword.phrase, idea_keyword.score, keyword.score)
                    break
        length = len(problem_keywords)
        print("Length: ", length)
        print("number_of_common_keywords", number_of_common_keywords)
        ratio = 0
        if length != 0:
            ratio = number_of_common_keywords / length
        status = 2
        if ratio < 0.66:
            status = 1
        if ratio < 0.33:
            status = 0
        solution_quality = SolutionQuality(status)
        idea_analysis.solutionQuality = solution_quality
