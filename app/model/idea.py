from app.model.document import Document
from app.model.problem import Problem


class Idea(Document):

    def __init__(self, title: str, text: str, snackPeak: str, problem: Problem,):
        self.snackPeak = snackPeak
        self.problem = problem
        Document.__init__(self, title=title, text=text)

    @classmethod
    def from_dict(cls, **d):
        obj = cls(**d)
        obj.problem = Problem.from_dict(**obj.problem)
        return obj

    def __str__(self):
        return Document.__str__(self) + " SnackPeak: " + self.snackPeak + " problem: " + self.problem.__str__()
