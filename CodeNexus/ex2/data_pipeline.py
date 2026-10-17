#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, Union


class DataProcessor(ABC):
    def __init__(self, name):
        self.name = name
        self._data = []
        self._rank = 0
        self.total_processed = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data to output")
        item = self._data.pop(0)
        rank = self._rank
        self._rank += 1
        return rank, item

    @property
    def remaining(self):
        return len(self._data)


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__("Numeric Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(self, data: Union[int, float, list[Union[int, float]]]):
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for x in data:
                self._data.append(str(x))
                self.total_processed += 1
        else:
            self._data.append(str(data))
            self.total_processed += 1


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__("Text Processor")

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Union[str, list[str]]):
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for x in data:
                self._data.append(x)
                self.total_processed += 1
        else:
            self._data.append(data)
            self.total_processed += 1


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__("Log Processor")

    def validate(self, data: Any) -> bool:
        def is_log(d: Any) -> bool:
            return (
                isinstance(d, dict)
                and "log_level" in d
                and "log_message" in d
            )

        if is_log(data):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(is_log(x) for x in data)
        return False

    def ingest(self, data: Union[dict[str, str], list[dict[str, str]]]):
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for d in data:
                self._data.append(f"{d['log_level']}: {d['log_message']}")
                self.total_processed += 1
        else:
            self._data.append(f"{data['log_levle']}: {data['log_message']}")
            self.total_processed += 1


class DataStream:
    def __init__(self):
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    handled = True
                    break
            if not handled:
                print("DataStream error - "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            print(f"{proc.name}: total {proc.total_processed} items processed, "
                  f"remaining {proc.remaining} on processor")


def main():
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream.\n")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Processors")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(num_proc)
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"\nSend first batch of data on stream: {batch}")
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
