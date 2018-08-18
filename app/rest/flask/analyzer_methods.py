from flask import Blueprint

from app.analyzers.analyzer_module import AnalyzerModule
from app.api_model.builders.api_analysis_response_builder import ApiAnalysisResponseBuilder
from app.api_model.generated.api_model_pb2 import AnalysisRequest, AnalysisResponse
from app.model.analysis.request.adapters.api.analysis_request_set_api_adapter import AnalysisRequestSetApiAdapter
from app.rest.rest_decorators import protobuf_to_json, json_to_protobuf, validate

rest = Blueprint("rest", __name__)
analyzer = AnalyzerModule.analyzer()


@rest.route('/analyzer', methods=['POST'])
@protobuf_to_json
@json_to_protobuf(AnalysisRequest)
@validate
def analyze(analysis_request: AnalysisRequest) -> AnalysisResponse:
    # Convert to internal model analysis request
    analysis_request_set = AnalysisRequestSetApiAdapter(analysis_request)

    # Analyze the request and write the response in analysis variable
    analysis = analyzer.analyze(analysis_request_set)

    # Build the analysis response (which is defined by the API model)
    api_analysis_response_builder = ApiAnalysisResponseBuilder(analysis_request, analysis)
    analysis_response = api_analysis_response_builder.build()

    return analysis_response
