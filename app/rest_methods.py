import jsonpickle
from flask import Blueprint
from flask import json
from flask import request
from flask.json import jsonify

from app.analyzers import analyzer
from app.analyzers.idea.idea_analyzer import IdeaAnalyzer
from app.analyzers.similar_documents import similar_documents
from app.analyzers.similar_documents import text_popularity_coefficient
from app.api_model.builders.api_analysis_response_builder import ApiAnalysisResponseBuilder
from app.api_model.generated.api_model_pb2 import AnalysisRequest, AnalysisResponse
from app.model.analysis.request.adapters.api.analysis_request_set_api_adapter import AnalysisRequestSetApiAdapter
from app.model.idea import Idea
from app.model.problem import Problem
from app.rest_decorators import convert_input_to, protobuf_to_json, json_to_protobuf, validate

idea_analyzer = IdeaAnalyzer()
rest = Blueprint("rest", __name__)


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


@DeprecationWarning
@rest.route('/api/analyzers/keywords', methods=['POST'])
def extract_keywords_analyzer():
    data = request.data
    request_body = json.loads(data)
    idea = Idea(**request_body)
    idea_analysis = idea_analyzer.analyze_idea(idea)
    return jsonpickle.encode(idea_analysis)


@DeprecationWarning
@rest.route('/processing/analyzers/idea', methods=['POST'])
@convert_input_to(Idea)
def analyze_idea(idea: Idea):
    idea_analysis = idea_analyzer.analyze_idea(idea)
    return jsonpickle.encode(idea_analysis)


@DeprecationWarning
@rest.route('/processing/analyzers/problem', methods=["POST"])
def analyze_problem():
    data = request.data
    request_body = json.loads(data)
    validate_problem(request_body)
    problem = Problem(**request_body)
    problem_analysis = idea_analyzer.analyze_problem(problem)
    return jsonpickle.encode(problem_analysis)


@DeprecationWarning
@rest.route('/processing/analyzers/idea/keywords', methods=["POST"])
def idea_keywords():
    data = request.data
    request_body = json.loads(data)
    validate_idea(request_body)
    idea = Idea(**request_body)
    idea.problem = Problem(**idea.problem)
    idea_k = idea_analyzer.get_idea_keywords(idea)
    return jsonpickle.encode(idea_k)


@DeprecationWarning
@rest.route('/processing/analyzers/problem/keywords', methods=["POST"])
def problem_keywords():
    data = request.data
    request_body = json.loads(data)
    validate_problem(request_body)
    problem = Problem(**request_body)
    problem_k = idea_analyzer.get_problem_keywords(problem)
    return jsonpickle.encode(problem_k)


@DeprecationWarning
@rest.route('/processing/analyzers/solutionQuality', methods=['POST'])
def solution_quality():
    data = request.data
    request_body = json.loads(data)
    validate_idea(request_body)
    idea = Idea(**request_body)
    idea.problem = Problem(**idea.problem)
    idea_analysis = idea_analyzer.get_solution_quality(idea)
    return jsonpickle.encode(idea_analysis)


@DeprecationWarning
def validate_document(document: dict):
    document["title"] = document.get("title", "")
    document["text"] = document.get("text", "")


@DeprecationWarning
def validate_problem(problem: dict):
    validate_document(problem)


@DeprecationWarning
def validate_idea(idea: dict):
    validate_document(idea)
    idea["snackPeak"] = idea.get("snackPeak", "")
    validate_problem(idea.get("problem", {}))


@rest.route('/processing/analyzer', methods=['POST'])
@protobuf_to_json
@json_to_protobuf(AnalysisRequest)
@validate
def analyze(analysis_request: AnalysisRequest) -> AnalysisResponse:
    # Convert to internal model analysis request
    analysis_request_set = AnalysisRequestSetApiAdapter(analysis_request)

    # Analyze the request and write the response in analysis variable
    analysis = analyzer.analyze(analysis_request_set)

    # Build the analysis response (which is defined by the API model
    api_analysis_response_builder = ApiAnalysisResponseBuilder(analysis_request, analysis)
    analysis_response = api_analysis_response_builder.build()

    return analysis_response
