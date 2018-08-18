from app.analyzers.keywords.keyword_builders.keyword_builder import KeywordBuilder, WordScores, Keywords


class DynamicKeywordBuilder(KeywordBuilder):
    def build(self, word_scores_dict: WordScores, pos_tokens: []) -> Keywords:
        return super().build(word_scores_dict, pos_tokens)
