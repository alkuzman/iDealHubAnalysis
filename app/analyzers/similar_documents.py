from app.data_import.connect_documents_with_words import get_words_from_text
from app.database.database import database
from app.database.neo4j_base_service import get_words_from_database, get_document_for_title
from stop_words import get_stop_words


# This function returns all documents that are similar to the text given as input,
# together with the coefficient of similarity between the returned document and the text
def similar_documents(text, limit, threshold=0.3, metric='Custom'):
    content_words = get_words_from_text(text)  # Extract the words from the text and put them in a list

    # Filter the words from the content so the irrelevant words can be excluded
    stop_words = get_stop_words("en")
    word_list = set([word.lower() for word in content_words if word.lower() not in stop_words])
    initial_word_count = len(word_list)

    important_words = word_list

    words = "\", \"".join(important_words)
    words = "\"" + words + "\""

    # Building the query
    if metric == 'Custom':
        string_query = "MATCH (w:Word) " \
                       "WHERE w.word in ["

        parameters = {}
        string_query += words
        # Returning all documents for which
        # number_of_same_words / min(number_words_text1, number_words_text2) > threshold
        string_query += "] " \
                        "WITH COUNT(w) as initial_doc_word_count " \
                        "MATCH (w:Word) " \
                        "WHERE w.word in ["
        string_query += words
        string_query += "] WITH w, initial_doc_word_count " \
                        "MATCH (doc:Document)-[:CONTAINS]->(w) " \
                        "WITH doc.title AS title, COUNT(DISTINCT(w)) AS number_of_same_words, " \
                        "initial_doc_word_count, doc.number_of_distinct_words AS number_of_words, " \
                        "CASE WHEN initial_doc_word_count < doc.number_of_distinct_words " \
                        "THEN initial_doc_word_count ELSE doc.number_of_distinct_words END AS min " \
                        "WITH number_of_same_words / toFloat(min) AS coefficient, initial_doc_word_count, " \
                        "title, number_of_words, number_of_same_words, min " \
                        "WHERE coefficient > toFloat({threshold}) " \
                        "AND number_of_same_words / toFloat(initial_doc_word_count) > 1 / toFloat(100) " \
                        "RETURN title, min, number_of_words, number_of_same_words, coefficient " \
                        "ORDER BY coefficient DESC, number_of_same_words DESC " \
                        "LIMIT {limit}"

        parameters["initial_doc_word_count"] = initial_word_count
        parameters["threshold"] = threshold
        parameters["limit"] = limit

    elif metric == 'Cosine':
        string_query = "MATCH (w:Word) " \
                       "WHERE w.word in ["

        parameters = {}
        string_query += words
        # Returning all documents for which
        # number_of_same_words / min(number_words_text1, number_words_text2) > threshold
        string_query += "] " \
                        "WITH COUNT(w) as initial_doc_word_count " \
                        "MATCH (w:Word) " \
                        "WHERE w.word in ["
        string_query += words
        string_query += "] WITH w, initial_doc_word_count " \
                        "MATCH (doc:Document)-[:CONTAINS]->(w) " \
                        "WITH doc.title AS title, COUNT(DISTINCT(w)) AS number_of_same_words, " \
                        "doc.number_of_distinct_words AS number_of_words, initial_doc_word_count " \
                        "WITH (number_of_same_words * number_of_same_words) / " \
                        "(toFloat(initial_doc_word_count) * number_of_words) " \
                        "AS coefficient, " \
                        "title, number_of_words, number_of_same_words " \
                        "WHERE coefficient > toFloat({threshold}) " \
                        "RETURN title, number_of_words, number_of_same_words, coefficient " \
                        "ORDER BY coefficient DESC, number_of_same_words DESC " \
                        "LIMIT {limit}"
        parameters["initial_doc_word_count"] = initial_word_count
        parameters["threshold"] = threshold
        parameters["limit"] = limit

    else:
        print('This metric is not known')

    print(string_query)

    database.open_connection()
    result = database.query(string_query, parameters)  # Return the query result
    database.close_connection()

    result_list = []

    for record in result:
        result_list.append({"title": record["title"], "coefficient": record["coefficient"]})

    return result_list


# This function is helper function which finds similar documents to text if the text is encapsulated in a document
def similar_documents_to_document(title, limit=20, threshold=0.3, metric='Custom'):
    return similar_documents(get_document_for_title(title).content, limit, threshold, metric)


# This function combines the coefficients of similarity between the text and the returned similar documents
# and returns one coefficient which describes how much the idea is innovative using the data in the database
def text_popularity_coefficient(text, metric='Cosine'):
    result = similar_documents(text, 100, 0, metric)
    coefficient = 0

    for entry in result:
        coefficient += entry["coefficient"]

    return format(coefficient / len(result), '.4f')


# This function is helper function which finds similar documents to text if the text is encapsulated in a document
def document_popularity_coefficient(title, metric='Cosine'):
    return text_popularity_coefficient(get_document_for_title(title).content, metric)