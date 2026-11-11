#!/usr/bin/env python3
import os
from dotenv import load_dotenv




def check_config():
    endpoint = os.getenv("ZION_ENDPOINT")

    if not endpoint:
        raise ValueError("Missing endpoint!")

    return True

load_dotenv()
print(check_config())
print("Starting Matrix...")