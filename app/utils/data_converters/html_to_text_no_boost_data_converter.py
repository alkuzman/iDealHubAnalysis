from bs4 import BeautifulSoup

from typing import List

from app.model.document.data import Data
from app.model.document.impl.data_impl import DataImpl
from app.utils.data_converters.data_converter import DataConverter


class HtmlToTextNoBoostDataConverter(DataConverter):
    def convert(self, data: Data, from_content_type: str, to_content_type: str) -> List[Data]:
        soup = BeautifulSoup(data.get_content(), 'html.parser')
        text = soup.get_text()
        return [DataImpl(data.get_id(), text, data.get_boost())]
