import jsonpickle
from flask import Blueprint
from flask import json
from flask import request
from flask.json import jsonify
from google.protobuf.json_format import Parse

from app.analyzers.idea.idea_analyzer import IdeaAnalyzer
from app.analyzers.similar_documents import similar_documents
from app.analyzers.similar_documents import text_popularity_coefficient
from app.api_model.generated.api_model_pb2 import Ackicko
from app.model.idea import Idea
from app.model.problem import Problem
from app.utils import convert_input_to, protobuf_to_json, json_to_protobuf

idea_analyzer = IdeaAnalyzer()
rest = Blueprint("rest", __name__)


@rest.route('/hello')
def hello_world():
    return 'Hello World'


@rest.route('/processing/analyzers/popularity', methods=['POST'])
def popularity_analyzer():
    data = request.data
    text = json.loads(data)
    print(text)
    return format(text_popularity_coefficient(text), '.4f')


@rest.route('/processing/analyzers/similarity', methods=['POST'])
def similar_documents_analyzer():
    data = request.data
    text = json.loads(data)
    limit = request.args.get("limit")
    print(text)
    print(limit)
    result = similar_documents(text, int(limit), 0)
    print(result)
    return jsonify(result)


@rest.route('/api/analyzers/keywords', methods=['POST'])
def extract_keywords_analyzer():
    data = request.data
    request_body = json.loads(data)
    idea = Idea(**request_body)
    idea_analysis = idea_analyzer.analyze_idea(idea)
    return jsonpickle.encode(idea_analysis)


@rest.route('/processing/analyzers/idea', methods=['POST'])
@convert_input_to(Idea)
def analyze_idea(idea: Idea):
    idea_analysis = idea_analyzer.analyze_idea(idea)
    return jsonpickle.encode(idea_analysis)


@rest.route('/processing/analyzers/problem', methods=["POST"])
def analyze_problem():
    data = request.data
    request_body = json.loads(data)
    validate_problem(request_body)
    problem = Problem(**request_body)
    problem_analysis = idea_analyzer.analyze_problem(problem)
    return jsonpickle.encode(problem_analysis)


@rest.route('/processing/analyzers/idea/keywords', methods=["POST"])
def idea_keywords():
    data = request.data
    request_body = json.loads(data)
    validate_idea(request_body)
    idea = Idea(**request_body)
    idea.problem = Problem(**idea.problem)
    idea_k = idea_analyzer.get_idea_keywords(idea)
    return jsonpickle.encode(idea_k)


@rest.route('/processing/analyzers/problem/keywords', methods=["POST"])
def problem_keywords():
    data = request.data
    request_body = json.loads(data)
    validate_problem(request_body)
    problem = Problem(**request_body)
    problem_k = idea_analyzer.get_problem_keywords(problem)
    return jsonpickle.encode(problem_k)


@rest.route('/processing/analyzers/solutionQuality', methods=['POST'])
def solution_quality():
    data = request.data
    request_body = json.loads(data)
    validate_idea(request_body)
    idea = Idea(**request_body)
    idea.problem = Problem(**idea.problem)
    idea_analysis = idea_analyzer.get_solution_quality(idea)
    return jsonpickle.encode(idea_analysis)


@rest.route('/ackicko', methods=['POST'])
@protobuf_to_json
@json_to_protobuf(Ackicko)
def ackicko(acko: Ackicko) -> Ackicko:
    print(acko)
    return acko


def validate_document(document: dict):
    document["title"] = document.get("title", "")
    document["text"] = document.get("text", "")


def validate_problem(problem: dict):
    validate_document(problem)


def validate_idea(idea: dict):
    validate_document(idea)
    idea["snackPeak"] = idea.get("snackPeak", "")
    validate_problem(idea.get("problem", {}))
