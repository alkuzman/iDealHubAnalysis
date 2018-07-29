from dependency_injector import containers, providers

from app.analyzers.keywords.relation_weight_calculator.combined_weight_calculator import CombinedWeightCalculator
from app.analyzers.keywords.relation_weight_calculator.cooccurrence_weight_calculator import \
    CooccurrenceWeightCalculator
from app.analyzers.keywords.relation_weight_calculator.topic_similarity_weight_calculator import \
    TopicSimilarityWeightCalculator
from app.data_import.topics.topics_module import TopicsModule


class RelationWeightCalculatorModule(containers.DeclarativeContainer):
    # Topic similarity weight calculator
    topic_min_similarity = providers.Object(0.5)
    topic_similarity_weight_calculator = providers.Singleton(TopicSimilarityWeightCalculator,
                                                             min_similarity=topic_min_similarity,
                                                             word_similarity=TopicsModule.word_similarity)
    # Coocurence weight calculator
    coocurence_window_size = providers.Object(2)
    coocurence_weight_calculator = providers.Singleton(CooccurrenceWeightCalculator,
                                                       window_size=coocurence_window_size)
    # Define the default weight calculator
    relation_weight_calculator = providers.Singleton(CombinedWeightCalculator,
                                                     topic_calculator=topic_similarity_weight_calculator,
                                                     coocurence_calculator=coocurence_weight_calculator)
