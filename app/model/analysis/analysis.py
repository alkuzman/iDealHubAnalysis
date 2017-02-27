from app.analyzers.keywords.keyword_builders.keyword_builder import Keywords
import json


class Analysis(object):
    def __init__(self, keywords: Keywords):
        self.keywords = keywords

    def __repr__(self):
        return json.dumps(self.__dict__)

    def reprJSON(self):
        return dict(keywords=self.keywords)