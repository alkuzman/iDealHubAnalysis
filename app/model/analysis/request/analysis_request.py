import abc
from typing import List

from app.model.document.document import Document


class AnalysisRequest(metaclass=abc.ABCMeta):
    """
    One request for analysis for given list of documents
    """

    @abc.abstractclassmethod
    def get_documents(self) -> List[Document]:
        """
        List of documents for which analysis is requested.

        :return: documents for which analysis is requested
            """
        pass
