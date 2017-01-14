from app.data_import.connect_documents_with_words import get_words_from_text
from app.database.database import database
from app.database.neo4j_base_service import get_words_from_database, get_document_for_title


# This function returns all documents that are similar to the text given as input,
# together with the coefficient of similarity between the returned document and the text
def similar_documents(text, limit, threshold=0.3):
    content_words = get_words_from_text(text)  # Extract the words from the text and put them in a list

    # Get all words from the database, we only need the relevant words to find similar documents
    database_words = get_words_from_database()

    database_words = [word.word for word in database_words]  # Extract the word value only not the whole node

    # Filter the words from the content so the irrelevant words can be excluded
    word_list = [word.lower() for word in content_words if word.lower() in database_words]
    initial_word_count = len(word_list)

    important_words = word_list

    # Building the query
    string_query = "MATCH (doc:Document)-[:CONTAINS]->(word:Word) " \
                   "WHERE word.word in ["

    parameters = {}
    print(len(important_words))
    index = 0
    for word in important_words:
        index += 1
        # parameter = "word" + str(index)
        # parameters[parameter] = word
        # string_query += "{" + parameter + "}"
        string_query += "\"" + word + "\""
        if index < len(important_words):
            string_query += ", "
        else:
            break
    # Returning all documents for which number_of_same_words / min(number_words_text1, number_words_text2) > 0.2
    # Also both texts need to have at least two same words
    string_query += "] " \
                    "WITH doc.title AS title, COUNT(word) AS number_of_same_words, " \
                    "doc.number_of_words AS number_of_words, " \
                    "CASE WHEN {initial_doc_word_count} < doc.number_of_words " \
                    "THEN {initial_doc_word_count} ELSE doc.number_of_words END AS min " \
                    "WITH number_of_same_words / toFloat(min) AS coefficient, " \
                    "title, number_of_words, number_of_same_words, min " \
                    "WHERE coefficient > toFloat({threshold}) " \
                    "AND number_of_same_words / toFloat({initial_doc_word_count}) > 1 / toFloat(100) " \
                    "RETURN title, min, number_of_words, number_of_same_words, coefficient " \
                    "ORDER BY coefficient DESC, number_of_same_words DESC " \
                    "LIMIT {limit}"

    print(string_query)
    parameters["initial_doc_word_count"] = initial_word_count
    parameters["threshold"] = threshold
    parameters["limit"] = limit

    database.open_connection()
    result = database.query(string_query, parameters)  # Return the query result
    database.close_connection()

    result_list = []

    for record in result:
        entry = record
        result_list.append(entry)

    return result_list


# This function is helper function which finds similar documents to text if the text is encapsulated in a document
def similar_documents_to_document(title, limit=20):
    return similar_documents(get_document_for_title(title).content, limit)


# This function combines the coefficients of similarity between the text and the returned similar documents
# and returns one coefficient which describes how much the idea is innovative using the data in the database
def text_popularity_coefficient(text):
    result = similar_documents(text, 100, 0)
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
