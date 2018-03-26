from app.model.document_file import Document


class Problem(Document):
    def __init__(self, title: str, text: str):
        Document.__init__(self, title, text)

    @classmethod
    def from_dict(cls, **d):
        obj = cls(**d)
        return obj

    def __init(self, **kwargs):
        self.__dict__.update(kwargs)
