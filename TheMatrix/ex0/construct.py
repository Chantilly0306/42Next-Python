#!/usr/bin/env python3
import sys
import site
import os


def status(is_virtual: bool):
    print("MATRIX STATUS: ",
    "Welcome to the construct" if is_virtual else "You're still plugged in")

    print("\nCurrent Python:", sys.executable)
    print("Virtual Environment: ",
    os.path.basename(sys.prefix) if is_virtual else "None detected\n")

    if is_virtual:
        print(
            f"Environment Path:{sys.prefix}\n\n"
            "SUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting the global system.\n"
            "\nPackage installation path:"
        )
        for path in site.getsitepackages():
            print(path)
    else:
        print(
            "WARNING: You're in the global environment!\n"
            "The machines can see everything you install.\n\n"
            "To enter the construct, run:\n"
            "python3 -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            r"matrix_env\Scripts\activate # On Windows"
            "\n\nThen run this program again."
        )


def main():
    status(sys.prefix != sys.base_prefix)


if __name__ == "__main__":
    main()
