from stop_words import get_stop_words
from app.database.neo4j_base_service import get_documents_from_database
import re
from app.database.database import database
from stemming.porter2 import stem


def connect_documents_with_words():
    documents = get_documents_from_database()  # Get all documents from database

    stop_words = get_stop_words("en")  # Python library that we use to exclude conjunction words and other stop words

    # This map we use to map every word in list of pairs: document id and position of the word in the document
    map_of_words_to_lists_with_document_position_tuples = {}
    # This map has pairs of words and the number of documents in which the word occurs
    map_of_words_to_number_of_documents_it_occurs = {}
    # This map is mapping every word in another map
    # which contains document and number of occurrences of the word in that document
    map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word = {}

    titles = []  # List of the titles of the documents

    total_documents = len(documents)

    for document in documents:  # For every document in the list of documents
        document_id = document.id
        title = document.title
        content = document.content
        content_words = get_words_from_text(content)  # We put all the words from the content in a list
        titles.append(title)  # Add the title in the list of titles
        word_list = [] # Filtered list of words in the document

        set_of_words_in_document = set()  # Set of all the words in the document content
        word_position_in_document = 0  # Counter for the position of the words in the document
        for word in content_words:  # For all words in the document content
            word = word.lower()  # We convert the letters of the word to lowercase
            word_position_in_document += 1  # Increase the position counter

            # If the word is in the list of stop words or has less than three letters we exclude it as irrelevant
            # We do not process it
            if word in stop_words or len(word) < 3:
                continue

            word_list.append(word)

            # If this is the first time the word is found in a document
            # create new empty list for the document position pairs
            if word not in map_of_words_to_lists_with_document_position_tuples:
                map_of_words_to_lists_with_document_position_tuples[word] = []
            # Temporary list for the document position pairs of the word
            document_position_tuple_list = map_of_words_to_lists_with_document_position_tuples[word]

            if word not in set_of_words_in_document:
                set_of_words_in_document.add(word)

            number_of_occurrences_of_word_in_document = 0
            if word not in map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word:
                map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word[word] = {}
            elif title in map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word[word]:
                number_of_occurrences_of_word_in_document = \
                    map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word[word][title]
            number_of_occurrences_of_word_in_document += 1
            map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word[word][title] = \
                number_of_occurrences_of_word_in_document
            document_position_tuple_list.append((document_id, word_position_in_document))

        # For every word in the document we increment for one the number of documents in which the word occurs
        for word in set_of_words_in_document:
            if word not in map_of_words_to_number_of_documents_it_occurs:
                map_of_words_to_number_of_documents_it_occurs[word] = 0
            map_of_words_to_number_of_documents_it_occurs[word] += 1

    # We clear the word list from all common words. Words that appear in more of 40% of the documents
    clear_word_lists_from_common_words(total_documents, map_of_words_to_number_of_documents_it_occurs,
                                       map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word,
                                       map_of_words_to_lists_with_document_position_tuples)

    # We clear the pairs document word if that word appeared less than three times in the document
    clear_word_lists_from_not_important_words(map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word,
                                              map_of_words_to_lists_with_document_position_tuples, titles)

    print(len(map_of_words_to_lists_with_document_position_tuples))

    database.open_connection()

    # For every word in the map of words to list of document position pairs
    for word in map_of_words_to_lists_with_document_position_tuples:
        # If there are documents in which the word occurs we add it to the database
        if len(map_of_words_to_lists_with_document_position_tuples[word]) > 0:
            stemmed_word = stem(word)
            result = database.query("CREATE (w:Word {word: {word}, stem: {stem}}) RETURN w",
                                    {"word": word, "stem": stemmed_word})
            id_word = 0
            for record in result:
                id_word = record["w"].id  # Retrieve the id to the saved word

            # For every document and position of word occurrence pair
            # we create separate relationship between the word and the document for every occurrence
            # The created relationship has a property for the position on which the word occurred
            for entry in map_of_words_to_lists_with_document_position_tuples[word]:
                database.query("MATCH (w:Word), (doc:Document) WHERE ID(doc) = {id_doc} AND ID(w) = {id_w} "
                               "CREATE (doc)-[:CONTAINS {position: {position}}]->(w)",
                               {"id_w": id_word, "id_doc": entry[0], "position": entry[1]})

    # Set the number of words in a document as a document property
    database.query("MATCH (doc:Document)-[:CONTAINS]->(w:Word) "
                   "WITH doc, COUNT(w) AS num_words "
                   "SET doc.number_of_words = num_words")

    database.close_connection()

    return


def clear_word_lists_from_common_words(total_documents, map_of_words_to_number_of_documents_it_occurs,
                                       map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word,
                                       map_of_words_to_lists_with_document_position_tuples):
    threshold = (40 / 100) * total_documents
    common_words = [word for word, value in map_of_words_to_number_of_documents_it_occurs.items() if value > threshold]
    for word in common_words:
        del map_of_words_to_number_of_documents_it_occurs[word]
        del map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word[word]
        del map_of_words_to_lists_with_document_position_tuples[word]

    return


def clear_word_lists_from_not_important_words(map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word,
                                              map_of_words_to_lists_with_document_position_tuples, titles):
    words = [word for word in map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word]
    for word in words:
        for title in titles:
            if title in map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word[word]:
                if map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word[word][title] <= 2:
                    del map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word[word][title]
                    map_of_words_to_lists_with_document_position_tuples[word] = \
                        [entry for entry in map_of_words_to_lists_with_document_position_tuples[word] if
                         entry[0] != title]

    return


# Extracting the words from a text using regular expression
def get_words_from_text(text):
    return re.compile('[a-zA-Z_]+').findall(text)
