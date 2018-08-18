from abc import abstractmethod
from typing import List

from app.model.analysis.request.analysis_request import AnalysisRequest
from app.model.document.document import Document
from app.model.keyword.keyword import Keyword


class CoverageAnalysisRequest(AnalysisRequest):
    """
    Analysis request for coverage factor for one document over the other.
    """

    @abstractmethod
    def get_cover(self) -> Document:
        """
        :return: document which should be anticipated as cover for requested analysis.
            """
        pass

    @abstractmethod
    def get_covered(self) -> Document:
        """
        :return: document which should be anticipated as covered document for requested analysis.
            """
        pass

    @abstractmethod
    def get_cover_keywords(self) -> List[Keyword]:
        """
        :return: list of keywords for the cover document.
            """
        pass

    @abstractmethod
    def get_covered_keywords(self) -> List[Keyword]:
        """
        :return: list of keywords for covered document.
            """
        pass

    def get_documents(self) -> List[Document]:
        result = []
        if self.get_cover() is not None:
            result.append(self.get_cover())
        if self.get_covered() is not None:
            result.append(self.get_covered())
        return result
