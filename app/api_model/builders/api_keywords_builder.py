from typing import List

from app.api_model.builders.api_keyword_builder import ApiKeywordBuilder
from app.api_model.generated.api_model_pb2 import Keyword as ApiKeyword
from app.model.keyword.keyword import Keyword


class ApiKeywordsBuilder:
    def __init__(self, keywords: List[Keyword]):
        self.keywords = keywords

    def build(self) -> List[ApiKeyword]:
        api_keywords = []
        for keyword in self.keywords:
            keyword_builder = ApiKeywordBuilder(keyword)
            api_keyword = keyword_builder.build()
            api_keywords.append(api_keyword)
        return api_keywords
