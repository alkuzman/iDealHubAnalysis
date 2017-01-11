from app.wikipedia.connect_documents_with_words import get_words_from_text
from stop_words import get_stop_words
from app.database.parsers.result_parser import result_parse
from app.database.database import database


def similar_documents(text):
    content_words = get_words_from_text(text)
    stop_words = get_stop_words("en")

    database.open_connection()
    result_words = database.query("MATCH (w:Word) RETURN (w)")
    database.close_connection()

    database_words = result_parse(result_words)
    database_words = [word.word for word in database_words]

    word_list = [word.lower() for word in content_words if word not in stop_words and len(word) > 2
                 and word.lower() in database_words]
    map_of_word_to_number_of_occurrences = {}

    for word in word_list:
        number_of_occurrences = 0
        if word in map_of_word_to_number_of_occurrences:
            number_of_occurrences = map_of_word_to_number_of_occurrences[word]
        number_of_occurrences += 1
        map_of_word_to_number_of_occurrences[word] = number_of_occurrences

    important_words = [word for word, num_occurrences in map_of_word_to_number_of_occurrences.items()
                       if num_occurrences > 2]

    string_query = "MATCH (doc:Document)-[rel:CONTAINS]->(w:Word) " \
                   "WITH doc, COUNT(DISTINCT(w)) AS number_of_words " \
                   "MATCH (doc:Document)-[rel:CONTAINS]->(w:Word) " \
                   "WHERE w.word in ["

    parameters = {}
    index = 0
    for word in important_words:
        index += 1
        parameter = "word" + str(index)
        parameters[parameter] = word
        string_query += "{" + parameter + "}"
        # string_query += "\"" + word + "\""
        if index < len(important_words):
            string_query += ", "
        else:
            break
    string_query += "] " \
                    "WITH doc, COUNT(DISTINCT(w)) AS number_of_same_words, number_of_words, " \
                    "CASE WHEN {initial_doc_word_count} < number_of_words " \
                    "THEN {initial_doc_word_count} ELSE number_of_words END AS min " \
                    "WITH number_of_same_words / toFloat(min) AS coefficient, " \
                    "doc, number_of_words, number_of_same_words " \
                    "WHERE coefficient > toFloat(\"0.2\") AND number_of_same_words >= 2 " \
                    "RETURN doc.title, number_of_words, number_of_same_words, coefficient " \
                    "ORDER BY coefficient DESC"

    print(string_query)
    parameters["initial_doc_word_count"] = index

    database.open_connection()
    result = database.query(string_query, parameters)
    database.close_connection()

    result_list = []

    for record in result:
        entry = record
        result_list.append(entry)

    return result_list


def text_popularity_coefficient(text):
    result = similar_documents(text)
    coefficient = 0
    sum_same_words = 0
    for record in result:
        sum_same_words += record["number_of_same_words"]

    for record in result:
        intermediate_coefficient = record["coefficient"] * (record["number_of_same_words"] / sum_same_words)
        print(intermediate_coefficient)
        coefficient += intermediate_coefficient

    print(sum_same_words)

    return format(coefficient, '.4f')
