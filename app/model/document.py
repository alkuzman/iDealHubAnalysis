class Document(object):
    def __init__(self, title: str, text: str):
        self.title = title
        self.text = text

    def __str__(self):
        return "\"" + self.title + "\": " + self.text

    @classmethod
    def from_dict(cls, d):
        obj = cls(**d)
        return obj

    def __init(self, **kwargs):
        self.__dict__.update(kwargs)
