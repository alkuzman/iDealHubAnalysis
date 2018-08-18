from app.analyzers.algorithms.word_similarity.word_similarity import WordSimilarity
from app.data_import.topics.topic_reader import TopicReader


class TopicWordSimilarity(WordSimilarity):
    def __init__(self, topic_reader: TopicReader):
        word_topic_distribution = topic_reader.read_word_topic_distribution()
        self.vocab_dict = topic_reader.read_vocab_dict()
        self.word_similarity_dict = topic_reader.calculate_similarity(word_topic_distribution)

    def get_similarity(self, word1: str, word2: str) -> float:
        word1_id = self.vocab_dict.get(word1)
        word2_id = self.vocab_dict.get(word2)
        if word1_id is None or word2_id is None or word1_id == word2_id:
            return 0.0
        return self.word_similarity_dict[frozenset([word1_id, word2_id])]
