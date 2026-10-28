from abc import ABC, abstractmethod
import typing
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: typing.Any) -> bool:
        pass

    @abstractmethod
    def act(self, creature: typing.Any) -> list[str]:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: typing.Any) -> bool:
        return True

    def act(self, creature: typing.Any) -> list[str]:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: typing.Any) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: typing.Any) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        actions = []
        actions.append(creature.transform())
        actions.append(creature.attack())
        actions.append(creature.revert())
        return actions


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: typing.Any) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: typing.Any) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
            )
        actions = []
        actions.append(creature.attack())
        actions.append(creature.heal())
        return actions
