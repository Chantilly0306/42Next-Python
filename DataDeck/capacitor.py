#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing_creatures() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()

    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print("")

    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())
    print("")


def test_transform_creatures():
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print("")

    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())
    print("")


def main():
    test_healing_creatures()
    test_transform_creatures()


if __name__ == "__main__":
    main()
