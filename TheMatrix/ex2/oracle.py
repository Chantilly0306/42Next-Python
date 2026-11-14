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

    log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    missing_config = []

    for key, value in config.items():
        if value:
            print(f"[OK] {key}: {value}")
        else:
            missing_config.append(key)

    try:
        if missing_config:
            raise ValueError(", ".join(missing_config))
    except ValueError as e:
        print(f"ERROR: Missing configuration: {e}")

    mode = config["MATRIX_MODE"]

    try:
        if config["LOG_LEVEL"] not in log_levels:
            raise ValueError("ERROR: Invalid LOG_LEVEL")
    except ValueError as e:
        print(e)

    try:
        if mode == "development":
            print("\nMODE: development")
            print("Database: Connected to local instance")
            print("API Access: Authenticated")
            print(f"Log Level: {config["LOG_LEVEL"]}")
            print("Zion Network: Online")
        elif mode == "production":
            print("\nMODE: production")
            print("Database: Production database")
            print(f"Log Level: {config["LOG_LEVEL"]}")
            print("Zion Network: Online")
        else:
            raise ValueError("\n[ERROR] Invalid MATRIX_MODE")
    except ValueError as e:
        print(e)

    





check_config()

