"""Module to load and lookup RPG tables."""

import json
import random as rdm
import re
from pathlib import Path
from typing import Dict, List, Optional

from python_scripts.src.common.config import (  # pylint: disable=import-error
    LoggingConfig,
)
from python_scripts.src.common.containers import Dice  # pylint: disable=import-error
from python_scripts.src.common.logging import (  # pylint: disable=import-error
    LoggedBaseClass,
)


class Table(LoggedBaseClass):
    """Class to hold a representation of a table to roll on.

    Attributes:
        name (str): the name of the table
        data (list): an ordered list of results from low to high
        min_roll (int): the minimum roll that the table will accept
        max_roll (int): the maximum roll that the table will accept as an input
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        name: str,
        data: List[str],
        config: LoggingConfig,
        max_roll: Optional[int] = None,
        min_roll: int = 1,
    ) -> None:
        """Class initialisation."""
        super().__init__(config)
        self.name = name
        self.data = self.parse_input(data)
        self.min_roll = min_roll
        if not max_roll:
            max_roll = len(data)
        self.max_roll = max_roll
        self.dice = Dice()

    def parse_input(self, data: List[str]) -> Dict[int, str]:
        """Unpacks the entries of a list into a dict for rolling against.

        Unpacking each entry is based on the structure of the string. If the string
        matches one of the regular expressions that represent the 'number, value' or
        the 'number-number, value', then split it up and parse appropriately. Otherwise
        treat the whole value as an entry.

        Args:
            data (List[str]): A list of packed entries. This takes the form of one of
                'value', 'number, value' or 'number-number, value'
        Returns:
            an dictionary of values keyed by integers.
        """
        return_dictionary = {}
        count = 1
        number_value = re.compile(r"^\d+, ")
        number_number_value = re.compile(r"^\d+[-]\d+, ")
        for datum in data:
            number = None
            match = re.match(number_value, datum)
            if not match:
                match = re.match(number_number_value, datum)
            if match:
                number = datum[: match.span()[1]].strip()
                value = datum[match.span()[1] :].strip()
            if not match:
                return_dictionary[count] = datum
            else:
                if match.re == number_value and number:
                    numberind = int(number[:-1])
                    return_dictionary[numberind] = value
                elif number:
                    number = number[:-1]  # strip the trailing ,
                    numbers = number.split("-")
                    low = int(numbers[0].strip())
                    high = int(numbers[1].strip())
                    for numberind in range(low, high + 1):
                        return_dictionary[numberind] = value
            count = max(return_dictionary.keys()) + 1
        self.logger.debug(return_dictionary)
        return return_dictionary

    def get_value(self, roll: int) -> str:
        """Look up a row in a table and return the value.

        Args:
            roll (int): The value to use in the look up

        Returns:
            str|int|float: The value looked up
        """
        return self.data[roll]

    def __eq__(self, other: object) -> bool:
        """Test to see if two Table objects are the same.

        Args:
            other (Table): A table object to compare to.

        Returns:
            bool: True if the tables are the same else False
        """
        return all(
            (
                self.name == other.name,  # type: ignore[attr-defined]
                self.data == other.data,  # type: ignore[attr-defined]
                self.max_roll == other.max_roll,  # type: ignore[attr-defined]
                self.min_roll == other.min_roll,  # type: ignore[attr-defined]
            ),
        )

    def roll(self, roll: Optional[str] = None) -> str:
        """Randomly select a value from a table.

        If a roll string is passed in, use the DiceRoller to roll the resulting
        dice string. If no dice string is passed into the function, use a uniform
        random distribution via the randbetween function.

        Args:
            roll (Optional[str], optional): A dice string that can be parsed by the
                DiceRoller class. Defaults to None.

        Returns:
            str: The look up value from the table
        """
        lookup_roll: int = 0
        if roll:
            lookup_roll = self.dice.roll(roll)
        else:
            lookup_roll = rdm.randint(self.min_roll, self.max_roll)
        return self.get_value(lookup_roll)


def read_json_files(filepath: Path, config: LoggingConfig) -> List[Table]:
    """Read in a YAML file and create Table objects.

    Args:
        filepath (Path): The file path leading to the YAML file

    Returns:
        List[Table]: A list of Table objects to be incorporated into other
            scripts.
    """
    with open(filepath, "r", encoding="utf-8") as json_file:
        tables = json.load(json_file)
        return_table = []
        for _, table in tables.items():
            if not all(
                (
                    "name" in table.keys(),
                    "data" in table.keys(),
                )
            ):
                continue
            current_table = Table(
                config=config,
                name=table["name"],
                data=table["data"],
            )
            if "min_roll" in table.keys():
                current_table.min_roll = table["min_roll"]
            if "max_roll" in table.keys():
                current_table.max_roll = table["max_roll"]
            return_table.append(current_table)
        return return_table
