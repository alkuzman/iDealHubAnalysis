import abc

from app.model.document.document import Document


class DocumentSet(metaclass=abc.ABCMeta):
    """
    This is set of documents
    """
    @classmethod
    def get_document(self, document_id) -> Document:
        """

        :param document_id: id of the requested document
        :return: the document which has the document id
        """
        pass
