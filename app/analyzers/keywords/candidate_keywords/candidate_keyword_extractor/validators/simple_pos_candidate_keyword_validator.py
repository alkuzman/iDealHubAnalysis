from typing import Set

from app.analyzers.keywords.candidate_keywords.candidate_keyword import CandidateKeyword
from app.analyzers.keywords.candidate_keywords.candidate_keyword_extractor.validators.candidate_keyword_validator \
    import \
    CandidateKeywordValidator
from app.api_model.generated.api_validation_error_model_pb2 import ValidationErrorResponse, ValidationError


class SimplePosCandidateKeywordValidator(CandidateKeywordValidator):
    def __init__(self, pos_tags: Set) -> None:
        self.pos_tags = pos_tags

    def validate(self, o: CandidateKeyword) -> ValidationErrorResponse:
        validation_error_response = ValidationErrorResponse()
        for pos_token in o.get_pos_tokens():
            if pos_token[1] not in self.pos_tags:
                validation_error_response.validation_errors.extend([self.get_validation_error(pos_token)])

        return validation_error_response

    def get_validation_error(self, pos_token):
        validation_error = ValidationError()
        validation_error.error_code = "keyword.candidate.syntax.not_valid"
        validation_error.field = "candidate_keyword.pos_tokens"
        validation_error.type = "Tuple[str, str]"
        validation_error.message = "Candidate keyword contains word: '" + pos_token[0] + "' with pos tag '" + \
                                   pos_token[1] + "' which is not permitted. Only permitted pos tags are: " + \
                                   str(self.pos_tags)
        return validation_error
