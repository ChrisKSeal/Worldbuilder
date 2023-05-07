"""Sets up logging from a config file."""

import logging
import logging.config
from abc import ABC
from typing import Any, Dict

from python_scripts.src.common.config import (  # pylint: disable=import-error
    LoggingConfig,
)

MB = 1024 * 1024


class LoggedBaseClass(ABC):  # pylint: disable=too-few-public-methods
    """A base class that initialises a class specific logger."""

    def __init__(self, config: LoggingConfig) -> None:
        """Class initialisation.

        Attributes:
            logger (Logger): A logging Logger class that child classes can use.
        """
        self.config = config
        logging.config.dictConfig(self.set_up_logging())
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )

    def set_up_logging(self) -> Dict[str, Any]:
        """Set up the logging file handler.

        Returns:
            dict: A dictionary ready to configure the logger
        """
        logging_config = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {"format": "%(asctime)s %(levelname)s %(name)s %(message)s"},
            },
            "handlers": {
                "file": {
                    "class": "logging.RotatingFileHandler",
                    "maxBytes": 1 * MB,
                    "bqckupCount": 5,
                    "level": self.config.level,
                    "formatter": "default",
                    "filename": self.config.filename,
                    "mode": "a",
                    "encoding": "utf-8",
                },
            },
            "root": {
                "handlers": ["file"],
                "level": self.config.level,
            },
        }
        return logging_config
