from typing import List

from app.api_model.generated.api_model_pb2 import Data as ApiData, Document as ApiDocument
from app.model.document.adapters.api.data_api_adapter import DataApiAdapter
from app.model.document.document import Document
from app.model.document.document_set import DocumentSet
from app.model.document.impl.document_impl import DocumentImpl
from app.utils.data_converters.data_converter import DataConverter


class DocumentSetApiAdapter(DocumentSet):
    def __init__(self, api_data: List[ApiData], api_documents: List[ApiDocument], data_converter: DataConverter):
        self.data_converter = data_converter
        self.api_data = {}
        for api_d in api_data:
            self.api_data[api_d.id] = api_d
        self.api_documents = {}
        for api_document in api_documents:
            self.api_documents[api_document.id] = api_document
        self.documents = {}
        self.data = {}

    def get_document(self, document_id) -> Document:
        # Get document from the cached document set
        document = self.documents.get(document_id, None)
        if document is not None:
            return document
        # If it is not cached then get try to find it in api_documents
        api_document = self.api_documents.get(document_id, None)
        if api_document is None:
            raise Exception("Requested id doesn't exists in the document set")
        # Get data for the api document
        data = self.get_data(api_document)
        document = DocumentImpl(identifier=api_document.id, data=data)
        self.documents[document.get_id()] = document
        return document

    def get_data(self, api_document: ApiDocument):
        data = []
        for data_reference in api_document.data_references:
            api_data = self.api_data.get(data_reference.data_id)
            d = self.data.get(api_data.id, None)
            if d is not None:
                data.extend(d)
                continue
            d = DataApiAdapter(api_data=api_data, api_data_reference=data_reference)
            # Convert the data (it should be just text). Remove all metadata
            converted_data = self.data_converter.convert(data=d, from_content_type=api_data.content_type,
                                                         to_content_type='text/plain')
            self.data[api_data.id] = converted_data
            data.extend(converted_data)
        return data
