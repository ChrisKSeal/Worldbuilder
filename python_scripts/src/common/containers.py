# pylint: disable=c-extension-no-member, R0903
"""A module to hold dependency containers from dependency injector."""
from dependency_injector import containers, providers

from python_scripts.src.common.random import DiceRoller  # pylint: disable=E0401


class Dice(containers.DeclarativeContainer):  # type: ignore[misc]
    """Container class holding the DiceRoller dependency.

    There should only be one dice roller to prevent the risk of replication of
    random results due to the pseudorandom nature of the random number generator.

    Attributes:
        dice_roller (DiceRoller): A Singleton instance of the DiceRoller.
    """

    dice_roller = providers.Singleton(DiceRoller)
