from app.database.database import database
from app.database.parsers.result_parser import result_parse


# Retrieving all documents in the database
def get_documents_from_database():
    database.open_connection()
    result = database.query("MATCH (doc:Document) RETURN (doc)")
    database.close_connection()

    documents = result_parse(result)

    return documents


def get_tags_for_document(title):
    database.open_connection()
    result = database.query("MATCH (doc:Document {title: {title}})-[:TAG]-(tag:Tag)"
                            "RETURN tag", {"title": title})
    database.close_connection()

    tags = result_parse(result)

    return tags