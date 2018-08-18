from abc import abstractmethod, ABCMeta
from typing import List

from app.model.document.document import Document


class AnalysisRequest(metaclass=ABCMeta):
    """
    One request for analysis for given list of documents
    """

    @abstractmethod
    def get_documents(self) -> List[Document]:
        """
        List of documents for which analysis is requested.

        :return: documents for which analysis is requested
            """
        pass
