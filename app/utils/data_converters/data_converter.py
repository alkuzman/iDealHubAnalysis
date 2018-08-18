from abc import abstractmethod, ABCMeta
from typing import List

from app.model.document.data import Data


class DataConverter(metaclass=ABCMeta):
    """
    This is converter of data
    """

    @abstractmethod
    def convert(self, data: Data, from_content_type: str, to_content_type: str) -> List[Data]:
        """
        Convert of the data can result in multiple chunks of data

        :param data: Data object which should be converted
        :param from_content_type: content type of the data object
        :param to_content_type: target content type
        :return: list of data chunks with target content type
        """
        pass
