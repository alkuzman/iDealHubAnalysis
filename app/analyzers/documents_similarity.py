from app.database.database import database
from app.database.neo4j_base_service import get_words_from_database
from math import sqrt, pow, e


# This function returns similarity between two texts
def document_similarity_coefficient(title1, title2, metric='Custom'):
    map_words_num_occurrences_doc1 = get_map_of_words_and_number_of_occurrences_for_document(title1)
    map_words_num_occurrences_doc2 = get_map_of_words_and_number_of_occurrences_for_document(title2)

    vector1 = []
    vector2 = []

    words = get_words_from_database()
    for word in words:
        if word.word in map_words_num_occurrences_doc1:
            vector1.append(map_words_num_occurrences_doc1[word.word])
        else:
            vector1.append(0)

        if word.word in map_words_num_occurrences_doc2:
            vector2.append(map_words_num_occurrences_doc2[word.word])
        else:
            vector2.append(0)

    similarity = 0
    if metric == 'Cosine':
        similarity = text_similarity_cosine(vector1, vector2)
    if metric == 'Euclid':
        similarity = text_similarity_euclid(vector1, vector2)
    if metric == 'Jaccard':
        similarity = text_similarity_jaccard(vector1, vector2)
    if metric == 'Custom':
        similarity = text_similarity_custom(vector1, vector2)

    return round(similarity, 3)


def text_similarity_cosine(vector1, vector2):
    numerator = sum(a * b for a, b in zip(vector1, vector2))
    denominator = square_rooted(vector1) * square_rooted(vector2)
    return round(numerator / float(denominator), 3)


def square_rooted(x):
    return round(sqrt(sum([a * a for a in x])), 3)


def text_similarity_jaccard(vector1, vector2):
    intersection_cardinality = sum(1 for a, b in zip(vector1, vector2) if min(a,b) > 0)
    union_cardinality = sum(1 for a, b in zip(vector1, vector2) if max(a,b) > 0)
    return intersection_cardinality / float(union_cardinality)


def text_similarity_euclid(vector1, vector2):
    distance = sqrt(sum(pow(a - b, 2) for a, b in zip(vector1, vector2)))
    if distance == 0:
        return 1
    print(e)
    return 1 / (1 + distance)


def text_similarity_custom(vector1, vector2):
    return sum(min(a, b) for a, b in zip(vector1, vector2)) / min(sum(vector1), sum(vector2))


# This function returns map of words and their number of occurrences in the
def get_map_of_words_and_number_of_occurrences_for_document(title):
    database.open_connection()
    result = database.query("MATCH (doc:Document {title: {title}})-[:CONTAINS]->(w:Word) "
                            "RETURN DISTINCT(w) AS word, COUNT(w) AS num_occurrences", {"title": title})
    database.close_connection()
    map_word_num_occurrences = {}
    for record in result:
        map_word_num_occurrences[record["word"].properties["word"]] = record["num_occurrences"]

    return map_word_num_occurrences

