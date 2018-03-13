from flask import json
from flask import request
from google.protobuf.json_format import Parse, MessageToJson


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
        return MessageToJson(func(*args, **kwargs))
    return wrapper