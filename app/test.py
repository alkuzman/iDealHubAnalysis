from app.database.database import database
from flask import Blueprint

test = Blueprint("test", __name__)
# This file is containing test functions in order to test the analyzers


def start():
    database.open_connection()
    database.close_connection()
    print("This function is used for testing without using the rest methods")
    return

# This function is used if we want to test the application without using the rest methods
start()
