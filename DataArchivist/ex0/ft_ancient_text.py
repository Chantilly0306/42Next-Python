#!/usr/bin/env python3
import sys


def main():
    if len(sys.argv) != 2:
        return print("Usage: ft_ancient_text.py <file>")
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        f = open(sys.argv[1], mode="r")
        print("---\n")
        print(f.read())
        print("\n---")
        f.close()
        print(f"File '{sys.argv[1]}' closed.")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
