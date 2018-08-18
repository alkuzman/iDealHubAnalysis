from abc import abstractmethod
from typing import List

from app.model.analysis.response.score_analysis import ScoreAnalysis
from app.model.document.document import Document
from app.model.keyword.keyword import Keyword


class CoverageAnalysis(ScoreAnalysis):
    """
    Coverage analysis for given pair of documents
    """

    @abstractmethod
    def get_cover(self) -> Document:
        """

        :return: cover document, of the covered document
        """
        pass

    @abstractmethod
    def get_covered(self) -> Document:
        """

        :return: covered or base document
        """
        pass

    @abstractmethod
    def get_covered_keywords(self) -> List[Keyword]:
        """
        :return: list of keywords in the covered documents which are also in the cover document.
            """
        pass

    @abstractmethod
    def get_not_covered_keywords(self) -> List[Keyword]:
        """
        :return: list of keywords in the covered document which are not in cover document.
            """
        pass

    def get_documents(self) -> List[Document]:
        result = []
        if self.get_cover() is not None:
            result.append(self.get_cover())
        if self.get_covered() is not None:
            result.append(self.get_covered())
        return result
