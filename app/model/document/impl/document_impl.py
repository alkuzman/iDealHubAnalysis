from typing import List

from app.model.document.data import Data
from app.model.document.document import Document


class DocumentImpl(Document):
    def __init__(self, identifier: str, data: List[Data]):
        self.identifier = identifier
        self.data = data

    def get_data(self) -> List[Data]:
        return self.data

    def get_id(self) -> str:
        return self.identifier

    def __reduce__(self):
        return (self.__class__, (self.identifier, self.data))
