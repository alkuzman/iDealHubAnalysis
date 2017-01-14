from app.database.database import database
from flask import Blueprint
from app.analyzers.documents_similarity import similar_documents_to_document
from app.data_import.connect_documents_with_tags import connect_documents_with_tags
from app.data_import.insert_documents_and_tags import insert_documents

# This file is containing test functions in order to test the analyzers

test = Blueprint("test", __name__)


# This function is used if we want to test the application without using the rest methods
def start():
    print("This function is used if we want to test the application without using the rest methods. "
          "The user must change username and password for the database in the config file")

    # This function is for importing 500 documents from Wikipedia starting from the page 'Science'
    import_documents()


def import_documents():
    insert_documents(500, 'Science')

start()
