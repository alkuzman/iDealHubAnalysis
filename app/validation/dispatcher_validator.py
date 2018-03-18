from app.api_model.generated.api_validation_error_model_pb2 import ValidationErrorResponse
from app.validation.validator_registry import ValidatorRegistry
from app.validation.validator import Validator


class DispatcherValidator(Validator):
    def __init__(self, validator_registry: ValidatorRegistry):
        self.validator_registry = validator_registry

    def validate(self, o) -> ValidationErrorResponse:
        validation_error_response = ValidationErrorResponse()
        for descriptor in o.DESCRIPTOR.fields:
            value = getattr(o, descriptor.name)
            if descriptor.type == descriptor.TYPE_MESSAGE:
                if descriptor.label == descriptor.LABEL_REPEATED:
                    for v in value:
                        validation_error_response.MergeFrom(self.validate_single(v))
                else:
                    validation_error_response.MergeFrom(self.validate_single(value))
        validation_error_response.MergeFrom(self.validate_single(o))
        return validation_error_response

    def validate_single(self, o) -> ValidationErrorResponse:
        if o is None:
            return ValidationErrorResponse()
        validator = self.validator_registry.get(type(o))
        return validator.validate(o)
