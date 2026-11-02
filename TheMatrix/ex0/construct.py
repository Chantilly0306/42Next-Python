import os
import sys


def is_virtual_env() -> bool:
    return (
        hasattr(sys, "real_prefix")
        or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
        or "VIRTUAL_ENV" in os.environ
    )


def main():
    in_venv = is_virtual_env()
    current_python = sys.executable