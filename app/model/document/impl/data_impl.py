from app.model.document.data import Data


class DataImpl(Data):
    def __init__(self, identifier: str, content: str, boost: float):
        self.identifier = identifier
        self.content = content
        self.boost = boost

    def get_content(self) -> str:
        return self.content

    def get_boost(self) -> float:
        return self.boost

    def get_id(self) -> str:
        return self.identifier

    def __reduce__(self):
        return self.__class__, (self.identifier, self.content, self.boost)
