#!/usr/bin/env python3

def input_temperature(tmp_str: str) -> int:
    tmp: int = int(tmp_str)
    if tmp > 40:
        raise ValueError(f"{tmp}°C is too hot for plants (max 40°C)")
    if tmp < 0:
        raise ValueError(f"{tmp}°C is too cold for plants (min 0°C)")
    return tmp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    test_inputs: list[str] = ["25", "abc", "100", "-50"]

    for data in test_inputs:
        print(f"Input data is '{data}'")
        try:
            tmp: int = input_temperature(data)
            print(f"Temperature is now {tmp}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
