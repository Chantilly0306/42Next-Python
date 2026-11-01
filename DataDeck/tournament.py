#!/usr/bin/env python3
import typing
from ex0 import FlamelingFactory, AquaFactory
from ex1 import HealingFactory, TransformFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def run_tournament(name: str, opponents: list[tuple[typing.Any, typing.Any]]):
    print(f"=== {name} ===")

    formatted_opponents = []
    for fact, strat in opponents:
        f_name = fact.__class__.__name__[:-7]
        s_name = strat.__class__.__name__[:-8]
        formatted_opponents.append(f"({f_name}+{s_name})")
    print(f"[{', '.join(formatted_opponents)}]")

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            fact1, strat1 = opponents[i]
            fact2, strat2 = opponents[j]

            c1 = fact1.create_base()
            c2 = fact2.create_base()

            print("\n* Battle *")
            print(c1.describe())
            print("VS.")
            print(c2.describe())
            print("now fight!")

            try:
                actions1 = strat1.act(c1)
                for action in actions1:
                    print(action)

                actions2 = strat2.act(c2)
                for action in actions2:
                    print(action)

            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")


def main():
    flame_factory = FlamelingFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingFactory()
    transform_factory = TransformFactory()

    normal_strat = NormalStrategy()
    aggressive_strat = AggressiveStrategy()
    defensive_strat = DefensiveStrategy()

    run_tournament(
        "Tournament 0 (basic)",
        [
            (flame_factory, normal_strat),
            (healing_factory, defensive_strat),
        ],
    )
    print("")
    run_tournament(
        "Tournament 1 (error)",
        [
            (flame_factory, aggressive_strat),
            (healing_factory, defensive_strat),
        ],
    )
    print("")
    run_tournament(
        "Tournament 2 (multiple)",
        [
            (aqua_factory, normal_strat),
            (healing_factory, defensive_strat),
            (transform_factory, aggressive_strat),
        ],
    )


if __name__ == "__main__":
    main()
