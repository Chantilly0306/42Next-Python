#!/usr/bin/env python3
import typing
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
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
        f_name = fact.__class__.__name__[:5]
        s_name = strat.__class__.__name__[:5]
        formatted_opponents.append(f"({f_name}+{s_name})")
    print(f"[{', '.join(formatted_opponents)}]")

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(len(opponents)):
            if i >= j:
                continue

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
                if not strat1.is_valid(c1):
                    raise InvalidStrategyError(
                        f"Invalid Creature '{c1.name}' "
                        "for this aggressive strategy"
                    )
                for act in strat1.act(c1):
                    print(act)

                if not strat2.is_valid(c2):
                    raise InvalidStrategyError(
                        f"Invalid Creature '{c2.name}' "
                        "for this defensive strategy"
                    )
                for act in strat2.act(c2):
                    print(act)

            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")


def main():
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

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

    run_tournament(
        "Tournament 1 (error)",
        [
            (flame_factory, aggressive_strat),
            (healing_factory, defensive_strat),
        ],
    )

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
