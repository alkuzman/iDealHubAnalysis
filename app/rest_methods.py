from flask import request
from app.analyzers.similar_documents import text_popularity_coefficient
from flask import Blueprint

rest = Blueprint("rest", __name__)



@rest.route('/idea_popularity', methods=['POST'])
def idea_popularity_coefficient():
    text = request.form['text']
    return text_popularity_coefficient(text)


@rest.route('/hello')
def hello_world():
    return 'Hello World'