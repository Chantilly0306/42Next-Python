#/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Union


class DataProcessor(ABC):
    def __init__(self):
        self._data: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data to output")
        item: str = self._data.pop(0)
        current_rank: int = self._rank
        self._rank += 1
        return (current_rank, item)



class NumericProcessor():


class TextProcessor


class LogProcessor