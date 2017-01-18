from flask import json
from flask import request
from flask.json import jsonify


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
    return format(text_popularity_coefficient(text), '.4f')


@rest.route('/analyzers/similarity', methods=['POST'])
def similar_documents_analyzer():
    data = request.data
    text = json.loads(data)
    limit = request.args.get("limit")
    print(text)
    print(limit)
    result = similar_documents(text, int(limit), 0)
    print(result)
    return jsonify(result)
