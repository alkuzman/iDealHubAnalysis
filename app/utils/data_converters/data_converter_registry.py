from typing import List, Dict, Tuple

from app.model.document.data import Data
from app.utils.data_converters.data_converter import DataConverter


class DataConverterRegistry(DataConverter):
    def __init__(self):
        self.registry = {}

    def register(self, from_content_type: str, to_content_type: str, data_converter: DataConverter):
        self.registry[(from_content_type, to_content_type)] = data_converter

    def convert(self, data: Data, from_content_type: str, to_content_type: str) -> List[Data]:
        converter = self.registry.get((from_content_type, to_content_type), None)
        if converter is None:
            raise Exception("No converter found for from: " + from_content_type + " to: " + to_content_type)
        return converter.convert(data, from_content_type, to_content_type)
