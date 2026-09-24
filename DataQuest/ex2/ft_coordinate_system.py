#!/usr/bin/env python3
import math


class InvalidInput(Exception):
    def __init__(self, message: str = "Invalid syntax"):
        super().__init__(message)


def get_player_pos() -> tuple:
    input_str = input("Enter new coordinates as floats in format ’x,y,z’: ")
    input_str = input_str.replace(" ", "")

    if input_str.count(',') != 2:
        try:
            raise InvalidInput
        except InvalidInput as e:
            print(f"{e}")
            return get_player_pos()

    lst = []
    for s in input_str.split(','):
        try:
            lst.append(float(s))
        except ValueError:
            print(f"Error on parameter '{s}': ", end="")
            print(f"could not convert string to float: '{s}'")
            return get_player_pos()

    return tuple(lst)


def get_distance(p1: tuple, p2: tuple = (0, 0, 0)) -> float:
    return round(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                           + (p1[2] - p2[2]) ** 2), 4)


def main():
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    print(f"Distance to center: {get_distance(first)}\n")

    print("Get a second set of coordinates")
    second = get_player_pos()
    distance = get_distance(first, second)
    print(f"Distance between the 2 sets of coordinates: {distance}")


if __name__ == "__main__":
    main()
