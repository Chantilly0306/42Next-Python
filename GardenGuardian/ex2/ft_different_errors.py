#!/usr/bin/env python3

def garden_operations(operation_number: int):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        _ = 10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        _ = "25" + 25
    else:
        return


def test_error_types():
    print("=== Garden Error Types Demo ===")

    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
