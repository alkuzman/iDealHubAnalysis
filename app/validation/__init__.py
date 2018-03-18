from app.validation.dispatcher_validator import DispatcherValidator
from app.validation.validator_registry import ValidatorRegistry

validator_registry = ValidatorRegistry()
validator_dispatcher = DispatcherValidator(validator_registry)
