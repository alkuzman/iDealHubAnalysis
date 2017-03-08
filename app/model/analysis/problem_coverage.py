import json

from app.model.complex_encoder import ComplexEncoder


class ProblemCoverage(object):
    def __init__(self, status: int, coverage: float, covered_keywords: [], not_covered_keywords: []):
        self.status = status
        self.coverage = coverage
        self.coveredKeywords = covered_keywords
        self.notCoveredKeywords = not_covered_keywords
        self.type = "ProblemCoverage"

    def __repr__(self):
        return json.dumps(self.__dict__, default=ComplexEncoder)
