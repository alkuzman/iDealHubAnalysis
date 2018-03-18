from app.validation.default_validator import DefaultValidator
from app.validation.validator import Validator

default_validator = DefaultValidator()


class ValidatorRegistry:
    def __init__(self):
        self.validators = {}

    def register(self, validator: Validator):
        self.validators[validator.validates()] = validator

    def get(self, _class: type) -> Validator:
        validator = self.validators.get(_class, default_validator)
        return validator
