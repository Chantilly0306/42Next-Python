#!/usr/bin/env python3
import random


def main():
    print("=== Game Data Alchemist ===\n")

    initial = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
               'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {initial}")

    all_capitalized = [name.capitalize() for name in initial]
    print(f"New list with all names capitalized: {all_capitalized}")

    names_deja_capitalized = [name for name in initial if name.istitle()]
    print(f"New list of capitalized names only: {names_deja_capitalized}\n")

    score_dict = {name: random.randrange(1000) for name in all_capitalized}
    print(f"Score dict: {score_dict}")

    average = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {average}")

    high_scores = {name: score for name, score in score_dict.items()
                   if score > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
