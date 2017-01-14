from app.database.database import database
from flask import Blueprint
from app.analyzers.documents_similarity import similar_documents_to_document
from app.data_import.connect_documents_with_tags import connect_documents_with_tags

test = Blueprint("test", __name__)
# This file is containing test functions in order to test the analyzers


def start():
    connect_documents_with_tags()

# This function is used if we want to test the application without using the rest methods
start()
