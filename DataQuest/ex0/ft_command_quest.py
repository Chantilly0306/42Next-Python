#!/usr/bin/env python3
import sys


def main():
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    args_after_program_name = sys.argv[1:]
    arg_count = len(args_after_program_name)

    if arg_count == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {arg_count}")
        idx = 1
        for arg in sys.argv[1:]:
            print(f"Argument {idx}: {arg}")
            idx += 1

    print(f"Total argument {len(sys.argv)}")


if __name__ == "__main__":
    main()
