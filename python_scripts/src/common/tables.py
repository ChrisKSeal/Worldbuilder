"""Module to load and lookup RPG tables"""
# from pathlib import Path
import re
from typing import Dict, List, Optional

# import yaml


class Table:
    """Class to hold a representation of a table to roll on

    Attributes:
        name (str): the name of the table
        data (list): an ordered list of results from low to high
        min_roll (int): the minimum roll that the table will accept
        max_roll (int): the maximum roll that the table will accept as an input
    """

    def __init__(
        self,
        name: str,
        data: List[str],
        max_roll: Optional[int],
        min_roll: int = 1,
    ) -> None:
        self.name = name
        self.data = Table.parse_input(data)
        self.min_roll = min_roll
        if not max_roll:
            max_roll = len(data)
        self.max_roll = max_roll

    @staticmethod
    def parse_input(data: List[str]) -> Dict:
        """Unpacks the entries of a list into a dict for rolling against

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
        number_value = re.compile("^\d+, ")
        number_number_value = re.compile("^\d+[-]\d+, ")
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
                    numberind = int(number[:-1])  # type: ignore[assignment]
                    return_dictionary[numberind] = value
                elif number:
                    number = number[:-1]  # strip the trailing ,
                    numbers = number.split("-")
                    low = int(numbers[0].strip())
                    high = int(numbers[1].strip())
                    for numberind in range(low, high + 1):
                        return_dictionary[numberind] = value
            count = max(return_dictionary.keys())
        return return_dictionary
