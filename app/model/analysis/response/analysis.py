import abc
from typing import List

from app.model.document.document import Document


class Analysis(metaclass=abc.ABCMeta):
    """
    One analysis for given list of documents
    """

    @abc.abstractclassmethod
    def get_documents(self) -> List[Document]:
        """
        List of documents of the analysis.

        :return: documents of the analysis.
            """
        pass
