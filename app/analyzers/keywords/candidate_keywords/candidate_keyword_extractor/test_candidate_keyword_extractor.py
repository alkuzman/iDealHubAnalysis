import unittest
from unittest.mock import MagicMock

from app.analyzers.keywords.candidate_keywords.candidate_keyword_extractor.max_length_candidate_keyword_extractor \
    import \
    MaxLengthCandidateKeywordExtractor
from app.analyzers.keywords.candidate_keywords.candidate_keyword_extractor.validators.candidate_keyword_validator \
    import \
    CandidateKeywordValidator
from app.api_model.generated.api_validation_error_model_pb2 import ValidationErrorResponse


class TestMaxLengthCandidateKeywordExtractor(unittest.TestCase):
    def setUp(self):
        candidate_keyword_validator: CandidateKeywordValidator = MagicMock()
        candidate_keyword_validator.validate.return_value = ValidationErrorResponse()
        self.candidate_keyword_extractor = MaxLengthCandidateKeywordExtractor(candidate_keyword_validator, 8)

    def test_number_of_keywords(self):
        pos_tokens = [("This", "DT"), ("is", "DT"), ("the", "DT"), ("world", "DT"), ("This", "DT"), ("is", "DT"),
                      ("the", "DT"), ("world", "DT")]
        candidate_keywords = self.candidate_keyword_extractor.get_candidate_keywords(pos_tokens)
        expected_num_of_keywords = 36
        self.assertEqual(expected_num_of_keywords, len(candidate_keywords))
