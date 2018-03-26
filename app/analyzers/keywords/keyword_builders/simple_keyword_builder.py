from app.analyzers.keywords.keyword_builders.keyword_builder import KeywordBuilder, WordScores, Keywords, KeywordImpl


class SimpleKeywordBuilder(KeywordBuilder):
    def build(self, word_scores_dict: WordScores, pos_tokens: []) -> Keywords:
        keywords = set()
        words = []
        score = 0.0
        for index, token in enumerate(pos_tokens):
            word_score = word_scores_dict.get(token[0], 0)
            if token[1] in ["JJ", "NN", "NNP"] and word_score > 1:
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