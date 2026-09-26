#!/usr/bin/env python3
import sys
import typing


def main():
    if len(sys.argv) != 2:
        return print("Usage: ft_archive_creation.py <file>")
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    f: typing.Optional[typing.IO[str]] = None
    try:
        f = open(sys.argv[1], mode="r")
        print("---\n")
        context = f.read()
        print(context)
        print("\n---")
        print(f"File '{sys.argv[1]}' closed.")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return
    finally:
        if f is not None:
            f.close()

    print("\nTransform data:\n---\n")
    lines = context.splitlines()
    transformed_line = [f"{line}#" for line in lines]
    new_content = "\n".join(transformed_line)
    print(new_content)
    print("\n---")

    new_file = input("Enter new file name (or empty): ").strip()
    if not new_file:
        return print("Not saving data.")

    print(f"Saving data to '{new_file}'")
    out_file: typing.Optional[typing.IO[str]] = None
    try:
        out_file = open(new_file, mode="w")
        out_file.write(new_content)
        print(f"Data saved in file '{new_file}'.")
    except Exception as e:
        print(f"Error saving file '{new_file}': {e}")
    finally:
        if out_file is not None:
            f.close()


if __name__ == "__main__":
    main()
