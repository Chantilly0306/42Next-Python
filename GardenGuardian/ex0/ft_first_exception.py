#!/usr/bin/env python3

def input_temperature(tmp: str) -> int:
    return int(tmp)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    d1: str = "25"
    print(f"Input data is '{d1}'")
    try:
        tmp1: int = input_temperature(d1)
        print(f"Temperature is now {tmp1}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    d2: str = "abc"
    print(f"Input data is '{d2}'")
    try:
        tmp: int = input_temperature(d2)
        print(f"Temperature is now {tmp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
