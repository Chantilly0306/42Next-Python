#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Union


class DataProcessor(ABC):
    def __init__(self):
        self._data = []
        self._rank = 0

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
        rank: int = self._rank
        self._rank += 1
        return (rank, item)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(self, data: Union[int, float, list[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for x in data:
                self._data.append(str(x))
        else:
            self._data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Union[str, list[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for x in data:
                self._data.append(x)
        else:
            self._data.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_log(d: Any) -> bool:
            return (
                isinstance(d, dict)
                and "log_level" in d
                and "log_message" in d
            )

        if is_valid_log(data):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(is_valid_log(x) for x in data)
        return False

    def ingest(self, data: Union[dict[str, str], list[dict[str, str]]]):
        if not self.validate(data):
            raise ValueError("Improper log data")

        def format_log(d: dict[str, str]) -> str:
            return f"{d['log_level']}: {d['log_message']}"

        if isinstance(data, list):
            for x in data:
                self._data.append(format_log(x))
        else:
            self._data.append(format_log(data))


def main():
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")

    test_num = [1, 2, 3, 4, 5]
    print(f"Processing data: {test_num}")
    num_proc.ingest(test_num)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")
    test_text = ["Hello", "Nexus", "World"]
    print(f"Processing data: {test_text}")
    text_proc.ingest(test_text)
    print("Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"Text value {rank}: {val}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    test_log = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {test_log}")
    log_proc.ingest(test_log)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")


if __name__ == "__main__":
    main()
