#!/usr/bin/env python3
import typing
from ex0 import FlameFactory, AquaFactory


def test_factory(factory: typing.Any):
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print("")


def test_battle(factory1, factory2):
    print("Testing battle")
    c1 = factory1.create_base()
    c2 = factory2.create_base()

    print(c1.describe())
    print("VS.")
    print(c2.describe())
    print("fight!")
    print(c1.attack())
    print(c2.attack())
    print("")


def main():
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
