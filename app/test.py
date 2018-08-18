from flask import Blueprint

from app.analyzers.algorithms.word_similarity.topic_word_similarity import TopicWordSimilarity
from app.analyzers.similar_documents import text_popularity_coefficient
from app.data_import.digital_library_theiet.parser import DigitalLibraryParser
from app.data_import.topics.topic_reader import TopicReader
from app.database.neo4j_base_service import get_documents_from_database

# This file is containing test functions in order to test the analyzers
from app.model.problem import Problem

test = Blueprint("test", __name__)

digital_library_parser = DigitalLibraryParser()


# This function is used if we want to test the application without using the rest methods
def start():
    print("This function is used if we want to test the application without using the rest methods. "
          "The user must change username and password for the database in the config file")

    # This function is for importing 500 documents from Wikipedia starting from the page 'Science'
    # insert_documents(500, 'Science')

    # This function is for connecting documents with the filtered words in their content
    # connect_documents_with_words()

    # This function is for testing how similar_documents are found. Metric can be Custom or Cosine
    # result = similar_documents_to_document('Cancer', 100, 0.05, "Cosine")
    # for record in result:
    #    print(record)

    # This function returns how much a document is popular in the database
    # print(document_popularity_coefficient('Cancer', 'Cosine'))

    # This function connects the documents with their tags
    # connect_documents_with_tags()

    # This function returns tags for content of a document.
    # We can also use the other function that takes text as argument
    # extract_tags_from_text('Some Text')
    # tags = extract_tags_from_document_content('Cancer')
    # for tag in tags:
    #    print(tag)

    # This function returns coefficient for how much the word is relevant in our database
    # word_relevance =  word_relevance_coefficient('cancer')
    # print(word_relevance)

    # This function returns coefficient for how much the word is relevant in our database
    # tag_relevance = tag_relevance_coefficient('Cancer')
    # print(tag_relevance)

    # This function returns coefficient of similarity between two documents for different metrics.
    # Metrics that can be chosen are Cosine, Euclid, Jaccard or Custom
    # print(document_similarity_coefficient('Cancer', 'Genetics', metric='Cosine'))
    # print(document_similarity_coefficient('Cancer', 'Genetics', metric='Euclid'))
    # print(document_similarity_coefficient('Cancer', 'Genetics', metric="Jaccard"))
    # print(document_similarity_coefficient('Cancer', 'Genetics'))

    # maxPopularity()
    # digital_library_parser.spider("/content/subject/c6000?pageSize=100&page=1")

    # keyword_extractor = KeywordExtractor()
    # nodes = keyword_extractor.extract_keywords_for_text("Natural Language processing helps with keyword extraction")
    # for node in nodes:
    #     print(node.name, node.score)
    #
    # tokens = word_tokenize("Natural Language processing helps with keyword extraction")
    # tokens_tags = nltk.pos_tag(tokens)
    # print(tokens_tags)

    # X = lda.datasets.load_reuters()
    # vocab = lda.datasets.load_reuters_vocab()
    # titles = lda.datasets.load_reuters_titles()
    # model = lda.LDA(n_topics=20, n_iter=2500, random_state=1)
    # model.fit(X)  # model.fit_transform(X) is also available
    # topic_word = model.topic_word_  # model.components_ also works
    # n_top_words = 10
    # for i, topic_dist in enumerate(topic_word):
    #     indices = np.argsort(topic_dist)
    #     topic_words = np.array(vocab)[indices][:-n_top_words:-1]
    #     topic_dists = np.array(topic_dist)[indices][:-n_top_words:-1]
    #     ttt = []
    #     for j in range(0, len(topic_words)):
    #         t_w = topic_words[j]
    #         t_d = topic_dists[j]
    #         ttt.append("(" + str(t_w) + ", " + str(t_d) + ")")
    #
    #     print('Topic {}: {}'.format(i, ' '.join(ttt)))
    # thefile = open('C:/Users/PC/Desktop/Data/iDeal-Hub/Analyzers/GK-LDA/LR-Sets/lrsets.txt', 'w')
    #

    # lemma_names = [n for n in wordnet.all_lemma_names()]
    # sub_lemma_names = lemma_names[0: 1000]
    # set_of_lr_sets = set()
    # for lemma_name in lemma_names:
    #     synsets = wordnet.synsets(lemma_name)
    #     for synset in synsets:
    #         LRSet = set()
    #         lemmas = synset.lemmas()
    #         for lemma in lemmas:
    #             LRSet.add(lemma.name().lower())
    #             antonyms = lemma.antonyms()
    #             for antonym in antonyms:
    #                 LRSet.add(antonym.name().lower())
    #         set_of_lr_sets.add(frozenset(LRSet))
    #
    # for s in set_of_lr_sets:
    #     l = list(s)
    #     thefile.write("{")
    #     thefile.write(', '.join(l))
    #     thefile.write("}\n")
    # thefile.close()


    # word_similarity = WordSimilarity()
    # print(word_similarity.get_similarity("cannon", "fuji"))
    # print(word_similarity.get_similarity("price", "expensive"))
    # print(word_similarity.get_similarity("cool", "record"))


def maxPopularity():
    documents = get_documents_from_database()
    max_popularity = 0
    counter = 0
    for document in documents:
        text_popularity = text_popularity_coefficient(document.content)
        counter += 1
        if max_popularity < text_popularity:
            max_popularity = text_popularity
        print(str(max_popularity) + " " + str(counter))

    print(max_popularity)


start()
