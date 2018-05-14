import abc
from typing import List

from app.model.analysis.response.score_analysis import ScoreAnalysis
from app.model.document.document import Document


class SneakPeekQualityAnalysis(ScoreAnalysis):
    """
    Sneak peek quality analysis for given pair of documents
    """

    @classmethod
    def get_sneak_peek(self) -> Document:
        """

        :return: sneak peek, of the main document, of this analysis
        """
        pass

    @classmethod
    def get_main_document(self) -> Document:
        """

        :return: main or base document of this analysis
        """
        pass

    def get_documents(self) -> List[Document]:
        result = []
        if self.get_sneak_peek() is not None:
            result.append(self.get_sneak_peek())
        if self.get_main_document() is not None:
            result.append(self.get_main_document())
        return result
