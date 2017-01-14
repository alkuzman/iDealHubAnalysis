from app.database.database import database
from app.database.parsers.result_parser import result_parse


# Retrieving all documents in the database
def get_documents_from_database():
    database.open_connection()
    result = database.query("MATCH (doc:Document) RETURN (doc)")
    database.close_connection()

    documents = result_parse(result)

    return documents


# Retrieving all tags for a document
def get_tags_for_document(title):
    database.open_connection()
    result = database.query("MATCH (doc:Document {title: {title}})-[:TAG]-(tag:Tag)"
                            "RETURN tag", {"title": title})
    database.close_connection()

    tags = result_parse(result)

    return tags


# Retrieve all distinct words from database
def get_words_from_database():
    database.open_connection()
    result = database.query("MATCH (w:Word) RETURN DISTINCT(w) ORDER BY w.word")
    database.close_connection()

    words = result_parse(result)

    return words


# Return document for given title
def get_document_for_title(title):
    database.open_connection()
    result = database.query("MATCH (doc:Document {title: {title}}) RETURN doc", {"title": title})
    database.close_connection()

    return result_parse(result)