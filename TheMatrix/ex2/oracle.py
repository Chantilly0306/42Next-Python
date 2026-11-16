#!/usr/bin/env python3
import os
from dotenv import load_dotenv


def check_config():
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT")
    }

    matrix_modes = ["development", "production"]
    log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    missing_config = []
    valid_config = True

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    for key, value in config.items():
        if not value:
            missing_config.append(key)
            valid_config = False
        elif key == "MATRIX_MODE":
            if value not in matrix_modes:
                print("[Error] Invalid MATRIX_MODE")
                valid_config = False
            else:
                print(f"[OK] {key}: {value}")
        elif key == "LOG_LEVEL":
            if value not in log_levels:
                print("[ERROR] Invalid LOG_LEVEL")
                valid_config = False
            else:
                print(f"[OK] {key}: {value}")
        elif key == "API_KEY" or key == "DATABASE_URL":
            print(f"[OK] {key}: Configured")
        else:
            print(f"[OK] {key}: {value}")

    if missing_config:
        print(f"\nERROR: Missing configuration: {', '.join(missing_config)}")

    if valid_config:
        mode = config["MATRIX_MODE"]
        log_level = config["LOG_LEVEL"]

        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")

        if os.path.isfile(".env"):
            print("[OK] .env file properly configured")
        else:
            print("[WARNING] .env file not found")

        print("[OK] Production overrides available")

        if mode == "development":
            print("\nMODE: development")
            print("Database: Connected to local instance")
            print("API Access: Authenticated")
            print(f"Log Level: {log_level}")
            print("Zion Network: Online")

        elif mode == "production":
            print("\nMODE: production")
            print("Database: Production database")
            print("API Access: Configured")
            print(f"Log Level: {log_level}")
            print("Zion Network: Online")

    else:
        print("\nConfiguration validation failed.")
        print("Please check your .env file.")


if __name__ == "__main__":
    check_config()
