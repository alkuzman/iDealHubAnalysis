import os

from dependency_injector import containers, providers

from app.data_import.topics.word_similarity import WordSimilarity

TOPICS_DIRECTORY_ENV = 'TOPICS_DIRECTORY'


class TopicsModule(containers.DeclarativeContainer):
    if TOPICS_DIRECTORY_ENV not in os.environ:
        raise Exception("Expected environment variable to be present", TOPICS_DIRECTORY_ENV)
    topics_directory = providers.Object(os.environ.get(TOPICS_DIRECTORY_ENV))
    word_similarity = providers.ThreadSafeSingleton(WordSimilarity,
                                                    data_directory=topics_directory)
