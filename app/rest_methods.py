from flask import json
from flask import request

from app.analyzers.similar_documents import text_popularity_coefficient
from app.analyzers.similar_documents import similar_documents
from flask import Blueprint

rest = Blueprint("rest", __name__)

@rest.route('/hello')
def hello_world():
    return 'Hello World'


@rest.route('/analyzers/popularity', methods=['POST'])
def popularity_analyzer():
    data = request.data
    text = json.loads(data)
    print(text)
    return text_popularity_coefficient(text)


@rest.route('/analyzers/similarity', methods=['POST'])
def similar_documents_analyzer():
    data = request.data
    text = json.loads(data)
    limit = request.args.get("limit")
    result = {}
    result.value = similar_documents(text, limit)
    return result
