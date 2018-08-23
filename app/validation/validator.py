from abc import abstractmethod
from typing import TypeVar, Generic

from app.api_model.generated.api_validation_error_model_pb2 import ValidationErrorResponse

T = TypeVar('T')


class Validator(Generic[T]):
    @abstractmethod
    def validate(self, o: T) -> ValidationErrorResponse:
        pass

    @abstractmethod
    def validates(self) -> type:
        pass
