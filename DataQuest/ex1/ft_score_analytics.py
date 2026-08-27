#!/usr/bin/env python3
import sys


class Analytics():
    def __init__(self, scores: list[int]):
        self.scores: list[int] = scores
        self.count: int = len(scores)
        self.total_score: int = sum(scores)
        self.average: float = self.total_score / self.count
        self.highest: int = max(scores)
        self.lowest: int = min(scores)
        self.range: int = self.highest - self.lowest

    def show(self):
        print(f"Scores processed: {self.scores}")
        print(f"Total players: {self.count}")
        print(f"Total score: {self.total_score}")
        print(f"Average score: {self.average}")
        print(f"High score: {self.highest}")
        print(f"Low score: {self.lowest}")
        print(f"Score range: {self.range}")


class NonArgument(Exception):
    def __init__(self, message: str = "No valid argument"):
        super().__init__(message)

    
def is_numeric(args: list[str]) -> list[int]:
    valid_scores: list[int] = []

    for arg in args:
        try:
            valid_scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    return(valid_scores)


def main():
    print("=== Player Score Analytics ===")
    scores = is_numeric(sys.argv[1:])

    if not scores:
        try:
            raise NonArgument(f"No scores provided.")
        except NonArgument as e:
            print(f"{e} Usage: python3 {sys.argv[0]} <score1> <score2> ...")
            return

    match = Analytics(scores)
    match.show()


if __name__ == "__main__":
    main()
