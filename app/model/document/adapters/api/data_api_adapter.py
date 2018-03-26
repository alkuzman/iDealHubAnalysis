from app.api_model.generated.api_model_pb2 import Data as ApiData, DataReference as ApiDataReference
from app.model.document.data import Data


class DataApiAdapter(Data):
    def __init__(self, api_data: ApiData, api_data_reference: ApiDataReference):
        self.api_data = api_data
        self.api_data_reference = api_data_reference

    def get_content(self) -> str:
        return self.api_data.content

    def get_boost(self) -> float:
        return self.api_data_reference.boost

    def get_id(self) -> str:
        return self.api_data.id
