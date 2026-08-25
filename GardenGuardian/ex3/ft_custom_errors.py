#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def trigger_plant_error():
    raise PlantError("The tomato plant is wilting!")


def trigger_water_error():
    raise WaterError("Not enough water in the tank!")


def main():
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        trigger_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        trigger_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    try:
        trigger_plant_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        trigger_water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
