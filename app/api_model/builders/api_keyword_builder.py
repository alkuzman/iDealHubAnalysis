from app.api_model.generated.api_model_pb2 import Keyword as ApiKeyword
from app.model.keyword.keyword import Keyword


class ApiKeywordBuilder:
    def __init__(self, keyword: Keyword):
        self.keyword = keyword

    def build(self) -> ApiKeyword:
        api_keyword = ApiKeyword()
        api_keyword.score = self.keyword.get_score()
        api_keyword.phrase = self.keyword.get_phrase()
        return api_keyword
