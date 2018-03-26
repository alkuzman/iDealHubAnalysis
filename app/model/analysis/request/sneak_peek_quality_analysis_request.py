import abc
from typing import List

from app.model.analysis.request.analysis_request import AnalysisRequest
from app.model.document.document import Document
from app.model.keyword.keyword import Keyword


class SneakPeekQualityAnalysisRequest(AnalysisRequest):
    """
    Analysis request for quality of the sneak peek over the main document.
    """

    @abc.abstractclassmethod
    def get_sneak_peek(self) -> Document:
        """
        :return: document which is sneak peek in the requested analysis.
            """
        pass

    @abc.abstractclassmethod
    def get_main_document(self) -> Document:
        """
        :return: document which is main document in the requested analysis.
            """
        pass

    @abc.abstractclassmethod
    def get_sneak_peek_keywords(self) -> List[Keyword]:
        """
        :return: list of keywords for the sneak peek.
            """
        pass

    @abc.abstractclassmethod
    def get_main_document_keywords(self) -> List[Keyword]:
        """
        :return: list of keywords for the main document.
            """
        pass

    def get_documents(self) -> List[Document]:
        result = []
        if self.get_sneak_peek() is not None:
            result.append(self.get_sneak_peek())
        if self.get_main_document() is not None:
            result.append(self.get_main_document())
        return result
