from app.api_model.generated.api_validation_error_model_pb2 import ValidationErrorResponse


class Validator:
    def validate(self, o) -> ValidationErrorResponse: ...

    def validates(self) -> type: ...
