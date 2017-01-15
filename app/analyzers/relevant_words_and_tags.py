from app.database.database import database


# Returns the value of number of documents containing the word divided with number of all documents
# as relevance coefficient
def word_relevance_coefficient(word):
    database.open_connection()
    result = database.query("MATCH (doc:Document)-[:CONTAINS]-(w:Word {word: {word}}) "
                            "WITH COUNT(DISTINCT(doc)) AS documents_containing_word "
                            "MATCH (doc:Document) "
                            "WITH COUNT(DISTINCT(doc)) AS num_documents, documents_containing_word "
                            "RETURN 1 - (documents_containing_word / toFloat(num_documents)) AS coefficient",
                            {"word": word})
    database.close_connection()

    coefficient = 0
    for record in result:
        coefficient = record['coefficient']
    return coefficient


# Returns the value of number of documents tagged with the tag divided with number of all documents
# as relevance coefficient
def tag_relevance_coefficient(tag):
    database.open_connection()
    result = database.query("MATCH (doc:Document)-[:TAG]-(tag:Tag {value: {value}}) "
                            "WITH COUNT(DISTINCT(doc)) AS documents_containing_tag "
                            "MATCH (doc:Document) "
                            "WITH COUNT(DISTINCT(doc)) AS num_documents, documents_containing_tag "
                            "RETURN 1 - (documents_containing_tag / toFloat(num_documents)) AS coefficient",
                            {"value": tag})
    database.close_connection()

    coefficient = 0
    for record in result:
        coefficient = record['coefficient']
    return coefficient
