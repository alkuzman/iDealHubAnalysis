from stop_words import get_stop_words
from app.database.parsers import result_parser
import re
from app.database.database import database


def connect_documents_with_words():
    documents = get_documents_from_database()

    stop_words = get_stop_words("en")

    map_of_words_to_lists_with_document_position_tuples = {}
    map_of_words_to_number_of_documents_it_occurs = {}
    map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word = {}

    titles = []

    total_documents = len(documents)

    for document in documents:
        document_id = document.id
        title = document.title
        content = document.content
        content_words = get_words_from_text(content)
        titles.append(title)

        set_of_words_in_document = set()
        word_position_in_document = 0
        for word in content_words:
            word = word.lower()
            word_position_in_document += 1

            if word in stop_words or len(word) < 3:
                continue

            if word not in map_of_words_to_lists_with_document_position_tuples:
                map_of_words_to_lists_with_document_position_tuples[word] = []
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

        for word in set_of_words_in_document:
            if word not in map_of_words_to_number_of_documents_it_occurs:
                map_of_words_to_number_of_documents_it_occurs[word] = 0
            map_of_words_to_number_of_documents_it_occurs[word] += 1

    clear_word_lists_from_common_words(total_documents, map_of_words_to_number_of_documents_it_occurs,
                                       map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word,
                                       map_of_words_to_lists_with_document_position_tuples)

    clear_word_lists_from_not_important_words(map_of_words_to_map_of_document_to_number_of_occurrences_of_the_word,
                                              map_of_words_to_lists_with_document_position_tuples, titles)

    print(len(map_of_words_to_lists_with_document_position_tuples))
    database.open_connection()

    for word in map_of_words_to_lists_with_document_position_tuples:
        if len(map_of_words_to_lists_with_document_position_tuples[word]) > 0:
            result = database.query("CREATE (w:Word {word: {word}}) RETURN w", {"word": word})
            id_word = 0
            for record in result:
                id_word = record["w"].id

            for entry in map_of_words_to_lists_with_document_position_tuples[word]:
                database.query("MATCH (w:Word), (doc:Document) WHERE ID(doc) = {id_doc} AND ID(w) = {id_w} "
                               "CREATE (doc)-[:CONTAINS {position: {position}}]->(w)",
                               {"id_w": id_word, "id_doc": entry[0], "position": entry[1]})

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


def get_documents_from_database():
    database.open_connection()
    result = database.query("MATCH (doc:Document) RETURN (doc)")
    database.close_connection()

    documents = result_parser.result_parse(result)

    return documents


def get_words_from_text(text):
    return re.compile('[a-zA-Z_]+').findall(text)
