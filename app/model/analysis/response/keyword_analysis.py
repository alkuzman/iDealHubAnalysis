import abc
from typing import List

from app.model.analysis.response.analysis import Analysis
from app.model.document.document import Document
from app.model.keyword.keyword import Keyword


class KeywordAnalysis(Analysis):
    """
    Keyword analysis for given document
    """

    @abc.abstractclassmethod
    def get_document(self) -> Document:
        """
        :return: document for which the keyword analysis is done
            """
        pass

    @abc.abstractclassmethod
    def get_keywords(self) -> List[Keyword]:
        """
            :return: list of keywords for the document of this analysis
        """
        pass

    def get_documents(self) -> List[Document]:
        result = []
        if self.get_document() is not None:
            result.append(self.get_document())
        return result
