import os

from dependency_injector import containers, providers

from app.data_import.topics.topic_reader import TopicReader

TOPICS_DIRECTORY_ENV = 'TOPICS_DIRECTORY'


class TopicsModule(containers.DeclarativeContainer):
    if TOPICS_DIRECTORY_ENV not in os.environ:
        raise Exception("Expected environment variable to be present", TOPICS_DIRECTORY_ENV)
    topics_directory = providers.Object(os.environ.get(TOPICS_DIRECTORY_ENV))
    topic_reader = providers.ThreadSafeSingleton(TopicReader,
                                                 data_directory=topics_directory)
