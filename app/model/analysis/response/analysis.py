from abc import abstractmethod, ABCMeta
from typing import List

from app.model.document.document import Document


class Analysis(metaclass=ABCMeta):
    """
    One analysis for given list of documents
    """

    @abstractmethod
    def get_documents(self) -> List[Document]:
        """
        List of documents of the analysis.

        :return: documents of the analysis.
            """
        pass
