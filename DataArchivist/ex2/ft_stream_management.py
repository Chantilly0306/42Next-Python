#!/usr/bin/env python3
import sys


def main():
    if len(sys.argv) != 2:
        return print("Usage: ft_stream_management.py <file>")
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    f = None
    lines = []
    try:
        f = open(filename, mode="r")
        print("---\n")
        while True:
            line = f.readline()
            if not line:
                break
            lines.append(line.rstrip("\n"))
        print("\n".join(lines))
        print("\n---")
        print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"[STDERR] Error opening file '{filename}': {e}",
              file=sys.stderr)
        return
    finally:
        if f is not None:
            f.close()

    print("\nTransform data:\n---\n")

    transformed_line = [f"{line}#" for line in lines]
    new_content = "\n".join(transformed_line)
    print(new_content)
    print("\n---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename = sys.stdin.readline().strip()

    if not new_filename:
        return print("Not saving data.")

    print(f"Saving data to '{new_filename}'")
    out_file = None
    try:
        out_file = open(new_filename, mode="w")
        out_file.write(new_content)
        print(f"Data saved in file '{new_filename}'.")
    except Exception as e:
        print(f"[STDERR] Error opening file '{new_filename}': {e}",
              file=sys.stderr)
        print("Data not saved.")
    finally:
        if out_file is not None:
            out_file.close()


if __name__ == "__main__":
    main()
