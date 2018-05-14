import abc
from typing import List

from app.model.document.data import Data


class Document(metaclass=abc.ABCMeta):
    """
    This object represents textual document which is composition of multiple data parts which are plain
    texts with boost factor.
    """
    @classmethod
    def get_data(self) -> List[Data]:
        """
        Get data objects which are part of the document composition.
        :return: list of data objects, which are plain texts with boost factor.
        """
        pass

    @classmethod
    def get_id(self) -> str:
        """
               Get the unique identifier of this object. Any object which is instance of Document and which has
               the exactly same id as this object, it represents the same object

               :return: id of this object
               """
        pass

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Document):
            return False
        if self.get_id() is None:
            return False
        return self.get_id().__eq__(other.get_id())

    def __hash__(self):
        self.get_id().__hash__()

    def __str__(self):
        result = (self.get_id(), self.get_data())
        return str(result)
