import app.validators
from flask import json
from flask import request
from flask import Response
from google.protobuf.json_format import Parse, MessageToJson

from app.api_model.generated.api_error_model_pb2 import ErrorResponse, ErrorType
from app.validation import validator_dispatcher


def convert_input_to(class_):
    def wrap(f):
        def decorator(*args):
            request_body = json.loads(request.data)
            obj = class_.from_dict(**request_body)
            return f(obj)
        return decorator
    return wrap


def json_to_protobuf(class_):
    def wrap(f):
        def decorator(*args):
            json_data = request.data
            obj = Parse(json_data, class_())
            return f(obj)
        return decorator
    return wrap


def protobuf_to_json(func):
    def wrapper(*args, **kwargs):
        o = func(*args, **kwargs)
        if isinstance(o, Response):
            message = MessageToJson(o.response, including_default_value_fields=True, use_integers_for_enums=True)
            return Response(message, status=o.status, mimetype=o.mimetype)
        return MessageToJson(o, including_default_value_fields=True, use_integers_for_enums=True)
    return wrapper


validator = validator_dispatcher


def validate(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            validation_error_response = validator.validate(arg)
            if len(validation_error_response.validation_errors) > 0:
                error_response = ErrorResponse()
                error_response.error_code = 'validation.error'
                error_response.data.Pack(validation_error_response)
                error_response.message = "Validation error occurred."
                error_response.error_type = ErrorType.Value('VALIDATION')
                return Response(error_response, status=400, mimetype='application/json')
        return Response(func(*args, **kwargs), status=200, mimetype='application/json')
    return wrapper
