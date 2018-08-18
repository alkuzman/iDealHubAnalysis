from abc import abstractmethod

from app.data_import.topics.topic_reader import TopicReader


class WordSimilarity(object):
    @abstractmethod
    def get_similarity(self, word1: str, word2: str) -> float:
        pass
