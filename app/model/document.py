class Document(object):
    def __init__(self, title: str, text: str):
        self.title = title
        self.text = text

    def __str__(self):
        return "\"" + self.title + "\": " + self.text