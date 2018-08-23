from abc import abstractmethod

from app.analyzers.keywords.candidate_keywords.candidate_keyword import CandidateKeyword
from app.api_model.generated.api_validation_error_model_pb2 import ValidationErrorResponse
from app.validation.validator import Validator


class CandidateKeywordValidator(Validator[CandidateKeyword]):
    @abstractmethod
    def validate(self, o: CandidateKeyword) -> ValidationErrorResponse:
        pass

    def validates(self) -> type:
        return CandidateKeyword
