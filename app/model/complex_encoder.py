import json


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'__repr__'):
            return obj.__repr__()
        else:
            return json.JSONEncoder.default(self, obj)