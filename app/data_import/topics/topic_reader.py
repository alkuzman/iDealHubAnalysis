from typing import List, Dict, Tuple

Vocab = List[str]
VocabDict = Dict[str, int]
TopicWordDistribution = List[List[float]]
WordTopicDistribution = List[List[float]]
TopicProbability = Tuple[int, float]
MostProbableTopicByWords = Dict[int, TopicProbability]
WordSimilarityDictionary = Dict[int, Dict[int, float]]


class TopicReader(object):
    def __init__(self, data_directory: str):
        self.data_directory = data_directory

    def read_vocab(self) -> Vocab:
        vocab = []
        with open(self.data_directory + "Dataset.vocab") as vocab_file:
            for line in vocab_file:
                word = line[line.find(':') + 1: -1]
                vocab.append(word)
        return vocab

    def read_vocab_dict(self) -> VocabDict:
        vocab_dict = dict()
        i = 0
        with open(self.data_directory + "Dataset.vocab") as vocab_file:
            for line in vocab_file:
                word = line[line.find(':') + 1: -1]
                vocab_dict[word] = i
                i += 1
        return vocab_dict

    def read_topic_word_distribution(self) -> TopicWordDistribution:
        topic_word_distribution = []
        with open(self.data_directory + "Dataset.twdist") as topic_word_distribution_file:
            for line in topic_word_distribution_file:
                probabilities = line.split(" ")
                topic = []
                for probability in probabilities:
                    topic.append(float(probability))
                topic_word_distribution.append(topic)
        return topic_word_distribution

    def read_word_topic_distribution(self) -> WordTopicDistribution:
        first_run = True
        word_topic_distribution = []
        with open(self.data_directory + "Dataset.twdist") as word_topic_distribution_file:
            for line in word_topic_distribution_file:
                probabilities = line.split(" ")
                for index in range(0, len(probabilities)):
                    probability = probabilities[index]
                    if first_run:
                        word = [float(probability)]
                        word_topic_distribution.append(word)
                    else:
                        word = word_topic_distribution[index]
                        word.append(float(probability))
                first_run = False
        return word_topic_distribution

    def calculate_similarity(self, word_topic_distribution: WordTopicDistribution) -> WordSimilarityDictionary:
        most_probable_topic_by_words = self.most_probable_topic_by_words(word_topic_distribution)
        word_similarity = dict()
        number_of_words = len(word_topic_distribution)
        for i in range(0, number_of_words - 1):
            for j in range(i + 1, number_of_words):
                similarity = self.get_similarity(word_topic_distribution, most_probable_topic_by_words, i, j)
                sim = word_similarity.get(i, None)
                if sim is None:
                    sim = dict()
                    word_similarity[i] = sim
                sim[j] = similarity
                sim = word_similarity.get(j, None)
                if sim is None:
                    sim = dict()
                    word_similarity[j] = sim
                sim[i] = similarity
        return word_similarity

    def get_similarity(self, word_topic_distribution: WordTopicDistribution,
                       most_probable_topic_by_words: MostProbableTopicByWords,
                       word_1: int,
                       word_2: int) -> float:
        similarity = -1
        # for i in range(0, 15):
        #     new_similarity = self.get_similarity_in_topic(word_topic_distribution, word_1, word_2, i)
        #     if new_similarity > similarity:
        #         similarity = new_similarity
        topic_1 = most_probable_topic_by_words[word_1]
        topic_2 = most_probable_topic_by_words[word_2]
        topic_1_similarity = self.get_similarity_in_topic(word_topic_distribution, word_1, word_2, topic_1[0])
        topic_2_similarity = self.get_similarity_in_topic(word_topic_distribution, word_1, word_2, topic_2[0])
        return max(topic_1_similarity, topic_2_similarity)
        # return similarity

    def get_similarity_in_topic(self, word_topic_distribution: WordTopicDistribution,
                                word_1: int,
                                word_2: int,
                                topic: int) -> float:
        probability_1 = word_topic_distribution[word_1][topic]
        probability_2 = word_topic_distribution[word_2][topic]
        if probability_1 > probability_2:
            pom = probability_1
            probability_1 = probability_2
            probability_2 = pom
        return probability_1 / probability_2

    def most_probable_topic_by_words(self, word_topic_distribution: WordTopicDistribution) -> MostProbableTopicByWords:
        max_word_probability = {}
        word_count = len(word_topic_distribution)
        topic_count = len(word_topic_distribution[0])
        topic_range = range(0, topic_count)
        for word_index in range(0, word_count):
            word = word_topic_distribution[word_index]
            max_probability = 0.0
            max_topic_index = 0
            for topic_index in topic_range:
                topic = word[topic_index]
                if topic > max_probability:
                    max_probability = topic
                    max_topic_index = topic_index
            max_word_probability[word_index] = (max_topic_index, max_probability)
        return max_word_probability
