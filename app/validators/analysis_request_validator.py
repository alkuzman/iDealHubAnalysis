from app.api_model.generated.api_model_pb2 import AnalysisRequest, IdValidationError, Document, \
    IdReferenceValidationError
from app.api_model.generated.api_validation_error_model_pb2 import ValidationErrorResponse, ValidationError
from app.validation.validator import Validator


class AnalysisRequestValidator(Validator[AnalysisRequest]):
    def validate(self, analysis_request: AnalysisRequest) -> ValidationErrorResponse:
        validation_error_response = ValidationErrorResponse()
        # Data ids are unique
        validation_errors = AnalysisRequestValidator.check_uniqueness_of_data_ids(analysis_request.data)
        validation_error_response.MergeFrom(validation_errors)
        # Document ids are unique
        validation_errors = AnalysisRequestValidator.check_uniqueness_of_document_ids(analysis_request.documents)
        validation_error_response.MergeFrom(validation_errors)
        # Data ids references
        validation_errors = AnalysisRequestValidator.check_data_references(analysis_request)
        validation_error_response.MergeFrom(validation_errors)
        # Document ids references
        validation_errors = AnalysisRequestValidator.check_document_references(analysis_request)
        validation_error_response.MergeFrom(validation_errors)
        return validation_error_response

    @staticmethod
    def check_uniqueness_of_data_ids(data) -> ValidationErrorResponse:
        validation_error_response = ValidationErrorResponse()
        data_ids = {}
        for d in data:
            data_id = d.id
            if data_id in data_ids:
                id_not_unique_validation_error = IdValidationError()
                id_not_unique_validation_error.id = data_id

                validation_error = ValidationError()
                validation_error.data.Pack(id_not_unique_validation_error)
                validation_error.error_code = "id.duplicate"
                validation_error.type = "string"
                validation_error.field = "analysisRequest.data[].id"
                validation_error.message = "id of the data within the analysis request is not unique for: " + data_id

                validation_error_response.validation_errors.extend([validation_error])
            data_ids[data_id] = True
        return validation_error_response

    @staticmethod
    def check_uniqueness_of_document_ids(documents) -> ValidationErrorResponse:
        validation_error_response = ValidationErrorResponse()
        document_ids = {}
        for document in documents:
            document_id = document.id
            if document_id in document_ids:
                id_not_unique_validation_error = IdValidationError()
                id_not_unique_validation_error.id = document_id

                validation_error = ValidationError()
                validation_error.data.Pack(id_not_unique_validation_error)
                validation_error.error_code = "id.duplicate"
                validation_error.type = "string"
                validation_error.field = "analysisRequest.documents[].id"
                validation_error.message = "id of the document within the analysis request is not unique for: " + document_id

                validation_error_response.validation_errors.extend([validation_error])
            document_ids[document_id] = True
        return validation_error_response

    @staticmethod
    def check_data_references(analysis_request: AnalysisRequest) -> ValidationErrorResponse:
        validation_error_response = ValidationErrorResponse()
        data_ids = []
        for data in analysis_request.data:
            data_ids.append(data.id)

        for document in analysis_request.documents:
            for data_reference in document.data_references:
                if data_reference.data_id not in data_ids:
                    id_validation_error = IdReferenceValidationError()
                    id_validation_error.id = data_reference.data_id
                    id_validation_error.present_ids.extend(data_ids)

                    validation_error = ValidationError()
                    validation_error.data.Pack(id_validation_error)
                    validation_error.error_code = "id_reference.not_found"
                    validation_error.type = "string"
                    validation_error.field = "analysisRequest.documents[].data_reference.data_id"
                    validation_error.message = "Reference data_id: " + data_reference.data_id + " not found in data messages"

                    validation_error_response.validation_errors.extend([validation_error])
        return validation_error_response

    @staticmethod
    def check_document_references(analysis_request: AnalysisRequest) -> ValidationErrorResponse:
        validation_error_response = ValidationErrorResponse()
        document_ids = []
        for document in analysis_request.documents:
            document_ids.append(document.id)

        for keyword_analysis_request in analysis_request.keyword_analysis_requests:
            if keyword_analysis_request.document_id not in document_ids:
                id_validation_error = IdReferenceValidationError()
                id_validation_error.id = keyword_analysis_request.document_id
                id_validation_error.present_ids.extend(document_ids)

                validation_error = ValidationError()
                validation_error.data.Pack(id_validation_error)
                validation_error.error_code = "id_reference.not_found"
                validation_error.type = "string"
                validation_error.field = "analysisRequest.keywordAnalysisRequests[].document_id"
                validation_error.message = "Reference document_id: " + keyword_analysis_request.document_id + " not found in document messages"

                validation_error_response.validation_errors.extend([validation_error])

        for sneak_peek_analysis_request in analysis_request.sneak_peek_analysis_requests:
            if sneak_peek_analysis_request.sneak_peek_document_id not in document_ids:
                id_validation_error = IdReferenceValidationError()
                id_validation_error.id = sneak_peek_analysis_request.sneak_peek_document_id
                id_validation_error.present_ids.extend(document_ids)

                validation_error = ValidationError()
                validation_error.data.Pack(id_validation_error)
                validation_error.error_code = "id_reference.not_found"
                validation_error.type = "string"
                validation_error.field = "analysisRequest.sneak_peek_analysis_requests[].sneak_peek_document_id"
                validation_error.message = "Reference sneak_peek_document_id: " + sneak_peek_analysis_request.sneak_peek_document_id + " not found in document messages"

                validation_error_response.validation_errors.extend([validation_error])

        for sneak_peek_analysis_request in analysis_request.sneak_peek_analysis_requests:
            if sneak_peek_analysis_request.main_document_id not in document_ids:
                id_validation_error = IdReferenceValidationError()
                id_validation_error.id = sneak_peek_analysis_request.main_document_id
                id_validation_error.present_ids.extend(document_ids)

                validation_error = ValidationError()
                validation_error.data.Pack(id_validation_error)
                validation_error.error_code = "id_reference.not_found"
                validation_error.type = "string"
                validation_error.field = "analysisRequest.sneak_peek_analysis_requests[].main_document_id"
                validation_error.message = "Reference main_document_id: " + sneak_peek_analysis_request.main_document_id + " not found in document messages"

                validation_error_response.validation_errors.extend([validation_error])

        for coverage_analysis_request in analysis_request.coverage_analysis_requests:
            if coverage_analysis_request.covered_document_id not in document_ids:
                id_validation_error = IdReferenceValidationError()
                id_validation_error.id = coverage_analysis_request.covered_document_id
                id_validation_error.present_ids.extend(document_ids)

                validation_error = ValidationError()
                validation_error.data.Pack(id_validation_error)
                validation_error.error_code = "id_reference.not_found"
                validation_error.type = "string"
                validation_error.field = "analysisRequest.coverage_analysis_requests[].covered_document_id"
                validation_error.message = "Reference covered_document_id: " + coverage_analysis_request.covered_document_id + " not found in document messages"

                validation_error_response.validation_errors.extend([validation_error])

        for coverage_analysis_request in analysis_request.coverage_analysis_requests:
            if coverage_analysis_request.cover_document_id not in document_ids:
                id_validation_error = IdReferenceValidationError()
                id_validation_error.id = coverage_analysis_request.cover_document_id
                id_validation_error.present_ids.extend(document_ids)

                validation_error = ValidationError()
                validation_error.data.Pack(id_validation_error)
                validation_error.error_code = "id_reference.not_found"
                validation_error.type = "string"
                validation_error.field = "analysisRequest.coverage_analysis_requests[].cover_document_id"
                validation_error.message = "Reference cover_document_id: " + coverage_analysis_request.cover_document_id + " not found in document messages"

                validation_error_response.validation_errors.extend([validation_error])

        return validation_error_response

    def validates(self) -> type:
        return AnalysisRequest
