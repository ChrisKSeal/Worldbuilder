"""Sets up logging from a config file."""

import logging
from abc import ABC


class LoggedBaseClass(ABC):  # pylint: disable=too-few-public-methods
    """A base class that initialises a class specific logger."""

    def __init__(self) -> None:
        """Class initialisation.

        Attributes:
            logger (Logger): A logging Logger class that child classes can use.
        """
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )
