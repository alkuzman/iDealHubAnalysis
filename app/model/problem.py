from app.model.document import Document


class Problem(Document):
    def __init__(self, title: str, text: str):
        Document.__init__(self, title, text)


    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def __init(self, **kwargs):
        self.__dict__.update(kwargs)
