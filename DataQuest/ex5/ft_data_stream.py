#!/usr/bin/env python3
from typing import Generator
import random


PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep", "grab", "move",
           "climb", "swim", "release", "grab"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(events) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        idx = random.randrange(len(events))
        event = events.pop(idx)
        yield event


def main():
    print("=== Game Data Stream Processor ===")

    stream = gen_event()
    for i in range(1000):
        event = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list = [next(stream) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
