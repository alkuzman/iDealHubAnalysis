import abc
from typing import List

from app.model.analysis.request.analysis_request import AnalysisRequest
from app.model.document.document import Document


class KeywordAnalysisRequest(AnalysisRequest):
    """
    Analysis request for keywords for one document
    """

    @abc.abstractclassmethod
    def get_document(self) -> Document:
        """
        :return: document for which keyword analysis are requested.
            """
        pass

    def get_documents(self) -> List[Document]:
        result = []
        if self.get_document() is not None:
            result.append(self.get_document())
        return result
