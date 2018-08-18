from dependency_injector import containers, providers

from app.analyzers.algorithms.word_similarity.topic_word_similarity import TopicWordSimilarity
from app.analyzers.algorithms.word_similarity.word_similarity import WordSimilarity
from app.analyzers.algorithms.word_similarity.word_similarity_module import WordSimilarityModule
from app.data_import.topics.topics_module import TopicsModule


@containers.override(WordSimilarityModule)
class TopicWordSimilarityModule(containers.DeclarativeContainer):
    word_similarity = providers.ThreadSafeSingleton(TopicWordSimilarity,
                                                    topic_reader=TopicsModule.topic_reader)