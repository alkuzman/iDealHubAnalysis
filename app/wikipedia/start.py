from flask import Blueprint
from app.wikipedia.connect_documents_with_words import connect_documents_with_words
from app.database.database import database

wiki = Blueprint("wikipedia", __name__)


def trial():
    connect_documents_with_words()

trial()