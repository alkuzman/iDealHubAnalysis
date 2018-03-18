from typing import Any

from app.api_model.generated.api_validation_error_model_pb2 import ValidationErrorResponse
from app.validation.validator import Validator


class DefaultValidator(Validator):
    def validate(self, o) -> ValidationErrorResponse:
        return ValidationErrorResponse()

    def validates(self) -> type:
        return Any
