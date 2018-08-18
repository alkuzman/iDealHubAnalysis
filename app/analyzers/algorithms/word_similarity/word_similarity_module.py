from dependency_injector import containers, providers

from app.analyzers.algorithms.word_similarity.word_similarity import WordSimilarity


class WordSimilarityModule(containers.DeclarativeContainer):
    word_similarity = providers.ThreadSafeSingleton(WordSimilarity)
