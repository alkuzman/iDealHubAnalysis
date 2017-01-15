from flask import Blueprint

from app.analyzers.similar_documents import similar_documents_to_document, document_popularity_coefficient

# This file is containing test functions in order to test the analyzers

test = Blueprint("test", __name__)


# This function is used if we want to test the application without using the rest methods
def start():
    print("This function is used if we want to test the application without using the rest methods. "
          "The user must change username and password for the database in the config file")

    # This function is for importing 500 documents from Wikipedia starting from the page 'Science'
    # insert_documents(500, 'Science')

    # This function is for connecting documents with the filtered words in their content
    # connect_documents_with_words()

    # This function is for testing how similar_documents are found. Metric can be Custom or Cosine
    #result = similar_documents_to_document('Cancer', 10, 0, "Cosine")
    #for record in result:
    #    print(record)

    # This function returns how much a document is popular in the database
    #print(document_popularity_coefficient('Cancer', 'Custom'))

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
    # print(document_similarity_coefficient('Cancer', 'Genetics'))


start()
