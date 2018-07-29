from app.analyzers.keywords.keyword_builders.keyword_builder import WordScores, Keywords, KeywordImpl
from app.analyzers.keywords.keyword_builders.simple_keyword_builder import SimpleKeywordBuilder


class PosKeywordBuilder(SimpleKeywordBuilder):
    def __init__(self, pos_tags: [], min_word_score: float):
        self.pos_tags = pos_tags
        self.min_word_score = min_word_score

    def build(self, word_scores_dict: WordScores, pos_tokens: []) -> Keywords:
        keywords = set()
        words = []
        score = 0.0
        for index, token in enumerate(pos_tokens):
            word_score = word_scores_dict.get(token[0], 0)
            if token[1] in self.pos_tags and word_score > self.min_word_score:
                words.append(token[0])
                score += word_score
            else:
                if len(words) > 0:
                    keywords.add(KeywordImpl(" ".join(words), score))
                words = []
                score = 0
        keywords_list = list(keywords)
        keywords_list.sort(key=lambda keyword: keyword.score, reverse=True)
        return keywords_list
