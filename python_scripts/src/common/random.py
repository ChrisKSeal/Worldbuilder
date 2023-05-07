"""Module to simulate a Dice and various permutations of dice."""

import random as rdm
import re
from os import urandom
from typing import List, Optional, Tuple

from python_scripts.src.common.logging import LoggedBaseClass

MODIFIERS = r"[+]|[-]|[*]|[/]|x"  # pylint: disable=invalid-name


class DiceRoller(LoggedBaseClass):  # pylint: disable=too-few-public-methods
    """A helper class to generate random numbers using the pseudorandom generator.

    Takes an optional seed in case we want to recreate the exact same conditions.
    The seed should be stored in the generated YAML so we can use this at a later stage.

    Attributes:
        seed (Optional[int]): the random number seed if one is provided.
    """

    def __init__(self, seed: Optional[int] = None) -> None:
        """Initialise the random number generator.

        Take the random number seed if it is provided, or generate
        one from the OS. The OS returns a bytestring, so cast this to int.

        Args:
            seed (Optional[int]): the random number seed if one is provided.
        """
        super().__init__()
        if not seed:
            self.seed = int.from_bytes(urandom(8), "big", signed=False)
        else:
            self.seed = seed
        rdm.seed(self.seed)

    def __parse_dice_string(  # pylint: disable=too-many-locals
        self, dicestring: str
    ) -> List[Tuple[Tuple[int, int, int, Optional[str], Optional[str]], Optional[str]],]:
        """Parse a dice string into a tuple that can be used by the roll function.

        Args:
            dicestring (str): the string to be parsed

        Returns:
            a list of tuples containing the roll tuple and
            the operator to combine multiple rolls.
            The roll tuple contains
             - the number of dice to roll,
             - the size of the dice,
             - a modifier to the roll,
             - the operator to apply to the modifier
             - a string containing information about the 'type' of roll,
                e.g. open ended rolls for Rolemaster

        Raises:
            ValueError: if the dice string isn't either the string representation of an integer
                or does not contain a '(int|None)d(int)' or '(int|None)D(int)' in accordance with
                standard TTRPG nomenclature
        """
        number: int = 1
        size: int = 1
        modifier: int = 0
        modifier_type: Optional[str] = None
        roll_type: Optional[str] = None
        dice_operator: Optional[str] = None
        dicestring = dicestring.lower()
        dice_matches = re.split(MODIFIERS, dicestring)
        dice_matches = [match.strip() for match in dice_matches]
        modifier_types = re.findall(MODIFIERS, dicestring)
        count = 0
        return_list = []
        for match in dice_matches:
            if re.search(r"d\d+", match):
                if count > 0:
                    dice_operator = modifier_types[count - 1]
                    return_list.append(
                        (
                            (number, size, modifier, modifier_type, roll_type),
                            dice_operator,
                        )
                    )
                    number = 1
                    modifier = 0
                    modifier_type = None
                    roll_type = None
                    dice_operator = None
                dice = match.split("d")
                dice = [dice_str for dice_str in dice if dice_str != ""]
                if len(dice) == 1:
                    number = 1
                    size_str = dice[0]
                else:
                    number = int(dice[0])
                    size_str = dice[1]
                has_roll_type = re.search(r"[a-ce-wyz]", size_str)
                if has_roll_type:
                    size = int(size_str[: has_roll_type.span()[0]])
                    roll_type = size_str[has_roll_type.span()[0] :]
                else:
                    size = int(size_str)
            else:
                modifier = int(match)
                modifier_type = modifier_types[count - 1]
            count += 1
        return_list.append(
            ((number, size, modifier, modifier_type, roll_type), dice_operator)
        )
        return return_list

    def __parse_dice_tuple(
        self, dice_tuple: Tuple[int, int, int, Optional[str], Optional[str]]
    ) -> int | float:
        """Process a roll tuple and roll the dice.

        Args:
            dice_tuple (tuple(int, int, int, str|None, str|None)): A dice tuple as
                generated from the __parse_dice_string function

        Returns:
            the integer result of the dice roll
        """
        number, size, modifier, modifier_type, roll_type = dice_tuple
        cumulative_sum = 0
        for _ in range(number):
            cumulative_sum += rdm.randint(1, size)  # nosec B311
        if modifier_type == "+":
            return cumulative_sum + modifier
        if modifier_type == "-":
            return cumulative_sum - modifier
        if modifier_type in ("*", "x"):
            return cumulative_sum * modifier
        if modifier_type == "/":
            if modifier != 0:
                return cumulative_sum / modifier
        if roll_type:
            pass
        return cumulative_sum

    def roll(self, variable_input: int | str) -> int | float:
        """Generate a dice roll of size.

        Args:
            variable_input (int | str): either an integer in which case this is
                the number of sides on the virtual dice to roll. If it is a string
                then it may be one of several different rolls, based on 'standard'
                TTRPG nomeclature.

        Returns:
            a random integer within the range defined by the dice
        """
        if isinstance(variable_input, int):
            return rdm.randint(1, variable_input)  # nosec
        results = []
        for roll in self.__parse_dice_string(variable_input):
            results.append((self.__parse_dice_tuple(roll[0]), roll[1]))
        cumulative_sum = results[0][0]
        if len(results) > 1:
            for i in range(len(results)):  # pylint: disable=C0200
                if i == 0:
                    continue
                modifier_type = results[i - 1][1]
                if modifier_type == "+":
                    cumulative_sum += results[i][0]
                elif modifier_type == "-":
                    cumulative_sum -= results[i][0]
                elif modifier_type in ("*", "x"):
                    cumulative_sum *= results[i][0]
                elif modifier_type == "/":
                    if results[i][0] != 0:
                        cumulative_sum /= results[i][0]
        return cumulative_sum
