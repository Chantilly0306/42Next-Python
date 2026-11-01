from ex0.factory import CreatureFactory
from ex0.creature import Creature
from .creature import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
