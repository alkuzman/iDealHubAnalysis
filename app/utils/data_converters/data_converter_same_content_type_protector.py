from typing import List

from app.model.document.data import Data
from app.utils.data_converters.data_converter import DataConverter


class DataConverterSameContentTypeProtector(DataConverter):
    def __init__(self, data_converter: DataConverter):
        self.data_converter = data_converter

    def convert(self, data: Data, from_content_type: str, to_content_type: str) -> List[Data]:
        if from_content_type.__eq__(to_content_type):
            return [data]
        return self.data_converter.convert(data, from_content_type, to_content_type)
