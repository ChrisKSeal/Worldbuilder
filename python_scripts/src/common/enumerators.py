"""Module to hold enumerators for 'tables' in settlement books."""

from enum import Enum
import yaml
from pathlib import Path
from typing import List


class Table:
    """A Table that holds an enum and a table name

    Attributes:
        name (str): The table name
        data (Enum): An Enum holding the data from the table
    """

    def __init__(self, name: str, data: List[str]):
        print(name)
        print(data)
        self.name = name
        self.table = Enum(name, data)


def table_constructor(
    loader: yaml.SafeLoader,
    node: yaml.nodes.MappingNode,
) -> Table:
    """Construct an employee."""
    print(**loader.construct_mapping(node))
    return Table(**loader.construct_mapping(node))


def get_loader():
    """Add constructors to PyYAML loader."""
    loader = yaml.SafeLoader
    loader.add_constructor("!Table", table_constructor)
    return loader


def create_table_from_yaml(filename: Path) -> Table:
    return yaml.load(open(filename, "rb"), Loader=get_loader())  # nosec
