from typing import TypeVar, Generic
DataType = TypeVar("DataType")
class DataBuffer(Generic[DataType]):
    def __init__(self):
        self._data = []
    def add_record(self, record: DataType) -> None:
        self._data.append(record)
    def get_last(self) -> DataType:
        return self._data[-1]
numeric_buffer = DataBuffer[float]()
text_buffer = DataBuffer[str]()